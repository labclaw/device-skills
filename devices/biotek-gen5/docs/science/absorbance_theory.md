# Absorbance Spectroscopy — Theory

**Source:** Standard biochemistry and spectroscopy references.

## Beer-Lambert Law

The fundamental relationship governing absorbance measurements:

```
A = epsilon * l * c
```

Where:
- **A** = absorbance (optical density, OD; dimensionless)
- **epsilon** = molar absorptivity (extinction coefficient; L mol^-1 cm^-1)
- **l** = optical path length (cm)
- **c** = analyte concentration (mol/L)

### Key Principles

1. **Linearity:** Absorbance is proportional to concentration within the linear range
   of the assay (typically OD 0.1-2.0 for plate readers).
2. **Path length dependency:** Microplate readers have variable path lengths depending
   on sample volume (unlike fixed 1 cm cuvettes). At 200 uL in a standard 96-well plate,
   the path length is approximately 5.7 mm.
3. **Wavelength specificity:** Each chromophore has a characteristic absorption spectrum.
   Measurements are taken at the wavelength of maximum absorbance (lambda_max) for best
   sensitivity.

### Common Chromophores and lambda_max

| Chromophore | Assay | lambda_max (nm) |
|-------------|-------|----------------|
| TMB (oxidized) | ELISA (HRP substrate) | 450 |
| pNPP (hydrolyzed) | ELISA (AP substrate) | 405 |
| ABTS (oxidized) | ELISA (HRP substrate) | 405 |
| Formazan (MTT) | Cell viability | 570 |
| Formazan (MTS/XTT) | Cell viability | 490 |
| Coomassie-protein complex | Bradford | 595 |
| BCA-Cu1+ complex | BCA protein assay | 562 |
| DNA/RNA | Nucleic acid | 260 |
| Protein (peptide bond) | Direct UV | 280 |
| NADH | Enzymatic | 340 |

## Dual-Wavelength Correction

A reference wavelength reading is subtracted from the primary wavelength reading to
correct for optical imperfections (scratches, fingerprints, plate material variations):

```
A_corrected = A_primary - A_reference
```

Common reference wavelengths:
- ELISA (450 nm primary): reference at 540 nm or 570 nm
- MTT (570 nm primary): reference at 650 nm

The reference wavelength should be in a region where the chromophore does not absorb.

## Limitations in Plate Readers

1. **Stray light:** At high OD values (>3.0), stray light causes deviations from
   linearity. Practical dynamic range for most plate readers is OD 0-3.0.
2. **Pathlength variation:** Well-to-well volume differences cause pathlength variation,
   increasing CV%. Careful pipetting is essential.
3. **Condensation:** Temperature differences between sample and reader can cause
   condensation on the plate bottom, scattering light and producing artifactual readings.
4. **Plate material:** Standard polystyrene plates absorb below 340 nm. Use UV-transparent
   plates for readings at 260-280 nm.
5. **Meniscus effects:** The curved liquid surface (meniscus) in each well can affect
   readings, particularly at low volumes.
