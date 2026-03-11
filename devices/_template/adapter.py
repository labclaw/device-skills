"""Instrument adapter for device-use."""
from __future__ import annotations

from typing import Any

from device_skills.base import BaseAdapter


class DeviceAdapter(BaseAdapter):
    """Implement BaseAdapter for this device. TODO: Rename to match your device."""

    def __init__(self) -> None:
        self._connected = False

    def info(self) -> dict[str, Any]:
        return {"name": "my-device", "vendor": "Vendor", "type": "category"}

    @property
    def connected(self) -> bool:
        return self._connected

    def connect(self) -> bool:
        self._connected = True
        return True

    def disconnect(self) -> None:
        self._connected = False

    def list_datasets(self) -> list[dict[str, Any]]:
        return []

    def acquire(self, **kwargs: Any) -> Any:
        raise NotImplementedError

    def process(self, data_path: str, **kwargs: Any) -> Any:
        raise NotImplementedError
