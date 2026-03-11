# tabs3, tabs2, tabs1

**Category:** Commands > Process > Baseline

## NAME

**tabs3** - Automatic baseline correction in F3 (3D)

**tabs2** - Automatic baseline correction in F2 (3D)

**tabs1** - Automatic baseline correction in F1 (3D)


## DESCRIPTION

tabs3 performs an automatic baseline correction in the F3 direction, by subtracting a polynomial. The degree of the polynomial is determined by the F3 parameter ABSG which has a value between 0 and 5, with a default of 5. tabs3 works like absf in 1D and abs2 in 2D. This means that it only corrects a certain spectral region which is determined by the parameters ABSF1 and ABSF2.
tabs2 works like tabs3, except that corrects data in the F2 direction using the F2 parameters ABSG, ABSF2 and ABSF1.
tabs1 works like tabs3, except that corrects data in the F1 direction using the F1 parameters ABSG, ABSF2 and ABSF1.


## INPUT PARAMETERS

### F3 parameters

Set by the user with edp or by typing absg:
ABSG - degree of the polynomial to be subtracted (0 to 5, default of 5)
### F3, F2 and F1 parameters

Set by the user with edp or by typing absf1, absf2:
ABSF1- low field limit of the correction region
ABSF2 - high field limit of the correction region


## INPUT FILES

<dir>/data/<user>/nmr/<name>/<expno>/pdata/<procno>/
3rrr - real processed 3D data
proc - F3 processing parameters
proc2 - F2 processing parameters
proc3 - F1 processing parameters


## OUTPUT FILES

<dir>/data/<user>/nmr/<name>/<expno>/pdata/<procno>/
3rrr - real processed 3D data 
procs - F3 processing status parameters
proc2s - F2 processing status parameters
proc3s - F1 processing status parameters
auditp.txt - processing audit trail


## USAGE IN AU PROGRAMS

TABS3
TABS2
TABS1


## SEE ALSO

abs, absf, absd, absn, bas, abs2, abst2, absd2, absot2
© 2025 Bruker BioSpin GmbH & Co. KG
