# Ultima Investigator — Operator's Manual Summary

> Source: Bruker Ultima Investigator Operator's Manual (System #5010).
> This is a structured summary for AI agent consumption, not a replacement for the full manual.

## System Overview

The Bruker Ultima Investigator is a multiphoton laser scanning microscope designed for
in vivo and in vitro fluorescence imaging of biological specimens. It is classified as a
**Class 1 laser product** with **Class 4 laser radiation enclosed** within the light box
and beam delivery path.

The system uses a mode-locked Ti:Sapphire ultrafast laser (Coherent Chameleon series)
to generate femtosecond pulses in the near-infrared range (680-1080 nm). Two-photon
excitation occurs only at the focal point of the objective, providing intrinsic optical
sectioning without a confocal pinhole.

## Major Components

### Light Box (Imaging Enclosure)

The light box is the central enclosure containing all beam-steering optics, scan mirrors,
and the objective turret. Key internal components:

- **Resonant galvanometer** (8 kHz) — X-axis fast scan mirror for high-speed imaging
- **Galvanometer mirror** — Y-axis (and optional X-axis for galvo-galvo mode)
- **Scan lens and tube lens** — relay optics forming the scan pattern
- **Primary dichroic mirror** — separates excitation (reflected) from emission (transmitted)
- **Objective turret** — holds water-dipping objectives; motorized Z via piezo
- **Collection optics** — lenses and filters directing emission to detectors

The light box has **interlocked access panels** on the door, sides, and back. Opening any
panel triggers the hard shutter to block the laser beam.

### Detector Assembly

Detectors are mounted below the objective (epi-detection geometry) for maximum collection
efficiency in scattering tissue:

- **GaAsP PMTs** (Hamamatsu H7422PA-40 SEL) — high quantum efficiency (40% at 500 nm),
  thermoelectrically cooled, 300-720 nm spectral range
- Up to 4 detection channels with interchangeable dichroic/filter cubes
- **Current-limiting protection circuit** — auto-shutoff at 50 uA to prevent PMT damage
- Maximum operating voltage: 900 V (control voltage, not actual dynode voltage)

### Stage and Z-Drive

- **XY Stage** — motorized, 6" x 3" travel, 0.3 um resolution, 1 um accuracy
- **Piezo Z-drive** — 150 um range, 0.05 um minimum step, up to 5 Hz stack rate
  (Bruker Piezo Amplifier/Driver unit)
- **Coarse Z** — manual or motorized focus for initial approach

### Laser Delivery

- Beam enters through a sealed port on the light box rear panel
- **Beam covers** enclose the Class 4 beam path from laser aperture to light box entry
- **Pockels cell** (electro-optic modulator) — controls laser power delivered to sample
  with microsecond response time; enables blanking during flyback

### Vibration Isolation

- **Newport Integrity 4 VCS** active vibration isolation table
- Pneumatic legs with active feedback for sub-micron stability
- Essential for in vivo imaging where mechanical noise degrades image quality

## Startup Procedure

Perform steps in this exact order. Do not skip or reorder.

1. **Turn on cooling water circulator.** Verify flow and temperature stable at 25 C.
   The laser crystal requires continuous cooling during operation.

2. **Power on the Resonant Galvo Control Box.** The resonant scanner needs time to reach
   stable oscillation frequency (8 kHz). Allow 5 minutes for stabilization.

3. **Turn laser key to ON position.** The Chameleon laser begins its internal startup
   sequence (pump diode warmup, cavity alignment, mode-lock acquisition).

4. **Wait for mode-lock.** The laser status indicator on the Chameleon controller should
   show "Mode-Locked" (solid green). This typically takes 2-5 minutes after key-on.
   If mode-lock is not achieved within 10 minutes, check alignment.

5. **Pockels cell warmup.** Wait 20-30 minutes after laser key-on for the Pockels cell
   to thermally stabilize. Imaging before warmup produces inconsistent power across
   the field of view.

6. **Launch PrairieView software.** The software initializes communication with all
   hardware controllers (galvo driver, piezo, stage, PMT power supplies, laser).
   Verify all subsystems show "Connected" in the hardware status panel.

7. **Set PMT voltages.** Start with gain at 0 for all channels. Increase to desired
   operating voltage (typically 500-750 V for GaAsP) only after verifying the light
   box is fully closed and the sample is in position.

8. **Set laser wavelength.** Use PrairieView or PrairieLink to tune to the desired
   wavelength. Allow 5-10 seconds for the laser to re-optimize at the new wavelength.

9. **Begin imaging.** Start with low Pockels cell transmission (5-10%) and increase
   gradually while monitoring the image. Never jump directly to high power.

## Shutdown Procedure

1. **Close the laser shutter** (Pockels cell to zero or shutter closed).
2. **Set all PMT gains to 0.** This protects the detectors before any enclosure is opened.
3. **Stop all active acquisitions** in PrairieView.
4. **Turn laser key to STANDBY.** The laser will begin its cooldown sequence.
5. **Close PrairieView** software.
6. **Keep cooling water running** for at least 15 minutes after laser key-off to allow
   the crystal to cool safely.
7. **Power off ancillary equipment** (resonant galvo control box, stage controller)
   after cooldown is complete.

## Maintenance

### Alignment Verification

Alignment should be checked periodically (monthly or after any vibration event):

1. Open Maintenance tab (Tools > Maintenance) — **senior operator approval required**
2. Use alignment tools with a fluorescent target (e.g., thin fluorescent slide)
3. Verify beam centering at the back aperture of the objective
4. Check scan field flatness with a uniform fluorescent sample
5. Verify Z-stack uniformity (brightness should not vary with Z at constant laser power)

### Objective Care

- **Water-dipping objectives** must be cleaned after every session
- Use lens paper with appropriate solvent (ethanol or lens cleaning solution)
- Never allow water to dry on the objective front element — salt residue scratches coatings
- Store with lens cap when not in use
- Check immersion water level every 30-60 minutes during long imaging sessions

### PMT Maintenance

- GaAsP PMTs degrade over time with cumulative photon exposure
- Monitor dark current periodically (should be <1 nA at operating voltage)
- If dark current increases significantly, the PMT may need replacement
- Expected lifetime: 2000-5000 hours of operation depending on usage conditions
