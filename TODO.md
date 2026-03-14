# device-skills TODO

Last updated: 2026-03-13

## Guiding Rule

Simulation-first is now a hard requirement for new imaging software skills.

TopSpin sets the bar: a device skill is substantially more valuable when the
software can be used end-to-end without a live instrument. For microscopy and
optical control software, priority goes to platforms with an official or
well-supported simulation path that lets us exercise acquisition, metadata, and
processing pipelines in CI and local development.

Commercially, Greater Boston is the first expansion region. We should favor
software skills that are common across Boston-area academic labs, hospital cores,
and biotech research groups.

Immediate product focus is narrower than the full roadmap. See
`PHASE1_SHORTLIST.md` for the current "suitable first devices" list.

## P0: Phase 1 Product Focus

- [ ] Treat `Micro-Manager`, `ScanImage`, `Bruker TopSpin`, and `Biotek Gen5`
      as the active first-wave software set.
- [ ] Treat `Bruker 2P` as an internal validation rig, not the main market
      expansion wedge.
- [ ] Avoid pulling Phase 2 commercial platforms into implementation until the
      first-wave set is stable enough to demo and sell.

## P0.1: Simulation-First Imaging Expansion

### Micro-Manager

- [ ] Create `devices/micro-manager/` from the template.
- [ ] Use `MICROMANAGER_DEMO.md` as the implementation target for a TopSpin-like
      complete no-hardware demo.
- [ ] Define `skill.yaml` around microscopy-widefield control plus simulation.
- [ ] Write `SOUL.md` with Micro-Manager's role as the default simulation-first
      microscopy platform.
- [ ] Write `profile.yaml` for the desktop app and script-first workflows.
- [ ] Implement `MicroManagerAdapter` with a no-hardware path built around
      `DemoCamera` / `FakeCamera`.
- [ ] Support launch-or-attach flows for `MMCore` / `pycro-manager`.
- [ ] Implement dataset discovery and acquisition summaries for simulated runs.
- [ ] Implement `MicroManagerProcessor` for `OME-TIFF` and `NDTiff`.
- [ ] Add deterministic demo fixtures that generate synthetic MDA runs for tests.
- [ ] Add end-to-end tests that run without hardware and prove:
      simulated acquire -> saved dataset -> process -> summarize.
- [ ] Add a second-layer realism demo using `FakeCamera` with curated source
      images on disk.
- [ ] Build a bounded GUI / CUA wrapper over the same adapter contract, rather
      than a separate GUI-only execution stack.
- [ ] Define one prepared customer walkthrough for GUI mode:
      launch app -> trigger acquisition -> show results.
- [ ] Document the minimum local setup for "works without hardware".

Acceptance criteria:

- A developer with no microscope can install deps and run a full acquisition
  demo locally.
- CI can execute at least one simulated acquisition test without GUI clicks.
- Output artifacts are stable enough for downstream `device-use` and `labclaw`
  pipeline tests.

### ScanImage

- [ ] Create `devices/scanimage/` from the template.
- [ ] Define `skill.yaml` for laser-scanning / 2P workflows plus simulation.
- [ ] Write `SOUL.md` around resonant scanning, galvos, PMTs, fast-Z, and 2P
      safety constraints.
- [ ] Implement `ScanImageAdapter` with priority on the official simulated
      camera path before any live hardware assumptions.
- [ ] Decide the control split between script/API control and GUI automation.
- [ ] Implement offline processing for ScanImage TIFF / BigTIFF metadata.
- [ ] Normalize ScanImage outputs into the same high-level imaging objects used
      by `bruker-2p` where practical.
- [ ] Add simulated-acquisition tests that do not require a live microscope.
- [ ] Add comparison notes versus `bruker-2p` so we can reuse 2P downstream
      processors, visualizers, and analysis prompts.

Acceptance criteria:

- We can run a dry-run ScanImage acquisition path without a live 2P rig.
- Saved output can be parsed into stable structured metadata.
- The skill is useful as a development surrogate for the real `bruker-2p`
  integration, not just as a separate demo.

## P0.5: Greater Boston Beachhead Mapping

- [ ] Build a list of target Boston-area research cores, hospitals, institutes,
      and biotech clusters where microscopy software choice can influence many
      downstream labs.
- [ ] Map each target site to likely software ecosystems:
      `Micro-Manager`, `ScanImage`, `ZEN`, `NIS-Elements`, `TopSpin`, and other
      recurring platforms.
- [ ] Identify which software choices maximize reachable labs in:
      Cambridge / Kendall, Longwood, Allston, Charlestown, and South Boston.
- [ ] Mark which targets are shared core facilities versus single-lab installs.
- [ ] Use this map to reorder expansion work after `Micro-Manager` and
      `ScanImage`.

Definition of done:

- We have a Boston-first target account list.
- We know which software platforms recur often enough to justify first-class
  support.
- Roadmap prioritization reflects reachable customer density, not just technical
  preference.

## P1: Architecture Follow-Through

- [ ] Decide whether imaging skills need an explicit `simulation` concept in
      manifests, or whether simulation stays an implementation detail of `api`
      mode.
- [ ] Define a shared imaging data model across `micro-manager`, `scanimage`,
      and `bruker-2p` to avoid three incompatible stack types.
- [ ] Add a standard "dry run" test contract for all future imaging skills.
- [ ] Add a repo-level checklist for "can this skill be meaningfully used
      without a live instrument?"
- [ ] Define a selection rubric for future imaging skills:
      installed base, simulation quality, API quality, file-format tractability,
      and reuse potential.

## P2: Growth Backlog After the First Two

- [ ] Promote `ZEISS ZEN` and `NIS-Elements` if Boston demand signals stay
      stronger than narrower simulation-friendly platforms.
- [ ] Evaluate `ACQ4` as a multi-device neuroscience platform.
- [ ] Evaluate `ThorImageLS` as a Thorlabs-centered optical platform.
- [ ] Evaluate `mesoSPIM-control` as a light-sheet platform with dry-run value.
- [ ] Evaluate `ZEISS ZEN` for commercial microscopy coverage.
- [ ] Evaluate `NIS-Elements` for Nikon ecosystems.
- [ ] Evaluate `LAS X` for Leica ecosystems.
- [ ] Evaluate `cellSens` for Evident ecosystems.

Definition of done for each candidate:

- We know whether it supports meaningful no-hardware development.
- We know whether it expands our reachable device count materially.
- We know whether it should become a first-class skill, a lower-priority skill,
  or stay out of scope.
