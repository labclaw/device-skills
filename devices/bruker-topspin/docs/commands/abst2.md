# abs2, abst2, absd2, absot2

**Category:** Commands > Process > Baseline

## NAME

**abs2** - Automatic baseline correction in F2 (2D)

**abst2** - Automatic selective baseline correction in F2 (2D)

**absd2** - Automatic baseline correction in F2, diff. algorithm (2D)

**absot2** - Automatic selective baseline correction in F2, diff. algorithm (2D)

**bas** - Open baseline correction dialog box (1D, 2D)


## DESCRIPTION

Baseline correction commands can be started from the command line, by entering abs2, abst2 etc. or from the baseline dialog box. The latter is opened with the command bas:
 
This dialog box offers several options, each of which selects a certain command for execution. The command further depends on the selected direction. Here we describe the commands for the F2 direction.
### F2 Auto-correct baseline using polynomial

This option selects the command abs2 for execution. It performs an automatic baseline correction in the F2 direction. This means it subtracts a polynomial from the rows of the processed 2D data. The degree of the polynomial is determined by the parameter ABSG which has a value between 0 and 5, with a default of 5. It works like absf in 1D which means it only corrects the spectral region between ABSF1 and ABSF2.
### F2 Auto-correct baseline, shift correction region

This option selects the command abst2 for execution. It performs an automatic selective baseline correction in the F2 direction. This means it corrects the rows of the processed 2D data. It works like abs2, except for the following: 
1. only the rows between F1-ABSF2 and F1-ABSF1 are corrected 
2. the part (region) of each row which is corrected shifts from row to row. The first row is corrected between F2-ABSF2 and F2-ABSF1. The last row is corrected between F2-SIGF2 and F2-SIGF1. For intermediate rows, the low field limit is an interpolation of F2-ABSF2 and F2-SIGF2 and the high field limit is an interpolation of F2-ABSF1 and F2-SIGF1. 
### F2 Auto-correct baseline, alternate algorithm

This option selects the command absd2 for execution. It works like abs2, except that it uses a different algorithm (it uses the same algorithm as the command abs in DISNMR). It is, for example, used when a small peak lies on the foot of a large peak. In that case, absd2 allows to correct the baseline around the small peak which can then be integrated. Usually absd2 is followed by abs2.
### F2 Auto-correct baseline, shift correction region, alternate algorithm

This option selects the command absot2 for execution. It works like abst2, except that it has a different algorithm which applies a larger correction. 
If you run a command like abs2 from the command line, you have to make sure that the required parameters are already set. Click the Procpars tab or enter edp to do that.
The bas command can be used on 1D, 2D or 3D data. It recognizes the data dimensionality and opens a dialog box with the appropriate options and parameters.


## INPUT PARAMETERS

Set from the bas dialog box, with edp or by typing absg, absf1 etc.: 
ABSG - degree of the polynomial to be subtracted (0 to 5, default is 5)
ABSF1 - low field limit of the region which is baseline corrected
ABSF2 - high field limit of the region which is baseline corrected
SIGF1 - low field limit of the correction region in the last row
SIGF2 - high field limit of the correction region in the last row


## INPUT FILES

<dir>/data/<user>/nmr/<name>/<expno>/pdata/<procno>/
2rr - real processed 2D data
proc - F2 processing parameters


## OUTPUT FILES

<dir>/data/<user>/nmr/<name>/<expno>/pdata/<procno>/
2rr - real processed 2D data
procs - F2 processing status parameters
auditp.txt - processing audit trail


## USAGE IN AU PROGRAMS

ABS2
ABST2
ABSD2
ABSOT2
© 2025 Bruker BioSpin GmbH & Co. KG
