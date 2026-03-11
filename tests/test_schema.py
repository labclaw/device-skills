"""Tests for SkillManifest schema."""
from __future__ import annotations

import pytest

from device_skills.schema import ControlMode, InterfaceType, SkillManifest


def test_minimal_manifest():
    m = SkillManifest(
        name="test-device",
        version="1.0.0",
        vendor="TestCorp",
        category="plate-reader",
    )
    assert m.name == "test-device"
    assert m.version == "1.0.0"
    assert m.vendor == "TestCorp"
    assert m.category == "plate-reader"
    assert m.control_modes == []
    assert m.capabilities == []


def test_full_manifest():
    m = SkillManifest(
        name="biotek-gen5",
        version="1.0.0",
        vendor="Agilent (BioTek)",
        category="plate-reader",
        model="Synergy H1",
        description="Microplate reader with absorbance, fluorescence, luminescence",
        platform="windows",
        interface_type=InterfaceType.GUI,
        control_modes=[ControlMode.API, ControlMode.GUI, ControlMode.OFFLINE],
        capabilities=["absorbance", "fluorescence", "luminescence"],
        data_formats=["csv", "xlsx"],
        safety_level="strict",
    )
    assert len(m.control_modes) == 3
    assert ControlMode.GUI in m.control_modes
    assert m.safety_level == "strict"
    assert m.interface_type == InterfaceType.GUI


def test_manifest_rejects_empty_name():
    with pytest.raises(ValueError):
        SkillManifest(name="", version="1.0", vendor="X", category="x")


def test_control_mode_values():
    assert ControlMode.API.value == "api"
    assert ControlMode.GUI.value == "gui"
    assert ControlMode.OFFLINE.value == "offline"


def test_interface_type_values():
    assert InterfaceType.FILE_BASED.value == "file_based"
    assert InterfaceType.SERIAL.value == "serial"
    assert InterfaceType.NETWORK_API.value == "network_api"
    assert InterfaceType.GPIO_DAQ.value == "gpio_daq"
    assert InterfaceType.SOFTWARE_BRIDGE.value == "software_bridge"
    assert InterfaceType.GUI.value == "gui"
