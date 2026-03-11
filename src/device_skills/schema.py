"""SkillManifest — the standard schema for device skills.

Every device skill has a skill.yaml parsed into this model. It defines
what the device is, what it can do, and how to interact with it.
"""
from __future__ import annotations

from enum import Enum

from pydantic import BaseModel, Field, field_validator


class ControlMode(str, Enum):
    """How the system talks to the instrument."""

    API = "api"
    GUI = "gui"
    OFFLINE = "offline"


class InterfaceType(str, Enum):
    """Physical/logical interface to the device."""

    FILE_BASED = "file_based"
    SERIAL = "serial"
    NETWORK_API = "network_api"
    GPIO_DAQ = "gpio_daq"
    SOFTWARE_BRIDGE = "software_bridge"
    GUI = "gui"


class SkillManifest(BaseModel):
    """Metadata for a device skill — parsed from skill.yaml."""

    name: str = Field(..., min_length=1, description="Unique device skill name (slug)")
    version: str = Field(..., description="Skill version (semver)")
    vendor: str = Field(..., description="Manufacturer or vendor name")
    category: str = Field(..., description="Device category: plate-reader, nmr, microscope, etc.")
    model: str = Field(default="", description="Specific model name")
    description: str = Field(default="", description="Human-readable description")
    platform: str = Field(default="", description="OS platform: windows, macos, linux, cross")
    interface_type: InterfaceType = Field(
        default=InterfaceType.FILE_BASED, description="Primary interface type"
    )
    control_modes: list[ControlMode] = Field(
        default_factory=list, description="Supported control modes"
    )
    capabilities: list[str] = Field(
        default_factory=list, description="What it can measure/do"
    )
    data_formats: list[str] = Field(
        default_factory=list, description="Output file formats"
    )
    safety_level: str = Field(default="normal", description="Safety level: normal, strict, critical")
    dependencies: list[str] = Field(
        default_factory=list, description="Python package dependencies beyond core"
    )

    @field_validator("name")
    @classmethod
    def name_not_empty(cls, v: str) -> str:
        if not v.strip():
            raise ValueError("name must not be empty")
        return v
