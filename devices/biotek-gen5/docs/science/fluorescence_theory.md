# Fluorescence Detection — Theory

**Source:** Standard biophysics and fluorescence spectroscopy references.

## Principle

Fluorescence occurs when a molecule (fluorophore) absorbs light at one wavelength
(excitation) and emits light at a longer wavelength (emission). The energy difference
between excitation and emission is the Stokes shift.

```
Excitation (shorter wavelength, higher energy)
    |
    v
Fluorophore absorbs photon → excited state
    |
    v (vibrational relaxation, internal conversion)
    |
    v
Fluorophore emits photon → ground state
    |
    v
Emission (longer wavelength, lower energy)
```

## Key Parameters

| Parameter | Description |
|-----------|-------------|
| Excitation wavelength | Wavelength at which the fluorophore is optimally excited |
| Emission wavelength | Wavelength at which emitted light is collected |
| Stokes shift | Difference between excitation and emission maxima (nm) |
| Quantum yield | Ratio of photons emitted to photons absorbed (0-1) |
| Extinction coefficient | How strongly the fluorophore absorbs at excitation wavelength |
| Brightness | Product of quantum yield and extinction coefficient |

## Common Fluorophores in Plate Reader Assays

| Fluorophore | Excitation (nm) | Emission (nm) | Application |
|-------------|----------------|---------------|-------------|
| Fluorescein/FITC | 485 | 528 | General labeling, FP assays |
| Calcein AM | 485 | 530 | Cell viability (live cells) |
| Resorufin (alamarBlue) | 530-560 | 590 | Cell viability/proliferation |
| DAPI | 360 | 460 | DNA quantification |
| Hoechst 33342 | 350 | 461 | DNA staining (live cells) |
| Propidium iodide | 535 | 617 | Dead cell marker |
| GFP | 488 | 507 | Reporter gene |
| Rhodamine B | 540 | 625 | General labeling |
| Europium chelate | 340 | 615 | TRF assays (long-lived emission) |
| Coumarin | 350 | 450 | Enzyme substrates |

## Fluorescence in Microplate Readers

### Top vs. Bottom Reading

- **Top read:** Excitation and emission optics above the plate. Standard for solution
  assays, cell suspensions.
- **Bottom read:** Excitation from below, emission collected below. Preferred for
  adherent cell assays (reads through clear plate bottom, avoids meniscus effects).

### Gain (Sensitivity) Setting

The PMT gain controls signal amplification. Higher gain = more sensitivity but also
more noise.

- **Auto-gain:** Gen5 can automatically set gain based on the brightest well.
- **Fixed gain:** Use the same gain across experiments for quantitative comparison.
- **Typical range:** 50-100 for bright fluorophores, 100-200 for dim signals.
  [UNVERIFIED — gain values are instrument-specific]

### Plate Selection

| Plate Type | When to Use |
|------------|-------------|
| Black, clear bottom | Adherent cells, bottom read |
| Black, opaque | Top-read solution assays, reduced well-to-well cross-talk |
| White | NOT for fluorescence (high background) |
| Clear | NOT for fluorescence (high cross-talk between wells) |

## Common Issues

### Inner Filter Effect

At high fluorophore concentrations, excitation light is absorbed before reaching the
center of the well, and emitted light is reabsorbed before reaching the detector. This
causes signal to plateau or decrease at high concentrations. Dilute samples to stay in
the linear range.

### Photobleaching

Repeated or prolonged excitation degrades fluorophores, reducing signal over time.
Minimize exposure time. For kinetic reads, use the minimum excitation intensity needed.

### Autofluorescence

Cell culture media (especially those containing phenol red), serum, and some plate
materials fluoresce at common wavelengths. Use phenol red-free media and appropriate
blank subtraction.

### Quenching

Certain molecules (oxygen, heavy metal ions, some buffer components) can quench
fluorescence, reducing signal. Control buffer composition carefully.
