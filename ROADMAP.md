# device-skills Roadmap

Last updated: 2026-03-13

## Direction

For microscopy and optical software, we will prioritize platforms that can be
used meaningfully without a live instrument. The target is not merely offline
file parsing. The target is a dry-run workflow that exercises acquisition,
metadata generation, processing, and downstream orchestration.

TopSpin is the reference standard here: simulation makes the software useful
before hardware integration is finished. We want the same leverage for imaging.

We also want to grow the number of supported devices steadily over time.
That means we should prefer software platforms that unlock families of devices,
not one-off integrations that only help a single instrument.

## Expansion Strategy

Support breadth will grow in waves:

1. Start with simulation-first software hubs that are useful without hardware.
2. Build shared imaging abstractions so new skills are mostly adapter work,
   not full rewrites.
3. Add vendor platforms that cover broad installed bases once the simulation and
   normalization pattern is stable.
4. Only then spend more time on narrower or hardware-specific integrations.

Selection rule:

- Prefer one software skill that covers many microscopes over one skill that
  covers one microscope.
- Prefer simulation-backed platforms over live-hardware-only platforms.
- Prefer formats and APIs that can feed CI and local demos.

## Beachhead Market: Greater Boston

The first commercial beachhead is Greater Boston.

Why this region first:

- It is one of the densest life sciences clusters in the world.
- It concentrates universities, hospitals, core facilities, and biotech
  companies in a small geography.
- The same software ecosystems appear repeatedly across academic and industry
  labs, which makes software-platform coverage more valuable than one-off
  instrument coverage.
- It is close to our existing network and the fastest place to validate whether
  a new skill matches real operator pain.

Working assumption:

- Scientific labs across Boston, Cambridge, Longwood, Allston, Charlestown, and
  nearby biotech corridors are all potential customers.
- Shared research cores matter disproportionately because one core facility can
  expose us to many labs and many instrument classes.

Observed software signal in the region:

- `Micro-Manager` is the best simulation-first general microscopy entry point.
- `ScanImage` is the strongest simulation-backed path adjacent to our 2P needs.
- `ZEISS ZEN` and `NIS-Elements` appear repeatedly in major Boston-area imaging
  cores and should remain near the top of the expansion wave.
- Existing `bruker-topspin` and `bruker-2p` support aligns with real research
  environments already present in the region.

Implication for device support:

- We should choose software skills partly by how often they recur in Boston-area
  cores and labs.
- After `Micro-Manager` and `ScanImage`, the next integrations should be picked
  to maximize reachable labs in Greater Boston, not just technical elegance.

## 2026 Priority Order

See also [PHASE1_SHORTLIST.md](PHASE1_SHORTLIST.md) for the narrower set of
software targets that are appropriate for immediate `labclaw` focus.

### 1. Micro-Manager

Why first:

- It is the most broadly adopted general-purpose microscopy control platform.
- It has the clearest no-hardware development story via `DemoCamera` /
  `FakeCamera`.
- It gives us a common entry point for stages, cameras, shutters, filter wheels,
  autofocus, and multi-dimensional acquisition.
- It is the best candidate for a default simulation target in CI.

Planned outcome:

- A `devices/micro-manager/` skill that supports dry-run acquisition and
  processing without a microscope.
- Stable processing support for `OME-TIFF` and `NDTiff`.
- A reusable imaging abstraction layer that future optical skills can inherit.

Milestones:

1. Ship the manifest, SOUL, profile, adapter, processor, and tests.
2. Prove a simulated MDA run works on a developer laptop with no hardware.
3. Use the generated dataset to exercise `device-use` and `labclaw` pipeline
   paths.

### 2. ScanImage

Why second:

- It is a strong fit for laser-scanning and two-photon workflows.
- It is closer to our real `bruker-2p` world than general microscopy software.
- It gives us a simulation-backed stepping stone before deeper PrairieView /
  PrairieLink maturity.

Planned outcome:

- A `devices/scanimage/` skill that supports dry-run scanning workflows first,
  then live control integration.
- Offline parsing for ScanImage-native output files.
- A shared analysis surface with `bruker-2p`, so ScanImage can act as a
  surrogate development target.

Milestones:

1. Validate the official simulated camera workflow as the default dev path.
2. Implement metadata parsing and normalized imaging objects.
3. Reuse as much of the `bruker-2p` processor / visualizer / brain shape as
   possible.

### 3. Expansion Wave After the First Two

Once `Micro-Manager` and `ScanImage` are stable, the next goal is to widen the
supported-device surface area as efficiently as possible.

Primary candidates:

- `ZEISS ZEN` for broad commercial microscopy coverage and strong Boston-area
  presence.
- `NIS-Elements` for Nikon ecosystems and recurring core-facility usage.
- `ACQ4` for neuroscience and multi-device experimental control.
- `ThorImageLS` for Thorlabs-centered optical systems.
- `mesoSPIM-control` for simulation-friendly light-sheet workflows.
- `LAS X` and `cellSens` if we need deeper Leica or Evident coverage.

The order inside this wave should be driven by one question:

"How many real lab setups does this software unlock for us per unit of adapter
and processor work?"

## What Success Looks Like

By the end of this roadmap slice:

- A new developer can run at least one microscopy acquisition pipeline without
  any instrument access.
- CI can validate simulated imaging datasets end-to-end.
- `bruker-2p` is no longer our only serious microscopy path during development.
- Adding future imaging software is easier because simulation and output
  normalization are already part of the pattern.
- The number of supportable imaging setups grows steadily because each new skill
  is chosen for platform leverage, not novelty.

## Not Current Priorities

These stay behind the first two items until they offer a clear simulation-first
path or become commercially urgent:

- ZEISS ZEN
- Nikon NIS-Elements
- Leica LAS X
- Evident cellSens

## References

- Micro-Manager project overview: https://micro-manager.org/
- Micro-Manager DemoCamera: https://micro-manager.org/DemoCamera
- Micro-Manager FakeCamera: https://micro-manager.org/FakeCamera
- Micro-Manager Python usage: https://micro-manager.org/Using_the_Micro-Manager_python_library
- MDA Simulator: https://mda-simulator.readthedocs.io/en/latest/
- ScanImage simulated camera: https://docs.scanimage.org/Configuration/Camera/Simulated%2BCamera.html
- MassBio overview: https://www.massbio.org/
- Boston life sciences cluster overview: https://www.boston.gov/business-strategy
- Harvard Center for Biological Imaging: https://hcbi.fas.harvard.edu/
- HMS CITE microscopy core: https://cite.hms.harvard.edu/
- HMS MicRoN core: https://micron.hms.harvard.edu/
- MIT Microscopy Core Facility: https://biology.mit.edu/tile/microscopy-core-facility/
- MGH PMB Microscopy Core: https://researchcores.partners.org/pmb/about
