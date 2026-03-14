# Gen5 COM Automation Interface

**Source:** BioTek Gen5 technical documentation; items marked [UNVERIFIED] need
confirmation against the actual Gen5 COM type library.

## Overview

Gen5 exposes a COM (Component Object Model) automation interface on Windows that allows
external programs to control the plate reader programmatically. This is the primary API
mode for automated workflows.

## Prerequisites

- Windows OS (7/10/11)
- Gen5 3.x installed with a valid license
- COM automation license (may be separate from the base Gen5 license) [UNVERIFIED]
- Gen5 must be running (the COM server is hosted in the Gen5 process)

## Connection

```python
# Python example using win32com (pywin32)
import win32com.client

gen5 = win32com.client.Dispatch("Gen5.Application")
# or: gen5 = win32com.client.Dispatch("BioTek.Gen5.Application")  [UNVERIFIED]
```

The ProgID used to instantiate the COM object may vary by Gen5 version. Check the
Windows Registry under `HKEY_CLASSES_ROOT` for the exact ProgID.

## Key COM Objects [UNVERIFIED]

The following object hierarchy is based on typical instrument COM interfaces. Exact
property and method names need verification against the Gen5 type library.

### Application Object

| Property/Method | Type | Description |
|----------------|------|-------------|
| `Visible` | bool | Show/hide Gen5 UI |
| `Quit()` | method | Close Gen5 application |
| `Plates` | collection | Connected plate readers |
| `Protocols` | collection | Available protocols |

### Plate Object

| Property/Method | Type | Description |
|----------------|------|-------------|
| `Name` | str | Reader name/serial |
| `IsConnected` | bool | Connection status |
| `ReadPlate(protocol)` | method | Execute a protocol read |
| `EjectPlate()` | method | Eject the plate carrier |
| `LoadPlate()` | method | Retract the plate carrier |
| `Temperature` | float | Current temperature (C) |
| `SetTemperature(target)` | method | Set incubation temperature |

### Protocol Object

| Property/Method | Type | Description |
|----------------|------|-------------|
| `Name` | str | Protocol name |
| `FileName` | str | Path to .prt file |
| `Open(path)` | method | Load a protocol file |
| `ReadType` | str | "Endpoint", "Kinetic", "Spectral" |

### Results Object

| Property/Method | Type | Description |
|----------------|------|-------------|
| `GetWellData(row, col)` | float | Get reading for a specific well |
| `Export(path, format)` | method | Export data to file |
| `WellCount` | int | Number of wells read |

## Typical Automation Workflow

```python
import win32com.client

# 1. Connect to Gen5
gen5 = win32com.client.Dispatch("Gen5.Application")
gen5.Visible = True

# 2. Open a protocol
protocol = gen5.Protocols.Open("C:\\Protocols\\ELISA_450nm.prt")

# 3. Read plate
results = gen5.Plates(1).ReadPlate(protocol)

# 4. Extract data
for row in range(8):      # A=0 through H=7
    for col in range(12):  # 1-12
        value = results.GetWellData(row, col)
        print(f"{chr(65+row)}{col+1}: {value:.4f}")

# 5. Export
results.Export("C:\\Data\\output.csv", "CSV")
```

**Note:** The above code is illustrative. Exact method signatures, parameter types, and
return values must be verified against the Gen5 COM type library on a system with Gen5
installed.

## REST API [UNVERIFIED]

Newer versions of Gen5 (3.12+) may expose a REST API for instrument control. Details:

- **Endpoint:** `http://localhost:5000/api/v1/` [UNVERIFIED]
- **Authentication:** Local API key [UNVERIFIED]
- **Capabilities:** Protocol execution, data retrieval, reader status [UNVERIFIED]

This REST API has not been confirmed in Gen5 documentation and may be a third-party
extension or future feature.

## Error Handling

Common COM errors when automating Gen5:

| Error | Cause | Resolution |
|-------|-------|------------|
| `COMException: Server not found` | Gen5 not running | Launch Gen5 before calling Dispatch |
| `COMException: Access denied` | Permissions issue | Run script as same user that owns Gen5 |
| `Timeout during ReadPlate` | Read taking too long | Check reader connection, plate loaded |
| `Protocol not found` | Invalid .prt path | Verify protocol file exists and is valid |
