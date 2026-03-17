"""Data processing pipeline for this device."""

from __future__ import annotations

from typing import Any

from device_skills.base import BaseProcessor


class TemplateProcessor(BaseProcessor):
    """Data processor. TODO: Rename to match your device."""

    def load(self, path: str) -> Any:
        raise NotImplementedError

    def transform(self, raw_data: Any) -> Any:
        raise NotImplementedError

    def extract(self, processed_data: Any) -> dict[str, Any]:
        raise NotImplementedError
