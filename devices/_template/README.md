# [Device Name] — Device Skill

## Overview

Short description of what this device does and how this skill supports it.

## Directory Structure

Each device skill uses a two-part knowledge architecture:

```
devices/<device-name>/
├── skill.yaml           # Device manifest (parsed into SkillManifest)
├── SOUL.md              # AI agent personality and identity
├── profile.yaml         # GUI automation profile (for device-use)
├── README.md            # This file — usage guide
├── __init__.py          # Python package entry point
│
├── docs/                # OFFICIAL KNOWLEDGE — vendor documentation
│   ├── README.md        #   How to organize documentation
│   ├── manual/          #   Operator & safety manuals
│   ├── api/             #   Programming interface references
│   ├── specs/           #   Hardware specifications & datasheets
│   ├── formats/         #   Data file format documentation
│   └── science/         #   Domain science background
│
├── user/                # USER KNOWLEDGE — instance-specific operational data
│   ├── MEMORY.md        #   Operational notebook (calibration, quirks, incidents)
│   ├── system_config.md #   Your specific hardware/software configuration
│   ├── calibration_log.md # Calibration event records
│   ├── protocols/       #   Lab-specific SOPs and workflows
│   └── findings/        #   Accumulated experimental findings
│
├── adapter.py           # BaseAdapter implementation
├── processor.py         # BaseProcessor implementation
├── brain.py             # BaseBrain AI analysis
├── driver.py            # DeviceDriver for labclaw
├── visualizer.py        # Plotting and output
└── tests/               # Per-device tests
```

### docs/ — Official Knowledge

The `docs/` directory contains vendor-sourced documentation distilled into Markdown.
An AI agent reading these files should fully understand the device's capabilities,
safety requirements, programming interface, data formats, and scientific context.

This knowledge is **static** — it comes from manuals, datasheets, and API references.
It does not change between instrument instances.

### user/ — User Knowledge

The `user/` directory contains instance-specific operational data for YOUR instrument.
This includes your system configuration, calibration history, lab protocols, and
accumulated findings. This knowledge is **dynamic** — it grows over time as the
instrument is used.

## Quick Start

```python
from devices.<device_name>.adapter import DeviceAdapter

adapter = DeviceAdapter()
adapter.connect()
data = adapter.acquire(wavelength=600)
result = adapter.process("path/to/data.csv")
```

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
