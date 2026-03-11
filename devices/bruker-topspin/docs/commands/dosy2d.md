# dosy2d

**Category:** Commands > Analyze > Dosy

## NAME

**dosy2d** - Process DOSY dataset (2D)


## DESCRIPTION

The command dosy2d processes a 2D DOSY dataset. 
DOSY is a special representation of diffusion measurements. Instead of generating just numbers using the T1/T2 fitting package (i.e. diffusion coefficients and error values), the DOSY processing gives pseudo 2D data, where the F1 axis displays diffusion constants rather than NMR frequencies.
For more information on dosy :
Click Help | Manuals | Acquisition Application Manuals | Dosy


## INPUT FILES

<dir>/data/<user>/nmr/<name>/<expno>/
difflist - list of gradient amplitudes in Gauss/cm
<dir>/data/<user>/nmr/<name>/<expno>/pdata/<procno>/
2rr - 2D data processed in F2 only
dosy - DOSY processing parameters


## OUTPUT FILES

<dir>/data/<user>/nmr/<name>/<expno>/pdata/<procno>/
2rr - 2D processed data
auditp.txt - processing audit trail


## SEE ALSO

eddosy, dosy3d 
© 2025 Bruker BioSpin GmbH & Co. KG
