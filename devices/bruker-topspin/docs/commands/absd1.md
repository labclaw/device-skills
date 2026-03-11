# abs1, abst1, absd1, absot1, bas

**Category:** Commands > Process > Baseline

## NAME

**abs1** - Automatic baseline correction in F1 (2D)

**abst1** - Automatic selective baseline correction in the F1 (2D)

**absd1** - Automatic baseline correction in F1, diff. algorithm (2D)

**absot1** - Automatic selective baseline correction in F1, diff. algorithm (2D)

**bas** - Open baseline correction dialog box (1D, 2D)


## DESCRIPTION

Baseline correction can be started from the command line, with abs1, abst1 etc., or from the baseline dialog box. The latter is opened with the command bas
 
This dialog box offers several options, each of which selects a certain command for execution. The command further depends on the selected direction. Here we describe the commands for the F1 direction.
### F1 Auto-correct baseline using polynomial

This option selects the command abs1 for execution. It performs an automatic baseline correction in the F1 direction. This means it subtracts a polynomial from the columns of the processed 2D data. The degree of the polynomial is determined by the parameter ABSG which has a value between 0 and 5, with a default of 5. It works like absf in 1D which means it only corrects the spectral region between ABSF1 and ABSF2.
### F1 Auto-correct baseline, shift correction region

This option selects the command abst1 for execution. It performs an automatic selective baseline correction in the F1 direction. This means it corrects the columns of the processed 2D data. It works like abs1, except for the following: 
1. only the columns between F2-ABSF2 and F2-ABSF1 are corrected 
2. the part (region) of each column which is corrected shifts from column to column. The first column is corrected between F1-ABSF2 and F1-ABSF1. The last column is corrected between F1-SIGF2 and F1-SIGF1. For intermediate columns, the low field limit is an interpolation of F1-ABSF2 and F1-SIGF2 and the high field limit is an interpolation of F1-ABSF1 and F1-SIGF1.
### F1 Auto-correct baseline, alternate algorithm

This option selects the command absd1 for execution. It works like abs1, except that it uses a different algorithm. It is, for example, used when a small peak lies on the foot of a large peak. In that case, absd1 allows to correct the baseline around the small peak which can then be integrated. Usually, absd1 is followed by abs1.
### F1 Auto-correct baseline, shift correction region, alternate algorithm

This option selects the command absot1 for execution. It works like abst1, except that it has a different algorithm which applies a larger correction. 
If you run a command like abs1 from the command line, you have to make sure that the required parameters are already set. Click the Procpars tab or enter edp to do that.
The bas command can be used on 1D or 2D data. It recognizes the data dimensionality and opens a dialog box with the appropriate options and parameters.


## INPUT PARAMETERS

Set from the bas dialog box, with edp or by typing absf1, absf2 etc.: 
ABSG - degree of the polynomial to be subtracted (0 to 5, default is 5)
ABSF1 - low field limit of the correction region in the first row
ABSF2 - high field limit of the correction region in the first row
SIGF1 - low field limit of the correction region in the last row
SIGF2 - high field limit of the correction region in the last row


## INPUT FILES

<dir>/data/<user>/nmr/<name>/<expno>/pdata/<procno>/
2rr - real processed 2D data
proc2 - F1 processing parameters


## OUTPUT FILES

<dir>/data/<user>/nmr/<name>/<expno>/pdata/<procno>/
2rr - real processed 2D data
proc2s - F1 processing status parameters
auditp.txt - processing audit trail


## USAGE IN AU PROGRAMS

ABS1
ABST1
ABSD1
ABSOT1


## SEE ALSO

abs2, abst2, absd2, absot2
© 2025 Bruker BioSpin GmbH & Co. KG
