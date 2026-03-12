---
name: "bruker-2p"
description: "Operate a Bruker Ultima Investigator two-photon fluorescence microscope via PrairieView/PrairieLink. Use this skill for: calcium imaging (GCaMP, tdTomato), z-stack acquisition, time-series recording, line-scan, tile-scan, vasculature imaging, OME-TIFF processing, Prairie XML metadata parsing, in vivo brain imaging, motion correction, FOV registration across sessions. Control modes: API (PrairieLink COM/TCP), GUI (Computer Use), Offline (data processing only). Safety-critical Class 4 laser system."
---

# Bruker Ultima Investigator Two-Photon Microscope

Read `SOUL.md` for device identity, quirks, and safety personality before first use.

## Safety — Read Before Anything Else

These rules are non-negotiable. Violating them causes permanent hardware damage or injury.

- **NEVER open the light box enclosure while PMTs are at operating gain.** GaAsP PMTs (H7422PA-40 SEL) are permanently degraded by ambient light exposure. Set gain to 0 first.
- **NEVER bypass interlocks.** Side panels, back panels, and primary dichroic all have safety interlocks protecting against Class 4 laser exposure.
- **ALWAYS verify cooling water is flowing at 25C** before powering the Ti:Sapphire laser. No cooling = crystal damage.
- **ALWAYS wait 20-30 min for Pockels cell warmup** before quantitative imaging. Skipping this causes power drift and uneven illumination.
- **Start laser power low.** Begin at 5-10% Pockels (20-30 mW at sample). Increase only as needed. Typical imaging: 20-60 mW.
- **Never look into the objective or any beam port** while the laser is enabled.

For full startup/shutdown procedures, read `docs/manual/operator_manual.md`.
For laser classification and safety details, read `docs/manual/safety_manual.md`.

## Three Control Modes

### API Mode — PrairieLink (fastest, recommended for automation)

Connect to running PrairieView via COM or TCP. Windows only.

```python
from devices.bruker_2p.adapter import TwoPhotonAdapter

adapter = TwoPhotonAdapter(data_dir="/path/to/data", mode="api", password="0000")
adapter.connect()  # COM: win32com.client.Dispatch("PrairieLink64.Application")

# Stage control
pos = adapter.get_motor_position()  # {"x": ..., "y": ..., "z": ...} in microns
adapter.set_motor_position("z", -250.0)

# Laser
adapter.set_laser_wavelength(920)  # 680-1080 nm range

# Acquisition
adapter.acquire(mode="tseries")   # or: "zseries", "single", "linescan"
adapter.start_tseries()           # convenience method
adapter.start_zseries()
adapter.abort()                   # stop current acquisition
```

TCP connection uses port 1236. Default password is "0000" (find it in PrairieView: Tools > Scripts > Edit Scripts, bottom-left).

For the full command set, read `docs/api/prairielink_commands.md`.
For COM interface details, read `docs/api/com_interface.md`.
For state queries, read `docs/api/prairielink_states.md`.

### GUI Mode — Computer Use (visual automation)

PrairieView must be visible on screen. The device-use operator layer handles screenshot-to-action via VLM. Not yet fully implemented in the adapter — use the device-use operator framework directly.

### Offline Mode — Data Processing Only (works anywhere)

No PrairieView or microscope needed. Parse existing datasets on any platform.

```python
adapter = TwoPhotonAdapter(data_dir="/path/to/experiments", mode="offline")
adapter.connect()  # always succeeds

# List available datasets (directories with XML + TIFFs)
datasets = adapter.list_datasets()
# [{"path": "...", "name": "...", "xml_file": "...", "num_tiffs": 18000}, ...]

# Process a dataset
stack = adapter.process("/path/to/experiment_001")
# Returns ImagingStack with frames, metadata, scan parameters
```

## Core Workflow: Acquire -> Process -> Analyze

### 1. Acquire (API/GUI mode)

Set wavelength for your indicator, position the FOV, then start acquisition.

| Indicator | Wavelength | Typical Power | Notes |
|-----------|-----------|---------------|-------|
| GCaMP6f/s | 920 nm | 20-60 mW | Most common calcium indicator |
| tdTomato | 1040 nm | 30-80 mW | Red structural marker |
| Structural dyes | 800 nm | 10-30 mW | Vasculature reference |

Resonant galvo: 30 fps (8 kHz), fixed line time, bidirectional. Use for time-series.
Galvo-galvo: slower, arbitrary dwell time, unidirectional. Use for z-stacks and tile scans.

### 2. Process (any mode)

The processor implements a three-step pipeline: `load -> transform -> extract`.

```python
from devices.bruker_2p.processor import TwoPhotonProcessor

proc = TwoPhotonProcessor()

# Step 1: Load — parse XML metadata, discover TIFF files
raw = proc.load("/path/to/dataset")
# {"metadata": {...}, "data_dir": Path, "tiff_files": [...]}

# Step 2: Transform — load frames into ImagingStack
stack = proc.transform(raw)
# ImagingStack with: frames, frame_rate, pixels_per_line, lines_per_frame,
#   microns_per_pixel_x/y, objective, laser_wavelength, laser_power, scan_mode

# Step 3: Extract — summary dict with max projection
summary = proc.extract(stack)
# {"num_frames": 18000, "frame_rate": 30.0, "max_projection": ndarray, ...}

# Utilities
max_proj = proc.max_projection(stack, channel=1)  # 2D ndarray
text_summary = proc.get_stack_summary(stack)       # human-readable string
```

**Critical quirk:** PrairieView writes XML 1.1 headers but Python's stdlib parser only supports XML 1.0. The processor uses `lxml.etree` with `recover=True` internally. If you parse XML manually, you MUST do the same — stdlib `xml.etree.ElementTree` will silently return empty results.

**Data volume warning:** Each frame is a separate OME-TIFF file. A 10-min T-series at 30 fps = ~18,000 files, ~2.8 GB/min. Plan storage and I/O accordingly.

For XML schema details, read `docs/formats/prairie_xml_schema.md`.
For OME-TIFF structure, read `docs/formats/ome_tiff_structure.md`.
For voltage recording format, read `docs/formats/voltage_recording.md`.

### 3. Analyze (AI interpretation)

The brain uses Claude to interpret imaging data. Falls back to cached demo responses when `ANTHROPIC_API_KEY` is not set.

```python
from devices.bruker_2p.brain import TwoPhotonBrain

brain = TwoPhotonBrain()  # uses claude-sonnet-4-20250514 by default

# General analysis
result = brain.analyze({"stack": stack}, context="V1 cortex, layer 2/3, GCaMP6f")

# Activity interpretation (with ROIs)
result = brain.interpret_activity(stack, rois=detected_rois, context="barrel cortex")

# Parameter suggestions
params = brain.suggest_imaging_params("GCaMP6s in hippocampus CA1")

# Cross-session comparison
comparison = brain.compare_sessions(session1_meta, session2_meta)

# Summarize multiple findings
summary = brain.summarize([result1, result2, result3])
```

### 4. Visualize

```python
from devices.bruker_2p.visualizer import (
    plot_max_projection,
    plot_fov_overlay,
    plot_calcium_traces,
)

# Max intensity projection with scale bar and metadata
plot_max_projection(stack, output_path="max_proj.png", channel=1)
plot_max_projection(stack, output_path=None)  # returns PNG bytes

# FOV overlay for cross-session registration (magenta=reference, green=current)
plot_fov_overlay(ref_image, current_image, output_path="overlay.png")

# Calcium traces (DF/F) for detected ROIs
plot_calcium_traces(rois, frame_rate=30.0, output_path="traces.png", max_rois=10)
```

## Driver Interface (for labclaw)

The driver wraps the adapter for labclaw's HardwareManager. Commands are sent via `write()`, results read via `read()`.

```python
from devices.bruker_2p.driver import TwoPhotonDriver

driver = TwoPhotonDriver(config={"mode": "offline", "data_dir": "/data"})
await driver.connect()

await driver.write({"action": "list_datasets"})
result = await driver.read()  # {"datasets": [...]}

await driver.write({"action": "process", "path": "/data/experiment_001"})
result = await driver.read()  # {"num_frames": ..., "frame_rate": ..., ...}

# API mode only:
await driver.write({"action": "tseries"})
await driver.write({"action": "zseries"})
await driver.write({"action": "abort"})
```

## Key Data Types

- **`ImagingStack`** — Collection of frames with metadata (frame_rate, resolution, laser params, scan mode)
- **`CalciumFrame`** — Single frame: `data` (2D ndarray), `timestamp`, `channel`, `plane_index`
- **`ROI`** — Detected cell: `id`, `x_center`, `y_center`, `mask` (binary ndarray), `trace` (1D ndarray)

## Reference Documentation

Read these on demand, not upfront:

| When you need to... | Read |
|---------------------|------|
| Send PrairieLink commands | `docs/api/prairielink_commands.md` |
| Use the COM interface | `docs/api/com_interface.md` |
| Query instrument state | `docs/api/prairielink_states.md` |
| Parse Prairie XML files | `docs/formats/prairie_xml_schema.md` |
| Understand OME-TIFF layout | `docs/formats/ome_tiff_structure.md` |
| Handle voltage recordings | `docs/formats/voltage_recording.md` |
| Start up / shut down the system | `docs/manual/operator_manual.md` |
| Review laser safety protocols | `docs/manual/safety_manual.md` |
| Configure laser parameters | `docs/specs/laser_specs.md` |
| Select objectives | `docs/specs/objective_specs.md` |
| Check hardware limits | `docs/specs/hardware_specs.md` |
| Understand two-photon physics | `docs/science/two_photon_principles.md` |
| Design calcium imaging experiments | `docs/science/calcium_imaging.md` |
| Register FOVs across sessions | `docs/science/fov_registration.md` |

## Common Pitfalls

1. **XML parsing fails silently** — Use `lxml` with `recover=True`, never stdlib `xml.etree`.
2. **Piezo Z hysteresis** — Always approach target Z from the same direction. Configure unidirectional stepping for z-stacks.
3. **Resonant vs galvo confusion** — Resonant = fast (30 fps) but fixed parameters, bidirectional artifacts. Galvo = slow but flexible, no artifacts.
4. **Massive file counts** — Each frame is a separate TIFF. Use `list_datasets()` to survey before loading.
5. **Windows only for live control** — API and GUI modes require PrairieView on Windows. Plan remote access (RDP/VNC/SSH tunnel).
6. **PrairieLink password** — Default "0000". Find it in PrairieView: Tools > Scripts > Edit Scripts.

## User Data

Mutable instance-specific data lives in `user/`:
- `user/MEMORY.md` — Session log, anomalies, maintenance history
- `user/system_config.md` — Current hardware configuration
- `user/calibration_log.md` — Calibration records
- `user/protocols/` — Saved acquisition protocols
- `user/findings/` — Analysis results and discoveries
