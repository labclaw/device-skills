# Two-Photon Excitation Microscopy — Principles

> Background science for AI agents operating the Bruker Ultima Investigator.

## Physics of Two-Photon Excitation

### Fundamental Mechanism

In conventional (one-photon) fluorescence, a single photon excites a fluorophore to
a higher energy state. The fluorophore then relaxes by emitting a lower-energy
(longer-wavelength) photon.

In two-photon excitation, **two photons of approximately half the energy (double the
wavelength)** are absorbed **simultaneously** (within ~0.5 femtoseconds) by the
fluorophore. The combined energy of the two photons equals the energy of a single
photon at the normal excitation wavelength.

Example: GFP absorbs at ~488 nm (one-photon). For two-photon excitation, two photons
at ~920 nm (approximately 2 x 488 nm) are absorbed simultaneously.

### Why This Requires an Ultrafast Laser

Two-photon absorption probability is proportional to the **square** of the instantaneous
light intensity. At continuous-wave (CW) laser powers used in biology (~10-100 mW),
two-photon absorption is negligibly rare.

Ultrafast (femtosecond) pulsed lasers solve this by compressing photons into brief
pulses:

- **Pulse duration:** ~140 fs
- **Repetition rate:** ~80 MHz
- **Duty cycle:** ~140 fs / 12.5 ns = 0.001% of the time, photons are present
- **Peak power:** average power / duty cycle = 10 mW / 0.00001 = ~1 MW peak
- At these peak powers, two-photon absorption becomes efficient

### Optical Sectioning Without a Pinhole

The key advantage of two-photon over confocal microscopy:

In confocal microscopy, fluorescence is generated throughout the illuminated cone, and
a pinhole in front of the detector rejects out-of-focus light. This wastes most of the
generated fluorescence.

In two-photon microscopy, excitation (and therefore fluorescence) occurs **only at the
focal point** where photon density is high enough for simultaneous two-photon absorption.
No pinhole is needed because no out-of-focus fluorescence is generated. This means:

1. **All emitted photons are signal** — no rejection losses
2. **Less photobleaching** — only the focal volume is excited
3. **Less phototoxicity** — surrounding tissue is not exposed

## Why Near-Infrared?

Two-photon microscopy uses wavelengths in the 680-1080 nm (near-infrared) range because:

### Deeper Tissue Penetration

- Scattering in biological tissue decreases with wavelength (approximately as 1/lambda^2)
- At 920 nm, the scattering mean free path in cortical tissue is ~200 um
  (vs ~50 um at 488 nm)
- Practical imaging depth: **500-800 um** in mouse cortex (vs ~100 um for confocal)
- Layer 5 pyramidal neurons at 500-600 um depth are routinely accessible
- Exceptional preparations can image to ~1000 um with high power and long-WD objectives

### Reduced Absorption

- Water absorption is relatively low at 700-950 nm (the "tissue optical window")
- Hemoglobin absorption is lower in NIR than in visible
- Above 1000 nm, water absorption increases significantly

### Safety Margin

- NIR photons individually have insufficient energy to excite (and potentially damage)
  biomolecules
- Phototoxicity is confined to the focal volume where two-photon absorption occurs

## Resolution

### Lateral Resolution

The lateral (XY) resolution of two-photon microscopy is given by:

```
d_lateral = 0.61 * lambda_excitation / NA
```

But because two-photon excitation depends on intensity-squared, the effective PSF is
narrower than the diffraction-limited spot. The effective resolution is:

```
d_2P_lateral ~ 0.61 * lambda / (NA * sqrt(2)) ~ 0.43 * lambda / NA
```

For the Nikon 16x/0.8 NA at 920 nm:
- **Lateral resolution: ~0.50 um** (Abbe criterion)
- Effective 2P lateral: ~0.35 um

### Axial Resolution

Axial resolution in two-photon microscopy:

```
d_2P_axial ~ 0.88 * lambda / (n - sqrt(n^2 - NA^2))
```

For 16x/0.8 NA at 920 nm in water (n=1.33):
- **Axial resolution: ~2.0 um**

### In Practice

In scattering tissue, actual resolution is degraded:

| Depth | Lateral (effective) | Axial (effective) |
|-------|--------------------|--------------------|
| 0-100 um | ~0.5 um | ~2 um |
| 100-300 um | ~0.7 um | ~3 um |
| 300-500 um | ~1.0 um | ~4 um |
| >500 um | ~1.5 um | ~6 um |

## Common Fluorophores for Two-Photon Excitation

### Genetically Encoded Calcium Indicators (GECIs)

| Indicator | 2P Excitation (nm) | Emission (nm) | Notes |
|-----------|-------------------|---------------|-------|
| GCaMP6s | 920-940 | 510 | Slow kinetics, high sensitivity |
| GCaMP6f | 920-940 | 510 | Fast kinetics, moderate sensitivity |
| GCaMP7f | 920-940 | 510 | Improved SNR over 6f |
| GCaMP8s | 920-940 | 510 | Highest sensitivity GECI |
| GCaMP8f | 920-940 | 510 | Fast + high sensitivity |
| jRGECO1a | 1000-1040 | 590 | Red calcium indicator |
| RCaMP | 1000-1040 | 580 | Red calcium indicator |

### Fluorescent Proteins

| Protein | 2P Excitation (nm) | Emission (nm) | Use |
|---------|-------------------|---------------|-----|
| EGFP | 880-920 | 510 | General labeling |
| tdTomato | 1000-1040 | 581 | Bright red, structural |
| mCherry | 1000-1040 | 610 | Red, slightly dimmer |
| YFP/Venus | 940-960 | 530 | Yellow channel |
| CFP/Cerulean | 840-860 | 475 | Cyan channel |

### Synthetic Dyes

| Dye | 2P Excitation (nm) | Emission (nm) | Use |
|-----|-------------------|---------------|-----|
| Alexa 488 | 780-800 | 520 | Morphology fills |
| Alexa 594 | 800-820 | 615 | Morphology fills (red) |
| Oregon Green BAPTA | 800 | 520 | Chemical calcium indicator |
| SR101 | 880 | 606 | Astrocyte marker |
| Fluorescein (FITC) | 780-800 | 520 | Vasculature (IV injection) |
| Texas Red dextran | 800-830 | 615 | Vasculature (IV injection) |

## Key Concepts for Imaging

### Photodamage vs Signal

Two-photon photodamage increases as the **square** of laser power (same as signal).
But at very high powers, three-photon processes dominate damage (cubic dependence),
making damage increase faster than signal. Rule of thumb:

- Start at low power (5-10% Pockels)
- Increase until adequate SNR is achieved
- Typical range: 20-60 mW at the sample for calcium imaging in cortex
- Above 100 mW, photodamage risk increases substantially

### Scattering and Collection Efficiency

In scattering tissue, emitted fluorescence photons scatter extensively before reaching
the detector. Non-descanned detection (NDD) collects more of these scattered photons
than descanned (confocal-path) detection, which is why all modern two-photon systems
use NDD for deep imaging.

The Ultima Investigator uses NDD geometry with large-area GaAsP PMTs positioned close
to the back aperture of the objective for maximum collection efficiency.
