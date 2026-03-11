"""Base classes for device skill components.

These ABCs define the standard interface that every device skill implements.
Both labclaw and device-use consume these interfaces.
"""
from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any

from device_skills.schema import ControlMode


class BaseAdapter(ABC):
    """Instrument adapter — how to connect, acquire, and process data.

    Consumed by device-use as BaseInstrument implementation.
    Maps to labclaw's DeviceDriver at a higher abstraction level.
    """

    @abstractmethod
    def info(self) -> dict[str, Any]:
        """Return instrument metadata (name, vendor, type, modes)."""
        ...

    @property
    @abstractmethod
    def connected(self) -> bool:
        """Whether the instrument is currently connected."""
        ...

    @property
    @abstractmethod
    def mode(self) -> ControlMode:
        """Current control mode (API, GUI, or OFFLINE)."""
        ...

    @abstractmethod
    def connect(self) -> bool:
        """Attempt to connect. Returns True if successful."""
        ...

    @abstractmethod
    def disconnect(self) -> None:
        """Disconnect from the instrument."""
        ...

    @abstractmethod
    def list_datasets(self) -> list[dict[str, Any]]:
        """List available datasets/samples."""
        ...

    @abstractmethod
    def acquire(self, **kwargs: Any) -> Any:
        """Acquire data (run experiment, take measurement)."""
        ...

    @abstractmethod
    def process(self, data_path: str, **kwargs: Any) -> Any:
        """Process raw data into a usable result."""
        ...


class BaseProcessor(ABC):
    """Data processing pipeline for a device.

    Three-step pipeline: load -> transform -> extract.
    """

    @abstractmethod
    def load(self, path: str) -> Any:
        """Load raw data from file path."""
        ...

    @abstractmethod
    def transform(self, raw_data: Any) -> Any:
        """Transform/clean raw data."""
        ...

    @abstractmethod
    def extract(self, processed_data: Any) -> dict[str, Any]:
        """Extract structured results from processed data."""
        ...


class BaseBrain(ABC):
    """AI-powered analysis for a device.

    Uses LLM to interpret data and generate insights.
    """

    @abstractmethod
    def analyze(self, data: dict[str, Any], context: str = "") -> str:
        """Analyze data and return interpretation."""
        ...

    @abstractmethod
    def summarize(self, findings: list[str]) -> str:
        """Summarize multiple findings into a coherent narrative."""
        ...
