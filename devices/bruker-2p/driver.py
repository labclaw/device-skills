"""DeviceDriver implementation for labclaw hardware layer.

This driver is consumed by labclaw's HardwareManager to connect,
read data, and send commands to the Bruker Ultima Investigator
two-photon fluorescence microscope.
"""
from __future__ import annotations

from typing import TYPE_CHECKING, Any

from device_skills.base import BaseDriver
from device_skills.schema import ControlMode

if TYPE_CHECKING:
    from .adapter import TwoPhotonAdapter


class TwoPhotonDriver(BaseDriver):
    """labclaw DeviceDriver for Bruker Ultima Investigator.

    Implements the BaseDriver ABC contract:
        device_id: str (property)
        device_type: str (property)
        async connect() -> bool
        async disconnect() -> None
        async read() -> dict[str, Any]
        async write(command) -> bool
        info() -> dict[str, Any]

    In offline mode the driver succeeds immediately without any
    network connection. In API mode it delegates to PrairieLink.
    """

    def __init__(
        self,
        device_id: str = "",
        config: dict[str, Any] | None = None,
    ) -> None:
        self._device_id = device_id or "bruker-2p-001"
        self._config = config or {}
        self._connected = False
        self._last_stack: dict[str, Any] = {}
        self._adapter: TwoPhotonAdapter | None = None

        mode_str = self._config.get("mode", "offline")
        self._mode = ControlMode(mode_str)

    @property
    def device_id(self) -> str:
        return self._device_id

    @property
    def device_type(self) -> str:
        return "two-photon-microscope"

    def info(self) -> dict[str, Any]:
        """Return instrument metadata."""
        return {
            "device_id": self._device_id,
            "device_type": self.device_type,
            "mode": self._mode.value,
            "connected": self._connected,
        }

    async def connect(self, config: dict[str, Any] | None = None) -> bool:
        """Connect to PrairieView. Uses mode from config."""
        if self._mode == ControlMode.OFFLINE:
            self._connected = True
            self._adapter = self._create_adapter()
            self._adapter.connect()
            return True

        if self._mode == ControlMode.API:
            self._adapter = self._create_adapter()
            result = self._adapter.connect()
            self._connected = result
            return result

        return False

    def _create_adapter(self) -> TwoPhotonAdapter:
        """Create and return a TwoPhotonAdapter for the current mode."""
        from .adapter import TwoPhotonAdapter

        data_dir = self._config.get("data_dir", "")
        return TwoPhotonAdapter(data_dir=data_dir, mode=self._mode)

    async def disconnect(self) -> None:
        """Disconnect from the instrument."""
        if self._adapter is not None:
            self._adapter.disconnect()
            self._adapter = None
        self._connected = False

    async def read(self, query: dict[str, Any] | None = None) -> dict[str, Any]:
        """Read the most recently processed imaging data.

        Returns a dict with stack metadata and summary, or an error dict
        if not connected or no data is available.
        """
        if not self._connected:
            return {"error": "Not connected"}
        if not self._last_stack:
            return {
                "error": "No imaging data available"
                " — call write() with process command first"
            }
        return self._last_stack

    async def write(self, command: dict[str, Any]) -> bool:
        """Send a command to PrairieView.

        Supported commands:
            {"action": "process", "path": "<data_dir_path>"}
                Process a dataset and cache the result for read().
            {"action": "list_datasets"}
                Enumerate available datasets; result in read().
            {"action": "tseries"}
                Start a T-series acquisition (API mode only).
            {"action": "zseries"}
                Start a Z-series acquisition (API mode only).
            {"action": "abort"}
                Abort current acquisition (API mode only).

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
                stack = self._adapter.process(path)
                self._last_stack = {
                    "path": path,
                    "num_frames": len(stack.frames),
                    "num_channels": stack.num_channels,
                    "frame_rate": stack.frame_rate,
                    "pixels_per_line": stack.pixels_per_line,
                    "lines_per_frame": stack.lines_per_frame,
                    "scan_mode": stack.scan_mode,
                    "laser_wavelength": stack.laser_wavelength,
                }
                return True
            except Exception:
                return False

        if action == "list_datasets":
            try:
                datasets = self._adapter.list_datasets()
                self._last_stack = {"datasets": datasets}
                return True
            except Exception:
                return False

        if action == "tseries":
            try:
                self._adapter.start_tseries()
                return True
            except Exception:
                return False

        if action == "zseries":
            try:
                self._adapter.start_zseries()
                return True
            except Exception:
                return False

        if action == "abort":
            try:
                self._adapter.abort()
                return True
            except Exception:
                return False

        return False

    async def status(self) -> dict[str, Any]:
        """Return current driver status."""
        return {
            "connected": self._connected,
            "device_id": self._device_id,
            "device_type": self.device_type,
            "mode": self._mode.value,
            "has_data": bool(self._last_stack),
        }
