"""device-skills — modular, standardized device skills for labclaw & device-use."""
from __future__ import annotations

from device_skills.loader import discover_skills, load_manifest
from device_skills.schema import ControlMode, InterfaceType, SkillManifest

__all__ = [
    "ControlMode",
    "InterfaceType",
    "SkillManifest",
    "discover_skills",
    "load_manifest",
]
