# [Device Name] — Device Skill

## Overview

Short description of what this device does and how this skill supports it.

## Quick Start

    from devices.<device_name>.adapter import DeviceAdapter

    adapter = DeviceAdapter()
    adapter.connect()
    data = adapter.acquire(wavelength=600)
    result = adapter.process("path/to/data.csv")

## Capabilities

- List what this device can do

## Control Modes

| Mode | Description | Requirements |
|------|-------------|--------------|
| Offline | Process existing data files | None |
| API | Programmatic control via REST/serial | Device connected |
| GUI | Visual automation via device-use | Device software running |

## Safety

- List safety constraints
- Emergency stop procedures

## Data Formats

- Input: what formats it reads
- Output: what formats it produces

## Known Quirks

- Device-specific issues and workarounds
