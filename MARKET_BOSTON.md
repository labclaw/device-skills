# Greater Boston Market Research

Last updated: 2026-03-13

Purpose: identify which software platforms maximize reachable lab coverage in
Greater Boston so `device-skills` expansion follows real customer density, not
just technical interest.

This document separates:

- Observed facts from official institution or ecosystem sources.
- Inferences used to prioritize software support.

## Executive Summary

Observed facts:

- Boston is part of a very large life sciences corridor with high density of
  biotech companies, research hospitals, universities, and shared core
  facilities.
- Major Boston-area imaging cores repeatedly show the same commercial software
  ecosystems: `ZEISS ZEN`, `Nikon NIS-Elements`, Leica software stacks, and
  Bruker / Olympus / multiphoton-specific control environments.
- Shared cores often serve not just one PI lab but the broader Boston research
  community, which makes each software integration more commercially leveraged.

Inference:

- `Micro-Manager` and `ScanImage` should still be the first two microscopy
  software targets because they offer the best simulation-first development
  path.
- After those two, `ZEISS ZEN` and `NIS-Elements` should likely move to the top
  of the next expansion wave because they recur across major Boston-area cores.

## Why Greater Boston First

Observed facts:

- Boston.gov states Boston has more than 500 life science companies, while the
  broader Greater Boston area has nearly 1,000 biotechnology companies.
- Boston.gov also states Boston had more than 16 million square feet of
  commercial life science lab space by the end of 2024.
- Boston.gov states the Longwood Medical and Academic Area includes 21 medical,
  academic, and research institutions, employs 73,000 people, hosts more than
  24,000 students, and received $1.3 billion in NIH funding in FY 2024.
- MassBio reports that in the first half of 2025, 54% of Massachusetts VC
  funding went to companies outside Cambridge, including Boston and other
  nearby cities, which suggests the demand base is not limited to Kendall
  Square alone.

Inference:

- Greater Boston is dense enough that a software integration can unlock many
  adjacent labs without national-scale go-to-market effort.
- Longwood, Cambridge, and Boston-area core facilities are strategic force
  multipliers because one successful deployment can influence many downstream
  research groups.

## Official Software and Instrument Signals

### Harvard Center for Biological Imaging

Observed facts:

- HCBI states it serves academic and industry researchers at Harvard and across
  Greater Boston.
- Its equipment page shows a strong `ZEISS` footprint: multiple `LSM 980`,
  `LSM 910`, `LSM 900`, `LSM 880`, `LSM 700`, `Lightsheet.7`, and `Axio Scan`
  systems.
- The same equipment lineup also includes a `Nikon` spinning disk confocal.
- HCBI published a 2025 newsletter advertising a `Nikon Elements JOBS` seminar
  for Nikon spinning disk users.

Implication:

- `ZEISS ZEN` and `NIS-Elements` are not fringe systems in this market; they
  show up in one of the region's flagship imaging cores.

### HMS CITE

Observed facts:

- CITE describes itself as a light microscopy core facility supporting the HMS
  research community since 2001.
- CITE states it offers workshops to the greater Boston area.
- CITE's workshop program explicitly names the `Nikon A1R` and `ZEISS LSM`
  series in its point-scanning confocal training material.
- A retired CITE microscope page shows a Nikon 3D `N-STORM` super-resolution /
  TIRF system.

Implication:

- `Nikon` and `ZEISS` are embedded not only in instrument inventory but also in
  staff training and operational practice.

### Brigham and Women's Hospital Confocal Core

Observed facts:

- The BWH Confocal Core states it uses a `ZEISS LSM 800 with Airyscan` on a
  `Zeiss Axio Observer Z1`.
- The same facility page lists `Zen 2.6 software` for both confocal and
  widefield workflows.

Implication:

- `ZEISS ZEN` is directly visible as an operational software surface in a major
  Longwood hospital environment.

### MGH Program in Membrane Biology Microscopy Core

Observed facts:

- The PMB Microscopy Core states it serves MGH investigators and the Boston-area
  scientific community.
- Its equipment list includes a `Zeiss LSM 800 Airyscan`, `Nikon AXR`,
  `Nikon A1R`, and Nikon upright microscopes.
- The core explicitly lists workstation software including `Nikon Elements` and
  `Zeiss Zen Blue`.

Implication:

- This is especially strong evidence that `ZEN` and `NIS-Elements` are active,
  operator-facing software targets, not just hidden vendor dependencies.

### Boston Children's Hospital Cellular Imaging Core

Observed facts:

- BCH lists `Zeiss LSM 700`, `Zeiss LSM 980 Airyscan 2`, `Zeiss LS7
  Lightsheet`, `Nikon Ti Eclipse`, `Olympus MPE-RS Two-photon Microscope`, and
  `Leica TCS SP8-STED`.

Implication:

- Boston Children's alone spans `ZEISS`, `Nikon`, `Leica`, `Olympus`, and
  two-photon workflows, which reinforces the need to prioritize software
  platforms that unlock many instrument families.

### MIT Microscopy Core

Observed facts:

- MIT states its Microscopy Core supports scanning and multiphoton confocal
  microscopy, intravital imaging, TIRF, FRAP, FRET, and related imaging modes.

Inference:

- Even without the public page naming every software package, MIT strengthens
  the case that multiphoton and advanced microscopy workflows are normal in the
  local market, not exceptional.

## Software Priority Implications

### Tier 1: Build Immediately

- `Micro-Manager`
  Rationale: highest simulation-first leverage; broad device abstraction; best
  route for no-hardware demos and CI.
- `ScanImage`
  Rationale: strongest simulation-backed path adjacent to our real 2P workflows;
  useful surrogate for `bruker-2p`.

### Tier 2: Likely Highest Commercial Leverage After the First Two

- `ZEISS ZEN`
  Rationale: repeatedly visible in Boston-area core equipment and software.
- `NIS-Elements`
  Rationale: repeatedly visible in Boston-area cores and workflows, including
  explicit `Nikon Elements` and `JOBS` evidence.

### Tier 3: Important but After the Above

- `LAS X`
  Rationale: Leica is present, but current Boston evidence in our sample is
  weaker than the Zeiss and Nikon software signal.
- `cellSens`
  Rationale: possible future need, but weak evidence in this initial Boston
  pass.
- `ACQ4`, `ThorImageLS`, `mesoSPIM-control`
  Rationale: still strategically valuable for simulation-first and niche
  modalities, but current Boston-core evidence is weaker than Zeiss / Nikon.

## Product Strategy Implications

Inference:

- We should treat Boston shared cores as design partners, not just targets.
- A software skill that is common in shared cores has more GTM leverage than a
  software skill only seen in single custom rigs.
- `Micro-Manager` remains the best first build for developer and demo velocity,
  even though the strongest visible commercial-core signal in Boston today is
  `ZEISS` plus `Nikon`.
- Therefore the right sequence is likely:
  `Micro-Manager` -> `ScanImage` -> `ZEISS ZEN` / `NIS-Elements`.

## Open Questions

- Which Boston-area cores expose usable automation APIs versus GUI-only
  workflows?
- How often are `Micro-Manager` and `ScanImage` used in individual labs even
  when they are less visible on public core equipment pages?
- Which specific Boston biotech companies operate internal imaging platforms
  with recurring software stacks we can support?
- Which cores are willing to act as reference customers or pilot partners?

## Sources

- Boston.gov business strategy:
  https://www.boston.gov/government/cabinets/economic-opportunity-and-inclusion/bostons-open-business
- MassBio industry snapshot:
  https://www.massbio.org/industry-reports/industry-snapshot/
- Harvard Center for Biological Imaging home:
  https://hcbi.fas.harvard.edu/
- Harvard Center for Biological Imaging equipment:
  https://hcbi.fas.harvard.edu/equipment
- HCBI September 2025 newsletter:
  https://hcbi.fas.harvard.edu/news/2025/09/hcbi-september-2025-newsletter
- HMS CITE home:
  https://cite.hms.harvard.edu/
- HMS CITE workshops:
  https://cite.hms.harvard.edu/education/workshops/
- HMS CITE Nikon N-STORM page:
  https://cite.hms.harvard.edu/microscopes/tobias/
- BWH Confocal Core facility page:
  https://confocal.bwh.harvard.edu/facility.html
- MGH PMB Microscopy Core:
  https://researchcores.partners.org/pmb/about
- Boston Children's Cellular Imaging Core equipment:
  https://research.childrenshospital.org/resources/cores/cellular-imaging-core/equipment
- MIT Microscopy Core:
  https://biology.mit.edu/tile/microscopy-core-facility/
