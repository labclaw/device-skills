"""DeviceDriver implementation for labclaw hardware layer.

This driver is consumed by labclaw's HardwareManager to connect,
read data, and send commands to the device.
"""
from __future__ import annotations

from typing import Any


class DeviceDriver:
    """Implement the labclaw DeviceDriver protocol.

    Required interface:
        device_id: str (property)
        device_type: str (property)
        async connect() -> bool
        async disconnect() -> None
        async read() -> dict[str, Any]
        async write(command) -> bool
        async status() -> dict[str, Any]
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

    async def connect(self) -> bool:
        self._connected = True
        return True

    async def disconnect(self) -> None:
        self._connected = False

    async def read(self) -> dict[str, Any]:
        if not self._connected:
            return {"error": "Not connected"}
        return {}

    async def write(self, command: dict[str, Any]) -> bool:
        if not self._connected:
            return False
        return True

    async def status(self) -> dict[str, Any]:
        return {"connected": self._connected, "device_id": self._device_id}
