# Phase 1 Shortlist

Last updated: 2026-03-13

Purpose: define the first set of device software targets that are actually
appropriate for `labclaw` to support now.

This is intentionally narrower than the full market opportunity. The goal is to
start with device software that is realistic for productization, testing, and
customer validation.

## Selection Rules

Phase 1 candidates should satisfy most of these:

- The software has a meaningful no-hardware or simulation-first path.
- The control surface is scriptable, API-accessible, or otherwise bounded.
- The output format is parseable and useful to downstream pipeline steps.
- The same software can unlock many labs, not just one custom setup.
- The operational and safety surface is manageable for an early product.
- The software is visible in Greater Boston research environments or adjacent to
  our current internal device base.

## Phase 1: Build or Productize Now

### 1. Micro-Manager

Role:

- Default simulation-first microscopy platform.
- Best general-purpose entry point for broad microscope coverage.

Why it belongs in Phase 1:

- Strong no-hardware story.
- Broad device abstraction.
- Good fit for CI, demos, and local development.
- High leverage across many possible customer labs.

Target outcome:

- First-class `device-skills` support with dry-run acquisition and processing.

### 2. ScanImage

Role:

- Simulation-backed bridge into laser-scanning and 2P workflows.

Why it belongs in Phase 1:

- Close to our real `bruker-2p` workflow.
- Useful as a surrogate development target before deeper live 2P integration.
- Better early fit than directly expanding from one PrairieView rig to many
  one-off microscope setups.

Target outcome:

- First-class `device-skills` support with dry-run scanning workflows and
  normalized output objects.

### 3. Bruker TopSpin

Role:

- Existing anchor software for "simulation/offline usable scientific software".

Why it belongs in Phase 1:

- Already present in the repo.
- Strong reference model for offline-capable product behavior.
- Relevant to Boston-area chemistry and translational research environments.

Target outcome:

- Keep hardening and productizing the existing support rather than treating it
  as a side demo.

### 4. Biotek Gen5

Role:

- Lower-complexity plate-reader workflow with practical automation value.

Why it belongs in Phase 1:

- Already present in the repo.
- Easier operational surface than many microscopy stacks.
- Useful for proving routine instrument automation and data processing paths.

Target outcome:

- Treat as an early applied automation surface for real lab workflows.

## Phase 1 Internal Validation Device

### Bruker 2P

Role:

- Internal anchor rig and advanced imaging validation target.

Why it is not the main expansion target yet:

- Valuable because we have a real machine.
- Not ideal as the first scalable outward-facing imaging platform because the
  simulation story is weaker and the workflow is narrower than
  `Micro-Manager`.

How to use it in Phase 1:

- Reuse it as the reality check for 2P assumptions.
- Use it to validate abstractions built for `ScanImage` and imaging pipelines.
- Do not let it dominate the roadmap for broad market expansion.

## Phase 2: Next Best Commercial Expansion

These should be next after the Phase 1 set is stable:

- `ZEISS ZEN`
- `NIS-Elements`

Why Phase 2:

- Strong Boston-area commercial and core-facility signal.
- Likely high customer reach.
- But weaker simulation-first story than `Micro-Manager`, so not the first
  build.

## Not Phase 1

These are not good first targets right now:

- Narrow custom rigs with little reuse across labs.
- Platforms with weak or unclear no-hardware development paths.
- Highly safety-sensitive systems where we do not yet have robust control and
  validation patterns.
- One-off integrations chosen for novelty rather than market leverage.

## Practical Build Order

1. Harden `bruker-topspin` and `biotek-gen5` as current product surfaces.
2. Build `micro-manager`.
3. Build `scanimage`.
4. Use `bruker-2p` as an internal validation rig, not the main outward-facing
   expansion wedge.
5. Move to `ZEISS ZEN` and `NIS-Elements`.

## Exit Criteria for Phase 1

We can say Phase 1 is complete when:

- We support at least one broad simulation-first microscopy platform.
- We support at least one scanning / 2P-adjacent software platform.
- We retain at least one lower-complexity routine instrument workflow.
- We can run at least one end-to-end imaging pipeline without hardware.
- We have enough confidence to start commercial conversations with Boston-area
  labs around a concrete supported-device story.
