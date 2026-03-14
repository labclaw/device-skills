# Micro-Manager Demo Plan

Last updated: 2026-03-13

Purpose: define how to build a complete `Micro-Manager` demo for `labclaw` that
plays the same strategic role that `TopSpin` plays today.

The bar is not "we can parse a TIFF". The bar is:

- no live microscope required
- acquisition path is real enough to exercise control logic
- output data is saved in production-like formats
- downstream processing and analysis can run on the result
- the entire flow is demoable for customers and repeatable in CI

## What "TopSpin-like" Means Here

For `TopSpin`, the important pattern is:

- software can be demonstrated meaningfully without a live instrument
- there is a believable data path for acquisition and processing
- the product story is end-to-end, not a disconnected parser demo

The `Micro-Manager` equivalent is not one single feature. It is the combination
of:

- `DemoCamera` plus the official demo configuration for synthetic microscope
  hardware
- `FakeCamera` for replaying realistic image content from disk
- `MMCore` / `pymmcore` for low-level control
- `pycro-manager` for acquisition orchestration and dataset handling
- `OME-TIFF` and `NDTiff` for downstream analysis

## Official Building Blocks

From official documentation:

- `DemoCamera` creates virtual demo devices across camera, filter wheel,
  light path, objective, stage, XY stage, autofocus, and shutter, and is
  explicitly described as useful for test-driving Micro-Manager without
  hardware.
- Micro-Manager's Python story centers on `pymmcore` / `pymmcore-plus` and
  `pycro-manager`.
- The recommended way to load devices is via a Micro-Manager config file such as
  `MMConfig_demo.cfg`.
- `pycro-manager` supports both GUI-attached use and headless mode.
- `pycro-manager` acquisitions save real datasets to disk and expose them
  through a `Dataset` API.
- Micro-Manager supports three main save formats: separate TIFFs, OME-TIFF image
  stacks, and `NDTiff`.
- `FakeCamera` can load arbitrary images from disk and act like a virtual camera.

This is enough to build a fully usable no-hardware demo.

## Demo Architecture

We should build the demo in two layers.

### Layer A: Synthetic Hardware Demo

Goal:

- Show a working microscope control and acquisition path immediately.

Mechanism:

- Install Micro-Manager.
- Load `MMConfig_demo.cfg`.
- Start `pycro-manager` or `pymmcore`.
- Run a time / channel / z acquisition.
- Save the dataset to disk.
- Process and analyze it through `device-skills`.

Why this matters:

- Fastest path to a believable "instrument control" story.
- Best fit for CI.
- Zero hardware dependency.

### Layer B: Replay-Realism Demo

Goal:

- Make the demo outputs look like real biology instead of abstract demo frames.

Mechanism:

- Use `FakeCamera` with curated input images on disk.
- Optionally vary images by stage position so XY moves look meaningful.
- Run the same acquisition pipeline as Layer A.

Why this matters:

- Closer to what `TopSpin` examdata does for NMR.
- Better for customer demos, screenshots, and downstream analysis quality.

## The Complete Demo Flow

### Demo 1: Headless End-to-End Baseline

This should be the first complete demo.

Flow:

1. Start Micro-Manager headlessly with the demo config.
2. Run a multi-dimensional acquisition from Python.
3. Save to disk in a format our processor supports.
4. Re-open the saved dataset.
5. Produce a structured summary.
6. Produce one or two visualization artifacts.
7. Feed the summary into a simple imaging brain prompt.

Why first:

- It is the smallest demo that proves the full product chain.
- It does not depend on GUI automation.
- It is testable in CI.

### Demo 2: Customer-Facing Realistic Demo

This should come right after Demo 1.

Flow:

1. Launch with `FakeCamera` or a realistic synthetic dataset source.
2. Run a scripted acquisition with channel, z, and XY variation.
3. Save to disk.
4. Show one acquisition preview and one analysis summary.
5. Optionally expose a simple UI or notebook wrapper for operator interaction.

Why second:

- Same architecture as Demo 1, but better storytelling quality.
- Better analog to the "TopSpin with examdata" experience.

## Recommended Technical Path

### Control Layer

Use two control surfaces, not one:

- `pymmcore-plus` or `pymmcore` for direct low-level control and config loading.
- `pycro-manager` for acquisition orchestration, saving, callbacks, and
  headless execution.

Reasoning:

- `pymmcore` is the simplest path for loading `MMConfig_demo.cfg`, discovering
  devices, and snapping images.
- `pycro-manager` is the right surface for multi-dimensional acquisition and
  dataset management.

### Data Layer

Support both:

- `OME-TIFF`
- `NDTiff`

Reasoning:

- `OME-TIFF` is the safer interoperability story for a broad ecosystem.
- `NDTiff` is the more native high-performance story for Micro-Manager and
  Pycro-Manager.

For the first demo, we should accept either, but strongly prefer supporting
`NDTiff` in the processor because that aligns with current Pycro-Manager usage.

### Processing Layer

The first `MicroManagerProcessor` should support:

- opening a saved dataset from disk
- reading summary metadata
- reading image planes by axis
- building a normalized imaging stack abstraction
- computing at least one projection or preview image
- exporting a compact text summary for LLM context

### Analysis Layer

The first `MicroManagerBrain` does not need to be fancy.

It should:

- read normalized stack metadata
- describe channels, time points, z planes, dimensions, and basic quality cues
- explain what was acquired in human-readable language
- make simple next-step suggestions

## Minimal Demo Script Shape

The first reproducible script should look conceptually like this:

```python
from pycromanager import Acquisition, multi_d_acquisition_events, start_headless

mm_app_path = "/path/to/Micro-Manager"
config_file = mm_app_path + "/MMConfig_demo.cfg"

start_headless(mm_app_path, config_file)

with Acquisition(directory="/tmp/demo_data", name="mm_demo", show_display=False) as acq:
    events = multi_d_acquisition_events(
        num_time_points=4,
        z_start=0,
        z_end=4,
        z_step=1,
        order="tz",
    )
    acq.acquire(events)

dataset = acq.get_dataset()
```

After that, our own processor should take over.

## Mapping to `device-skills`

### Files to Create

Initial target:

- `devices/micro-manager/skill.yaml`
- `devices/micro-manager/SOUL.md`
- `devices/micro-manager/profile.yaml`
- `devices/micro-manager/adapter.py`
- `devices/micro-manager/processor.py`
- `devices/micro-manager/brain.py`
- `devices/micro-manager/visualizer.py`
- `devices/micro-manager/tests/test_micro_manager.py`

### `MicroManagerAdapter`

Responsibilities:

- load a config file, defaulting to demo config when in simulation mode
- start headless or attach to a running server
- enumerate loaded devices
- run basic acquisitions through `pycro-manager`
- expose a stable `acquire()` and `list_datasets()` interface

### `MicroManagerProcessor`

Responsibilities:

- load `NDTiff` and `OME-TIFF`
- normalize metadata into a common imaging structure
- provide summary and preview utilities

### `MicroManagerBrain`

Responsibilities:

- consume processor outputs
- provide acquisition summary and lightweight interpretation

## Demo Milestones

### M1: Core Proof

Success means:

- `MMConfig_demo.cfg` loads
- a headless acquisition completes
- a dataset is saved to disk
- processor can open it

### M2: Full Pipeline Proof

Success means:

- `adapter.acquire()` produces data
- `processor.extract()` returns structured results
- `visualizer` creates one artifact
- `brain.analyze()` returns a readable report

### M3: Realistic Replay Proof

Success means:

- `FakeCamera` replays curated image content
- the same pipeline works unchanged
- the demo looks plausible to a microscopy user

### M4: Customer Demo Proof

Success means:

- one command or script runs the whole flow
- no hardware is required
- the output is stable enough for repeated demos

## Recommended Phase 1 Scope

Do now:

- headless demo config path
- `pycro-manager` acquisition
- saved dataset processing
- one summary artifact
- one visual artifact

Defer:

- broad GUI automation
- exotic plugins
- adaptive acquisition complexity
- hardware triggering complexity
- large-scale UI work

## Risks

### Risk 1: We stop at a notebook, not a product surface

Mitigation:

- Require the demo to run through `device-skills` adapter and processor classes,
  not only ad hoc notebook code.

### Risk 2: DemoCamera is too synthetic to impress users

Mitigation:

- Add a second-layer `FakeCamera` replay demo early.

### Risk 3: File-format support becomes fragmented

Mitigation:

- Normalize everything into a shared imaging stack abstraction from the start.

### Risk 4: We overbuild the GUI story too early

Mitigation:

- Make headless demo success the first gate.

## Concrete Recommendation

The first complete Micro-Manager demo for `labclaw` should be:

1. headless
2. simulation-first
3. driven by `MMConfig_demo.cfg`
4. acquired through `pycro-manager`
5. saved to disk in `NDTiff` or `OME-TIFF`
6. reopened by our processor
7. summarized and visualized by our own code

Then immediately after that, we should add:

8. a `FakeCamera` realism mode using curated biological images on disk

That combination is the closest Micro-Manager equivalent to the role `TopSpin`
plays for us today.

## Sources

- Micro-Manager homepage:
  https://micro-manager.org/
- DemoCamera:
  https://micro-manager.org/DemoCamera
- FakeCamera:
  https://micro-manager.org/FakeCamera
- Using the Micro-Manager python libraries:
  https://micro-manager.org/Using_the_Micro-Manager_python_library
- Micro-Manager file formats:
  https://micro-manager.org/Micro-Manager_File_Formats
- pycro-manager README:
  https://github.com/micro-manager/pycro-manager
- pycro-manager acquisitions overview:
  https://pycro-manager.readthedocs.io/en/latest/acq_overview.html
- pycro-manager API reference:
  https://pycro-manager.readthedocs.io/en/latest/apis.html
- pycro-manager saved image callbacks:
  https://pycro-manager.readthedocs.io/en/latest/image_saved_callbacks.html
- pycro-manager acquisition hooks:
  https://pycro-manager.readthedocs.io/en/latest/acq_hooks.html
