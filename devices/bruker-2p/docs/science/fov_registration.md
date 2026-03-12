# FOV Registration Across Sessions

> Methods for finding the same neurons across days, weeks, or months.

## The Problem

In longitudinal experiments (e.g., learning studies, disease progression), the same
population of neurons must be imaged repeatedly across sessions separated by days to
months. Between sessions:

- The cranial window may shift slightly
- Brain tissue can swell or shrink
- The stage coordinates have limited absolute accuracy (~1 um)
- The animal is removed and re-headfixed each session

The challenge: given a reference image from session 1 and a live image from session N,
find the transformation that aligns them so the same neurons can be identified.

## Vasculature Landmark Approach

### Why Vasculature?

Blood vessels provide natural fiducial landmarks:

- Visible in widefield and two-photon (with or without dye)
- Highly stable over weeks to months
- Unique branching patterns at each cortical location
- Visible at the brain surface (easy to image before diving deep)

### Practical Workflow

1. **Session 1 (reference):**
   - Navigate to target cortical region
   - Capture a widefield or low-zoom 2P image of surface vasculature
   - Save as reference image: `vasculature_reference_session01.tif`
   - Record stage coordinates: X, Y, Z
   - Image the target FOV at experimental zoom and depth
   - Save FOV reference: `fov_reference_session01.tif`

2. **Session N:**
   - Navigate to saved stage coordinates (PrairieLink):
     ```python
     pl.SendScriptCommands("-SetMotorPosition 'X' '5000.0'")
     pl.SendScriptCommands("-SetMotorPosition 'Y' '3000.0'")
     pl.SendScriptCommands("-SetMotorPosition 'Z' '150.0'")
     ```
   - Capture live vasculature image
   - Compare with reference; adjust XY until vessels match
   - Capture live FOV image at experimental settings
   - Run image registration against reference FOV

## Stage Coordinate Save/Recall

### Saving Coordinates via PrairieLink

```python
# Record current position
x = pl.GetMotorPosition("X")
y = pl.GetMotorPosition("Y")
z = pl.GetMotorPosition("Z")

# Save to file
import json
coords = {"x": x, "y": y, "z": z, "session": "session_01", "date": "2024-01-15"}
with open("fov_coordinates.json", "w") as f:
    json.dump(coords, f, indent=2)
```

### Recalling Coordinates

```python
with open("fov_coordinates.json") as f:
    coords = json.load(f)

pl.SendScriptCommands(f"-SetMotorPosition 'X' '{coords['x']}'")
pl.SendScriptCommands(f"-SetMotorPosition 'Y' '{coords['y']}'")
pl.SendScriptCommands(f"-SetMotorPosition 'Z' '{coords['z']}'")
```

### Limitations of Coordinate Recall

- Stage repeatability: ~0.5 um (encoder-based)
- But animal positioning in the headbar introduces ~10-50 um variability
- Coordinates provide a starting point; fine alignment requires image registration

## Image Registration Algorithms

### Rigid Registration (Translation + Rotation)

Sufficient when:
- Good cranial window quality
- Minimal tissue deformation
- Short inter-session intervals (days)

```python
from skimage.registration import phase_cross_correlation
import numpy as np

def rigid_register(reference: np.ndarray, moving: np.ndarray) -> tuple:
    """Find rigid (translation) alignment between two images.

    Returns:
        Tuple of (shift_y, shift_x) in pixels.
    """
    shift, error, diffphase = phase_cross_correlation(reference, moving)
    return shift

# Apply
from scipy.ndimage import shift as ndi_shift
aligned = ndi_shift(moving_image, rigid_register(reference, moving_image))
```

### Affine Registration (Translation + Rotation + Scaling + Shear)

Useful when:
- Zoom or focus changed between sessions
- Slight tissue distortion

```python
from skimage.transform import AffineTransform, warp
from skimage.feature import match_descriptors, ORB
from skimage.measure import ransac

def affine_register(reference: np.ndarray, moving: np.ndarray) -> AffineTransform:
    """Find affine transformation using feature matching."""
    orb = ORB(n_keypoints=500)

    orb.detect_and_extract(reference)
    kp_ref, desc_ref = orb.keypoints, orb.descriptors

    orb.detect_and_extract(moving)
    kp_mov, desc_mov = orb.keypoints, orb.descriptors

    matches = match_descriptors(desc_ref, desc_mov, cross_check=True)

    src = kp_ref[matches[:, 0]]
    dst = kp_mov[matches[:, 1]]

    model, inliers = ransac(
        (src, dst), AffineTransform, min_samples=3, residual_threshold=2
    )
    return model

# Apply
transform = affine_register(reference, moving_image)
aligned = warp(moving_image, transform.inverse, output_shape=reference.shape)
```

### Non-Rigid Registration (Deformable)

Required when:
- Significant tissue deformation (chronic windows over months)
- Brain pulsation artifacts not fully corrected
- Large FOVs with variable distortion

Tools:
- **ANTs (Advanced Normalization Tools):** Gold standard for non-rigid registration.
  SyN algorithm provides diffeomorphic warping.
  ```bash
  antsRegistration -d 2 -f reference.tif -m moving.tif \
    -t SyN[0.1] -c 100x70x50 -s 2x1x0 -o aligned_
  ```
- **SimpleITK:** Python interface to ITK registration algorithms
- **suite2p:** Built-in non-rigid registration for within-session motion correction
  (can be adapted for cross-session)

## Cell Matching Across Sessions

After image registration, individual cells must be matched:

### CellReg (Sheintuch et al., 2017)

- **Paper:** "Tracking the Same Neurons across Multiple Days in Ca2+ Imaging Data"
  (Cell Reports, 2017)
- **Repository:** github.com/zivlab/CellReg (MATLAB)
- **Method:**
  1. Register spatial footprints from each session using the centroid-based approach
  2. Compute pairwise distances between all cell pairs across sessions
  3. Use a probabilistic model to determine matches (accounting for registration
     uncertainty and cell density)
  4. Output: mapping table of cell IDs across sessions

### Track2p

- **Repository:** github.com/rfrancis1/Track2p (Python)
- **Method:** Similar to CellReg but implemented in Python
- **Input:** suite2p output directories from multiple sessions
- **Output:** Cross-session cell matching table

### Manual Matching

For small populations (<50 cells) or validation:
1. Overlay registered FOV images from two sessions
2. Visually identify matching cells by position and morphology
3. Create a correspondence table
4. Use as ground truth for validating automated methods

## Complete Cross-Session Pipeline

```
Session 1:
  Navigate to target → Image vasculature → Save coordinates
  → Image FOV → Run suite2p → Extract ROIs

Session N:
  Recall coordinates → Image vasculature → Manual XY adjustment
  → Image FOV → Run suite2p → Extract ROIs
  → Register Session N FOV to Session 1 (rigid or affine)
  → Run CellReg/Track2p for cell matching
  → Merge traces into longitudinal dataset
```

## Tips for Reliable Cross-Session Registration

1. **Use consistent imaging parameters** — same zoom, same wavelength, same PMT gain
   if possible. Changes make registration harder.
2. **Always capture a vasculature reference** at the start of each session.
3. **Save coordinates AND reference images** — coordinates are approximate, images are
   the ground truth for alignment.
4. **Use a high-quality cranial window** — a stable, clear window is the single most
   important factor for longitudinal imaging.
5. **Image at consistent depth** — use the vasculature pattern and Z-stack to find the
   same focal plane.
6. **Maintain consistent head fixation** — the more reproducible the head position,
   the closer the initial coordinates will be.
