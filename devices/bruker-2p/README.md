# Bruker Ultima Investigator — Two-Photon Microscope Device Skill

Control and process data from a Bruker Ultima Investigator two-photon fluorescence
microscope. Designed for in vivo calcium imaging in neuroscience research.

## Quick Start

```python
from devices.bruker_2p import *  # noqa: F403 (placeholder — code in future commit)

# For now, this skill provides documentation and configuration only.
# Adapter, processor, brain, and driver implementations are planned.
```

## Three Control Modes

### Offline Mode (Data Processing)

Process OME-TIFF stacks and Prairie XML metadata without PrairieView. Works on any
platform with Python. Capabilities:

- Parse Prairie XML metadata (scan parameters, timing, file references)
- Load OME-TIFF image stacks into numpy arrays
- Read voltage recording (.env) files
- Motion correction, ROI detection, signal extraction (via suite2p/CaImAn)

### API Mode (PrairieLink)

Programmatic control via PrairieLink COM/TCP interface. Requires PrairieView running
on Windows. Capabilities:

- Full acquisition control (T-series, Z-series, single image, line scan)
- Laser wavelength and power control
- PMT gain control
- Stage positioning (XYZ)
- Live image retrieval
- State queries

```python
# API mode example (Windows only)
import win32com.client
pl = win32com.client.Dispatch("PrairieLink64.Application")
pl.Connect("127.0.0.1", "0000")
pl.SendScriptCommands("-SetMultiphotonWavelength '920' 1")
pl.SendScriptCommands("-TSeries")
```

### GUI Mode (Computer Use)

Visual automation of the PrairieView desktop application via device-use. Requires
PrairieView visible on screen. Handles any operation accessible through the GUI.

## Capabilities

| Capability | Description |
|------------|-------------|
| Calcium imaging | In vivo time-series at 30 fps (resonant galvo) |
| Z-stacks | Structural volumetric imaging with piezo Z |
| Line scans | High temporal resolution 1D imaging |
| Tile scans | Large-area mosaics via motorized XY stage |
| Vasculature imaging | Surface vessel mapping for FOV registration |
| Multi-channel | Up to 4 simultaneous detection channels |
| Longitudinal | Cross-session FOV registration and cell tracking |

## Safety Level: CRITICAL

This device contains a Class 4 laser (>2.5 W, >200 kW peak) enclosed in a Class 1
system. Key safety rules:

- **ALWAYS** verify light box closed before enabling laser or PMTs
- **NEVER** expose GaAsP PMTs to ambient light at operating voltage
- **NEVER** bypass safety interlocks
- **ALWAYS** confirm cooling water flow before laser key-on
- **ALWAYS** wait for Pockels cell warmup (20-30 min)

See `docs/manual/safety_manual.md` for complete safety documentation.

## Directory Structure

```
devices/bruker-2p/
├── skill.yaml              # Device manifest
├── SOUL.md                 # AI agent personality
├── profile.yaml            # GUI automation profile
├── __init__.py             # Python package
├── README.md               # This file
│
├── docs/                   # Official documentation
│   ├── manual/             # Operator & safety manuals
│   │   ├── operator_manual.md
│   │   └── safety_manual.md
│   ├── api/                # PrairieLink programming reference
│   │   ├── prairielink_commands.md
│   │   ├── prairielink_states.md
│   │   └── com_interface.md
│   ├── specs/              # Hardware specifications
│   │   ├── hardware_specs.md
│   │   ├── laser_specs.md
│   │   └── objective_specs.md
│   ├── formats/            # Data file formats
│   │   ├── prairie_xml_schema.md
│   │   ├── ome_tiff_structure.md
│   │   └── voltage_recording.md
│   └── science/            # Domain science background
│       ├── two_photon_principles.md
│       ├── calcium_imaging.md
│       └── fov_registration.md
│
└── user/                   # Instance-specific operational data
    ├── MEMORY.md           # System #5010 operational notebook
    ├── system_config.md    # Hardware configuration
    ├── calibration_log.md  # Calibration records
    ├── protocols/          # Lab SOPs
    │   ├── longitudinal_calcium.md
    │   └── zstack_acquisition.md
    └── findings/           # Accumulated experimental findings
```

## Data Formats

| Format | Extension | Description |
|--------|-----------|-------------|
| OME-TIFF | `.ome.tif` | Single-page image files (one per frame per channel) |
| Prairie XML | `.xml` | Complete acquisition metadata |
| Voltage recording | `.env` | DAQ analog input recordings |
| Raw binary | `RAWDATA_*` | Uncompressed pixel data (optional) |

See `docs/formats/` for complete format documentation including parsing examples.

## Hardware

| Component | Specification |
|-----------|---------------|
| Laser | Coherent Chameleon Ultra II, 680-1080 nm, ~140 fs, 80 MHz |
| Detectors | Hamamatsu H7422PA-40 SEL GaAsP PMTs (x4) |
| Scanner | 8 kHz resonant + galvo, 30 fps at 512x512 |
| Objective | Nikon CFI75 16x/0.8 NA water-dipping, 3.0 mm WD |
| Piezo Z | 150 um range, 0.05 um step, 5 Hz stack rate |
| XY Stage | 6" x 3" travel, 0.3 um resolution |

See `docs/specs/` for detailed specifications.

## Dependencies

```
tifffile     # OME-TIFF reading
numpy        # Array operations
matplotlib   # Visualization
scikit-image # Image registration
lxml         # Prairie XML parsing (required for XML 1.1 support)
```

Optional (for full analysis pipeline):
```
suite2p      # Motion correction, ROI detection, signal extraction
caiman       # Alternative analysis pipeline (CNMF)
pywin32      # PrairieLink COM interface (Windows only)
```

## References

- Bruker Ultima Investigator Operator's Manual
- PrairieView Help Documentation (PrairieLink API)
- Coherent Chameleon Laser User Manual
- Hamamatsu H7422PA-40 PMT Datasheet
- Sheintuch et al. (2017). "Tracking the Same Neurons across Multiple Days in
  Ca2+ Imaging Data." Cell Reports.
- Pachitariu et al. (2017). "Suite2p: beyond 10,000 neurons with standard
  two-photon microscopy." bioRxiv.
- Giovannucci et al. (2019). "CaImAn: An open source tool for scalable Calcium
  Imaging data Analysis." eLife.
