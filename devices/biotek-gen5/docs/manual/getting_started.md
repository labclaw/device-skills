# Getting Started — BioTek Synergy H1 with Gen5

**Source:** BioTek/Agilent official documentation; items marked [UNVERIFIED] need confirmation.

## Prerequisites

- **Software:** Gen5 3.x installed and licensed (Windows only)
- **Connection:** USB or Ethernet cable between PC and Synergy H1
- **Microplates:** Standard SBS-format plates (6 to 384 well)

## First-Time Setup

1. **Install Gen5 software** from the Agilent/BioTek installation media or download portal.
2. **Connect the reader** via USB (default) or Ethernet (requires network configuration).
3. **Launch Gen5** — the software auto-detects connected readers on startup.
4. **Verify connection:** The status bar at the bottom of Gen5 shows "Connected" with the
   reader serial number when communication is established.

## Warm-Up

- **Absorbance reads:** No warm-up required; the xenon flash lamp fires per-read.
- **Fluorescence reads:** Allow 15-30 minutes warm-up for the tungsten-halogen lamp to
  stabilize. Cold reads produce higher coefficient of variation (CV%).
- **Luminescence reads:** No warm-up needed; the PMT detector does not require thermal
  equilibration. [UNVERIFIED]

## Running a Basic Read

### Using a Predefined Protocol

1. **File > Open Protocol** or click "Protocols" in the task manager.
2. Select an existing `.prt` file (e.g., "Absorbance Endpoint 450nm").
3. Click **Read Plate** in the toolbar.
4. When prompted, ensure the plate is loaded (carrier extends automatically).
5. Wait for "Reading Complete" dialog.

### Creating a New Protocol

1. **File > New Protocol** (or Task Manager > Create New).
2. Select detection method: Absorbance, Fluorescence, or Luminescence.
3. Configure read parameters:
   - **Absorbance:** Wavelength(s), read type (endpoint/kinetic/spectral scan).
   - **Fluorescence:** Excitation and emission wavelengths, optics position (top/bottom),
     sensitivity/gain setting.
   - **Luminescence:** Integration time, gain.
4. Set plate type (96-well, 384-well, etc.).
5. Optionally add pre-read steps: temperature incubation, shaking, delay.
6. Save protocol as `.prt` file.

## Exporting Data

1. After a read completes, the data appears in the Gen5 results view.
2. **File > Export** — choose CSV, Excel, or PDF format.
3. CSV export includes metadata header rows followed by the well grid (rows A-H, columns
   1-12 for a 96-well plate).
4. Exported files use UTF-8 with BOM encoding (`utf-8-sig`).

## Plate Handling

- The Synergy H1 has a motorized plate carrier that extends when a read is initiated.
- **Keep hands clear** when the carrier is moving.
- Load the plate with **well A1 in the back-left corner** (standard SBS orientation).
- The reader accepts plates from 6-well to 384-well format. Plate type must match the
  protocol configuration.

## Troubleshooting

| Symptom | Likely Cause | Resolution |
|---------|-------------|------------|
| Gen5 shows "No Reader Found" | USB cable disconnected or driver issue | Reconnect USB, reinstall driver |
| High CV% on fluorescence reads | Insufficient warm-up | Wait 15-30 min after power-on |
| Edge wells read high/low | Evaporation artifacts | Use plate sealers for long incubations |
| Blank wells not near zero | Plate fingerprints or condensation | Clean plate bottom, equilibrate temperature |
