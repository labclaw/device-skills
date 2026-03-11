# filt

**Category:** Commands > Process > Advanced > Miscellaneous Operations

## NAME

**filt** - Digital filtering of the data (1D)


## DESCRIPTION

The command filt smoothes the data by replacing each point with a weighted average of its surrounding points. By default, filt uses the weighting coefficients 1-2-1 which means that the intensity p(i) of data point i is replaced by:
1 * p(i – 1) + 2 * p(i) + 1 * p(i + 1).
Different weighting algorithms can be set up by creating a new file in the directory:
<tshome>/exp/stan/nmr/filt/1d
Just copy the default file threepoint to a different name and modify it with a text editor. The file must look like:
3,1,2,1
or 
5,1,2,3,2,1
Where the first number represents the number of points used for smoothing and must be odd. The other numbers are the weighting coefficients for the data points. The processing parameter DFILT determines which file is used by filt. 
This is one of the few cases where file handling cannot be done from TopSpin and needs to be done on operating system level.


## INPUT PARAMETERS

Set by the user with edp or by typing dfilt, datmod etc. : 
DFILT - digital filter filename
DATMOD - data mode: work on raw or processed data


## INPUT FILES

<dir>/data/<user>/nmr/<name>/<expno>/pdata/<procno>/
1r, 1i - processed 1D data (real, imaginary)
proc - processing parameters
<tshome>/exp/stan/nmr/filt/1d/*
digital filtering file(s)


## OUTPUT FILES

<dir>/data/<user>/nmr/<name>/<expno>/pdata/<procno>/
1r, 1i - processed 1D data (real, imaginary)
procs - processing status parameters
auditp.txt - processing audit trail


## USAGE IN AU PROGRAMS

FILT
© 2025 Bruker BioSpin GmbH & Co. KG
