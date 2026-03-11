"""AI-powered analysis for this device."""
from __future__ import annotations

from typing import Any

from device_skills.base import BaseBrain


class TemplateBrain(BaseBrain):
    """LLM-powered analysis. TODO: Rename to match your device."""

    def analyze(self, data: dict[str, Any], context: str = "") -> str:
        raise NotImplementedError

    def summarize(self, findings: list[str]) -> str:
        raise NotImplementedError
