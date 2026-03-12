# PrairieLink Command Reference

> Source: PrairieView Help documentation, Bruker PrairieLink API Guide, and community usage.
> Commands are sent via `pl.SendScriptCommands(cmd)` (COM) or as raw strings over TCP (port 1236).
> Commands marked `[UNVERIFIED]` are inferred from community scripts and not confirmed in
> official Bruker documentation.

## Acquisition Commands

### `-TSeries`
Start a time-series acquisition with current settings.

```
pl.SendScriptCommands("-TSeries")
```

Acquires the configured number of frames at the current frame rate. Files are saved
to the path set by `-SetSavePath` with the name set by `-SetFileName Tseries`.

### `-ZSeries`
Start a Z-stack acquisition.

```
pl.SendScriptCommands("-ZSeries")
```

Acquires frames at each Z position between the configured start and stop positions,
stepping by the configured step size. See Z-stack configuration commands below.

### `-SingleImage`
Acquire a single frame.

```
pl.SendScriptCommands("-SingleImage")
```

Captures one frame at the current settings. Useful for preview, alignment, and
reference images.

### `-LineScan`
Start a line-scan acquisition.

```
pl.SendScriptCommands("-LineScan")
```

Acquires a single scan line repeatedly over time. Used for high-temporal-resolution
measurements (e.g., calcium transients in dendrites, blood flow velocity).

### `-Abort`
Stop the current acquisition immediately.

```
pl.SendScriptCommands("-Abort")
```

Halts any running acquisition (T-series, Z-series, line scan). Data acquired up to
the abort point is saved.

### `-LiveScan` `[UNVERIFIED]`
Start continuous live scanning (preview mode).

```
pl.SendScriptCommands("-LiveScan")
```

Begins continuous scanning for live preview. Frames are displayed but not saved to disk.

### `-StopLiveScan` `[UNVERIFIED]`
Stop live scanning.

```
pl.SendScriptCommands("-StopLiveScan")
```

## Scan Mode Commands

### `-SetAcquisitionMode ResonantGalvo`
Switch to resonant-galvo scanning mode.

```
pl.SendScriptCommands("-SetAcquisitionMode ResonantGalvo")
```

Resonant galvo mode uses the 8 kHz resonant scanner for the X axis, providing
30 fps at 512x512. Bidirectional scanning. Best for calcium imaging and time-series.

### `-SetAcquisitionMode Galvo`
Switch to galvo-galvo scanning mode.

```
pl.SendScriptCommands("-SetAcquisitionMode Galvo")
```

Galvo-galvo mode uses conventional galvanometers for both axes. Slower but allows
arbitrary dwell times and unidirectional scanning. Best for z-stacks, tile scans,
and high-resolution structural imaging.

## Laser Commands

### `-SetMultiphotonWavelength '<nm>' 1`
Set the Ti:Sapphire laser wavelength.

```
pl.SendScriptCommands("-SetMultiphotonWavelength '920' 1")
```

- First argument: wavelength in nm (string, quoted)
- Second argument: laser index (1 = primary laser)
- Range: 680-1080 nm (Chameleon Ultra II) or 690-1040 nm (Ultra I)
- Tuning speed: >40 nm/s; allow 5-10 seconds for stabilization at new wavelength
- The `delays.after_wavelength_change` in profile.yaml (8000 ms) accounts for this

### `-SetLaserPower '<percent>' 1` `[UNVERIFIED]`
Set the Pockels cell transmission as a percentage.

```
pl.SendScriptCommands("-SetLaserPower '25' 1")
```

Controls power delivered to the sample via the Pockels cell EOM. Actual power at
the sample depends on wavelength, objective transmission, and optical path losses.

## Channel / PMT Commands

### `-SetChannel '<n>' 'On'` / `-SetChannel '<n>' 'Off'`
Enable or disable a detection channel.

```
pl.SendScriptCommands("-SetChannel '1' 'On'")
pl.SendScriptCommands("-SetChannel '2' 'Off'")
```

Channel numbers correspond to PMT detector positions (1-4 on quad detector systems).

### `-SetPMTVoltage '<n>' '<voltage>'` `[UNVERIFIED]`
Set the PMT control voltage for a channel.

```
pl.SendScriptCommands("-SetPMTVoltage '1' '650'")
```

Maximum safe voltage: 900 V. Higher voltages increase gain but also increase noise
and risk of PMT damage from bright signals.

## Stage Commands

### `-SetMotorPosition 'Z' '<position>'`
Move the Z-axis motor to an absolute position.

```
pl.SendScriptCommands("-SetMotorPosition 'Z' '100.5'")
```

Position in micrometers. Use `pl.GetMotorPosition("Z")` to read current position.
Allow settling time after moves (1000 ms recommended for piezo Z).

### `-SetMotorPosition 'X' '<position>'` `[UNVERIFIED]`
### `-SetMotorPosition 'Y' '<position>'` `[UNVERIFIED]`
Move XY stage to absolute positions.

```
pl.SendScriptCommands("-SetMotorPosition 'X' '5000.0'")
pl.SendScriptCommands("-SetMotorPosition 'Y' '3000.0'")
```

## Z-Stack Configuration

### `-SetZSeriesStepSize '<um>'`
Set the Z-step size for z-stack acquisition.

```
pl.SendScriptCommands("-SetZSeriesStepSize '1.0'")
```

Minimum step: 0.05 um (piezo limit). Typical values: 0.5-2.0 um for cellular resolution.

### `-SetZSeriesStart 'allSettings'`
Set the current position and settings as the Z-stack start point.

```
pl.SendScriptCommands("-SetZSeriesStart 'allSettings'")
```

Records current Z position, laser power, PMT gain, and all other parameters as the
starting configuration. The `allSettings` argument preserves all parameters, not just Z.

### `-SetZSeriesStop 'allSettings'`
Set the current position and settings as the Z-stack end point.

```
pl.SendScriptCommands("-SetZSeriesStop 'allSettings'")
```

## File Management Commands

### `-SetSavePath <directory>`
Set the directory where acquired data will be saved.

```
pl.SendScriptCommands("-SetSavePath C:\\Data\\2024-01-15")
```

Use Windows path separators. Directory must exist.

### `-SetFileName Tseries <name>`
Set the base filename for T-series acquisitions.

```
pl.SendScriptCommands("-SetFileName Tseries experiment_001")
```

### `-SetFileName Zseries <name>`
Set the base filename for Z-series acquisitions.

```
pl.SendScriptCommands("-SetFileName Zseries zstack_001")
```

### `-SetFileIteration Zseries <n>`
Set the iteration counter for Z-series filenames.

```
pl.SendScriptCommands("-SetFileIteration Zseries 1")
```

Resets the auto-increment counter. Useful when starting a new experiment sequence.

## Mark Points Commands

### `-MarkPoints '<group>' '<protocol>'`
Execute a mark-points stimulation protocol.

```
pl.SendScriptCommands("-MarkPoints 'StimGroup1' 'PhotostimProtocol'")
```

Mark Points is used for targeted photostimulation (e.g., optogenetic activation of
specific cells). The group and protocol must be pre-configured in PrairieView's
Mark Points interface.

## Zoom and Resolution `[UNVERIFIED]`

### `-SetZoom '<factor>'`
Set the optical zoom factor.

```
pl.SendScriptCommands("-SetZoom '2.0'")
```

Zoom range: 1x to 16x (resonant galvo mode). Higher zoom reduces FOV but increases
pixel density. At 16x/0.8NA with 1x zoom, the FOV is approximately 800 um.

### `-SetPixelsPerLine '<n>'` `[UNVERIFIED]`
Set the number of pixels per scan line.

```
pl.SendScriptCommands("-SetPixelsPerLine '512'")
```

Common values: 256, 512, 1024. Higher values increase spatial resolution but reduce
frame rate in resonant mode.
