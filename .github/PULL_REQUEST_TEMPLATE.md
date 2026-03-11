## Summary

## Changes

## Validation
- [ ] `make lint` passes
- [ ] `make test` passes
- [ ] New device follows template structure
- [ ] SOUL.md updated if device behavior changed

## New Device Checklist (if adding a device)
- [ ] `skill.yaml` manifest created
- [ ] `adapter.py` inherits `BaseAdapter`
- [ ] `processor.py` inherits `BaseProcessor`
- [ ] `brain.py` inherits `BaseBrain`
- [ ] `driver.py` inherits `BaseDriver`
- [ ] Tests added in `devices/<name>/tests/`
- [ ] SOUL.md written with domain knowledge
