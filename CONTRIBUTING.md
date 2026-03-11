# Contributing to device-skills

## Setup

```bash
git clone git@github.com:labclaw/device-skills.git
cd device-skills
pip install -e ".[dev]"
pre-commit install
```

## Adding a New Device

1. Copy the template:
   ```bash
   cp -r devices/_template devices/<device-name>
   ```
2. Fill in `skill.yaml` with device metadata (name, manufacturer, capabilities).
3. Write `SOUL.md` with device identity, quirks, and safety notes.
4. Implement the required modules:
   - `adapter.py` — inherits `BaseAdapter` (connect, acquire, process)
   - `processor.py` — inherits `BaseProcessor` (load, transform, extract)
   - `brain.py` — inherits `BaseBrain` (analyze, summarize)
   - `driver.py` — inherits `BaseDriver` (labclaw hardware layer)
5. Add tests in `devices/<device-name>/tests/`.
6. If the device needs extra dependencies, add an optional extra in `pyproject.toml`.
7. Run validation:
   ```bash
   make lint
   make test
   ```

## Branch Naming

- `feat/<description>` — new features or devices
- `fix/<description>` — bug fixes

## Commit Format

Use [Conventional Commits](https://www.conventionalcommits.org/):

- `feat(bruker-topspin): add 2D processing pipeline`
- `fix(biotek-gen5): handle missing well data`
- `chore: update ruff config`
- `docs: add plate reader usage guide`

## Code Style

- Python 3.11+
- `from __future__ import annotations` in every module
- Type hints on all public functions
- Pydantic models for all schemas
- Linting: `ruff` with rules E, F, I, N, W, UP (line-length 100)

## Pull Request Process

1. Create a focused branch from `main`.
2. Make small, atomic commits.
3. Ensure `make lint` and `make test` pass.
4. Fill in the PR template completely.
5. Request review from `@labclaw/core-team`.
