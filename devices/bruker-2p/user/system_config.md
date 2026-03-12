# System Configuration — Bruker Ultima Investigator #5010

## Hardware Components

| Component | Model | Details |
|-----------|-------|---------|
| Microscope | Bruker Ultima Investigator | Multiphoton laser scanning microscope |
| Laser (primary) | Coherent Chameleon Ultra II | Ti:Sapphire, 680-1080 nm, >2.5 W avg |
| Laser (secondary) | Coherent (with Axon module) | Dual-laser configuration for dual-wavelength |
| Scanner (resonant) | 8 kHz resonant galvanometer | 30 fps at 512x512 (bidirectional) |
| Scanner (galvo) | Conventional galvanometer | Variable speed, unidirectional |
| Objective | Nikon CFI75 LWD 16X/0.8 W | Water-dipping, 3.0 mm WD |
| Detectors | Hamamatsu H7422PA-40 SEL | Quad GaAsP PMT, 300-720 nm, max 900 V |
| Piezo Z | Bruker Piezo Amplifier/Driver | 150 um range, 0.05 um step |
| XY Stage | Motorized | 6" x 3" travel, 0.3 um resolution |
| Vibration isolation | Newport Integrity 4 VCS | Active cancellation |
| Pockels cell | KDP EOM | Power modulation, <1 us response |

## Software

- **Control software:** PrairieView
- **Version:** 5.6+
- **OS:** Windows 10/11
- **PrairieLink:** COM (PrairieLink64.Application) + TCP (port 1236)

## Network / Connectivity

- **PrairieLink TCP port:** 1236
- **PrairieLink password:** See Tools > Scripts > Edit Scripts (default: 0000)
- **Remote access:** RDP or VNC to Windows workstation

## Environment Requirements

- **Room temperature:** 20-25 C (stable within +/- 1 C)
- **Humidity:** 30-60% RH, non-condensing
- **Cooling water:** 25 C circulator, must be running before laser key-on
- **Vibration isolation:** Active table, avoid foot traffic during imaging
- **Lighting:** Room dark during imaging (PMT sensitivity)

## Detection Channel Configuration

| Channel | Typical Filter | Wavelength | Common Use |
|---------|---------------|------------|------------|
| Ch1 (Green) | 500-550 nm BP | Green | GCaMP, GFP, Alexa 488 |
| Ch2 (Red) | 570-620 nm BP | Red | tdTomato, Texas Red, SR101 |
| Ch3 | Configurable | Variable | Second red or far-red |
| Ch4 | Configurable | Variable | Additional channel |

Note: Filter cubes are interchangeable. Verify current configuration before imaging.
