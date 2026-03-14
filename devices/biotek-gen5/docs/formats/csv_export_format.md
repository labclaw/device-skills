# Gen5 CSV Export Format

**Source:** Observed Gen5 CSV exports and Gen5Processor implementation.

## Overview

Gen5 exports plate reader data as CSV files with a specific structure: metadata header
rows followed by an 8x12 (96-well) or 16x24 (384-well) grid of numeric values.

## File Encoding

- **Encoding:** UTF-8 with BOM (`utf-8-sig`)
- **Delimiter:** Comma (`,`)
- **Line endings:** CRLF (`\r\n`)

## Structure

### Metadata Section

The first N rows contain key-value metadata as comma-separated pairs. These rows do NOT
start with a plate row letter (A-H). Common metadata fields:

| Key | Example Value | Description |
|-----|--------------|-------------|
| Protocol | ELISA 450nm | Protocol name used for the read |
| Mode | absorbance | Detection mode (absorbance/fluorescence/luminescence) |
| Wavelength | 450 | Primary read wavelength in nm |
| Date | 2025-01-15 | Read date |
| Time | 14:30:22 | Read time |
| Temperature | 25.0 | Reader temperature in Celsius |
| Reader | Synergy H1 | Reader model |
| Serial | 12345678 | Reader serial number [UNVERIFIED] |

### Data Grid Section

After the metadata rows, the data grid appears. Each row starts with a row letter (A-H
for 96-well plates) followed by 12 numeric values:

```
A,0.0451,0.0523,0.8921,0.7654,...,0.0412,0.0398
B,0.0478,0.0501,1.2345,0.9876,...,0.0425,0.0410
...
H,0.0390,0.0415,0.5432,0.4321,...,0.0401,0.0395
```

### Complete Example (96-well absorbance)

```csv
Protocol,ELISA Demo
Mode,absorbance
Wavelength,450
Date,2025-01-15

,1,2,3,4,5,6,7,8,9,10,11,12
A,2.4521,2.4689,0.8921,0.7654,1.2345,0.9876,0.5432,1.1234,0.6789,0.8765,0.0412,0.0398
B,1.2103,1.2256,1.0234,0.8901,0.7654,1.3456,0.4321,0.9876,1.1234,0.5678,0.0425,0.0410
C,0.6234,0.6178,0.9012,1.1234,0.8765,0.6543,1.2345,0.7890,0.4567,1.0123,0.0401,0.0415
D,0.3012,0.3089,0.7890,0.5432,1.0123,0.8765,0.6789,1.0987,0.8901,0.7654,0.0390,0.0408
E,0.1567,0.1523,1.1234,0.6789,0.4321,1.1234,0.9012,0.5432,1.0234,0.8901,0.0412,0.0395
F,0.0789,0.0812,0.5678,0.8901,0.9876,0.4567,1.0123,0.8765,0.7890,0.6543,0.0398,0.0420
G,0.0401,0.0423,0.4321,1.0123,0.7890,0.9012,0.5678,1.2345,0.6543,0.9876,0.0410,0.0401
H,0.0390,0.0415,0.6543,0.4321,1.0987,0.7890,0.8901,0.6789,1.1234,0.5432,0.0401,0.0395
```

## Parsing Notes

- **Row detection:** A line is a data row if its first field (stripped, uppercased) is a
  single letter A-H (96-well) or A-P (384-well).
- **Column count:** Data rows have 12 values after the row letter (96-well) or 24 values
  (384-well).
- **Non-numeric values:** Some wells may contain text (e.g., "OVERFLOW", "ERR") instead
  of numbers. These should be preserved as strings.
- **Empty rows:** Blank lines between metadata and data sections are common and should be
  skipped.
- **Header row:** An optional header row with column numbers (`,1,2,3,...,12`) may appear
  before the data grid.

## Gen5Processor Compatibility

The `Gen5Processor.load()` method in the device-skills codebase parses this format:

1. Lines where the first field is a row letter are parsed as well data.
2. All other non-empty lines with at least 2 fields are parsed as key-value metadata.
3. Returns a dict with keys: `wells` (dict[str, float|str]), `metadata` (dict[str, str]),
   `file` (str).

## Excel Export Format [UNVERIFIED]

Gen5 can also export to `.xlsx` format. The structure is similar:

- Sheet 1: Protocol information and metadata
- Sheet 2: Raw data in grid format
- Sheet 3: Reduced data (if data reduction is configured in the protocol)

The exact sheet names and layout may vary by Gen5 version.
