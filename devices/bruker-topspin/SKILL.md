---
name: "bruker-topspin"
description: "Operate a Bruker NMR spectrometer via TopSpin software. Covers 1H-NMR, 13C-NMR, 2D-COSY, HSQC, HMBC experiments. Process FID data, pick peaks, analyze chemical shifts, identify compounds. Handles spectrum acquisition, Fourier transform, phase correction, baseline correction, peak picking, and structure elucidation."
---

# Bruker TopSpin NMR Skill

Read SOUL.md for NMR personality, spectroscopic quirks, and solvent knowledge before first use.

You are operating a Bruker NMR spectrometer through TopSpin 5.x software. This skill gives you three ways to control the instrument and a complete data processing pipeline.

## Safety

NMR spectrometers have a superconducting magnet that is ALWAYS energized:

- **Magnetic field hazard.** No ferromagnetic objects (tools, chairs, gas cylinders) within the 5-gauss line. Pacemakers and implants are contraindicated.
- **Cryogen awareness.** Liquid helium and nitrogen maintain the magnet. Never block the vent stack. A quench releases ~100L of helium gas rapidly — evacuate the room if the quench alarm sounds.
- **RF exposure.** The probe generates high-power RF pulses. Never reach into the bore during acquisition.
- **Sample handling.** Use non-magnetic NMR tubes only. Verify spinner balance before insertion.

## Three Control Modes

| Mode | When to use | Requirements |
|------|-------------|--------------|
| **Offline** | Process existing FID data without TopSpin running | `nmrglue`, `numpy` |
| **API** | Programmatic control of a running TopSpin instance | TopSpin running, gRPC port 3081 |
| **GUI** | Visual automation of TopSpin window via Computer Use | TopSpin visible, `ANTHROPIC_API_KEY` |

Always start with Offline mode unless you specifically need live instrument control.

## Quick Start: Process a Spectrum (Offline)

```python
from devices.bruker_topspin.adapter import TopSpinAdapter
from devices.bruker_topspin.processor import TopSpinProcessor
from devices.bruker_topspin.visualizer import plot_spectrum

# 1. Connect in offline mode (default)
adapter = TopSpinAdapter(mode="offline")
adapter.connect()

# 2. List available datasets
datasets = adapter.list_datasets()
# Each entry: {"path": str, "sample": str, "expno": int, "title": str}

# 3. Process a dataset (FID -> spectrum with peaks)
spectrum = adapter.process(data_path="/opt/topspin5.0.0/examdata/exam_CMCse_1/1")
# Returns NMRSpectrum with: data, ppm_scale, peaks, nucleus, solvent, frequency_mhz

# 4. Inspect peaks
for peak in spectrum.peaks[:10]:
    print(f"  {peak.ppm:.3f} ppm  (intensity: {peak.intensity:.1f})")

# 5. Plot
plot_spectrum(spectrum, output_path="spectrum.png", annotate_peaks=True)
```

## Key Data Types

### NMRSpectrum
The central data object returned by all processing paths:
- `data` (np.ndarray) -- processed spectrum intensities
- `ppm_scale` (np.ndarray) -- chemical shift axis
- `peaks` (list[NMRPeak]) -- detected peaks, sorted high-to-low ppm
- `nucleus` (str) -- e.g. "1H"
- `solvent` (str) -- e.g. "CDCl3"
- `frequency_mhz` (float) -- spectrometer frequency
- `title`, `sample_name` (str) -- metadata from dataset

### NMRPeak
- `ppm` (float) -- chemical shift position
- `intensity` (float) -- peak height
- `width_hz` (float) -- line width
- `multiplicity` (str) -- splitting pattern
- `integral` (float) -- relative area

## Core Workflows

### 1. Process Raw FID (Offline)

The processor runs the standard NMR pipeline: digital filter removal, zero-fill, apodization, FFT, phase correction, baseline correction, peak picking.

```python
processor = TopSpinProcessor(line_broadening=0.3)
dic, fid = processor.read_bruker("/path/to/dataset/1")
spectrum = processor.process_1d(dic, fid, dataset_path="/path/to/dataset/1")
```

Processing steps (automatic):
1. Remove Bruker digital filter artifact
2. Zero-fill to next power of 2 (min 65536 points)
3. Exponential line broadening (default 0.3 Hz)
4. Fourier transform
5. Reverse spectrum (Bruker convention: high-ppm on left)
6. Automatic phase correction (ACME algorithm)
7. Polynomial baseline correction
8. Peak picking (threshold = 2% of max intensity)

### 2. Process via TopSpin API (Live)

```python
adapter = TopSpinAdapter(mode="api")
if adapter.connect():  # connects to gRPC port 3081
    spectrum = adapter.process(data_path="/path/to/dataset/1")
    # TopSpin runs: efp (FT+phase) -> apbk (baseline) -> ppf (peak pick)
    # Then reads processed pdata back via nmrglue
```

### 3. Process via GUI Automation

```python
adapter = TopSpinAdapter(mode="gui")
if adapter.connect():  # detects TopSpin window
    spectrum = adapter.process(data_path="/path/to/dataset/1")
    # Types commands into TopSpin command line: efp, apbk, ppf
```

### 4. AI-Powered Spectrum Interpretation

```python
from devices.bruker_topspin.brain import TopSpinBrain

brain = TopSpinBrain()  # needs ANTHROPIC_API_KEY or uses cached demos
interpretation = brain.interpret_spectrum(spectrum, molecular_formula="C9H8O4")
# Returns markdown: Peak Analysis, Proposed Structure, Confidence, Next Steps

# Streaming variant
for chunk in brain.interpret_spectrum(spectrum, stream=True):
    print(chunk, end="")

# Suggest follow-up experiments
suggestion = brain.suggest_next_experiment(spectrum, hypothesis="aspirin")
```

### 5. Spectral Library Matching

```python
from devices.bruker_topspin.library import SpectralLibrary

lib = SpectralLibrary.from_examdata()  # loads all TopSpin example data
matches = lib.match(unknown_spectrum, top_k=3)
for m in matches:
    print(f"  {m.entry.name}: score={m.score:.2f} ({m.matched_peaks} peaks matched)")
```

### 6. Driver Interface (for labclaw)

```python
from devices.bruker_topspin.driver import TopSpinDriver

driver = TopSpinDriver(config={"mode": "offline"})
await driver.connect()
await driver.write({"action": "process", "path": "/path/to/dataset/1"})
result = await driver.read()  # returns dict with peaks, metadata
```

## TopSpin Command Reference

This skill includes 525 command reference files in `docs/commands/`. Do NOT try to load them all. Instead, search by topic:

```bash
# Find commands related to a topic
grep -ril "phase correction" devices/bruker-topspin/docs/commands/
grep -ril "baseline" devices/bruker-topspin/docs/commands/
grep -ril "peak pick" devices/bruker-topspin/docs/commands/
grep -ril "2D" devices/bruker-topspin/docs/commands/
```

Files are named by command (e.g., `efp.md`, `apk.md`, `ppf.md`). Read a specific file when you need details about a command.

### Essential Commands

| Command | Purpose |
|---------|---------|
| `efp` | Exponential multiply + Fourier transform + phase correction |
| `apk` | Automatic phase correction |
| `apbk` | Auto phase + baseline (neural-net algorithm) |
| `absn` | Baseline correction |
| `ppf` | Peak picking (find peaks) |
| `re` | Open/load a dataset |
| `zg` | Start acquisition (go) |
| `rga` | Receiver gain adjustment |
| `lock` | Lock on solvent signal |
| `topshim` | Automatic shimming |

### Standard Processing Pipeline

For a typical 1D 1H spectrum, the command sequence is:

```
re <dataset_path>    # open dataset
efp                  # FT + phase
apbk -n              # neural-net auto phase + baseline
ppf                  # peak picking
```

## Bruker Directory Format

Each experiment is a directory tree:

```
<sample_name>/
  <expno>/              # experiment number (1, 2, 3...)
    fid                 # raw Free Induction Decay
    acqus               # acquisition parameters
    acqu2s              # 2D acquisition parameters (if 2D)
    pdata/
      1/                # processing number
        1r, 1i          # processed real/imaginary data
        procs           # processing parameters
        title           # experiment title
        peaklist.xml    # peak list (after ppf)
```

Default examdata location: `/opt/topspin5.0.0/examdata/`

Read SOUL.md for chemical shift interpretation, solvent peaks, and NMR personality.

## User Data

Instance-specific operational data in `user/`:

| Path | When to read |
|------|-------------|
| `MEMORY.md` | Before any session — check calibration dates, known issues |
| `user/system_config.md` | When configuring acquisition parameters |
| `user/calibration_log.md` | Before quantitative measurements |
| `user/protocols/` | When running standard experiment protocols |
| `user/findings/` | When reviewing previous analysis results |

## Key Files

| File | Purpose |
|------|---------|
| `adapter.py` | `TopSpinAdapter` -- main entry point, 3 control modes |
| `processor.py` | `TopSpinProcessor` -- offline FID processing, `NMRSpectrum`, `NMRPeak` |
| `brain.py` | `TopSpinBrain` -- Claude-powered spectrum interpretation |
| `driver.py` | `TopSpinDriver` -- async driver for labclaw integration |
| `library.py` | `SpectralLibrary` -- fingerprint matching against known compounds |
| `visualizer.py` | `plot_spectrum()` -- publication-quality spectrum plots |
| `gui_automation.py` | GUI mode helper — use when PrairieView-style visual automation is needed |
| `demo_cache.py` | Offline demo data — used when no spectrometer available |
| `skill.yaml` | Device manifest (capabilities, modes, dependencies) |
| `SOUL.md` | Device identity, NMR personality, quirks, safety |
| `docs/commands/` | 525 TopSpin command reference files (search, don't load all) |
