"""Visualization for this device's data."""
from __future__ import annotations

from typing import Any


class DeviceVisualizer:
    """Visualizer. TODO: Rename to match your device."""

    def plot(self, data: Any, **kwargs: Any) -> Any:
        raise NotImplementedError
