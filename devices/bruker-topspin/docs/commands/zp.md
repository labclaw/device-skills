# zp

**Category:** Commands > Process > Advanced > Miscellaneous Operations

## NAME

**zp** - Zero the first NZP data points (1D)


## DESCRIPTION

The command zp sets the intensity of the first NZP points of the dataset to zero. It works on raw or processed data depending on the value of the parameter DATMOD. The parameter NZP can take a value between 0 and the size of the FID or spectrum.
The value of NZP is the number of the real plus imaginary data points that are zeroed. As such, the first (NZP+1)/2 real points and the first NSP/2 imaginary data points are zeroed.


## INPUT PARAMETERS

Set by the user with edp or by typing nzp, datmod etc.: 
NZP - number of data points set to zero intensity
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

ZP


## SEE ALSO

zf 
© 2025 Bruker BioSpin GmbH & Co. KG
