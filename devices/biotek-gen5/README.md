# BioTek Gen5 Device Skill

Device skill for the BioTek (Agilent) Gen5 microplate reader — absorbance, fluorescence,
and luminescence detection for 96- and 384-well plates.

## Quick Start

```python
from devices.biotek_gen5 import Gen5Adapter, Gen5Brain, Gen5Processor
from device_skills.schema import ControlMode

# Offline mode — works without hardware, uses built-in demo data
adapter = Gen5Adapter(mode=ControlMode.OFFLINE)
adapter.connect()
datasets = adapter.list_datasets()
reading = adapter.process("ELISA_IL6_plate1")
print(f"Well A1: OD={reading.plate.get_well('A1').value:.4f}")
```

## Usage Modes

### Offline Mode (no hardware required)

Offline mode uses built-in demo data: an ELISA absorbance plate and a cell viability
fluorescence plate. Useful for testing, demos, and analysis pipeline development.

```python
adapter = Gen5Adapter(mode=ControlMode.OFFLINE)
adapter.connect()

# List available demo datasets
datasets = adapter.list_datasets()
# [{'name': 'ELISA_IL6_plate1', ...}, {'name': 'CellViability_DrugScreen', ...}]

# Process ELISA demo
reading = adapter.process("ELISA_IL6_plate1")
print(f"Plate format: {reading.plate.format.value}-well")
print(f"Mode: {reading.mode.value}")
print(f"Wavelength: {reading.wavelength_nm} nm")

# Export to CSV
csv_text = Gen5Adapter.reading_to_csv(reading)
Path("output/plate.csv").write_text(csv_text)
```

### With device-use (Adapter)

The adapter is the primary interface for device-use orchestration.

```python
from device_skills.schema import ControlMode
from devices.biotek_gen5 import Gen5Adapter

adapter = Gen5Adapter(mode=ControlMode.OFFLINE)

# Register with device-use orchestrator
from device_use import create_orchestrator
orch = create_orchestrator()
orch.register(adapter)

# Use via tool calling
reading = orch.call_tool("gen5.process", data_path="ELISA_IL6_plate1")
```

### With labclaw (Driver)

The driver integrates with labclaw's hardware layer for file-based data ingestion.

```python
import asyncio
from pathlib import Path
from devices.biotek_gen5.driver import Gen5Driver

async def main():
    driver = Gen5Driver(
        device_id="gen5-lab1",
        watch_path=Path("/data/gen5/exports/"),
    )
    await driver.connect()

    # Reads the most recently modified CSV in watch_path
    data = await driver.read()
    print(data["wells"])   # {"A1": 0.523, "A2": 0.491, ...}
    print(data["metadata"])

    # Or parse a specific file
    result = driver.parse_file(Path("/data/gen5/exports/elisa_2025-01-15.csv"))

asyncio.run(main())
```

### Processor (file parsing pipeline)

```python
from devices.biotek_gen5.processor import Gen5Processor

processor = Gen5Processor()

# Step 1: Load CSV file
raw = processor.load("data/elisa_plate1.csv")

# Step 2: Apply blank correction
corrected = processor.transform(raw)

# Step 3: Extract structured result
result = processor.extract(corrected)

reading = result["reading"]   # PlateReading
stats = result["stats"]       # {"well_count": 96, "min": ..., "max": ..., "mean": ...}
```

### AI Analysis (Brain)

```python
from devices.biotek_gen5 import Gen5Adapter, Gen5Brain
from device_skills.schema import ControlMode

adapter = Gen5Adapter(mode=ControlMode.OFFLINE)
reading = adapter.process("ELISA_IL6_plate1")

brain = Gen5Brain()

# Full interpretation (uses cached response if no API key)
analysis = brain.interpret_reading(reading)
print(analysis)

# Streaming response
for chunk in brain.interpret_reading(reading, stream=True):
    print(chunk, end="", flush=True)

# BaseBrain interface
analysis = brain.analyze({"reading": reading}, context="Run from 2025-01-15")
summary = brain.summarize([analysis])
```

### Visualization

```python
from devices.biotek_gen5.visualizer import plot_plate_heatmap
from devices.biotek_gen5 import Gen5Adapter
from device_skills.schema import ControlMode

adapter = Gen5Adapter(mode=ControlMode.OFFLINE)
reading = adapter.process("ELISA_IL6_plate1")

png_bytes = plot_plate_heatmap(reading, output_path="output/heatmap.png")
```

## Control Modes

| Mode | Requirements | Notes |
|------|-------------|-------|
| `OFFLINE` | None | Demo data, works anywhere |
| `API` | Windows + Gen5 3.x installed and licensed | Uses Gen5 COM automation |
| `GUI` | Windows + Gen5 software running | Computer Use automation |

## CSV Format

Gen5 exports have a specific format:

```
Protocol: ELISA Demo,Mode: absorbance,Wavelength: 450nm
[blank line]
,1,2,3,4,5,6,7,8,9,10,11,12
A,2.5012,2.4987,...
B,1.2501,1.2478,...
...
H,0.0400,0.0395,...
```

The driver and processor both handle this format, including `utf-8-sig` BOM encoding
from Windows Excel exports.

## Dependencies

- `matplotlib` — heatmap visualization
- `numpy` — array operations for plotting
- `anthropic` — AI analysis (optional, falls back to cached responses)

Install:
```bash
pip install "device-skills[biotek-gen5]"
```
