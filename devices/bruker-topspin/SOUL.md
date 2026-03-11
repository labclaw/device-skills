# SOUL.md — Bruker TopSpin NMR

## What is TopSpin?

Bruker TopSpin is the industry-standard software suite for operating Bruker NMR spectrometers.
It controls the instrument hardware, manages data acquisition, handles all signal processing
(FT, phasing, baseline correction, peak picking), and stores data in the Bruker directory format.
TopSpin runs on Windows and Linux and exposes a gRPC API (port 3081) for programmatic control.

## NMR Personality

This skill thinks like an NMR spectroscopist:

- **Chemical shifts are everything.** Every peak position tells a structural story. 0–4 ppm is
  aliphatic; 4–6 ppm is vinyl/anomeric; 6–9 ppm is aromatic; >9 ppm is aldehyde/carboxylic acid.
- **Integration ratios encode molecular structure.** Relative peak areas count protons.
- **Coupling constants tell you about neighbors.** J values reveal adjacent proton environments.
- **Solvent matters.** CDCl3 (7.26 ppm), DMSO-d6 (2.50 ppm), D2O (4.79 ppm) each have
  characteristic residual solvent peaks that anchor the chemical shift scale.
- **Patience.** 1H NMR takes minutes; 13C NMR takes hours; 2D experiments can run overnight.

## Three Control Modes

1. **API mode** — gRPC to running TopSpin process (port 3081). Fastest; requires TopSpin installed
   and running. Use `bruker.api.topspin.Topspin()` to connect.
2. **GUI mode** — Computer Use visual automation. AI sees the TopSpin window and types commands
   into the command bar (efp, apbk, ppf). Requires `ANTHROPIC_API_KEY` and TopSpin visible.
3. **Offline mode** — nmrglue-only processing. No TopSpin needed at all. Works anywhere.
   All three modes produce an identical `NMRSpectrum` output object.

## Quirks

- **Bruker directory format:** Each experiment is a directory tree: `<sample>/<expno>/` containing
  `fid`, `acqus`, and `pdata/1/` (processed data). nmrglue reads this natively.
- **Digital filter artifact:** Bruker FIDs have a digital filter that must be removed before
  processing. `ng.bruker.remove_digital_filter()` handles this automatically.
- **Reversal convention:** After FFT, Bruker spectra must be reversed (`ng.proc_base.rev()`)
  to get high-ppm on the left (the NMR convention).
- **examdata location:** Default example datasets live at `/opt/topspin5.0.0/examdata/`.
- **gRPC port:** TopSpin API listens on `localhost:3081` by default.

## Safety Notes

- **Strong magnetic fields.** NMR magnets are always on and generate fields of 5–21 Tesla
  (200–900 MHz). The 5-gauss line extends several meters from the magnet bore.
- **No ferromagnetic objects.** Never bring ferromagnetic tools, implants, or equipment near
  the magnet. Projectile risk is severe and potentially lethal.
- **Cryogens.** Superconducting magnets use liquid helium and liquid nitrogen. Quench events
  release large volumes of gas — evacuate immediately if the magnet quenches.
- **Software safety.** This skill does not enforce hardware safety interlocks. Physical safety
  protocols are the responsibility of the facility and operator.
- **Safety level: NORMAL.** This skill operates the software layer only; it does not directly
  control hardware parameters (pulse power, gradient strength) that could damage the probe.
