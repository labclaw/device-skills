"""DeviceDriver implementation for labclaw hardware layer.

This driver is consumed by labclaw's HardwareManager to connect,
read data, and send commands to the device.
"""

from __future__ import annotations

from typing import Any

from device_skills.base import BaseDriver


class TemplateDriver(BaseDriver):
    """Implement the labclaw DeviceDriver protocol.

    TODO: Rename to match your device (e.g. MyDeviceDriver).
    """

    def __init__(self, device_id: str = "", config: dict[str, Any] | None = None) -> None:
        self._device_id = device_id or "my-device-001"
        self._config = config or {}
        self._connected = False

    @property
    def device_id(self) -> str:
        return self._device_id

    @property
    def device_type(self) -> str:
        return "my-device"

    def info(self) -> dict[str, Any]:
        """Return device metadata."""
        return {
            "device_id": self._device_id,
            "device_type": self.device_type,
            "connected": self._connected,
        }

    async def connect(self, config: dict[str, Any] | None = None) -> bool:
        raise NotImplementedError

    async def disconnect(self) -> None:
        raise NotImplementedError

    async def read(self, query: dict[str, Any] | None = None) -> dict[str, Any]:
        raise NotImplementedError

    async def write(self, command: dict[str, Any]) -> bool:
        raise NotImplementedError
