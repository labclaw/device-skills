# mul, mulc, nm, div

**Category:** Commands > Process > Advanced

## NAME

**mul** - Multiply two datasets (1D)

**mulc** - Multiply data with a constant (1D)

**nm** - Negate data (1D)

**div** - Divide two datasets (1D)

**adsu** - Open add/subtract/multiply workflow button bar (1D, 2D)


## DESCRIPTION

Multiplication commands can be entered on the command line or started from the add/subtract/multiply workflow button bar. The latter is opened with adsu.
 
This workflow button bar offers several options, each of which selects a certain command for execution.
### Multiply with 1D spectrum/fid

This option selects the command mul for execution. It multiplies the second dataset with the third dataset. The result is stored in the current dataset.
### Multiply with constant

This option selects the command mulc for execution. It multiplies the current data with the value of DC.
### Multiply with -1

This option selects the command nm for execution. It negates the current data which means all data points are multiplied by -1.
### Divide by 1D spectrum/fid

This option selects the command div for execution. It divides the second dataset by the third dataset. The result is stored in the current dataset. 
mul/div perform a complex multiplication/division on complex spectra. This requires that for both the second and third dataset:
1. the status parameter FT_mod = fqc or fsc
2. real (file 1r) and imaginary (file 1i) data exist
This is the case for most data that have been acquired in Avance spectrometers. If the above requirements are not fulfilled, real and imaginary data are multiplied/divided pointwise. When a complex operation has been performed, this is reported in the audit trail output file. 
Please note in addition that deleting the imaginary data enforces a pointwise multiplication for the command mul instead of a complex multiplication. 
mul, div, mulc and nm work on raw or on processed data, depending on the value of DATMOD. The result is always stored as processed data in the current dataset. The raw data are not overwritten. 
When mul and div are started from the command line, they will run without user interaction if the second dataset is already defined (file curdat2). If this is not defined, you will be prompted to use the edc2 command to set it. When you run a multiplication or division command from the command line, make sure that the required parameters are set. Click the Procpars tab or enter edp to do that.
The adsu command can be used on 1D or 2D data. It recognizes the data dimensionality and opens a workflow button bar with the appropriate options and parameters.


## INPUT PARAMETERS

Set from the adsu workflow button bar, with edp or by typing dc, datmod etc.: 
DC - multiplication factor (input of mulc)
DATMOD - data mode: work on raw or processed data


## INPUT FILES

<dir>/data/<user>/nmr/<name>/<expno>/
fid - raw data (input if DATMOD = raw)
<dir>/data/<user>/nmr/<name>/<expno>/pdata/<procno>/
1r, 1i - processed 1D data (input if DATMOD = proc)
proc - processing parameters
curdat2 - definition of the second dataset
<dir2>/data/<user2>/nmr/<name2>/<expno2>/
fid - second raw data (input if DATMOD = raw)
<dir2>/data/<user2>/nmr/<name2>/<expno2>/pdata/<procno2>/
1r, 1i - processed 1D data (input if DATMOD = proc)


## OUTPUT FILES

<dir>/data/<user>/nmr/<name>/<expno>/pdata/<procno>/
1r, 1i - processed 1D data (real, imaginary)
procs - processing status parameters
auditp.txt - processing audit trail


## USAGE IN AU PROGRAMS

MUL
MULC
NM
DIV


## SEE ALSO

add  
© 2025 Bruker BioSpin GmbH & Co. KG
