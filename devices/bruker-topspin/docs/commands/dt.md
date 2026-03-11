# dt

**Category:** Commands > Process > Advanced > Miscellaneous Operations

## NAME

**dt** - Calculate the first derivative of the data (1D)


## DESCRIPTION

The command dt calculates the first derivative of the current dataset. Depending on the value of DATMOD, dt works on the raw or on the processed data.


## INPUT PARAMETERS

Set by the user with edp or by typing datmod.
DATMOD - data mode: work on raw or processed data


## INPUT FILES

<dir>/data/<user>/nmr/<name>/<expno>/
fid - raw data (input if DATMOD = raw)
<dir>/data/<user>/nmr/<name>/<expno>/pdata/<procno>/
1r, 1i - processed 1D data (input if DATMOD = proc)
proc - processing parameters


## OUTPUT FILES

<dir>/data/<user>/nmr/<name>/<expno>/pdata/<procno>/
1r, 1i - processed 1D data (real, imaginary)
procs - processing status parameters
auditp.txt - processing audit trail


## USAGE IN AU PROGRAMS

DT
© 2025 Bruker BioSpin GmbH & Co. KG
