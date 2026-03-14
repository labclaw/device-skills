# Gen5 Protocol File Format (.prt)

**Source:** General knowledge of Gen5 protocol files.
Items marked [UNVERIFIED] need confirmation against actual Gen5 protocol internals.

## Overview

Gen5 protocols are saved as `.prt` files. These files define the complete read procedure
including detection parameters, plate layout, pre-read steps, and data reduction settings.

## File Characteristics [UNVERIFIED]

| Property | Value |
|----------|-------|
| Extension | `.prt` |
| Format | Proprietary binary/XML hybrid |
| Created by | Gen5 Protocol Editor |
| Editable outside Gen5 | No (proprietary format) |
| Portable | Yes, between Gen5 installations of same major version |

## Protocol Contents

A Gen5 protocol encapsulates:

### 1. Read Configuration

- Detection mode (absorbance, fluorescence, luminescence)
- Wavelength(s) for excitation and emission
- Optics position (top/bottom for fluorescence)
- Gain/sensitivity settings
- Read type (endpoint, kinetic, spectral scan)

### 2. Procedure Steps

Ordered sequence of steps executed before or between reads:

- **Temperature Set** — target temperature and wait-for-equilibration flag
- **Delay** — wait time in seconds or minutes
- **Shake** — mode (linear/orbital/double-orbital), duration, speed
- **Read** — the actual measurement step

### 3. Plate Layout (optional)

- Well assignments: standards, unknowns, blanks, controls
- Concentration values for standard wells
- Sample identifiers
- Group definitions for statistical analysis

### 4. Data Reduction (optional)

- Blank subtraction settings
- Curve fitting parameters (linear, 4PL, 5PL, polynomial)
- Concentration calculation method
- Cutoff values and flags

## Experiment Files (.xpt) [UNVERIFIED]

When a protocol is executed, the results are saved as an experiment file:

| Property | Value |
|----------|-------|
| Extension | `.xpt` |
| Contains | Protocol + raw data + analysis results |
| Reopenable | Yes, in Gen5 |
| Exportable | Yes, to CSV/Excel/PDF from within Gen5 |

## Working with Protocol Files

- Protocols are created and edited exclusively within the Gen5 software.
- Protocols can be shared between computers with the same Gen5 version.
- Forward compatibility is generally maintained (older protocols open in newer Gen5).
  [UNVERIFIED]
- Backward compatibility is not guaranteed (newer protocols may not open in older Gen5).
  [UNVERIFIED]

## Automation Note

For COM automation, protocols are referenced by file path:

```python
# Load a protocol for automated reading
protocol = gen5.Protocols.Open("C:\\Protocols\\ELISA_450nm.prt")
results = reader.ReadPlate(protocol)
```

Protocol files cannot be programmatically created or modified through the COM interface.
They must be created in the Gen5 GUI. [UNVERIFIED]
