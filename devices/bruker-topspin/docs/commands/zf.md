# zf

**Category:** Commands > Process > Advanced > Miscellaneous Operations

## NAME

**zf** - Zero all data points (1D)


## DESCRIPTION

The command zf sets the intensity of all data points to zero. Depending on the value of the parameter DATMOD, zf works on raw or processed data. The result is always stored as processed data, the raw data are never overwritten. 
The output of zf is usually the same for DATMOD = raw or processed, namely SI processed data points with zero intensity. However, for DATMOD = proc, the existing processed data are set to zero whereas for DATMOD = raw, new processed data are created according to the current processing parameters. The result is different when the data have been Fourier transformed with STSI < SI. zf with DATMOD = proc creates STSI zeroes whereas zf with DATMOD = raw creates SI zeroes. The reason is that zf with DATMOD = raw reprocesses the raw data but does not interpret STSI since no Fourier transform is done.


## INPUT PARAMETERS

Set by the user with edp or by typing datmod, si etc.:
DATMOD - data mode: work on raw or processed data
SI - size of the processed data
STSI - strip size (input if DATMOD = proc)


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

ZF


## SEE ALSO

zp 
© 2025 Bruker BioSpin GmbH & Co. KG
