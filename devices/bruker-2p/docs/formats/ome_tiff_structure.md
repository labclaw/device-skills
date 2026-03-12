# OME-TIFF File Structure — PrairieView Output

> Source: PrairieView file format documentation, empirical analysis of output files.

## Overview

PrairieView saves image data as individual OME-TIFF files — one file per frame per
channel. This is **not** a multi-page TIFF stack; each file contains exactly one 2D image.
The complete dataset is a directory of thousands of individual TIFF files plus an XML
metadata file.

## Directory Structure

### T-Series (Calcium Imaging)

```
TSeries-01012024-1200-001/
├── TSeries-01012024-1200-001.xml          # Complete metadata
├── TSeries-01012024-1200-001.env          # Environment file (voltage recordings)
├── TSeries-01012024-1200-001_Cycle00001_Ch1_000001.ome.tif
├── TSeries-01012024-1200-001_Cycle00001_Ch1_000002.ome.tif
├── TSeries-01012024-1200-001_Cycle00001_Ch1_000003.ome.tif
├── ...
├── TSeries-01012024-1200-001_Cycle00001_Ch1_018000.ome.tif
├── TSeries-01012024-1200-001_Cycle00001_Ch2_000001.ome.tif  # If 2 channels
├── ...
├── References/
│   └── TSeries-01012024-1200-001_Cycle00001_Ch1_000001_reference.tif
└── CYCLE_00001_RAWDATA_000001              # Raw binary (if enabled)
```

### Z-Series (Z-Stack)

```
ZSeries-01012024-1300-001/
├── ZSeries-01012024-1300-001.xml
├── ZSeries-01012024-1300-001_Cycle00001_Ch1_000001.ome.tif  # Slice 1
├── ZSeries-01012024-1300-001_Cycle00001_Ch1_000002.ome.tif  # Slice 2
├── ...
├── ZSeries-01012024-1300-001_Cycle00001_Ch1_000100.ome.tif  # Slice 100
└── ZSeries-01012024-1300-001_Cycle00001_Ch2_000001.ome.tif  # Ch2, Slice 1
```

### Single Image

```
SingleImage-01012024-1100-001/
├── SingleImage-01012024-1100-001.xml
├── SingleImage-01012024-1100-001_Cycle00001_Ch1_000001.ome.tif
└── SingleImage-01012024-1100-001_Cycle00001_Ch2_000001.ome.tif
```

## Filename Convention

```
<Type>-<DDMMYYYY>-<HHMM>-<###>_Cycle<#####>_Ch<#>_<######>.ome.tif
```

| Field | Format | Description |
|-------|--------|-------------|
| Type | string | "TSeries", "ZSeries", "SingleImage", "LineScan" |
| Date | DDMMYYYY | Acquisition date |
| Time | HHMM | Acquisition start time (24h) |
| Index | ### | Acquisition index (auto-incremented) |
| Cycle | ##### | Cycle number (zero-padded, 1-based) |
| Ch | # | Channel number (1-based) |
| Frame | ###### | Frame number within cycle (zero-padded, 1-based) |

## Image Properties

| Property | Value |
|----------|-------|
| Format | OME-TIFF (single-page) |
| Bit depth | 13-bit (stored as 16-bit unsigned integer) |
| Resolution | Typically 512x512 pixels |
| Pixel size | Depends on zoom and objective (see `micronsPerPixel` in XML) |
| Byte order | Little-endian |
| Compression | None (uncompressed) |
| OME metadata | Embedded in TIFF header (OME-XML) |

## Data Rate and Storage

| Configuration | Frame Rate | Data Rate | 10 min Session |
|--------------|------------|-----------|----------------|
| 512x512, 1 ch, 30 fps | 30 Hz | ~15.7 MB/s (~940 MB/min) | ~9.4 GB |
| 512x512, 2 ch, 30 fps | 30 Hz | ~31.4 MB/s (~1.88 GB/min) | ~18.8 GB |
| 256x256, 1 ch, 60 fps | 60 Hz | ~7.9 MB/s (~470 MB/min) | ~4.7 GB |

Storage planning: A typical 30-minute calcium imaging session at 512x512, 2 channels,
30 fps generates approximately 56 GB of data.

## File Count

A 10-minute T-series at 30 fps with 2 channels produces:

```
30 fps * 600 seconds * 2 channels = 36,000 individual TIFF files
```

This large file count can cause issues with:
- File system performance (especially on Windows NTFS with >100k files per directory)
- Backup and transfer operations
- File listing and sorting operations

## Loading with Python

### Using tifffile (Recommended)

```python
import tifffile
import numpy as np
from pathlib import Path


def load_tseries(directory: str, channel: int = 1) -> np.ndarray:
    """Load a T-series into a 3D numpy array (T, Y, X).

    Args:
        directory: Path to the TSeries directory.
        channel: Channel number (1-based).

    Returns:
        3D array of shape (n_frames, height, width), dtype uint16.
    """
    path = Path(directory)
    pattern = f"*_Ch{channel}_*.ome.tif"
    files = sorted(path.glob(pattern))

    if not files:
        raise FileNotFoundError(f"No files matching {pattern} in {directory}")

    # Read first frame to get dimensions
    first = tifffile.imread(str(files[0]))
    stack = np.empty((len(files), *first.shape), dtype=first.dtype)
    stack[0] = first

    for i, f in enumerate(files[1:], 1):
        stack[i] = tifffile.imread(str(f))

    return stack


# Usage
data = load_tseries("TSeries-01012024-1200-001", channel=1)
print(f"Shape: {data.shape}")  # (18000, 512, 512)
print(f"Dtype: {data.dtype}")  # uint16
```

### Memory-Mapped Loading (Large Datasets)

For datasets too large to fit in RAM:

```python
import tifffile
import numpy as np
from pathlib import Path


def load_tseries_mmap(directory: str, channel: int = 1) -> np.ndarray:
    """Load a T-series as a memory-mapped array.

    Uses a temporary binary file for memory-mapped access.
    Suitable for datasets larger than available RAM.
    """
    path = Path(directory)
    files = sorted(path.glob(f"*_Ch{channel}_*.ome.tif"))
    first = tifffile.imread(str(files[0]))

    mmap_path = path / f"_mmap_ch{channel}.dat"
    mmap = np.memmap(
        str(mmap_path),
        dtype=first.dtype,
        mode="w+",
        shape=(len(files), *first.shape),
    )

    for i, f in enumerate(files):
        mmap[i] = tifffile.imread(str(f))
        if i % 1000 == 0:
            mmap.flush()

    mmap.flush()
    return mmap
```

## Raw Binary Format

When raw data saving is enabled, PrairieView also writes raw binary data files:

```
CYCLE_00001_RAWDATA_000001
CYCLE_00001_RAWDATA_000002  # Split at 2 GB boundaries
```

| Property | Value |
|----------|-------|
| Format | Raw unsigned 16-bit integers |
| Byte order | Little-endian |
| Layout | Interleaved channels, frame-by-frame |
| Max file size | 2 GB (files split at boundary) |
| Header | None — pure pixel data |

To read raw data, you need the frame dimensions from the XML metadata:

```python
import numpy as np

width = 512   # from XML: pixelsPerLine
height = 512  # from XML: linesPerFrame
n_channels = 2

raw = np.fromfile("CYCLE_00001_RAWDATA_000001", dtype=np.uint16)
n_pixels_per_frame = width * height * n_channels
n_frames = len(raw) // n_pixels_per_frame
data = raw.reshape(n_frames, n_channels, height, width)
```

## Reference Images

PrairieView can save reference images in the `References/` subdirectory. These are
typically maximum-intensity projections or average frames used for alignment:

```
References/
├── TSeries-..._Cycle00001_Ch1_000001_reference.tif
└── TSeries-..._Cycle00001_Ch2_000001_reference.tif
```
