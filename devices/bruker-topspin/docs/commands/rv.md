# rv

**Category:** Commands > Process > Advanced > Miscellaneous Operations

## NAME

**rv** - Reverse spectrum or FID (1D)


## DESCRIPTION

The command rv reverses the data with respect to the middle data point, i.e. the leftmost data point becomes the rightmost point and vice versa. The real and imaginary parts of the spectrum are thereby interchanged. Depending on the value of DATMOD, rv works on the raw or on the processed data. The result is always stored as processed data. 
A spectrum can also be reversed as a part of the Fourier transform by setting the processing parameter REVERSE to TRUE.


## INPUT PARAMETERS

Set by the user with edp or by typing datmod :
DATMOD - data mode: work on raw or processed data


## INPUT FILES

<dir>/data/<user>/nmr/<name>/<expno>/
fid - raw data (input if DATMOD = raw)
<dir>/data/<user>/nmr/<name>/<expno>/pdata/<procno>/
1r, 1i - processed 1D data (input if DATMOD = proc)
proc - processing parameters


## OUTPUT FILES

<dir>/data/<user>/nmr/<name>/<expno>/pdata/<procno>/
1r, 1i - processed 1D data
procs - processing status parameters
auditp.txt - processing audit trail


## USAGE IN AU PROGRAMS

RV


## SEE ALSO

ft, ftf, trf, trfp
© 2025 Bruker BioSpin GmbH & Co. KG
