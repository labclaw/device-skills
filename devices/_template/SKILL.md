---
name: "my-device"
description: "TODO: Comprehensive description including device type, vendor, model, measurement capabilities, data formats, and use cases. This description determines when Claude activates this skill."
---

<!-- SKILL.md — The operational guide Claude reads when using this device.
     Unlike SOUL.md (identity/personality) and README.md (human developer docs),
     SKILL.md tells the AI agent HOW to operate the device step by step.

     Fill in each section below. Remove sections that don't apply.
     Replace all TODO placeholders with device-specific content. -->

# [Device Name] — Skill Guide

> This file is the primary operational reference for AI agents controlling this device.
> It covers control modes, workflows, safety constraints, and code patterns.

## Control Modes

<!-- List which control modes this device supports.
     Not every device supports all three — remove rows that don't apply.
     See skill.yaml `control_modes` for the canonical list. -->

### API Mode

<!-- TODO: Direct programmatic control (gRPC, REST, SDK, serial).
     - What library or protocol is used?
     - What host/port does it listen on?
     - What authentication is needed?
     - Delete this section if the device has no API. -->

- **Protocol:** TODO (e.g., gRPC on localhost:3081, REST on :8080, serial /dev/ttyUSB0)
- **Library:** TODO (e.g., `bruker.api.topspin.Topspin()`, `requests`, `pyserial`)
- **Authentication:** TODO (e.g., none, API key, token)
- **Connect snippet:**

```python
from devices.<device_name>.adapter import DeviceAdapter

adapter = DeviceAdapter()
adapter.connect()  # TODO: document what happens on connect
```

### GUI Mode

<!-- TODO: Visual automation via device-use (Computer Use / A11y / Script layers).
     - What software must be running?
     - What are the key UI elements (command bar, menus, buttons)?
     - What commands or actions does the AI type/click?
     - Delete this section if the device has no GUI. -->

- **Software:** TODO (e.g., TopSpin 5.x, Gen5 3.x)
- **Key UI elements:** TODO (e.g., command bar at bottom, File menu, Run button)
- **Common commands:** TODO (list the most-used commands/clicks)

### Offline Mode

<!-- TODO: Processing existing data files without the device or its software.
     - What file formats can be loaded?
     - What processing library is used?
     - What are the limitations vs. API/GUI mode? -->

- **Supported formats:** TODO (e.g., .csv, .fid, .tif, .xlsx)
- **Processing library:** TODO (e.g., nmrglue, pandas, tifffile)
- **Limitations:** TODO (e.g., cannot acquire new data, no real-time control)

## Workflows

<!-- Define the standard workflows this device supports.
     Each workflow should describe: trigger conditions, steps, expected output.
     These workflows map to adapter/processor method calls. -->

### Acquire

<!-- TODO: How to start a new measurement or experiment.
     When is this workflow used? What parameters does it accept?
     Delete if the device only supports offline processing. -->

**When:** TODO (e.g., user requests a new measurement, protocol calls for data collection)

**Steps:**
1. TODO: Connect to device (`adapter.connect()`)
2. TODO: Configure parameters (`adapter.acquire(param=value)`)
3. TODO: Wait for acquisition to complete
4. TODO: Verify data was collected

**Code:**

```python
adapter = DeviceAdapter()
adapter.connect()
# TODO: fill in acquisition parameters
raw_data = adapter.acquire(
    # param1="value1",
    # param2="value2",
)
```

**Output:** TODO (e.g., raw FID file, CSV with absorbance readings, TIFF image stack)

### Process

<!-- TODO: How to transform raw data into usable results.
     This maps to the BaseProcessor pipeline: load -> transform -> extract. -->

**When:** TODO (e.g., after acquisition, when user provides a data file)

**Steps:**
1. TODO: Load raw data (`processor.load(path)`)
2. TODO: Apply transforms (`processor.transform(raw)`) — list specific transforms
3. TODO: Extract results (`processor.extract(processed)`)

**Code:**

```python
from devices.<device_name>.processor import DeviceProcessor

processor = DeviceProcessor()
raw = processor.load("/path/to/data")
processed = processor.transform(raw)
results = processor.extract(processed)
# results is a dict with keys: TODO (list expected keys)
```

**Output:** TODO (e.g., dict with peaks, concentrations, images)

### Analyze

<!-- TODO: AI-powered interpretation of processed results.
     This maps to BaseBrain.analyze() and BaseBrain.summarize(). -->

**When:** TODO (e.g., after processing, when user asks "what does this data mean?")

**Code:**

```python
from devices.<device_name>.brain import DeviceBrain

brain = DeviceBrain()
interpretation = brain.analyze(results, context="TODO: what context helps")
summary = brain.summarize([interpretation])
```

**Output:** TODO (e.g., natural language interpretation, compound identification, quality assessment)

## Safety

<!-- TODO: Fill in safety constraints for this device.
     Delete this section only if safety_level is "normal" AND there are
     no physical hazards. When in doubt, keep the section. -->

- **Safety level:** TODO (normal / strict / critical — must match skill.yaml)
- **Physical hazards:** TODO (e.g., high voltage, radiation, cryogens, biohazard, lasers)
- **Parameter bounds:** TODO (e.g., max temperature 300C, max voltage 5V, max RPM 14000)
- **Actions requiring confirmation:** TODO (e.g., long acquisitions, high-power settings)
- **Emergency stop:** TODO (e.g., hardware E-stop button, software abort command, `adapter.disconnect()`)
- **Never do:** TODO (e.g., never change X while Y is running, never exceed Z parameter)

## Progressive Disclosure

<!-- This section tells the AI agent where to find deeper knowledge.
     The agent reads SKILL.md first for operational guidance, then drills
     into docs/ and user/ only when it needs more detail. -->

### Official Documentation (`docs/`)

| Directory | What's There | When to Read |
|-----------|-------------|--------------|
| `docs/manual/` | TODO: Operator and safety manuals | Setting up, troubleshooting, safety questions |
| `docs/api/` | TODO: Programming interface reference | Writing adapter code, understanding commands |
| `docs/specs/` | TODO: Hardware specifications | Checking device limits, capabilities |
| `docs/formats/` | TODO: Data file format documentation | Parsing raw data, understanding file structure |
| `docs/science/` | TODO: Domain science background | Interpreting results, explaining to users |
| `docs/commands/` | TODO: Command reference | Looking up specific device commands |
| `docs/guides/` | TODO: Step-by-step guides | Complex workflows, advanced usage |

### User Knowledge (`user/`)

| File | What's There | When to Read |
|------|-------------|--------------|
| `user/MEMORY.md` | Operational history, calibration notes, quirks discovered | Before any operation — check for known issues |
| `user/system_config.md` | This specific instrument's configuration | On connect — verify expected setup |
| `user/calibration_log.md` | Calibration event records | Before quantitative measurements |
| `user/protocols/` | Lab-specific SOPs and workflows | When user references a protocol by name |
| `user/findings/` | Accumulated experimental findings | When analyzing similar samples |

## Data Formats

<!-- TODO: Document the primary data formats this device produces and consumes.
     Include enough detail that the processor can be implemented from this spec. -->

### Input

- TODO: Format name, file extension, structure description

### Output

- TODO: Format name, file extension, structure description

<!-- Example (delete when filling in):
**Input:**
- Bruker FID — binary file named `fid`, 32-bit complex float pairs, little-endian. Parameters in `acqus` text file.
- JCAMP-DX — ASCII spectrum export, one (X,Y) pair per line.

**Output:**
- Processed spectrum as NumPy array via `processor.process()`
- PNG plot via `visualizer.plot_spectrum()`
- CSV peak table via `processor.pick_peaks()`
-->

## Known Quirks

<!-- Critical quirks that affect specific workflow steps should ALSO be called out inline
in that step, not only listed here. This section is for cross-cutting or startup quirks
that don't belong to a single workflow. -->

<!-- TODO: Device-specific gotchas that affect how the AI operates.
     These should be things the AI needs to know to avoid mistakes.
     More detailed quirks go in SOUL.md; operational ones go here. -->

- TODO: Quirk 1 and its workaround
- TODO: Quirk 2 and its workaround
