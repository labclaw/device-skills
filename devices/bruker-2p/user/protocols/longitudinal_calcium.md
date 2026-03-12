# Protocol: Longitudinal Calcium Imaging

> Standard operating procedure for chronic calcium imaging across multiple sessions.
> Tracks the same neurons over days to weeks using FOV registration.

## Prerequisites

- Cranial window implanted and clear
- GCaMP expressed (AAV: wait 2-4 weeks; transgenic: ready)
- Reference images from first session saved
- Stage coordinates from first session saved
- PrairieView running, system warmed up (Pockels >20 min)

## Session Workflow

### 1. System Preparation (15 min before imaging)

1. Verify cooling water running at 25 C
2. Power on resonant galvo control box
3. Turn laser key ON; wait for mode-lock
4. Launch PrairieView
5. Wait for Pockels cell warmup (20-30 min from key-on)

### 2. Animal Preparation

1. Anesthetize animal (if applicable) or habituate to headbar
2. Secure in headbar on the microscope stage
3. Clean cranial window with sterile saline
4. Apply water-dipping medium (sterile water or artificial CSF) to objective

### 3. Navigate to Saved Coordinates

```python
# Recall saved coordinates
pl.SendScriptCommands("-SetMotorPosition 'X' '<saved_x>'")
pl.SendScriptCommands("-SetMotorPosition 'Y' '<saved_y>'")
pl.SendScriptCommands("-SetMotorPosition 'Z' '<saved_z>'")
```

Or manually enter coordinates in PrairieView stage control panel.

### 4. Capture Vasculature Reference Image

1. Set wavelength to 920 nm (or 800 nm if using fluorescein-dextran)
2. Set zoom to 1x (widest FOV)
3. Focus on the brain surface (pial vasculature visible)
4. Start live scan at low power (5-10% Pockels)
5. Capture single image: `vasculature_sessionN.tif`
6. Compare with reference vasculature from session 1
7. Adjust XY position until vessel pattern matches reference

### 5. FOV Registration

1. Navigate to imaging depth (Z position from previous session)
2. Set experimental zoom (same as reference session)
3. Capture a single frame or short average
4. Compare with reference FOV image:
   - Overlay in ImageJ/FIJI
   - Or run rigid registration algorithm
5. Fine-adjust XY and Z until cell pattern matches
6. Record final coordinates for this session

### 6. Set Imaging Parameters

| Parameter | Typical Value | Notes |
|-----------|---------------|-------|
| Wavelength | 920 nm | Standard for GCaMP |
| Scan mode | Resonant galvo | 30 fps |
| Resolution | 512x512 | Standard |
| Zoom | 2-4x | Match previous sessions |
| PMT voltage | 600-750 V | Adjust for consistent brightness |
| Pockels (%) | 15-40% | Adjust for consistent brightness |
| Duration | 5-30 min | Per trial/block |

**Important:** Use the same zoom and wavelength as previous sessions for consistent
pixel size and field of view. Adjust only PMT gain and laser power to compensate for
day-to-day brightness variations.

### 7. Acquire T-Series

```python
# Configure file saving
pl.SendScriptCommands(f"-SetSavePath {save_directory}")
pl.SendScriptCommands(f"-SetFileName Tseries {session_name}")

# Start acquisition
pl.SendScriptCommands("-TSeries")

# Monitor (check periodically for completion)
# Typical: 5-30 minute acquisition
```

During acquisition:
- Monitor image quality (focus drift, motion artifacts)
- Check water level on objective every 30 minutes
- Verify PMT dark areas remain dark (no light leaks)

### 8. Save Session Metadata

Record in a session log file:

```json
{
  "session_id": "session_015",
  "date": "2024-01-15",
  "animal_id": "mouse_042",
  "coordinates": {"x": 5000.0, "y": 3000.0, "z": 150.5},
  "wavelength_nm": 920,
  "zoom": 3.0,
  "pmt_voltage": [680, 600, 0, 0],
  "pockels_percent": 25,
  "duration_min": 10,
  "n_frames": 18000,
  "data_path": "D:\\Data\\mouse042\\session015\\",
  "notes": "Good window clarity, minimal motion"
}
```

### 9. Post-Acquisition

1. Stop acquisition (if not auto-stopped)
2. Capture final vasculature image for reference
3. Capture a final FOV image for registration verification
4. Set PMT gain to 0
5. Remove animal from headbar
6. Clean objective

## Post-Processing Pipeline

### Same Day

1. Transfer data to analysis server
2. Run suite2p motion correction + ROI detection
3. Quick-check: overlay with previous session's ROIs

### Cross-Session Analysis

1. Register FOV images across all sessions (rigid or affine)
2. Run CellReg or Track2p for cell matching
3. Merge fluorescence traces into longitudinal dataset
4. Analyze: stability of tuning, learning-related changes, etc.

## Troubleshooting

| Issue | Cause | Solution |
|-------|-------|----------|
| Cannot find vasculature | Wrong Z or XY position | Start from scratch: low zoom, surface focus, search for landmarks |
| FOV looks different | Tissue growth or window degradation | Use non-rigid registration; may need to adjust ROIs |
| Lower SNR than previous | Indicator bleaching or window opacity | Increase power slightly; check window clarity |
| More motion artifacts | Loose headbar or animal stress | Re-tighten headbar; reduce stress; use heavier motion correction |
| Focus drifts during imaging | Thermal drift or water evaporation | Refill water; let system thermally equilibrate longer |
