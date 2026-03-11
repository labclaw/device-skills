"""Tests for device skill loader."""
from __future__ import annotations

from pathlib import Path

import pytest
import yaml

from device_skills.loader import discover_skills, load_manifest
from device_skills.schema import SkillManifest


@pytest.fixture()
def tmp_devices(tmp_path: Path) -> Path:
    """Create a temp devices directory with two fake skills."""
    dev_a = tmp_path / "device-a"
    dev_a.mkdir()
    manifest_a = {
        "name": "device-a",
        "version": "1.0.0",
        "vendor": "VendorA",
        "category": "plate-reader",
        "capabilities": {"can_observe": ["absorbance"]},
    }
    (dev_a / "skill.yaml").write_text(yaml.dump(manifest_a))
    (dev_a / "__init__.py").write_text("")

    dev_b = tmp_path / "device-b"
    dev_b.mkdir()
    manifest_b = {
        "name": "device-b",
        "version": "2.0.0",
        "vendor": "VendorB",
        "category": "nmr",
    }
    (dev_b / "skill.yaml").write_text(yaml.dump(manifest_b))
    (dev_b / "__init__.py").write_text("")

    # _template should be skipped
    tmpl = tmp_path / "_template"
    tmpl.mkdir()
    tmpl_data = {"name": "template", "version": "0", "vendor": "x", "category": "x"}
    (tmpl / "skill.yaml").write_text(yaml.dump(tmpl_data))

    return tmp_path


def test_load_manifest(tmp_devices: Path):
    m = load_manifest(tmp_devices / "device-a" / "skill.yaml")
    assert isinstance(m, SkillManifest)
    assert m.name == "device-a"
    assert m.category == "plate-reader"


def test_load_manifest_missing_file():
    with pytest.raises(FileNotFoundError):
        load_manifest(Path("/nonexistent/skill.yaml"))


def test_discover_skills(tmp_devices: Path):
    skills = discover_skills(tmp_devices)
    names = [s.name for s in skills]
    assert "device-a" in names
    assert "device-b" in names
    assert len(skills) == 2


def test_discover_skills_empty(tmp_path: Path):
    skills = discover_skills(tmp_path)
    assert skills == []


def test_discover_skills_skips_invalid(tmp_devices: Path):
    bad = tmp_devices / "bad-device"
    bad.mkdir()
    (bad / "skill.yaml").write_text("invalid: yaml: [[[")
    skills = discover_skills(tmp_devices)
    assert len(skills) == 2
