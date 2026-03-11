# fromzip

**Category:** Commands > Miscellaneous > Dataset Handling

## NAME

**fromzip** - Unzip / display a zipped TopSpin data set (nD)


## DESCRIPTION

The command fromzip opens a dialog box to unzip a ZIP TopSpin data set.
 
Here you can enter the ZIP file (pathname) and the DIR and USER part of the output data path.
fromzip takes up to three arguments and can be used as follows:
1. fromzip
2. opens the above dialog box.
3. fromzip <pathname> <dir> <user>
4. converts the ZIP file specified by the path name and stores it under the specified <dir> and <user> and the name, expno and procno as stored in the ZIP archive.
In the examples above, fromzip stores the output data set in the directory:
<dir>/data/<user>/nmr/<name>/<expno>/pdata/<procno>
The TopSpin data set created by fromzip becomes the active data set.


## INPUT FILES

<path name>/<mydata.bnmr.zip> - TopSpin data as stored by tozip


## OUTPUT FILES

### For 1D and 2D data:

<tshome>/prog/curdir/<user>/
curdat - current data definition
<dir>/data/<user>/nmr/<name>/<expno>/
audita.txt - acquisition audit trail (if input file contains raw data)
 
<dir>/data/<user>/nmr/<name>/<expno>/pdata/<procno>
auditp.txt - processing audit trail (if input file contains processed data)
outd - output device parameters
title - title file (see edti)
### For 1D data:

<dir>/data/<user>/nmr/<name>/<expno>/
fid - 1D raw data (if input file contains 1D raw data)
acqu - acquisition parameters
acqus - acquisition status parameters
 
<dir>/data/<user>/nmr/<name>/<expno>/pdata/<procno>
1r - real processed 1D data (if input file contains 1D real processed data)
1i - imaginary processed 1D data (if input file contains 1D imaginary data)
proc - processing parameters
procs - processing status parameters
### For 2D data:

<dir>/data/<user>/nmr/<name>/<expno>/
ser - 2D raw data (input if Output Data = raw)
acqu - F2 acquisition parameters
acqu2 - F1 acquisition parameters
acqus - F2 acquisition status parameters
acqu2s - F1 acquisition status parameters
 
<dir>/data/<user>/nmr/<name>/<expno>/pdata/<procno>
2rr - real processed 2D data (if input file contains 2D real processed data)
proc - F2 processing parameters
proc2 - F1 processing parameters
procs - F2 processing status parameters
proc2s - F1 processing status parameters
clevels - 2D contour levels
For 3D data, the additional parameter files acqu3, acqu3s, proc3 and proc3s will be created.


## SEE ALSO

tozip, tojdx, totxt, fromzip
© 2025 Bruker BioSpin GmbH & Co. KG
