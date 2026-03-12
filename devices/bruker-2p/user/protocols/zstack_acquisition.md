# Protocol: Z-Stack Acquisition

> Standard operating procedure for acquiring Z-stacks on the Bruker Ultima Investigator.
> Z-stacks are used for structural imaging, measuring expression depth profiles,
> and 3D reconstruction of neural populations.

## Prerequisites

- System warmed up (Pockels cell >20 min)
- Sample in place, objective immersed
- Correct objective and filters installed
- Scan mode: galvo-galvo (recommended for z-stacks)

## Workflow

### 1. Set Scan Mode

Switch to galvo-galvo mode for z-stacks (unidirectional scanning, more uniform
illumination per plane):

```python
pl.SendScriptCommands("-SetAcquisitionMode Galvo")
```

Resonant galvo can also be used for faster z-stacks when speed matters more than
per-plane quality.

### 2. Set Wavelength

```python
# For GCaMP/GFP structural imaging
pl.SendScriptCommands("-SetMultiphotonWavelength '920' 1")

# Wait for stabilization
import time
time.sleep(8)  # 8 seconds for wavelength change
```

### 3. Navigate to Region of Interest

1. Start live scanning at low zoom (1x) and low power
2. Find the target region using vasculature landmarks
3. Increase zoom to desired level
4. Focus through the sample to identify the depth range of interest

### 4. Define Z-Stack Range

Navigate to the **top** of the desired range and mark it:

```python
# Move to top position
# (manually adjust Z in PrairieView, or:)
pl.SendScriptCommands("-SetMotorPosition 'Z' '100.0'")
time.sleep(1)

# Mark as z-stack start
pl.SendScriptCommands("-SetZSeriesStart 'allSettings'")
```

Navigate to the **bottom** of the desired range and mark it:

```python
# Move to bottom position
pl.SendScriptCommands("-SetMotorPosition 'Z' '250.0'")
time.sleep(1)

# Mark as z-stack stop
pl.SendScriptCommands("-SetZSeriesStop 'allSettings'")
```

### 5. Set Step Size

```python
# Typical step sizes:
# Fine:   0.5 um (Nyquist sampling for ~2 um axial resolution)
# Normal: 1.0 um (standard structural imaging)
# Coarse: 2.0-5.0 um (survey stack, faster)
pl.SendScriptCommands("-SetZSeriesStepSize '1.0'")
```

**Nyquist criterion:** For optimal axial sampling, step size should be less than half
the axial resolution. With 16x/0.8 NA at 920 nm, axial resolution is ~2 um, so
steps of 0.5-1.0 um are appropriate.

### 6. Configure Power Compensation (Optional)

For deep z-stacks, laser power should increase with depth to compensate for tissue
scattering. PrairieView supports automatic power depth compensation:

1. Set a lower Pockels value at the start (shallow) position
2. Set a higher Pockels value at the stop (deep) position
3. PrairieView interpolates (linearly or exponentially) between them

The `allSettings` argument in `-SetZSeriesStart` and `-SetZSeriesStop` captures
the Pockels setting at each endpoint.

### 7. Configure File Saving

```python
pl.SendScriptCommands(f"-SetSavePath {save_directory}")
pl.SendScriptCommands("-SetFileName Zseries zstack_001")
```

### 8. Acquire

```python
pl.SendScriptCommands("-ZSeries")
```

The acquisition proceeds automatically from start to stop, stepping by the
configured step size. Each Z plane is saved as a separate OME-TIFF per channel.

### 9. Verify

After acquisition completes:
1. Open the z-stack in PrairieView or ImageJ/FIJI
2. Scroll through Z planes to verify:
   - Consistent brightness (power compensation working)
   - No focus drift
   - Complete coverage of the region of interest
   - No motion artifacts

## Typical Parameters

### Structural Z-Stack (Survey)

| Parameter | Value |
|-----------|-------|
| Mode | Galvo |
| Resolution | 512x512 or 1024x1024 |
| Zoom | 1-2x |
| Step size | 2.0 um |
| Range | 0-300 um (cortex surface to deep layers) |
| Number of planes | 150 |
| Wavelength | 920 nm |
| Time | ~5-10 minutes |

### Fine Z-Stack (Single-Cell Resolution)

| Parameter | Value |
|-----------|-------|
| Mode | Galvo |
| Resolution | 512x512 |
| Zoom | 4-8x |
| Step size | 0.5 um |
| Range | 50 um centered on target cell |
| Number of planes | 100 |
| Wavelength | 920 nm |
| Time | ~3-5 minutes |

### Fast Z-Stack (Resonant, for Functional Volumes)

| Parameter | Value |
|-----------|-------|
| Mode | Resonant galvo |
| Resolution | 512x512 |
| Zoom | 2x |
| Step size | 5.0 um (piezo fast-Z) |
| Range | 50-100 um |
| Number of planes | 10-20 |
| Volume rate | Up to 5 Hz (piezo limited) |
| Use case | Volumetric calcium imaging |

## Post-Processing

### Loading Z-Stacks in Python

```python
import tifffile
import numpy as np
from pathlib import Path


def load_zstack(directory: str, channel: int = 1) -> np.ndarray:
    """Load a Z-stack into a 3D array (Z, Y, X)."""
    path = Path(directory)
    files = sorted(path.glob(f"*_Ch{channel}_*.ome.tif"))
    stack = np.array([tifffile.imread(str(f)) for f in files])
    return stack


# Maximum intensity projection
zstack = load_zstack("ZSeries-01012024-1300-001", channel=1)
mip = zstack.max(axis=0)  # Max projection along Z
```

### Common Visualizations

- **Maximum Intensity Projection (MIP):** `zstack.max(axis=0)` — shows all bright
  structures collapsed into a single plane
- **Average Projection:** `zstack.mean(axis=0)` — less noisy than MIP
- **Orthogonal Views (XZ, YZ):** Show depth profile at selected X or Y positions
- **3D Rendering:** Using napari, FIJI 3D Viewer, or Imaris

## Tips

1. **Always approach Z from the same direction** — piezo hysteresis can cause ~1 um
   offset depending on approach direction. Configure z-stacks as top-to-bottom
   (or bottom-to-top consistently).

2. **Use galvo mode for publication-quality stacks** — resonant mode's bidirectional
   scanning can introduce phase artifacts between odd/even lines.

3. **Monitor water level** — for long z-stacks, the immersion water may evaporate,
   degrading image quality at later Z planes.

4. **Check power compensation** — if deep planes are much dimmer than shallow planes,
   increase the power compensation range.
