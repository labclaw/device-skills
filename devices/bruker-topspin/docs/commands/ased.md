# ased

**Category:** Commands > Miscellaneous > Graphical User Interface

## NAME

**ased** - Edit acquisition parameters used in pulse program


## DESCRIPTION

The command ased opens a dialog box with the acquisition parameters which are used for the current experiment (see the next figure).
 
This means that ased shows much less parameters then eda which shows all acquisition parameters. Entering ased on the command line is equivalent to clicking the AcquPars tab and then clicking the  button.
The following buttons are available:
 Undo the last modification (unused for status parameters).
 Switch to all acquisition parameters.
 Force parse of the pulse program.
 Set probe/solvent dependant parameters.
 Open the nuclei and routing table.
 Create a multi-receiver or a multi-dataset acquisition.
In front of the probe name the search function allows to go to a specific parameter.
ased compiles and interprets the pulse program defined by PULPROG. For pulses, delays and constants, the parameter description in the right column of the ased window is taken from the comment section at the end of the pulse program.
### INPUT AND OUTPUT PARAMETERS

1. For all experiments:
1. PULPROG - pulse program used for the acquisition.
2. TD - time domain; number of raw data points.
3. NS - number of scans.
4. DS - number of dummy scans.
5. SWH - spectral width in Hz.
6. AQ - acquisition time in seconds.
7. RG - receiver gain.
8. DW - dwell time.
9. DE - pre-scan delay.
2. For each frequency channel defined with edasp:
1. NUCx - nucleus for channel x.
2. SFOx - irradiation frequency for channel x.
3. All delays, pulse lengths, power levels etc. defined in the pulse program, e.g.:
1. D[1] - relaxation delay.
2. P[1] - 90° pulse length.
3. PL[1] - power level for pulse.
4. PCPD[1] - CPD pulse length.


## INPUT FILES

1. <tshome>/exp/stan/nmr/lists/pp/ (primary source) or <dir>/data/<user>/nmr/<name>/<expno>/lists/pp (fallback if not found in primary source)
1. The pulse program defined by PULPROG
2. <dir>/data/<user>/nmr/<name>/<expno>/
1. acqu - acquisition parameters


## OUTPUT FILES

1. <dir>/data/<user>/nmr/<name>/<expno>/
1. acqu - acquisition parameters


## SEE ALSO

eda, edcpul
© 2025 Bruker BioSpin GmbH & Co. KG
