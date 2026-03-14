# Plan Closeout

Last updated: 2026-03-13

Purpose: close the current planning phase cleanly and prepare the project for
 implementation without further scope drift.

This document is the project-level wrap-up for the current strategy work. It
 compresses the key decisions, defines what still must be checked, and sets the
 exit criteria for moving from planning into build execution.

## What Is Now Decided

These decisions are no longer open:

- `Micro-Manager` is the first new microscopy software target.
- `ScanImage` is the second new microscopy software target.
- `Bruker TopSpin` and `Biotek Gen5` remain part of the Phase 1 product surface.
- `Bruker 2P` is an internal validation rig, not the main outward-facing
  expansion wedge.
- Greater Boston is the first commercial beachhead.
- Simulation-first is a hard requirement for new microscopy software skills.
- `Micro-Manager` will be built in two versions:
  - `API / headless` first
  - `GUI / CUA` second
- The first `Micro-Manager` MVP will be:
  - native macOS
  - `DemoCamera`
  - `MMConfig_demo.cfg`
  - `NDTiff` first
  - one complete `acquire -> save -> process -> visualize -> summarize` loop

## Source Documents

The current plan package is:

- [ROADMAP.md](ROADMAP.md)
- [TODO.md](TODO.md)
- [PHASE1_SHORTLIST.md](PHASE1_SHORTLIST.md)
- [MARKET_BOSTON.md](MARKET_BOSTON.md)
- [MICROMANAGER_DEMO.md](MICROMANAGER_DEMO.md)

These documents should now be treated as the active planning baseline.

## Scope Freeze For MVP

The following items are inside the first executable MVP:

- native macOS `Micro-Manager` install
- headless acquisition
- demo config path
- `NDTiff` dataset save and reopen
- `device-skills` adapter / processor / visualizer / brain path
- one repeatable end-to-end demo command

The following items are explicitly outside the MVP:

- VM-first packaging
- broad GUI automation
- open-ended CUA flows
- `OME-TIFF` parity on day one
- `FakeCamera` realism on day one
- deep commercial platform expansion before `Micro-Manager` works

## Project-Level Closeout Checklist

Before implementation begins, the project should satisfy all items below.

### 1. Decision Alignment

- [x] README points to the authoritative planning documents.
- [x] TODO matches roadmap and shortlist decisions.
- [x] Micro-Manager dual-mode strategy is documented in one place.
- [x] Phase 1 device set is explicit and stable.

### 2. MVP Boundary Clarity

- [x] The first build target is only `API / headless`.
- [x] The first saved format is only `NDTiff`.
- [x] GUI / CUA is documented as a wrapper, not a second stack.
- [x] `FakeCamera` is explicitly post-MVP.

### 3. Technical Validation Gates

- [ ] Confirm Micro-Manager installs and launches on macOS.
- [ ] Confirm `MMConfig_demo.cfg` loads successfully.
- [ ] Confirm `pycro-manager` headless acquisition works on the chosen setup.
- [ ] Confirm saved `NDTiff` can be reopened programmatically.
- [ ] Confirm we can extract enough metadata to build a normalized imaging
      object.

### 4. Repo Hygiene

- [ ] Planning docs are pushed to GitHub.
- [x] Unrelated local changes are identified and not mixed into the next
      implementation commit.
- [ ] The next code implementation starts from a clean, intentional commit
      boundary.

### 5. Implementation Package Readiness

- [x] We know which files must be created under `devices/micro-manager/`.
- [ ] We know which external dependencies are required.
- [x] We know the first demo command we want to support.
- [x] We know the first automated tests we want to add.

### 6. Commercial Readiness

- [x] We can explain why `Micro-Manager` is first in one paragraph.
- [x] We can explain why `ScanImage` is second in one paragraph.
- [x] We can explain why `ZEISS ZEN` and `NIS-Elements` are delayed to Phase 2.
- [x] We can explain why Boston is the first market focus.

## Pre-Build Validation Plan

The fastest path to execution should be:

1. Validate native macOS install.
2. Validate headless acquisition with official demo config.
3. Validate saved `NDTiff` reopen.
4. Freeze the normalized result schema.
5. Only then create the `device-skills` implementation files.

This is intentionally front-loaded with environment proof so we do not spend
 time building abstractions on top of an unverified runtime.

## Open Questions That Still Matter

These are still open, but they should not expand MVP scope.

- Which exact Micro-Manager version should we pin for reproducibility?
- Do we use `pymmcore`, `pymmcore-plus`, or both in v1?
- What is the minimum normalized imaging schema needed for `MicroManagerBrain`?
- How much acquisition progress should be surfaced in the v1 demo output?

These questions should be answered during implementation kickoff, not by adding
 more strategy documents.

## Risks To Watch During Closeout

### Risk: Planning continues to expand sideways

Mitigation:

- treat the current planning package as frozen
- only modify it if a build-blocking fact changes

### Risk: GUI pressure distorts the MVP

Mitigation:

- enforce the rule that headless proof must land before GUI work starts

### Risk: The project looks organized but is not ready to build

Mitigation:

- require environment validation before coding the full adapter stack

### Risk: Closeout becomes another planning loop

Mitigation:

- use this document to end planning, not extend it

## Exit Criteria

The planning phase is complete when:

- all source documents are aligned
- the MVP scope is frozen
- the validation gates are understood
- the next implementation step is concrete

At that point, the correct next action is not more planning. The correct next
 action is to begin `devices/micro-manager/` implementation.

## Immediate Next Action

Start implementation kickoff with this exact sequence:

1. prove local `Micro-Manager` install on macOS
2. prove headless demo acquisition
3. choose the v1 dependency set
4. create `devices/micro-manager/`
5. build the MVP path only
