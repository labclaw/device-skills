# CLAUDE.md — Device Skills

## Project Overview

Modular, standardized device skills for labclaw & device-use. Each device is a self-contained
sub-package under `devices/` following a standard structure.

**Tech stack:** Python 3.11+, Pydantic 2.x, PyYAML, hatchling
**Consumers:** labclaw (brain), device-use (hands), labwork (desktop app)

## Build & Test

pip install -e ".[dev]"                          # core + dev tools
pip install -e ".[dev,biotek-gen5]"               # + plate reader
pip install -e ".[dev,bruker-topspin]"            # + NMR
pip install -e ".[dev,all]"                       # everything
pytest                                            # run all tests
ruff check .                                      # lint

## Architecture

Each device directory follows a standard structure:

    devices/<device-name>/
      skill.yaml       # Metadata, capabilities, interfaces (the manifest)
      SOUL.md          # Identity, quirks, safety notes
      MEMORY.md        # Calibration, maintenance, usage history
      profile.yaml     # GUI automation profile (for device-use)
      driver.py        # DeviceDriver impl (for labclaw hardware layer)
      adapter.py       # BaseAdapter impl (for device-use instrument layer)
      brain.py         # AI analysis logic (LLM-powered)
      processor.py     # Data processing pipeline
      visualizer.py    # Output/plotting
      README.md        # Full usage documentation
      tests/           # Per-device tests

## Key Abstractions

- `SkillManifest` (Pydantic) — parsed from skill.yaml, defines device identity + capabilities
- `BaseAdapter` — ABC for instrument adapters (connect, acquire, process)
- `BaseBrain` — ABC for AI analysis (analyze, summarize)
- `BaseProcessor` — ABC for data processing (load, transform, extract)
- `load_manifest(path)` — load a skill.yaml into SkillManifest
- `discover_skills(dir)` — discover all available device skills

## Code Style

- Same as labclaw: ruff (E,F,I,N,W,UP), line-length 100
- `from __future__ import annotations` in every module
- Type hints on all public functions
- Pydantic models for all schemas

## Adding a New Device

1. Copy `devices/_template/` to `devices/<device-name>/`
2. Fill in `skill.yaml` with device metadata
3. Fill in `SOUL.md` with identity and quirks
4. Implement `adapter.py`, `processor.py`, etc.
5. Add tests in `tests/`
6. Add optional extra in `pyproject.toml` if device needs special deps
7. Submit PR
