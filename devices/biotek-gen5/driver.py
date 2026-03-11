"""Gen5Driver — standalone CSV driver for labclaw hardware layer.

Implements the labclaw DeviceDriver protocol (async connect/disconnect/read/write/status).
Parses Gen5 CSV exports using the same logic as Gen5Processor.load().

Used by labclaw's HardwareManager to ingest plate reader data files.
"""

from __future__ import annotations

import logging
from pathlib import Path
from typing import Any

from device_skills.base import BaseDriver

from .processor import Gen5Processor

logger = logging.getLogger(__name__)


class Gen5Driver(BaseDriver):
    """DeviceDriver for BioTek Gen5 CSV exports.

    Implements the BaseDriver ABC contract:
        device_id: str (property)
        device_type: str (property)
        async connect() -> bool
        async disconnect() -> None
        async read() -> dict[str, Any]
        async write(command) -> bool
        info() -> dict[str, Any]

    The driver is file-based: it reads CSV files exported from Gen5 software.
    No live connection to the instrument is made in this driver; for live
    control use the Gen5Adapter with GUI or API mode.

    Example::

        driver = Gen5Driver(device_id="gen5-001", watch_path=Path("/data/gen5/"))
        await driver.connect()
        data = await driver.read()
        print(data["wells"])
    """

    def __init__(
        self,
        device_id: str = "gen5-001",
        config: dict[str, Any] | None = None,
        watch_path: Path | None = None,
        file_patterns: list[str] | None = None,
    ) -> None:
        self._device_id = device_id
        self._config = config or {}
        self._watch_path = watch_path or Path(".")
        self._file_patterns = file_patterns or ["*.csv"]
        self._connected = False
        self._last_file: Path | None = None

    @property
    def device_id(self) -> str:
        return self._device_id

    @property
    def device_type(self) -> str:
        return "biotek-gen5"

    def info(self) -> dict[str, Any]:
        """Return device metadata."""
        return {
            "device_id": self._device_id,
            "device_type": self.device_type,
            "connected": self._connected,
            "watch_path": str(self._watch_path),
        }

    async def connect(self, config: dict[str, Any] | None = None) -> bool:
        """Mark driver as connected (file-based — no network connection needed)."""
        self._connected = True
        logger.info("Gen5Driver connected (file-based mode, watch_path=%s)", self._watch_path)
        return True

    async def disconnect(self) -> None:
        """Mark driver as disconnected."""
        self._connected = False
        logger.info("Gen5Driver disconnected")

    async def read(self, query: dict[str, Any] | None = None) -> dict[str, Any]:
        """Read the most recently modified CSV file from watch_path.

        Returns:
            Dict with keys: wells, metadata, file.
            Returns error dict if not connected or no files found.
        """
        if not self._connected:
            return {"error": "Not connected", "device_id": self._device_id}

        # Find the most recently modified CSV matching patterns
        candidates: list[Path] = []
        for pattern in self._file_patterns:
            candidates.extend(self._watch_path.glob(pattern))

        if not candidates:
            logger.warning("Gen5Driver: no CSV files found in %s", self._watch_path)
            return {"wells": {}, "metadata": {}, "file": "", "device_id": self._device_id}

        latest = max(candidates, key=lambda p: p.stat().st_mtime)
        self._last_file = latest
        return self.parse_file(latest)

    async def write(self, command: dict[str, Any]) -> bool:
        """Write is not supported for a file-based read-only driver.

        Returns:
            Always False — Gen5 CSV driver is read-only.
        """
        logger.warning(
            "Gen5Driver.write() called but driver is read-only (file-based): %s", command
        )
        return False

    async def status(self) -> dict[str, Any]:
        """Return driver connection status."""
        return {
            "connected": self._connected,
            "device_id": self._device_id,
            "device_type": self.device_type,
            "watch_path": str(self._watch_path),
            "last_file": str(self._last_file) if self._last_file else None,
        }

    # -- CSV parsing (Gen5 export format) ---------------------------------

    def parse_file(self, path: Path) -> dict[str, Any]:
        """Parse a Gen5 96-well plate CSV export.

        Delegates core CSV parsing to Gen5Processor.load() and adds
        driver-specific fields (device_id).

        Returns::

            {
                "wells": {"A1": 0.123, "A2": 0.456, ..., "H12": 1.234},
                "metadata": {"Protocol": "...", "Wavelength": "450nm", ...},
                "file": "/path/to/file.csv",
                "device_id": "gen5-001",
            }
        """
        result = Gen5Processor().load(str(path))
        result["device_id"] = self._device_id
        logger.debug(
            "Gen5Driver parsed %d wells, %d metadata fields from %s",
            len(result.get("wells", {})),
            len(result.get("metadata", {})),
            path,
        )
        return result
