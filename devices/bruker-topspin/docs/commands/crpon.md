# crpon, crpoff, crplock, crpobs

**Category:** Commands > Acquire > Sample

## NAME

**crpon** - Switch the cryo preamplifier on for the lock and observe channel

**crpoff** - Switch the cryo preamplifier off for the lock and observe channel

**crpobs** - Switch the cryo preamplifier on for the observe channel

**crplock** - Switch the cryo preamplifier on for the lock channel


## DESCRIPTION

The crp* commands listed above control the internal preamplifier of a cryoprobe. Cryo probes operate at a reduced coil and preamplifier temperature which improves the signal to noise with a factor of 4. They are available as Dual (13C observe), Triple resonance (TCI 1H, 13C, 15N) and also on Quadruple Resonance (QCI) probes.
The command crpon switches from the external (HPPR) preamplifier to the internal cryo preamplifier. This happens for both the observe and the lock channel.
The command crpoff switches from the internal cryo preamplifier to the external (HPPR) preamplifier. This happens for both the observe and the lock channel.
The command crplock switches from the external (HPPR) preamplifier to the internal cryo preamplifier. This happens for the lock channel only.
The command crpobs switches from the external (HPPR) preamplifier to the internal cryo preamplifier. This happens for the observe channel only.
### NOTE

Note that the internal cryo amplifier is also cooled down, like the coil and internal electronics of the Cryo Probe.


## SEE ALSO

edprobe 
© 2025 Bruker BioSpin GmbH & Co. KG
