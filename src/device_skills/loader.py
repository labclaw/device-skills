"""Discover and load device skills from a devices directory.

Each subdirectory with a valid skill.yaml is a device skill.
Directories starting with _ (like _template) are skipped.
"""
from __future__ import annotations

import importlib.resources
import logging
from pathlib import Path

import yaml

from device_skills.schema import SkillManifest

logger = logging.getLogger(__name__)

try:
    _DEFAULT_DEVICES_DIR = Path(str(importlib.resources.files("devices")))
except (TypeError, ModuleNotFoundError):
    _DEFAULT_DEVICES_DIR = Path(__file__).resolve().parent.parent.parent / "devices"


def load_manifest(skill_yaml_path: Path) -> SkillManifest:
    """Load and validate a single skill.yaml into a SkillManifest."""
    if not skill_yaml_path.exists():
        raise FileNotFoundError(f"skill.yaml not found: {skill_yaml_path}")

    with open(skill_yaml_path) as f:
        data = yaml.safe_load(f)

    return SkillManifest(**data)


def discover_skills(devices_dir: Path | None = None) -> list[SkillManifest]:
    """Discover all valid device skills in a directory.

    Scans each subdirectory for a skill.yaml. Skips directories starting with _.
    Invalid manifests are logged and skipped.
    """
    devices_dir = devices_dir or _DEFAULT_DEVICES_DIR

    if not devices_dir.is_dir():
        return []

    manifests: list[SkillManifest] = []
    for child in sorted(devices_dir.iterdir()):
        if not child.is_dir() or child.name.startswith("_"):
            continue
        skill_yaml = child / "skill.yaml"
        if not skill_yaml.exists():
            continue
        try:
            manifest = load_manifest(skill_yaml)
            manifests.append(manifest)
        except Exception:
            logger.warning("Skipping invalid device skill: %s", child.name, exc_info=True)

    return manifests
