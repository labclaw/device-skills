"""DeviceDriver implementation for labclaw hardware layer.

This driver is consumed by labclaw's HardwareManager to connect,
read data, and send commands to the Bruker TopSpin NMR spectrometer.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any

from device_skills.base import BaseDriver
from device_skills.schema import ControlMode

if TYPE_CHECKING:
    from .adapter import TopSpinAdapter


class TopSpinDriver(BaseDriver):
    """labclaw DeviceDriver for Bruker TopSpin NMR.

    Implements the BaseDriver ABC contract:
        device_id: str (property)
        device_type: str (property)
        async connect() -> bool
        async disconnect() -> None
        async read() -> dict[str, Any]
        async write(command) -> bool
        info() -> dict[str, Any]

    In offline mode the driver succeeds immediately without any
    network connection.  In API mode it delegates to the TopSpin
    gRPC API (port 3081).
    """

    def __init__(
        self,
        device_id: str = "",
        config: dict[str, Any] | None = None,
    ) -> None:
        self._device_id = device_id or "bruker-topspin-001"
        self._config = config or {}
        self._connected = False
        self._last_spectrum: dict[str, Any] = {}
        self._adapter: TopSpinAdapter | None = None

        # Parse mode string into ControlMode enum at init time
        mode_str = self._config.get("mode", "offline")
        self._mode = ControlMode(mode_str)

    @property
    def device_id(self) -> str:
        return self._device_id

    @property
    def device_type(self) -> str:
        return "nmr-spectrometer"

    def info(self) -> dict[str, Any]:
        """Return instrument metadata."""
        return {
            "device_id": self._device_id,
            "device_type": self.device_type,
            "mode": self._mode.value,
            "connected": self._connected,
        }

    async def connect(self, config: dict[str, Any] | None = None) -> bool:
        """Connect to TopSpin.  Uses mode from config."""
        if self._mode == ControlMode.OFFLINE:
            self._connected = True
            self._adapter = self._create_adapter()
            self._adapter.connect()
            return True

        if self._mode == ControlMode.API:
            result = await self._connect_api()
            if result:
                self._adapter = self._create_adapter()
                self._adapter.connect()
            return result

        # Unknown mode — fail gracefully
        return False

    def _create_adapter(self) -> TopSpinAdapter:
        """Create and return a TopSpinAdapter for the current mode."""
        from .adapter import TopSpinAdapter

        return TopSpinAdapter(mode=self._mode)

    async def _connect_api(self) -> bool:
        """Attempt gRPC connection to running TopSpin (port 3081)."""
        try:
            from bruker.api.topspin import Topspin

            ts = Topspin()
            _ = ts.getVersion()
            self._connected = True
            return True
        except Exception:
            self._connected = False
            return False

    async def disconnect(self) -> None:
        """Disconnect from the instrument."""
        if self._adapter is not None:
            self._adapter.disconnect()
            self._adapter = None
        self._connected = False

    async def read(self, query: dict[str, Any] | None = None) -> dict[str, Any]:
        """Read the most recently processed spectrum data.

        Returns a dict with spectrum metadata and peak list, or an
        error dict if not connected or no data is available.
        """
        if not self._connected:
            return {"error": "Not connected"}
        if not self._last_spectrum:
            return {"error": "No spectrum data available — call write() with process command first"}
        return self._last_spectrum

    async def write(self, command: dict[str, Any]) -> bool:
        """Send a command to TopSpin.

        Supported commands:
            {"action": "process", "path": "<dataset_path>"}
                Process a dataset and cache the result for read().
            {"action": "list_datasets"}
                Enumerate available examdata; result in status().

        Returns True if the command was accepted, False otherwise.
        """
        if not self._connected:
            return False

        action = command.get("action", "")

        if action == "process":
            path = command.get("path", "")
            if not path:
                return False
            try:
                spectrum = self._adapter.process(path)
                self._last_spectrum = {
                    "path": path,
                    "nucleus": spectrum.nucleus,
                    "solvent": spectrum.solvent,
                    "frequency_mhz": spectrum.frequency_mhz,
                    "title": spectrum.title,
                    "sample_name": spectrum.sample_name,
                    "num_peaks": len(spectrum.peaks),
                    "peaks": [{"ppm": p.ppm, "intensity": p.intensity} for p in spectrum.peaks],
                }
                return True
            except Exception:
                return False

        if action == "list_datasets":
            # Just triggers a refresh; results surfaced via status()
            return True

        return False

    async def status(self) -> dict[str, Any]:
        """Return current driver status."""
        return {
            "connected": self._connected,
            "device_id": self._device_id,
            "device_type": self.device_type,
            "mode": self._mode.value,
            "has_spectrum": bool(self._last_spectrum),
        }
