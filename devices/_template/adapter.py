"""Instrument adapter for device-use."""

from __future__ import annotations

from typing import Any

from device_skills.base import BaseAdapter
from device_skills.schema import ControlMode


class TemplateAdapter(BaseAdapter):
    """Implement BaseAdapter for this device. TODO: Rename to match your device."""

    def __init__(self) -> None:
        self._connected = False

    def info(self) -> dict[str, Any]:
        raise NotImplementedError

    @property
    def connected(self) -> bool:
        return self._connected

    @property
    def mode(self) -> ControlMode:
        return ControlMode.OFFLINE

    def connect(self) -> bool:
        raise NotImplementedError

    def disconnect(self) -> None:
        raise NotImplementedError

    def list_datasets(self) -> list[dict[str, Any]]:
        raise NotImplementedError

    def acquire(self, **kwargs: Any) -> Any:
        raise NotImplementedError

    def process(self, data_path: str, **kwargs: Any) -> Any:
        raise NotImplementedError
