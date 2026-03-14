# Luminescence Detection — Theory

**Source:** Standard biochemistry and bioluminescence references.

## Principle

Luminescence is light emission from a chemical or biological reaction, not from external
light excitation (unlike fluorescence). No excitation wavelength is needed — the reaction
itself produces photons.

```
Substrate + Enzyme → Product* (excited state) → Product + photon (light)
```

## Types of Luminescence

### Bioluminescence

Enzyme-catalyzed light production. Most common in plate reader assays:

| System | Enzyme | Substrate | Peak Emission (nm) |
|--------|--------|-----------|-------------------|
| Firefly | Firefly luciferase | D-luciferin + ATP | 560 |
| Renilla | Renilla luciferase | Coelenterazine | 480 |
| NanoLuc | NanoLuc luciferase | Furimazine | 460 |
| Gaussia | Gaussia luciferase | Coelenterazine | 480 |

### Chemiluminescence

Chemical reaction produces light without an enzyme. Examples:

| System | Substrate | Application |
|--------|-----------|-------------|
| HRP + luminol | Luminol/ECL substrate | Western blot, ELISA |
| AP + CSPD/CDP-Star | Dioxetane substrate | ELISA, reporter assays |
| Acridinium esters | — | Immunoassays |

## Signal Kinetics

### Flash Luminescence

- Signal peaks rapidly (seconds) then decays exponentially.
- **Examples:** Firefly luciferase (standard reagents), Renilla luciferase.
- **Challenge:** Signal changes during plate read; wells read last have lower signal.
- **Mitigation:** Use injector for substrate addition or read quickly.

### Glow Luminescence

- Signal rises slowly and remains stable for 30-60+ minutes.
- **Examples:** Firefly luciferase with stabilized reagents (Steady-Glo, Bright-Glo),
  NanoLuc.
- **Advantage:** All wells can be read at similar signal intensity.

## Luminescence in Microplate Readers

### Plate Selection

White opaque plates are mandatory for luminescence:

| Plate Type | Suitability | Reason |
|------------|-------------|--------|
| White opaque | Best | Reflects light toward detector, maximizes signal |
| Black opaque | Acceptable | Reduces cross-talk but absorbs some signal |
| Clear | Poor | High cross-talk between wells, signal loss |

### Key Parameters

| Parameter | Consideration |
|-----------|--------------|
| Integration time | Longer = higher signal but slower reads. Typical: 0.5-1.0 sec/well. |
| Gain | Set to match signal intensity. Auto-gain often appropriate. |
| Read height | Distance from well to detector. [UNVERIFIED — may be fixed on Synergy H1] |
| Temperature | Most luciferase reactions are temperature-sensitive; 20-25C is standard. |

### Cross-Talk

Luminescence can leak between adjacent wells, especially in clear or translucent plates.
Cross-talk specification for Synergy H1 is < 0.01% between adjacent wells. [UNVERIFIED]

## Common Applications

### Reporter Gene Assays

- Firefly and Renilla luciferase as transcriptional reporters.
- Dual-luciferase assays: firefly (experimental) + Renilla (normalization control).
- Read firefly first, then quench and add Renilla substrate.

### ATP Quantification (Cell Viability)

- CellTiter-Glo and similar reagents lyse cells and produce luminescence proportional
  to ATP content (proxy for viable cell number).
- Linear over 4+ logs of cell number.
- Glow-type signal stable for 30+ minutes.

### ELISA (Chemiluminescent Detection)

- HRP-conjugated antibody + luminol substrate.
- Higher sensitivity than colorimetric ELISA (TMB).
- Flash kinetics — read within 5-10 minutes of substrate addition.

## Advantages over Fluorescence

1. **No excitation light needed** — no background from autofluorescence, scattered
   excitation light, or plate material fluorescence.
2. **Higher sensitivity** — lower background means better signal-to-noise ratio.
3. **Wider dynamic range** — typically 7+ decades vs. 6 for fluorescence.

## Limitations

1. **Reagent-dependent** — requires specific enzyme-substrate system.
2. **Signal decay** — flash assays require careful timing.
3. **Temperature sensitivity** — enzymatic reactions are temperature-dependent.
4. **Cost** — luminescent substrates are typically more expensive than fluorescent dyes.
