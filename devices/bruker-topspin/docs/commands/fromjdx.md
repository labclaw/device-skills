# fromjdx

**Category:** Commands > Miscellaneous > Dataset Handling

## NAME

**fromjdx** - Convert a JCAMP-DX data file to TopSpin format (1D, 2D)


## DESCRIPTION

The command fromdjx converts a JCAMP-DX data file to a TopSpin data set. JCAMP-DX is a standard ascii exchange format for spectroscopic data.
 
1. fromdjx supports the conversion of 1D data (raw or processed) and 2D data (raw or processed-real). 
2. fromjdx takes up to three arguments and can be used as follows:
1. fromjdx
2. prompts for the path name of the JCAMP-DX input file, converts it and stores it under the lowest empty expno and procno 1.
3. fromjdx <pathname>
4. converts the JCAMP-DX file specified by the path name and stores it under the lowest empty expno and procno 1.
5. fromjdx <pathname> y
6. converts the JCAMP-DX file specified by the path name and stores it under expno 1 and procno 1. Possibly existing data are overwritten (y).
In the examples above, fromjdx stores the output data set in the directory:
<dir>/data/<user>/nmr/<name>/<expno>/pdata/<procno>
Where
<dir> - the data directory of the current data set
<user> - the user of the currently current data set
<name> - the name of the JCAMP-DX file but without the extension .dx
Further examples:
1. fromjdx <pathname> du
2. Converts the JCAMP-DX file specified by the path name and stores it under the dir (=du), user, name, expno and procno as specified in the input JCAMP-DX file.
3. fromjdx <pathname> user
4. Converts the JCAMP-DX file specified by the path name and stores it under the dir of the current data set and the user, name, expno and procno as specified in the input JCAMP-DX file.
5. fromjdx <pathname> name
6. Converts the JCAMP-DX file specified by the path name and stores it under the dir and user of the active data set and the name, expno and procno as specified in the input JCAMP-DX file.
7. fromjdx <pathname> expno
8. Converts the JCAMP-DX file specified by the path name and stores it under the dir, user and name of the active data set and the expno and procno as specified in the input JCAMP-DX file.
9. fromjdx <pathname> procno
10. Converts the JCAMP-DX file specified by the path name and stores it under the dir, user and name of the active data set, expno 1 and the procno as specified in the input JCAMP-DX file.
All the above examples can be used with the y option to overwrite possibly existing data.


## INPUT FILES

<path name>/<mydata.dx> - TopSpin data in JCAMP-DX format


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


## USAGE IN AU PROGRAMS

FROMJDX(name)
For example FROMJDX("/tmp/mydata.dx")


## SEE ALSO

tojdx, totxt, tozip, fromzip
© 2025 Bruker BioSpin GmbH & Co. KG
