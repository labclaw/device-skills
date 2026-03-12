# PrairieLink GetState Reference

> Source: PrairieView Help documentation and PrairieLink API reference.
> States are queried via `pl.GetState(key)` or `pl.GetState(key, subkey)`.
> Return values are always strings — parse to appropriate types in client code.

## Usage

```python
import win32com.client
pl = win32com.client.Dispatch("PrairieLink64.Application")
pl.Connect("127.0.0.1", "0000")

# Single-key query
framerate = float(pl.GetState("framerate"))

# Two-key query (key + subkey)
um_per_px_x = float(pl.GetState("micronsPerPixel", "XAxis"))
```

## Acquisition States

| Key | Subkey | Return Type | Description |
|-----|--------|-------------|-------------|
| `framerate` | — | float (string) | Current frame rate in Hz (e.g., "29.97") |
| `pixelsPerLine` | — | int (string) | Pixels per scan line (e.g., "512") |
| `linesPerFrame` | — | int (string) | Lines per frame (e.g., "512") |
| `micronsPerPixel` | `XAxis` | float (string) | Microns per pixel, X dimension |
| `micronsPerPixel` | `YAxis` | float (string) | Microns per pixel, Y dimension |
| `opticalZoom` | — | float (string) | Current zoom factor (e.g., "1.0") |
| `dwellTime` | — | float (string) | Pixel dwell time in microseconds |
| `scanMode` | — | string | Current scan mode: "ResonantGalvo" or "Galvo" |
| `acquisition_state` | — | string | "Idle", "Running", "Paused" `[UNVERIFIED]` |

## Laser States

| Key | Subkey | Return Type | Description |
|-----|--------|-------------|-------------|
| `laser_power` | — | float (string) | Current Pockels cell setting (percent or raw) |
| `multiphoton_wavelength` | — | float (string) | Current laser wavelength in nm |
| `laser_mode_locked` | — | bool (string) | "True" if laser is mode-locked `[UNVERIFIED]` |

## Channel / PMT States

| Key | Subkey | Return Type | Description |
|-----|--------|-------------|-------------|
| `channel_number` | — | int (string) | Number of active channels |
| `pmt_voltage` | `1` | float (string) | PMT 1 control voltage `[UNVERIFIED]` |
| `pmt_voltage` | `2` | float (string) | PMT 2 control voltage `[UNVERIFIED]` |
| `pmt_voltage` | `3` | float (string) | PMT 3 control voltage `[UNVERIFIED]` |
| `pmt_voltage` | `4` | float (string) | PMT 4 control voltage `[UNVERIFIED]` |

## Motor / Stage States

| Key | Subkey | Return Type | Description |
|-----|--------|-------------|-------------|
| `motor_position` | `X` | float (string) | XY stage X position in um `[UNVERIFIED]` |
| `motor_position` | `Y` | float (string) | XY stage Y position in um `[UNVERIFIED]` |
| `motor_position` | `Z` | float (string) | Z-axis position in um `[UNVERIFIED]` |

Note: For motor positions, the COM method `pl.GetMotorPosition("Z")` returns a float
directly and is the preferred API. The GetState keys above are less commonly used.

## Z-Stack States `[UNVERIFIED]`

| Key | Subkey | Return Type | Description |
|-----|--------|-------------|-------------|
| `zstack_start` | — | float (string) | Z-stack start position in um |
| `zstack_stop` | — | float (string) | Z-stack end position in um |
| `zstack_step_size` | — | float (string) | Z-stack step size in um |
| `zstack_num_slices` | — | int (string) | Computed number of slices |

## File States `[UNVERIFIED]`

| Key | Subkey | Return Type | Description |
|-----|--------|-------------|-------------|
| `save_path` | — | string | Current save directory |
| `file_name` | — | string | Current base filename |
| `file_iteration` | — | int (string) | Current iteration counter |

## Notes

- All return values are strings. Cast to `float`, `int`, or `bool` as needed.
- If a key is not recognized, GetState returns an empty string `""`.
- Some keys are version-dependent — behavior may differ between PrairieView 5.x versions.
- The `[UNVERIFIED]` keys are reported by community users but not confirmed in official
  Bruker documentation. Test on your system before relying on them in automation scripts.
