# Laser Specifications — Coherent Chameleon Ti:Sapphire

> Source: Coherent Chameleon product specifications, laser safety documentation.
> The Ultima Investigator uses a Coherent Chameleon series ultrafast Ti:Sapphire laser
> as the two-photon excitation source.

## Chameleon Ultra II Specifications

| Parameter | Value |
|-----------|-------|
| Laser type | Ti:Sapphire, mode-locked ultrafast |
| Pump source | Continuous-wave diode-pumped solid-state (Verdi) |
| Tuning range | 680-1080 nm |
| Average output power | >2.5 W (peak at ~800 nm) |
| Peak power | >200 kW |
| Pulse duration | ~140 fs (sech-squared) |
| Repetition rate | ~80 MHz |
| Spectral bandwidth | ~10 nm (FWHM, transform-limited) |
| Beam quality (M-squared) | <1.1 (TEM00) |
| Beam diameter | ~1.2 mm at output (1/e-squared) |
| Polarization | Horizontal, linear, >500:1 |
| Tuning speed | >40 nm/s (automated, motorized birefringent filter) |
| Spatial mode | TEM00 |
| Noise | <0.15% RMS (20 Hz - 20 MHz) |
| Long-term power stability | <1% over 8 hours |

## Chameleon Ultra I (Alternate Configuration)

| Parameter | Value |
|-----------|-------|
| Tuning range | 690-1040 nm (narrower than Ultra II) |
| Average power | >2.5 W |
| All other specs | Same as Ultra II |

## Tuning and Wavelength Selection

### Common Wavelengths for Two-Photon Excitation

| Wavelength | Fluorophore | Application |
|------------|-------------|-------------|
| 800 nm | DAPI, Hoechst, Alexa 350 | Nuclear staining, structural |
| 880 nm | EGFP, Fluorescein, Alexa 488 | Green fluorescent proteins |
| 920 nm | GCaMP6/7/8 | Calcium imaging (most common) |
| 940 nm | YFP, Venus | Yellow fluorescent proteins |
| 1000 nm | DsRed | Red fluorescent proteins |
| 1040 nm | tdTomato, mCherry | Red indicators, dual-color with GCaMP |

### Tuning Behavior

- Wavelength changes are fully automated (motorized filter)
- Tuning speed: >40 nm/s, so a 100 nm change takes ~2.5 seconds mechanically
- After tuning, allow 5-10 seconds for power stabilization and re-optimization
- Power varies with wavelength: maximum around 800 nm, decreasing toward 680 nm and 1080 nm
- Some wavelengths near the tuning range edges may not mode-lock reliably

## Pockels Cell (Electro-Optic Modulator)

The Pockels cell controls the laser power delivered to the sample:

| Parameter | Value |
|-----------|-------|
| Type | KDP or KD*P electro-optic crystal |
| Response time | <1 us (enables line-by-line blanking) |
| Extinction ratio | >200:1 |
| Warmup time | 20-30 minutes for thermal stabilization |
| Control | 0-100% via PrairieView or PrairieLink |
| Functions | Power modulation, flyback blanking, Z-dependent power compensation |

### Pockels Cell Usage Notes

- **Warmup is critical.** The crystal's half-wave voltage drifts with temperature.
  Imaging during warmup produces non-uniform illumination across the field of view.
- **Power compensation.** For z-stacks, the Pockels cell can be programmed to increase
  power with depth to compensate for tissue scattering (exponential length constant
  typically 100-200 um in cortex).
- **Blanking.** During resonant scanning flyback (mirror turnaround), the Pockels cell
  blanks the beam to prevent unwanted exposure at the field edges.

## Cooling Requirements

| Parameter | Requirement |
|-----------|-------------|
| Coolant | Distilled/deionized water (closed loop) |
| Flow rate | Typically 3-5 L/min |
| Temperature | 25 C (+/- 0.5 C recommended) |
| Chiller type | Recirculating water-to-air chiller |
| Power for chiller | Standard 15A circuit |
| Warm-up after coolant start | 5-10 min before laser key-on |

### Cooling Failure Consequences

- The Ti:Sapphire crystal and pump laser diodes require continuous cooling
- If cooling fails during operation, the laser will shut down automatically (thermal interlock)
- Extended operation without cooling risks permanent crystal damage
- **ALWAYS verify coolant flow before turning the laser key**

## Laser Safety Parameters

| Parameter | Value |
|-----------|-------|
| ANSI laser class (enclosed) | Class 1 |
| Internal laser class | Class 4 |
| Maximum Permissible Exposure (MPE) | Not applicable at Class 4 levels |
| Nominal Hazard Zone (NHZ) | Within beam enclosure + 2 m around any opening |
| Required eyewear (maintenance) | OD 5+ at 680-1080 nm |
| Skin damage threshold | ~20 mW/cm-squared CW equivalent `[UNVERIFIED]` |

## Dual-Laser Configuration

Some Ultima Investigator systems include a second laser (e.g., for dual-wavelength
excitation or for an Axon module for photoactivation):

- Second laser typically a fixed-wavelength 1040 nm fiber laser
  (for simultaneous red + green imaging)
- Or a second tunable Chameleon for maximum flexibility
- Beam combining via polarization or dichroic before the scan mirrors
- System #5010 is configured with dual lasers and Axon module
