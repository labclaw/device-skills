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

## Two-Version Product Strategy

We should explicitly build two demo versions on top of one shared core.

### Version A: API / Headless Demo

Purpose:

- real execution path
- repeatable end-to-end pipeline
- CI and local developer workflow
- operational baseline we trust

What the user sees:

- structured progress logs
- saved dataset on disk
- generated preview image
- generated summary report

Primary value:

- this is the "truth path"
- fastest path to a stable MVP
- best path for automated testing

### Version B: GUI / CUA Demo

Purpose:

- customer-facing visual demonstration
- operator-friendly story
- closer experiential match to the way `TopSpin` demos feel

What the user sees:

- the Micro-Manager GUI opens
- CUA interacts with visible controls
- acquisition starts from the GUI surface
- images and results update in a visible way
- the same downstream processor and report run at the end

Primary value:

- better sales demo
- easier for a user to understand than a terminal-only flow
- useful later as a guided operator surface

### Critical Design Rule

Version B must not become a separate implementation stack.

The correct architecture is:

- shared acquisition and processing core
- API / headless path executes directly
- GUI / CUA path is a presentation and control wrapper over the same core

If GUI mode has separate business logic, it will drift and become unreliable.

## Shared Core Architecture

Both versions should share the same internal layers.

### Shared Layer 1: Environment Bootstrap

Responsibilities:

- locate Micro-Manager install
- select runtime mode: native GUI, headless, or GUI-attached
- select config file
- select simulation source: `DemoCamera` or `FakeCamera`

### Shared Layer 2: Control Backend

Responsibilities:

- load config
- expose device list
- snap / acquire through Python interfaces
- save datasets
- report progress and errors

Recommended split:

- `pymmcore-plus` for config and direct device access
- `pycro-manager` for acquisition orchestration and dataset handling

### Shared Layer 3: Data Pipeline

Responsibilities:

- reopen saved dataset
- normalize metadata
- generate summary
- generate preview images
- feed brain / report layer

### Shared Layer 4: Presentation

Mode-specific:

- API version presents logs, artifacts, and summaries
- GUI / CUA version presents windows, visible interactions, and the same
  output artifacts at the end

## Deployment Decision: Native macOS First, VM Optional Later

For MVP, the preferred deployment is native macOS.

Reasoning:

- Micro-Manager supports macOS directly.
- The no-hardware demo story does not require virtualization.
- Native setup is less fragile than GUI automation through a VM display stack.
- Headless and GUI-attached Python integration are easier to debug natively.

VM should be treated as optional later packaging, not the first target.

Use VM only if we later need:

- tightly isolated demo environments
- controlled customer-facing appliance packaging
- a reproducible GUI automation box that should not depend on the host machine

The same principle applies as with `TopSpin`: VM can help packaging, but it
should not define the architecture.

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

### Demo 3: GUI / CUA Customer Walkthrough

This should follow only after Demo 1 is stable and Demo 2 has credible image
content.

Flow:

1. Launch Micro-Manager GUI on macOS.
2. Use CUA to activate the window and navigate to a prepared acquisition setup.
3. Trigger the acquisition from visible controls.
4. Let the shared backend save the dataset.
5. Run the same processor / visualizer / brain path as the API version.
6. Present a final report with links to saved artifacts.

Why third:

- it improves sales and operator trust
- but it should never precede the stable API baseline
- otherwise we risk building a nice-looking demo with weak execution integrity

## API / Headless Demo Design

### User Story

"Run one command and show that labclaw can operate a simulated microscope,
produce data, and analyze the result without any hardware."

### Inputs

- Micro-Manager install path
- config file path, defaulting to `MMConfig_demo.cfg`
- acquisition recipe:
  - channels
  - time points
  - z range
  - output directory

### Outputs

- saved dataset path
- JSON-like acquisition summary
- preview image path
- short report text

### How To Show Effect

Even without GUI, the effect is visible through:

- progress logs during acquisition
- event counters
- one live or post-run preview image
- one structured summary at the end
- saved artifacts on disk

This is enough for engineering validation and internal demos.

### MVP Commands

The first runnable interface should be a script such as:

```bash
python devices/micro-manager/demo_headless.py --output /tmp/mm-demo
```

And optionally a repo-level wrapper later:

```bash
make micromanager-demo
```

## GUI / CUA Demo Design

### User Story

"Show a user that labclaw can visibly operate Micro-Manager like an operator,
while still producing a real saved dataset and downstream analysis."

### Requirements

- Micro-Manager GUI installed and runnable on macOS
- a stable demo configuration
- a prepared acquisition layout with limited branching
- screenshot / accessibility / input permissions configured

### Recommended Interaction Model

Do not let CUA improvise across the entire GUI.

Instead:

- predefine the acquisition workspace
- restrict the GUI flow to a small number of stable actions
- use CUA mainly for:
  - app activation
  - config selection
  - acquisition start
  - confirming completion state

If we later find useful accessibility hooks on macOS, they should be preferred
over purely visual automation.

### How To Show Effect

GUI mode should show:

- the Micro-Manager window
- visible acquisition starting
- image updates or acquisition counters
- final preview artifact and report outside or alongside the app

### What GUI Mode Should Not Own

GUI mode should not own:

- dataset parsing
- metadata normalization
- report generation
- acquisition semantics beyond the visible launch sequence

Those all belong in the shared core.

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

For GUI mode:

- the CUA layer should invoke a bounded orchestration command or adapter method,
  not duplicate acquisition logic through clicks alone
- the GUI path should be thought of as "visible initiation and monitoring"
  rather than "all logic lives in the GUI"

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

## GUI / CUA Script Shape

The GUI wrapper should conceptually look like this:

```python
adapter = MicroManagerAdapter(mode="gui", simulation="demo")
adapter.connect()
adapter.prepare_demo_workspace()
adapter.launch_gui()

# CUA performs a bounded set of visible actions:
# - focus app
# - confirm config
# - start acquisition

result = adapter.acquire(recipe)
summary = adapter.process(result["dataset_path"])
report = adapter.summarize(summary)
```

In other words, GUI mode still delegates to the same adapter contract.

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
- start headless, attach to a running server, or coordinate GUI mode
- enumerate loaded devices
- run basic acquisitions through `pycro-manager`
- expose a stable `acquire()` and `list_datasets()` interface
- expose progress events for both API and GUI presentation layers

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

### M4: GUI / CUA Demo Proof

Success means:

- Micro-Manager GUI launches and is controllable in a bounded workflow
- CUA can reliably start the prepared demo acquisition
- the same downstream pipeline runs after acquisition
- GUI mode does not fork business logic away from API mode

### M5: Customer Demo Proof

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
- GUI demo design and contract definition

Do shortly after MVP:

- bounded GUI / CUA wrapper over the same core
- prepared workspace for customer walkthroughs
- optional `FakeCamera` realism mode

Defer:

- broad open-ended GUI automation
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

### Risk 5: GUI mode drifts away from API mode

Mitigation:

- enforce one shared adapter contract
- keep GUI mode as a thin wrapper
- test that GUI mode and API mode produce the same structured result shape

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
9. a bounded GUI / CUA walkthrough that triggers the same core pipeline

That combination is the closest Micro-Manager equivalent to the role `TopSpin`
plays for us today.

## Build Sequence

### Week 1

- prove native macOS install
- prove headless demo config acquisition
- define output format choice

### Week 2

- implement `MicroManagerAdapter`
- implement `MicroManagerProcessor`
- implement one visual artifact and one summary report

### Week 3

- add `FakeCamera` realism path
- harden dataset reopening and normalization
- package one command end-to-end demo

### Week 4

- implement bounded GUI / CUA wrapper
- script the prepared workspace walkthrough
- validate that GUI mode still uses the same result pipeline

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
