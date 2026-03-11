# dosy3d

**Category:** Commands > Analyze > Dosy

## NAME

**dosy3d** - Process DOSY dataset (3D)


## DESCRIPTION

The command dosy3d processes a 3D DOSY dataset.
DOSY is a special representation of diffusion measurements. Instead of generating just numbers using the T1/T2 fitting package (i.e. diffusion coefficients and error values), the DOSY processing gives pseudo 3D data where the F2 or F1 axis displays diffusion constants rather than NMR frequencies.
For more information on dosy3d :
Click Help | Manuals | Acquisition Application Manuals | Dosy


## INPUT FILES

<dir>/data/<user>/nmr/<name>/<expno>/
difflist - list of gradient amplitudes in Gauss/cm
<dir>/data/<user>/nmr/<name>/<expno>/pdata/<procno>/
3rrr - 3D data which are processed in F3 and F2 or in F3 and F1
dosy - DOSY processing parameters


## OUTPUT FILES

<dir>/data/<user>/nmr/<name>/<expno>/pdata/<procno>/
3rrr - 3D processed data
auditp.txt - processing audit trail


## SEE ALSO

eddosy, dosy2d
© 2025 Bruker BioSpin GmbH & Co. KG
