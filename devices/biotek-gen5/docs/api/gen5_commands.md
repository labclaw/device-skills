# Gen5 Software Commands Reference

**Source:** BioTek Gen5 user interface; items marked [UNVERIFIED] need confirmation.

## Menu Structure

### File Menu

| Command | Shortcut | Description |
|---------|----------|-------------|
| New Protocol | Ctrl+N | Create a new read protocol |
| Open Protocol | Ctrl+O | Open an existing .prt file |
| Save Protocol | Ctrl+S | Save the current protocol |
| New Experiment | — | Create a new experiment from a protocol |
| Open Experiment | — | Open a saved experiment (.xpt) |
| Export | — | Export data (CSV, Excel, PDF, XML) |
| Print | Ctrl+P | Print results or protocol |
| Exit | Alt+F4 | Close Gen5 |

### Protocol Menu

| Command | Description |
|---------|-------------|
| Protocol Summary | View/edit protocol steps |
| Plate Layout | Define well assignments (standards, samples, blanks) |
| Read Step | Configure detection parameters |
| Procedure | Add pre-read steps (shake, incubate, delay) |
| Data Reduction | Configure calculations (blanking, curve fitting) |

### Read Operations

| Command | Description |
|---------|-------------|
| Read Plate | Execute the current protocol on the loaded plate |
| Read Now | Quick single-wavelength read without a full protocol [UNVERIFIED] |
| Eject Plate | Extend the plate carrier for plate loading |
| Temperature | Set or check incubation temperature |
| Shake | Manual plate shaking |

### Data Menu [UNVERIFIED]

| Command | Description |
|---------|-------------|
| Statistics | View well statistics (mean, SD, CV%) |
| Standard Curve | View/edit standard curve fit |
| Well Data | View individual well readings |
| Plate View | Heatmap view of plate data |
| Kinetic Plot | Time-course plot (kinetic reads only) |

## Protocol Step Types

A Gen5 protocol is a sequence of steps executed in order:

1. **Set Temperature** — Set and wait for target temperature.
2. **Delay** — Wait a specified time.
3. **Shake** — Linear, orbital, or double-orbital shaking for a set duration.
4. **Read** — Perform the actual measurement.
5. **Loop** — Repeat steps (used in kinetic reads).

### Read Step Parameters

#### Absorbance

| Parameter | Range | Description |
|-----------|-------|-------------|
| Wavelength | 200-999 nm | Primary read wavelength |
| Reference wavelength | 200-999 nm | Background correction wavelength (optional) |
| Read speed | Normal / Fast | Normal reads each well individually [UNVERIFIED] |
| Read type | Endpoint / Kinetic / Spectral | Single point, time course, or wavelength scan |

#### Fluorescence

| Parameter | Range | Description |
|-----------|-------|-------------|
| Excitation | 200-700 nm | Excitation wavelength (filter or monochromator) |
| Emission | 300-700 nm | Emission wavelength (filter or monochromator) |
| Optics position | Top / Bottom | Read from above or below the plate |
| Sensitivity | 1-255 | PMT gain setting |
| Read type | Endpoint / Kinetic | Single point or time course |

#### Luminescence

| Parameter | Range | Description |
|-----------|-------|-------------|
| Integration time | 0.1-10 sec | Signal collection time per well [UNVERIFIED] |
| Gain | 100-255 | PMT gain [UNVERIFIED] |
| Read type | Endpoint / Kinetic | Single point or time course |

## Keyboard Shortcuts [UNVERIFIED]

| Shortcut | Action |
|----------|--------|
| F5 | Read Plate |
| F2 | Edit protocol |
| Ctrl+E | Export data |
| Ctrl+D | Data reduction settings |
| Ctrl+L | Plate layout editor |
