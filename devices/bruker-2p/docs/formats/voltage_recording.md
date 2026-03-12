# Voltage Recording Format (.env files)

> Source: PrairieView documentation, empirical analysis of .env output files.

## Overview

PrairieView can record analog voltage signals synchronized with image acquisition using
the system's DAQ (data acquisition) board. These recordings are saved as `.env` files
alongside the image data. Common uses:

- Stimulus timing (photodiode, TTL triggers)
- Locomotion (treadmill encoder)
- Licking sensor
- Electrophysiology (LFP, EEG)
- Respiration monitoring
- Frame clock and line clock signals

## File Format

The `.env` file is a binary file containing interleaved voltage samples from all
configured input channels.

### Header

The `.env` file has no header. All recording parameters (sample rate, channel count,
channel names) are stored in the accompanying XML metadata file.

### Data Layout

| Property | Value |
|----------|-------|
| Data type | 64-bit floating-point (double) |
| Byte order | Little-endian |
| Layout | Interleaved: [ch0_t0, ch1_t0, ..., chN_t0, ch0_t1, ch1_t1, ...] |
| Sample rate | Defined in XML (typically 1-10 kHz) |
| Voltage range | Typically +/- 10 V (DAQ dependent) |

### Relevant XML Keys

The voltage recording parameters are stored in the Prairie XML metadata:

| XML Key | Description |
|---------|-------------|
| `VoltageRecording` | Parent element for all recording config |
| `VoltageOutput` | Output channel configuration `[UNVERIFIED]` |
| `VoltageInput` | Input channel configuration `[UNVERIFIED]` |

Within the XML `Sequence` elements, timing information links voltage samples to frames:

```xml
<VoltageData absoluteTime="0.000" relativeTime="0.000" />
```

## Reading .env Files with Python

```python
import numpy as np


def load_voltage_recording(
    env_path: str,
    n_channels: int,
    sample_rate: float,
) -> tuple[np.ndarray, np.ndarray]:
    """Load a PrairieView voltage recording (.env file).

    Args:
        env_path: Path to the .env file.
        n_channels: Number of recorded channels (from XML metadata).
        sample_rate: Sampling rate in Hz (from XML metadata).

    Returns:
        Tuple of (time_array, voltage_array).
        time_array: 1D array of time points in seconds.
        voltage_array: 2D array of shape (n_samples, n_channels).
    """
    raw = np.fromfile(env_path, dtype=np.float64)

    n_samples = len(raw) // n_channels
    voltages = raw[:n_samples * n_channels].reshape(n_samples, n_channels)

    time = np.arange(n_samples) / sample_rate

    return time, voltages


# Usage
time, voltages = load_voltage_recording(
    "TSeries-01012024-1200-001.env",
    n_channels=3,
    sample_rate=10000.0,  # 10 kHz
)

print(f"Duration: {time[-1]:.1f} seconds")
print(f"Channels: {voltages.shape[1]}")

# Extract individual channels
stimulus = voltages[:, 0]
locomotion = voltages[:, 1]
lick_sensor = voltages[:, 2]
```

## Synchronization with Imaging

### Frame-Voltage Alignment

Voltage recordings are synchronized with imaging via the DAQ clock:

1. PrairieView records a frame clock signal (internal TTL pulse at each frame start)
2. This clock signal can be recorded on one of the voltage channels for verification
3. The XML metadata provides `absoluteTime` for each frame, which corresponds to the
   voltage recording timeline

### Typical Synchronization Workflow

```python
import numpy as np
from pathlib import Path


def align_voltage_to_frames(
    env_path: str,
    xml_metadata: dict,
    n_channels: int,
    sample_rate: float,
    frame_channel: int = 0,
) -> dict:
    """Align voltage recording samples to imaging frames.

    Uses frame times from XML metadata to compute voltage sample indices
    corresponding to each frame.
    """
    time, voltages = load_voltage_recording(env_path, n_channels, sample_rate)

    # Get frame times from XML metadata
    frame_times = []
    for seq in xml_metadata.get("sequences", []):
        for frame in seq.get("frames", []):
            t = float(frame.get("absolute_time", 0))
            frame_times.append(t)

    frame_times = np.array(frame_times)

    # Convert frame times to voltage sample indices
    frame_indices = (frame_times * sample_rate).astype(int)
    frame_indices = np.clip(frame_indices, 0, len(time) - 1)

    return {
        "time": time,
        "voltages": voltages,
        "frame_times": frame_times,
        "frame_indices": frame_indices,
    }
```

## Common Channel Configurations

| Channel | Signal | Typical Range | Sample Rate |
|---------|--------|---------------|-------------|
| 0 | Frame clock (TTL) | 0-5 V | 10 kHz |
| 1 | Stimulus trigger | 0-5 V | 10 kHz |
| 2 | Treadmill encoder | 0-5 V | 10 kHz |
| 3 | Lick sensor | 0-5 V | 10 kHz |
| 4 | Photodiode | 0-10 V | 10 kHz |

Note: Channel assignments are lab-specific. Always verify with the XML metadata
and your lab's DAQ wiring documentation.
