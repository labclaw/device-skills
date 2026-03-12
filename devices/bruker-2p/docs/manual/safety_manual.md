# Ultima Investigator — Safety Manual

> Source: Bruker Ultima Investigator Safety Documentation and Laser Safety Manual.
> Compliance: ANSI Z136.1 (Safe Use of Lasers), IEC 60825-1 (Laser Safety).

## Laser Classification

### System Classification

The Bruker Ultima Investigator is a **Class 1 laser product** when all enclosures and
beam covers are properly installed and interlocks are functional. This means the system
is safe under all conditions of normal use.

### Internal Laser Classification

The enclosed laser radiation is **Class 4** — the highest hazard class:

- **Ti:Sapphire laser:** >2.5 W average power, >200 kW peak power
- **Wavelength range:** 680-1080 nm (near-infrared, INVISIBLE to the eye)
- **Pulse duration:** ~140 fs at ~80 MHz repetition rate
- **Hazards:** Immediate and permanent eye damage (retinal burn), skin burns,
  fire ignition potential

The beam is invisible. You cannot see it. You cannot feel low-level exposure until
damage has already occurred. The IR wavelength penetrates the cornea and is focused
by the eye's lens directly onto the retina.

## Interlock Systems

### Light Box Door Interlock

- **Trigger:** Opening the light box front door
- **Action:** Hard shutter closes, blocking all laser light from entering the light box
- **Recovery:** Close door fully; shutter re-enables automatically (verify in PrairieView)
- **NEVER defeat this interlock**

### Side and Back Panel Interlocks

- **Trigger:** Removing any side or back panel from the light box enclosure
- **Action:** Hard shutter closes
- **Purpose:** Prevents exposure during maintenance or objective changes
- **Recovery:** Reinstall panel securely; verify shutter status in software

### Primary Dichroic Interlock

- **Trigger:** Removal or misalignment of the primary dichroic mirror
- **Action:** Transmitted light path shutoff
- **Purpose:** Prevents uncontrolled laser light from reaching the sample or operator
  through the transmitted light path

### Beam Cover Interlocks

- Beam covers enclose the Class 4 beam from the laser aperture to the light box entry port
- Removing beam covers exposes Class 4 radiation
- Beam covers should only be removed by trained service personnel with laser safety eyewear

## PMT Protection

### GaAsP PMT Sensitivity

The Hamamatsu H7422PA-40 SEL GaAsP PMTs are extremely sensitive photon detectors:

- **Maximum control voltage:** 900 V (actual dynode voltage is higher internally)
- **Overcurrent protection:** Auto-shutoff at 50 uA anode current
- **Spectral range:** 300-720 nm
- **CRITICAL:** GaAsP photocathodes are permanently damaged by exposure to bright
  light at operating voltage. Damage is cumulative and irreversible.

### PMT Safety Rules

1. **ALWAYS set PMT gain to 0 before opening any enclosure panel or door**
2. **NEVER turn on room lights while PMTs are at operating voltage**
3. **NEVER remove a filter cube while PMTs are powered** — this can expose them
   to excitation laser light
4. The auto-protection circuit (50 uA limit) is a last resort, not a primary safety measure
5. If the auto-protection trips, immediately set gain to 0 and investigate the cause
6. Monitor PMT dark current periodically — increasing dark current indicates degradation

### Light Box Ambient Light

Even with the door interlock, verify:
- Room lights are dimmed or off during high-gain imaging
- Computer monitors near the microscope are dimmed
- No light leaks around cable feed-throughs
- Sample illumination (transmitted light) is off during fluorescence imaging

## Beam Path Safety

### Enclosed Beam Sections

The Class 4 beam travels through:
1. Laser output aperture
2. Beam conditioning optics (Pockels cell, beam expander)
3. Periscope / beam delivery tube
4. Light box entry port
5. Scan mirrors, scan lens, tube lens
6. Objective

All sections from laser to light box entry must be enclosed by beam covers.

### Objective Safety

- The objective focuses the beam to a diffraction-limited spot — peak irradiance is
  extreme at the focal point
- **NEVER look into the objective while the laser is enabled,** even at minimum power
- **NEVER place reflective objects at the focal plane** — specular reflections of
  Class 4 radiation can exit the light box through gaps
- When the objective is not immersed in sample/water, significant laser power can
  propagate upward if the shutter is open

## Maintenance Mode

- Access via Tools > Maintenance tab in PrairieView
- **Requires senior operator approval** — maintenance mode may disable certain interlocks
  for alignment procedures
- Only trained personnel with appropriate laser safety training (ANSI Z136 or equivalent)
  should perform maintenance
- Required PPE during maintenance: OD 5+ laser safety eyewear rated for 680-1080 nm

## Emergency Procedures

### Laser Emergency Stop

1. **Turn laser key to OFF** (not standby — OFF removes all power)
2. If key is not accessible, close the main laser shutter manually
3. If the situation involves potential exposure, do NOT look toward the beam path

### Suspected Eye Exposure

1. Stop all laser operation immediately
2. Do NOT rub eyes
3. Note the time, wavelength, estimated power, and duration of exposure
4. Seek immediate medical evaluation — ophthalmological exam within 24 hours
5. Report to institutional Laser Safety Officer (LSO)

### Electrical Emergency

- The laser power supply operates at high voltage (>1000 V internally)
- Do NOT open the laser housing
- In case of electrical fault: power off at the mains breaker
- Do NOT attempt to service the laser — contact Coherent/Bruker service

### Fire

- The Class 4 beam can ignite flammable materials
- Keep flammable materials away from the beam path
- In case of fire: power off laser, use CO2 or dry chemical extinguisher
  (NOT water near electrical equipment)

## Personal Protective Equipment

| Situation | Required PPE |
|-----------|-------------|
| Normal imaging (enclosure closed) | None (Class 1 system) |
| Maintenance / alignment | OD 5+ laser eyewear (680-1080 nm) |
| Objective changes | Set PMT gain to 0 first; no laser PPE needed if shutter closed |
| Laser housing service | Laser eyewear + high-voltage awareness training |

## Training Requirements

Before operating this system, users must complete:

1. Institutional laser safety training (ANSI Z136.1 or equivalent)
2. Bruker-specific system training (provided by Bruker or PI/lab manager)
3. Supervised operation (minimum 3 sessions with experienced operator)
4. Read this safety manual and the full operator's manual
5. Sign the lab laser safety acknowledgment form
