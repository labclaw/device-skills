# device-skills

Modular, standardized device skills for [labclaw](https://github.com/labclaw/labclaw) and [device-use](https://github.com/labclaw/device-use).

Each lab instrument gets a self-contained skill package with everything needed to operate it:

- **Identity** (SOUL.md) — what it is, what it can do, known quirks
- **Memory** (MEMORY.md) — calibration history, maintenance log, usage patterns
- **GUI Profile** (profile.yaml) — screen layout, workflows, safety bounds for GUI automation
- **Driver** (driver.py) — labclaw DeviceDriver implementation
- **Adapter** (adapter.py) — device-use BaseInstrument implementation
- **Brain** (brain.py) — AI-powered analysis and interpretation
- **Processor** (processor.py) — raw data processing pipeline
- **Visualizer** (visualizer.py) — publication-quality output

## Install

    pip install device-skills                     # core only
    pip install device-skills[biotek-gen5]         # + plate reader
    pip install device-skills[bruker-topspin]      # + NMR
    pip install device-skills[all]                 # everything

## Usage

    from device_skills import load_manifest, discover_skills

    # Discover available devices
    for skill in discover_skills():
        print(f"{skill.name} ({skill.category})")

    # Load a specific device manifest
    from pathlib import Path
    manifest = load_manifest(Path("devices/biotek_gen5/skill.yaml"))
    print(manifest.capabilities)

## Adding a Device

Copy `devices/_template/` → `devices/your-device/`, fill in the files, add tests, submit PR.

## Roadmap

See [ROADMAP.md](ROADMAP.md) for the simulation-first imaging expansion plan and
[TODO.md](TODO.md) for the active worklist. See
[PHASE1_SHORTLIST.md](PHASE1_SHORTLIST.md) for the narrow first-wave set that is
actually suitable for immediate `labclaw` focus.

## How It Fits Together

    ┌─────────────────────────────────────────┐
    │           device-skills                  │
    │   One directory per device, standard     │
    └────────┬───────────────────┬─────────────┘
             │                   │
       labclaw imports     device-use imports
       driver, SOUL,       profile, adapter,
       MEMORY              brain
             │                   │
             ▼                   ▼
        LABCLAW (brain)    DEVICE-USE (hands)
             │                   │
             └─────┬─────────────┘
                   │ both exposed via MCP
                   ▼
              LABWORK (desktop app)

## License

Apache 2.0
