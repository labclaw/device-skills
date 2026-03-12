# PrairieLink COM / TCP Interface

> Source: Bruker PrairieLink API documentation, PrairieView Help system.
> PrairieLink provides programmatic control of PrairieView via COM (local) or TCP (remote).

## Overview

PrairieLink is Bruker's automation interface for PrairieView. It exposes two connection
mechanisms:

1. **COM/ActiveX** — In-process or local out-of-process automation. Windows only.
   Fastest option for scripts running on the PrairieView workstation.
2. **TCP** — Network socket on port 1236. Allows remote control from any machine on the
   network. Same command set as COM, with string-based request/response protocol.

Both interfaces require the PrairieLink password for authentication.

## COM ProgIDs

| ProgID | Architecture | Use When |
|--------|-------------|----------|
| `PrairieLink.Application` | 32-bit | 32-bit Python, MATLAB 32-bit, older scripts |
| `PrairieLink64.Application` | 64-bit | 64-bit Python (recommended), MATLAB 64-bit |

The 64-bit ProgID is recommended for modern setups. The 32-bit ProgID requires a
32-bit COM client process.

## Password

PrairieLink requires a password for both COM and TCP connections:

- **Location in PrairieView:** Tools > Scripts > Edit Scripts
- The password is displayed in the bottom-left corner of the script editor window
- **Default password:** `0000`
- The password can be changed in PrairieView settings but most installations keep the default

## Python (win32com)

### Installation

```bash
pip install pywin32
```

### Connection

```python
import win32com.client

# Create COM object (64-bit)
pl = win32com.client.Dispatch("PrairieLink64.Application")

# Connect (IP, password)
pl.Connect("127.0.0.1", "0000")

# Verify connection
if pl.Connected():
    print("Connected to PrairieView")
else:
    print("Connection failed")
```

### Acquisition Example

```python
# Set save location
pl.SendScriptCommands("-SetSavePath C:\\Data\\2024-01-15")
pl.SendScriptCommands("-SetFileName Tseries calcium_session1")

# Configure
pl.SendScriptCommands("-SetMultiphotonWavelength '920' 1")
pl.SendScriptCommands("-SetAcquisitionMode ResonantGalvo")

# Acquire
pl.SendScriptCommands("-TSeries")
```

### Reading State

```python
# Frame rate
fps = float(pl.GetState("framerate"))

# Microns per pixel
um_px = float(pl.GetState("micronsPerPixel", "XAxis"))

# Motor positions
z_pos = pl.GetMotorPosition("Z")

# Image dimensions
px_per_line = pl.PixelsPerLine()
lines = pl.LinesPerFrame()
```

### Live Image Retrieval

```python
import numpy as np

# Get current frame from channel 1
# Arguments: channel (int), width (int), height (int)
width = pl.PixelsPerLine()
height = pl.LinesPerFrame()

# Returns a flat array of pixel values
img_data = pl.GetImage_2(1, width, height)

# Reshape to 2D
image = np.array(img_data).reshape(height, width)
```

### Disconnect

```python
pl.Disconnect()
```

## MATLAB

### Connection

```matlab
% Create COM object
pl = actxserver('PrairieLink64.Application');

% Connect
pl.Connect('127.0.0.1', '0000');

% Verify
if pl.Connected()
    disp('Connected');
end
```

### Commands

```matlab
% Send acquisition command
pl.SendScriptCommands('-TSeries');

% Read state
fps = str2double(pl.GetState('framerate'));

% Get motor position
z = pl.GetMotorPosition('Z');

% Get image
img = pl.GetImage_2(1, 512, 512);
img = reshape(img, [512, 512]);
```

### Disconnect

```matlab
pl.Disconnect();
delete(pl);
```

## C++ / C#

### C++ (COM)

```cpp
#include <comdef.h>

// Initialize COM
CoInitialize(NULL);

// Create PrairieLink object
CLSID clsid;
CLSIDFromProgID(L"PrairieLink64.Application", &clsid);

IDispatch* pPL;
CoCreateInstance(clsid, NULL, CLSCTX_LOCAL_SERVER, IID_IDispatch, (void**)&pPL);

// Use IDispatch::Invoke for method calls
// (or import the type library for early binding)
```

### C# (.NET)

```csharp
dynamic pl = Activator.CreateInstance(
    Type.GetTypeFromProgID("PrairieLink64.Application"));
pl.Connect("127.0.0.1", "0000");
pl.SendScriptCommands("-SingleImage");
pl.Disconnect();
```

## TCP Interface

### Protocol

- **Port:** 1236 (configurable in PrairieView)
- **Transport:** TCP
- **Authentication:** First message after connection must be the password
- **Encoding:** UTF-8 strings
- **Terminator:** Newline (`\n`)

### Python TCP Example

```python
import socket

def prairielink_tcp(host="127.0.0.1", port=1236, password="0000"):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((host, port))

    # Authenticate
    sock.sendall(f"{password}\n".encode())
    response = sock.recv(1024).decode().strip()

    if "Connected" not in response:
        raise ConnectionError(f"Auth failed: {response}")

    return sock

def send_command(sock, cmd):
    sock.sendall(f"{cmd}\n".encode())
    return sock.recv(4096).decode().strip()

# Usage
sock = prairielink_tcp()
send_command(sock, "-SetMultiphotonWavelength '920' 1")
send_command(sock, "-TSeries")
sock.close()
```

### Use Cases for TCP vs COM

| Feature | COM | TCP |
|---------|-----|-----|
| Same machine | Yes (fastest) | Yes |
| Remote machine | No | Yes |
| Requires pywin32 | Yes | No |
| Cross-platform client | No (Windows only) | Yes |
| Image retrieval (GetImage_2) | Yes | No `[UNVERIFIED]` |
| Latency | ~1 ms | ~5-10 ms |

## COM Object Method Reference

| Method | Arguments | Returns | Description |
|--------|-----------|---------|-------------|
| `Connect(ip, password)` | string, string | void | Connect to PrairieView |
| `Disconnect()` | — | void | Disconnect |
| `Connected()` | — | bool | Check connection status |
| `SendScriptCommands(cmd)` | string | void | Send a `-Command` string |
| `GetState(key)` | string | string | Query a state value |
| `GetState(key, subkey)` | string, string | string | Query a state value with subkey |
| `GetMotorPosition(axis)` | string | float | Get motor position ("X", "Y", "Z") |
| `PixelsPerLine()` | — | int | Current pixels per scan line |
| `LinesPerFrame()` | — | int | Current lines per frame |
| `GetImage_2(ch, w, h)` | int, int, int | array | Get current frame pixel data |

## Troubleshooting

### "Class not registered" Error
- PrairieView is not installed, or the COM server is not registered
- Run PrairieView at least once after installation to register COM objects
- Try the 32-bit ProgID if 64-bit fails (or vice versa)

### Connection Refused (TCP)
- PrairieView must be running with PrairieLink enabled
- Check that port 1236 is not blocked by Windows Firewall
- Verify the password matches PrairieView's script editor setting

### GetImage_2 Returns Empty
- Ensure a scan is active (live scan or acquisition in progress)
- Verify channel number is correct (1-based, and that channel is enabled)
- Check that width and height match current PixelsPerLine and LinesPerFrame
