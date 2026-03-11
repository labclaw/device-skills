# teget, te1get, te2get, te3get, te4get

**Category:** Commands > Acquire > Sample

## NAME

**teget** - Read the temperature from the temperature unit

**te1get** - Equivalent to teget

**te2get** - Read the second temperature from the temperature unit

**te3get** - Read third temperature from the temperature unit

**te4get** - Read fourth temperature from the temperature unit


## DESCRIPTION

The command teget queries the temperature from the temperature unit and stores it in the acquisition status parameter TE.
The command te2get queries the second temperature from a temperature unit with two regulators and stores it in the acquisition status parameter TE2. Temperature units with two regulators are, for example, used in BEST NMR where the first regulator controls the sample temperature, and the second regulator controls the inlet capillary temperature.
### OUTPUT PARAMETERS

1. TE - temperature set on the temperature unit.
2. TE1 - temperature set on the temperature unit.
3. TE2 - temperature set on the second temperature unit.
4. TE3 - temperature set on the third temperature unit.
5. TE4 - temperature set on the fourth temperature unit.


## OUTPUT FILES

1. <dir>/data/<user>/nmr/<name>/<expno>/
1. acqus - acquisition status parameters


## USAGE IN AU PROGRAMS

1. TEGET
2. TE1GET
3. TE2GET
4. TE3GET
5. TE4GET


## SEE ALSO

edte, teset, te2set
© 2025 Bruker BioSpin GmbH & Co. KG
