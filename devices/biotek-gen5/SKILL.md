---
name: "biotek-gen5"
description: "Operate a BioTek Gen5 (Agilent Synergy H1) microplate reader for absorbance, fluorescence, and luminescence assays on 96-well plates. Use for: ELISA quantification, cell viability screens, dose-response curves, fluorescence intensity reads. Parses Gen5 CSV exports offline on any platform; live control (API/GUI) requires Windows with Gen5 3.x. Outputs well-by-well numeric readings, blank-corrected values, and plate heatmaps."
---

# BioTek Gen5 Plate Reader Skill

Operate and analyze data from the BioTek Gen5 (Agilent Synergy H1) microplate reader. Supports absorbance, fluorescence, and luminescence on 96-well plates (rows A-H, columns 1-12).

## Safety

Safety level: normal

- **Plate carrier ejection:** Carrier can eject if protocol is interrupted mid-read; keep hands clear during acquisition.
- **Warm-up required:** Allow 15-30 min warm-up for fluorescence reads. Cold reads show higher CV% and unreliable baselines.
- **Windows-only for live control:** GUI and API modes require Windows with Gen5 3.x installed and licensed. Do not attempt live instrument control from other platforms.

## Control Modes

| Mode | Platform | Requirements | Use Case |
|------|----------|-------------|----------|
| **OFFLINE** | Any | None (demo data built-in) | Parse exported CSV, demos, testing |
| **API** | Windows | Gen5 3.x installed + COM license | Programmatic instrument control (not yet implemented) |
| **GUI** | Windows | Gen5 3.x running | Computer Use automation fallback (not yet implemented) |

Offline mode works immediately with built-in demo datasets. API and GUI modes require Windows with Gen5 software.

> **Note:** API and GUI modes are defined but not yet implemented. `connect()` returns `False` for both.

## Quick Start

```python
# Note: Directory is 'biotek-gen5' on disk but imports use underscores
from device_skills.schema import ControlMode
from devices.biotek_gen5.adapter import Gen5Adapter

reader = Gen5Adapter(mode=ControlMode.OFFLINE)
reader.connect()

# List available datasets
datasets = reader.list_datasets()
# Returns: [{"name": "ELISA_IL6_plate1", "mode": "absorbance", ...}, ...]

# Process a dataset
reading = reader.process("ELISA_IL6_plate1")
print(f"Mode: {reading.mode.value}, Wavelength: {reading.wavelength_nm}nm")
print(f"Well A1: OD={reading.plate.get_well('A1').value}")

reader.disconnect()
```

## Key Workflows

### 1. Run Assay and Read Plate

In OFFLINE mode, `acquire()` is not available (no physical reader). Use `process()` to load data from demo datasets or exported files.

```python
reader = Gen5Adapter(mode=ControlMode.OFFLINE)
reader.connect()

# ELISA absorbance data
elisa = reader.process("ELISA_IL6_plate1")

# Cell viability fluorescence data (name matching: "viability" or "cell")
viability = reader.process("CellViability_DrugScreen")
```

Dataset name matching: names containing "viability" or "cell" return fluorescence data; all others return absorbance data.

### 2. Process Exported Data

> **WARNING:** In OFFLINE mode, `adapter.process()` returns demo data for testing, not real file contents. Use `Gen5Processor` directly for real CSV files.

```python
# For real exported CSV files, use the processor directly:
from devices.biotek_gen5.processor import Gen5Processor
processor = Gen5Processor()
raw = processor.load("/path/to/export.csv")
corrected = processor.transform(raw)
reading = processor.extract(corrected)
```

### 3. Process CSV Exports (Detailed Pipeline)

Use `Gen5Processor` for the three-step pipeline on Gen5 CSV files:

```python
from devices.biotek_gen5.processor import Gen5Processor

processor = Gen5Processor()

# Step 1: Parse CSV (metadata header rows + 8x12 grid)
raw = processor.load("data/elisa_plate1.csv")
# Returns: {"wells": {"A1": 0.123, ...}, "metadata": {...}, "file": "..."}

# Step 2: Blank correction (cols 11-12 as blanks)
corrected = processor.transform(raw)
# Adds: "blank_avg" and "blank_corrected" dict

# Step 3: Extract structured PlateReading
result = processor.extract(corrected)
reading = result["reading"]   # PlateReading object
stats = result["stats"]       # {"well_count", "min", "max", "mean", "blank_avg"}
```

**CSV format expected:** Gen5 export with metadata rows at top, then rows A-H with 12 numeric columns. Non-row lines are parsed as key-value metadata.

### 4. Analyze Results with AI

```python
from devices.biotek_gen5.brain import Gen5Brain

brain = Gen5Brain()  # Uses ANTHROPIC_API_KEY; falls back to cached responses

# From adapter output
reading = reader.process("ELISA_IL6_plate1")
analysis = brain.analyze({"reading": reading})

# Streaming analysis
for chunk in brain.interpret_reading(reading, stream=True):
    print(chunk, end="")

# With experimental context
analysis = brain.interpret_reading(
    reading,
    context="Testing IL-6 response to LPS stimulation in THP-1 cells",
)

# Summarize multiple findings
summary = brain.summarize([analysis_1, analysis_2])
```

Without `ANTHROPIC_API_KEY`, the brain serves cached responses for ELISA and cell viability protocols.

### 5. Visualize Plate Data

```python
from devices.biotek_gen5.visualizer import plot_plate_heatmap

# Generate heatmap PNG
png_bytes = plot_plate_heatmap(reading, output_path="output/plate.png")

# Bytes only (no file save)
png_bytes = plot_plate_heatmap(reading, output_path=None, title="My ELISA")
```

Colormap: `YlOrRd` for absorbance, `YlGn` for fluorescence. Wells are annotated with values.

### 6. Export to CSV

```python
csv_string = Gen5Adapter.reading_to_csv(reading)
# Gen5-style CSV: header row with protocol/mode/wavelength, then 8x12 grid
```

### 7. File-Based Driver (for labclaw integration)

```python
from pathlib import Path
from devices.biotek_gen5.driver import Gen5Driver

driver = Gen5Driver(device_id="gen5-001", watch_path=Path("/data/gen5/"))
await driver.connect()

# Reads most recently modified CSV in watch_path
data = await driver.read()
# Returns: {"wells": {"A1": 0.123, ...}, "metadata": {...}, "file": "...", "device_id": "gen5-001"}

# Driver is read-only; write() always returns False
await driver.disconnect()
```

## Data Models

| Model | Description |
|-------|-------------|
| `Well` | Single well: `row` (A-H), `col` (1-12), `value`, `blank_corrected` |
| `WellPlate` | Plate with wells list. Methods: `get_well("A1")`, `column(1)`, `row("A")` |
| `PlateReading` | Full reading: `plate`, `mode`, `wavelength_nm`, `protocol`, `metadata` |
| `PlateFormat` | Enum: `PLATE_6`, `PLATE_12`, `PLATE_24`, `PLATE_48`, `PLATE_96`, `PLATE_384` |
| `ReadingMode` | Enum: `ABSORBANCE`, `FLUORESCENCE`, `LUMINESCENCE` |

## Demo Datasets

| Name | Protocol | Mode | Wavelength |
|------|----------|------|------------|
| `ELISA_IL6_plate1` | ELISA Demo | Absorbance | 450nm |
| `CellViability_DrugScreen` | Cell Viability (Calcein AM) | Fluorescence | 530nm (Ex 485) |

**ELISA demo layout:** Standards in cols 1-2 (serial dilution A-H), samples in cols 3-10, blanks in cols 11-12.

**Cell viability demo layout:** Positive controls (healthy cells) in cols 1-2, drug treatment in cols 3-4 (dose-dependent by row), test compounds in cols 5-10, negative controls (dead cells) in cols 11-12.

## Plate Layout Conventions

- **Columns 1-2:** Standards or positive controls
- **Columns 3-10:** Samples or test compounds
- **Columns 11-12:** Blanks or negative controls
- **Edge wells** (row A/H, col 1/12): Prone to evaporation artifacts in long incubations (>2h at 37C)

## Important Notes

- **CSV parsing:** Gen5Processor expects the specific Gen5 export format, not generic CSVs
- **Blank correction:** Automatic in both adapter (demo data) and processor pipeline, using cols 11-12
- **Quality thresholds:** CV% >15% = warning, >25% = problematic; Z-factor >0.5 = good screening assay

## Reference Documentation

| File | When to read |
|------|-------------|
| `SOUL.md` | Before first use — device personality, operational quirks, measurement philosophy |
| `MEMORY.md` | Before sessions — calibration dates, maintenance history, known issues |
| `user/system_config.md` | When configuring reader parameters for your specific instrument |
| `user/calibration_log.md` | Before quantitative assays — check last calibration date |
| `user/protocols/` | When running standard assay protocols |
| `user/findings/` | When reviewing previous assay results |

Note: No `docs/` directory exists yet for this device. Core operational knowledge is in this SKILL.md and SOUL.md.
