# Bruker TopSpin NMR — Device Skill

Control and process NMR data from Bruker TopSpin spectrometers.
Three modes of operation: API (gRPC), GUI (Computer Use), and Offline (nmrglue).

## Quick Start

```python
from devices.bruker_topspin import TopSpinAdapter, TopSpinBrain, TopSpinProcessor

# Offline processing — no TopSpin needed
adapter = TopSpinAdapter()
adapter.connect()

datasets = adapter.list_datasets()
spectrum = adapter.process(datasets[0]["path"])

print(f"Found {len(spectrum.peaks)} peaks")
print(f"Strongest peak at {spectrum.peaks[0].ppm:.2f} ppm")
```

## Three Control Modes

### Offline Mode (default)

Processes Bruker FID data using `nmrglue`. No TopSpin installation required.
Works on any machine with the raw data files.

```python
from device_skills.schema import ControlMode
adapter = TopSpinAdapter(mode=ControlMode.OFFLINE)
adapter.connect()
spectrum = adapter.process("/path/to/dataset/1")
```

### API Mode

Connects to a running TopSpin instance via gRPC (port 3081). Requires TopSpin
5.x to be running on the same machine. Processing is performed inside TopSpin
and results are read back via nmrglue.

```python
adapter = TopSpinAdapter(mode=ControlMode.API)
if adapter.connect():
    spectrum = adapter.process("/path/to/dataset/1")
```

### GUI Mode

Uses Anthropic Computer Use to visually operate the TopSpin GUI.
Requires `ANTHROPIC_API_KEY` and a visible TopSpin window.

```python
import os
os.environ["ANTHROPIC_API_KEY"] = "sk-ant-..."

adapter = TopSpinAdapter(mode=ControlMode.GUI)
if adapter.connect():           # detects TopSpin window
    spectrum = adapter.process("/path/to/dataset/1")
```

## AI Interpretation (TopSpinBrain)

```python
from devices.bruker_topspin import TopSpinBrain

brain = TopSpinBrain()

# With ANTHROPIC_API_KEY: live Claude analysis
# Without API key: cached demo responses for alpha-ionone and strychnine
interpretation = brain.interpret_spectrum(spectrum)
print(interpretation)

# Streaming output
for chunk in brain.interpret_spectrum(spectrum, stream=True):
    print(chunk, end="", flush=True)

# Suggest next experiment
suggestion = brain.suggest_next_experiment(spectrum)

# Compare two spectra (API key required)
comparison = brain.compare_spectra(spectrum_a, spectrum_b)
```

### BaseBrain interface

`TopSpinBrain` also implements `BaseBrain`:

```python
result = brain.analyze({"spectrum": spectrum}, context="crude reaction mixture")
summary = brain.summarize(["Finding 1...", "Finding 2..."])
```

## Offline Processing (TopSpinProcessor)

```python
from devices.bruker_topspin import TopSpinProcessor

proc = TopSpinProcessor(line_broadening=0.3)

# BaseProcessor interface
dic, fid = proc.load("/path/to/dataset/1")
spectrum = proc.transform((dic, fid, "/path/to/dataset/1"))
results = proc.extract(spectrum)   # returns dict with peaks, summary, metadata

# Direct methods
peaks = proc.pick_peaks(spectrum)
summary_text = proc.get_spectrum_summary(spectrum)
peak_table = proc.format_peak_list(peaks)
```

## Spectral Library

```python
from devices.bruker_topspin.library import SpectralLibrary

# Build from TopSpin examdata
lib = SpectralLibrary.from_examdata()

# Add manually
lib.add("ethanol", [1.17, 3.69])
lib.add_spectrum(spectrum, name="unknown_sample_01")

# Match
matches = lib.match(query_spectrum, top_k=5)
for m in matches:
    print(f"{m.entry.name}: score={m.score:.2f}, matched {m.matched_peaks} peaks")
```

## Visualization

```python
from devices.bruker_topspin.visualizer import plot_spectrum

# Save to file
plot_spectrum(spectrum, output_path="spectrum.png")

# Get PNG bytes (for embedding in reports)
png_bytes = plot_spectrum(spectrum, output_path=None)
```

## labclaw Integration (TopSpinDriver)

```python
import asyncio
from devices.bruker_topspin.driver import TopSpinDriver

async def main():
    driver = TopSpinDriver(device_id="nmr-lab-01", config={"mode": "offline"})
    await driver.connect()

    await driver.write({"action": "process", "path": "/path/to/dataset/1"})
    data = await driver.read()
    print(data["num_peaks"], "peaks found")

    await driver.disconnect()

asyncio.run(main())
```

## Data Format

Bruker FID data is stored in a directory tree:

```
<topspin_dir>/examdata/
  <sample_name>/
    <expno>/           # experiment number (integer directory)
      fid              # raw FID data
      acqus            # acquisition parameters
      pdata/
        1/
          title        # experiment title (first line = compound name)
          1r           # processed real spectrum (if already processed)
```

The default examdata location is `/opt/topspin5.0.0/examdata/`.

## Dependencies

- `nmrglue` — Bruker data I/O and processing
- `numpy` — array math
- `matplotlib` — spectrum plotting
- `anthropic` — Claude API for brain (optional; cached fallback available)
- `bruker.api.topspin` — TopSpin gRPC API (optional; API mode only)

Install:

```bash
pip install "device-skills[bruker-topspin]"
```

## Safety

This skill operates the TopSpin **software** layer only. It does not control
hardware parameters (pulse power, gradient strength, shimming). Physical safety
around the NMR magnet (strong magnetic fields, cryogens) is the responsibility
of the facility and operator. See `SOUL.md` for full safety notes.
