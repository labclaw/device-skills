# Objective Specifications — Nikon CFI75 LWD 16X W

> Source: Nikon Instruments objective specifications, Bruker system documentation.

## Nikon CFI75 LWD 16X/0.8 NA Water-Dipping Objective

This is the primary objective for in vivo two-photon imaging on the Ultima Investigator.

| Parameter | Value |
|-----------|-------|
| Model | Nikon CFI75 LWD 16X W |
| Magnification | 16x |
| Numerical Aperture | 0.80 |
| Immersion | Water dipping (no coverslip) |
| Working Distance | 3.0 mm |
| Field of View (FOV) number | 16.5 mm `[UNVERIFIED]` |
| FOV diameter at sample | ~1.0 mm (without zoom) `[UNVERIFIED]` |
| Parfocal length | 75 mm (CFI75 series) |
| Thread | M32 x 0.75 (Nikon standard) |
| Correction | Plan Fluorite |
| Coating | Anti-reflection multi-coating for NIR transmission |
| Transmission at 900 nm | >80% `[UNVERIFIED]` |

## Key Features for Two-Photon Imaging

### High NA for Deep Imaging

- NA 0.80 provides excellent two-photon excitation efficiency
- Lateral resolution: ~0.5 um at 920 nm (Abbe: 0.61 * lambda / NA)
- Axial resolution: ~2.0 um at 920 nm (2 * lambda * n / NA-squared, effective 2P)
- High NA collects more scattered emission photons from deep tissue

### Long Working Distance

- 3.0 mm WD accommodates:
  - Cranial windows (glass + water gap: ~0.5-1.0 mm)
  - Thick tissue preparations
  - Micromanipulator access for electrophysiology probes
- Water dipping: no coverslip required, objective dips directly into immersion water
  on top of the cranial window

### Water Dipping vs Water Immersion

| Property | Water Dipping | Water Immersion |
|----------|--------------|-----------------|
| Coverslip | Not required | Required |
| Contact | Objective touches water surface | Sealed water chamber |
| Evaporation | Water evaporates over time | Sealed, no evaporation |
| Maintenance | Must refill water during long sessions | No refilling needed |
| Typical use | In vivo brain imaging | In vitro slice imaging |

### CFI75 Parfocal Standard

The CFI75 series uses a 75 mm parfocal length (compared to 60 mm standard CFI60).
This provides:
- Longer working distance designs
- Better mechanical clearance for equipment around the sample
- Requires CFI75-compatible objective turret or adapter

## Resolution at Common Wavelengths

| Wavelength | Lateral (Abbe) | Axial (2P effective) |
|------------|---------------|---------------------|
| 800 nm | 0.43 um | 1.7 um |
| 920 nm | 0.50 um | 2.0 um |
| 1040 nm | 0.57 um | 2.2 um |

Note: These are theoretical diffraction limits. Actual resolution in tissue is degraded
by scattering and aberrations. At 300 um depth in cortex, effective resolution is
typically 1.5-2x worse than diffraction-limited values.

## Care and Maintenance

### During Imaging

- Check water level every 30-60 minutes during long sessions
- Use distilled or deionized water for immersion
- Avoid air bubbles between objective and preparation
- Water temperature should match room temperature to avoid convection currents

### Cleaning

1. Rinse front element with distilled water after every session
2. If debris present, use lens paper with a drop of ethanol
3. Wipe gently in a circular motion from center outward
4. Never use acetone or strong solvents
5. Inspect front element under magnification periodically for scratches

### Storage

- Store with protective cap when not mounted
- If left on microscope, cover with parafilm or cap to prevent dust accumulation
- Store in low-humidity environment if removed for extended periods

## Alternative Objectives

Other objectives commonly used with the Ultima Investigator:

| Objective | NA | WD | Use Case |
|-----------|-----|-----|----------|
| Nikon 25x/1.05 W (CFI75) | 1.05 | 2.0 mm | Higher resolution, less deep |
| Olympus 25x/1.05 W | 1.05 | 2.0 mm | High-resolution in vivo |
| Nikon 40x/0.80 W | 0.80 | 3.5 mm | Higher mag, same NA |
| Nikon 10x/0.45 W | 0.45 | 4.0 mm | Wide FOV mapping |

The 16x/0.8 NA is the most common choice for in vivo calcium imaging because it
balances resolution, FOV, working distance, and light collection efficiency.
