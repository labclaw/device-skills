# absnd

**Category:** Commands > Process > Baseline

## NAME

**absnd** - nD automatic baseline correction (≥3D)


## DESCRIPTION

The command absnd performs an automatic baseline correction of data of dimension ≥3D. It takes one argument, the direction to be corrected. If no argument is specified on the command line, it is requested:
 
absnd subtracts a polynomial, the degree of which is determined by the parameter ABSG, which has a value between 0 and 5, with a default of 5. It only corrects a certain spectral region which is determined by the parameters ABSF1 and ABSF2.
absnd actually processes 2D planes of an nD data set, performing a series of abs2 or abs1 commands. On 3D data, the commands absnd 3, absnd 2 and absnd 1 are equivalent to tabs3, tabs2 and tabs1, respectively.


## INPUT PARAMETERS

### Acquisition direction:

Set by the user with edp or by typing absg.:
ABSG - degree of the polynomial to be subtracted (0 to 5, default of 5)
### All directions:

Set by the user with edp or by typing absf1, absf2:
ABSF1- low field limit of the correction region
ABSF2 - high field limit of the correction region


## INPUT FILES

### For 4D data:

<dir>/data/<user>/nmr/<name>/<expno>/pdata/<procno>/
4rrrr - processed 4D data
proc - F4 processing parameters
proc2 - F3 processing parameters
proc3 - F2 processing parameters
proc4 - F1 processing parameters
For 3D data, the input data file is 3rrr whereas the proc4 does not exist. For data of dimension n where n ≥ 5, input data files are named nr and ni, e.g. 5r, 5i, 6r, 6i etc.


## OUTPUT FILES

### For 4D data:

<dir>/data/<user>/nmr/<name>/<expno>/pdata/<procno>/
4rrrr - processed 4D data
procs - F4 processing status parameters
proc2s - F3 processing status parameters
proc3s - F2 processing status parameters
proc4s - F1 processing status parameters
For 3D data, the output data file is 3rrr whereas proc4s does not exist. For data of dimension n where n ≥ 5, output data files are named nr and ni, e.g. 5r, 5i, 6r, 6i etc.


## SEE ALSO

abs2, abst2, absd2, absot2, tabs3, tabs2, tabs1
© 2025 Bruker BioSpin GmbH & Co. KG
