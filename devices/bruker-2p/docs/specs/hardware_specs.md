# Ultima Investigator — Hardware Specifications

> Source: Bruker Ultima Investigator specifications, component datasheets.

## System Summary

| Parameter | Value |
|-----------|-------|
| System type | Multiphoton laser scanning microscope |
| Laser safety class | Class 1 (Class 4 enclosed) |
| Excitation | Two-photon (femtosecond pulsed NIR) |
| Detection | Epi-fluorescence, non-descanned |
| Scan modes | Resonant-galvo, galvo-galvo |
| Max channels | 4 (simultaneous) |
| Platform | Windows 10/11, PrairieView software |

## Scanning System

### Resonant Galvanometer

| Parameter | Value |
|-----------|-------|
| Type | CRS (Cambridge Resonant Scanner) or equivalent |
| Resonant frequency | 8 kHz |
| Frame rate (512x512) | ~30 fps (bidirectional) |
| Frame rate (256x256) | ~60 fps (bidirectional) `[UNVERIFIED]` |
| Scan direction | Bidirectional (with phase correction) |
| Optical zoom range | 1x to 16x |
| Field of view (1x, 16x/0.8) | ~800 um diameter |

### Galvanometer (Conventional)

| Parameter | Value |
|-----------|-------|
| Scan type | Unidirectional or bidirectional |
| Frame rate | Variable (depends on dwell time and resolution) |
| Typical dwell time | 2-200 us per pixel |
| Use cases | Z-stacks, tile scans, line scans, high-resolution |

### Zoom

| Zoom | Approx. FOV (16x obj) | Pixel size (512x512) |
|------|----------------------|---------------------|
| 1x | ~800 um | ~1.56 um/px |
| 2x | ~400 um | ~0.78 um/px |
| 4x | ~200 um | ~0.39 um/px |
| 8x | ~100 um | ~0.20 um/px |
| 16x | ~50 um | ~0.10 um/px |

Note: Exact FOV depends on scan lens / tube lens combination and objective magnification.
Values above are approximate for the Nikon 16x/0.8 NA objective.

## Detectors

### GaAsP PMT — Hamamatsu H7422PA-40 SEL

| Parameter | Value |
|-----------|-------|
| Type | GaAsP (Gallium Arsenide Phosphide) photocathode |
| Model | Hamamatsu H7422PA-40 SEL (selected for low dark current) |
| Spectral range | 300-720 nm |
| Peak QE | ~40% at 500-550 nm |
| Cooling | Thermoelectric (Peltier), forced air |
| Max control voltage | 900 V |
| Anode current limit | 50 uA (auto-protection) |
| Dark current (typical) | <1 nA at max gain, cooled |
| Rise time | ~0.6 ns |
| Number installed | Up to 4 (quad detector configuration) |

### Detection Geometry

- **Non-descanned (NDD):** Emission collected through the objective is directed to
  detectors without passing back through the scan mirrors. This maximizes collection
  efficiency for scattered emission from deep tissue.
- **Dichroic/filter cubes:** Interchangeable cubes split emission into spectral channels.
  Common configurations:
  - Green channel: 500-550 nm (GCaMP, GFP, fluorescein)
  - Red channel: 570-620 nm (tdTomato, Texas Red)
  - Far red: 650-720 nm (Cy5, Alexa 647)

## Piezo Z-Drive

| Parameter | Value |
|-----------|-------|
| Type | Piezoelectric objective positioner |
| Controller | Bruker Piezo Amplifier/Driver |
| Travel range | 150 um |
| Minimum step size | 0.05 um |
| Maximum stack rate | 5 Hz (full range) |
| Repeatability | <0.1 um |
| Hysteresis | ~1% of travel (use unidirectional approach for precision) |
| Response time | <10 ms for small steps |

## XY Motorized Stage

| Parameter | Value |
|-----------|-------|
| Travel range | 6" x 3" (152 mm x 76 mm) |
| Resolution | 0.3 um |
| Accuracy | 1 um |
| Repeatability | 0.5 um |
| Speed | Up to 7 mm/s `[UNVERIFIED]` |
| Encoder | Linear encoder, closed-loop |

## Vibration Isolation

| Parameter | Value |
|-----------|-------|
| Table | Newport Integrity 4 VCS |
| Isolation type | Active vibration cancellation system |
| Vertical natural frequency | ~1.5 Hz |
| Horizontal natural frequency | ~1.5 Hz |
| Load capacity | Up to 500 kg |
| Active cancellation range | 1-200 Hz |

## Electrical

| Component | Power |
|-----------|-------|
| Laser (Chameleon) | Dedicated 20A circuit, 208-240 VAC |
| PrairieView workstation | Standard 15A circuit |
| Resonant galvo controller | Standard 15A circuit |
| Piezo driver | Shares circuit with controller electronics |
| Cooling water circulator | Standard 15A circuit |
| Total system | Typically 2-3 dedicated circuits |

## Environmental Requirements

| Parameter | Requirement |
|-----------|-------------|
| Temperature | 20-25 C (stable within +/- 1 C) |
| Humidity | 30-60% RH, non-condensing |
| Vibration | Optical table required; avoid HVAC vents, foot traffic |
| Light | Darkened room for imaging (light leaks degrade SNR) |
| Floor | Ground floor preferred; upper floors need vibration assessment |
