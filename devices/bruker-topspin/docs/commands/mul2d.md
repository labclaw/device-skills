# add2d, mul2d, addser

**Category:** Commands > Process > Advanced

## NAME

**add2d** - Add or subtract two datasets (2D)

**mul2d** - Multiply two datasets (2D)

**addser** - Add two raw datasets (2D, 3D)

**adsu** - Open add/subtract/multiply workflow button bar (1D, 2D)


## DESCRIPTION

Addition commands can be started from the command line or from the add/subtract workflow button bar. The latter is opened with the command adsu.
 
This workflow button bar offers several options, each of which selects a certain command for execution.
### Add a 2D spectrum

This option selects the command add2d for execution. It adds the processed data of the second dataset to those of the current 2D dataset, according to the following formula:
current = ALPHA*current + GAMMA*second
Where ALPHA and GAMMA are processing parameters. Both real and imaginary data are added. The result overwrites the current processed data. For APLHA = 1 and GAMMA = -1, the spectra are subtracted.
### Multiply with another 2D spectrum

This option selects the command mul2d for execution. It multiplies the processed data of the second dataset with those of the current 2D dataset. Both real and imaginary data are multiplied. The result overwrites the current processed data.
### Add 2D fid (ser)

This option selects the command addser for execution. It adds the raw data of the second dataset to those of the current 2D dataset. The result overwrites the current raw data. Note that addser also works on 3D data.
### NOTE

The two 2D datasets to be added or multiplied must have equal sizes.
If you run a command like add2d from the command line, you have to make sure that the required parameters are already set. Click the Procpars tab or enter edp to do that. If the second dataset has not been defined yet, add2d opens the add/subtract (adsu) dialog box.
The adsu command can be used on 1D or 2D data. It recognizes the data dimensionality and opens a dialog box with the appropriate options and parameters.


## INPUT PARAMETERS

Set from the adsu workflow button bar, with edp or by typing alpha, gamma etc.:
ALPHA - multiplication factor of the current spectrum
GAMMA - multiplication factor of the second spectrum


## INPUT FILES

<dir>/data/<user>/nmr/<name>/<expno>/pdata/<procno>/
2rr, 2ir, 2ri, 2ii - processed data of the current dataset
proc - F2 processing parameters
<dir2>/data/<user2>/nmr/<name2>/<expno2>/pdata/<procno2>/
2rr, 2ir, 2ri, 2ii - processed data of the second dataset


## OUTPUT FILES

<dir>/data/<user>/nmr/<name>/<expno>/pdata/<procno>/
2rr, 2ir, 2ri, 2ii - processed data
procs - F2 processing status parameters
auditp.txt - processing audit trail


## USAGE IN AU PROGRAMS

ADD2D
ADDSER
MUL2D


## SEE ALSO

add, duadd, addfid, addc, adsu, mul, mulc, nm, div
© 2025 Bruker BioSpin GmbH & Co. KG
