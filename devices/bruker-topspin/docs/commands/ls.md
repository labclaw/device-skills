# ls, rs

**Category:** Commands > Process > Advanced > Miscellaneous Operations

## NAME

**ls** - Left shift data NSP points (1D)

**rs** - Right shift data NSP points (1D)


## DESCRIPTION

The command ls shifts 1D data to the left. The number of points shifted is determined by the parameter NSP. The right end of the data is filled with NSP zeroes.
rs shifts 1D data to the right. The number of points shifted is determined by the parameter NSP. The left end of the data is filled with NSP zeroes. 
Depending on the parameter DATMOD, rs and ls work on raw or processed data. 
The value of NSP is the number of the real plus imaginary data points that are shifted. As such, the real data are shifted NSP/2 points and the imaginary data are shifted NSP/2 points. For odd values of NSP the real and imaginary data points are interchanged. As such the displayed spectrum is not only shifted but also changes from real (absorption) to imaginary (dispersion) or vice versa. Note that his only plays a role for DATMOD = proc.


## INPUT PARAMETERS

Set by the user with edp or by typing nsp, datmod etc.:
NSP - number of points to be shifted
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

LS
RS
© 2025 Bruker BioSpin GmbH & Co. KG
