# sinm, qsin, sinc, qsinc

**Category:** Commands > Process > Processing Spectrum

## NAME

**sinm** - Sine window multiplication of the FID (1D)

**qsin** - Sine squared window multiplication of the FID (1D)

**sinc** - Sinc window multiplication of the FID (1D)

**qsinc** - Sinc squared window multiplication of the FID (1D)

**wm** - Open window function dialog box (1D, 2D)


## DESCRIPTION

Window multiplication commands can be started from the command line or from the window function dialog box. The latter is opened with the command wm:
 
This dialog box offers several window functions, each of which selects a certain command for execution.
### Sine bell

This window function selects the command sinm for execution. It performs a sine window multiplication, according to the function:
SINM(t) = sin((π – PHI) * (t / AQ) + PHI)
where
0 < t < AQ and PHI = π /  SSB
Where AQ is an acquisition status parameter and SSB a processing parameter. 
Typical values are SSB = 1 for a pure sine function and SSB = 2 for a pure cosine function. Values greater than 2 give a mixed sine/cosine function. Note that all values smaller than 2, for example 0, have the same effect as SSB = 1, namely a pure sine function. 
### Squared sine bell

This window function selects the command qsin for execution. It performs a sine squared window multiplication, according to the function:
QSIN (t) = sin ((π – PHI ) × (t / AQ) + PHI )2
where 
0 < t < AQ and PHI = π / SSB
Where AQ is an acquisition status parameter and SSB a processing parameter.
Typical values are SSB = 1 for a pure sine function and SSB = 2 for a pure cosine function. Values greater than 2 give mixed sine/cosine functions. Note that all values smaller than 2 have the same effect as SSB = 1, namely a pure sine function. 
If commands like qsin are typed on a 2D or 3D spectrum, the following warning message is displayed. Enter the appropriate values.
 
### Sinc

This window function selects the command sinc for execution. It performs a sinc window multiplication, according to the function:
Where 
– 2 π * SSB * GB < t < 2 π * SSB *  (1 – GB)
and SSB and GB are processing parameters. 
### Squared sinc

This window function selects the command qsinc for execution. It performs a sinc squared window multiplication, according to the function:
Where 
– 2π * SSB * GB < t < 2 π * SSB * (1 – GB)
and SSB and GB are processing parameters.
The *sin* commands implicitly perform a baseline correction of the FID, according to the processing parameter BC_mod. Furthermore, they perform linear prediction according to the parameters ME_mod, NCOEF and LPBIN.
If you run a command like sinm from the command line, you have to make sure that the required parameters are already set. Click the Procpars tab or enter edp to do that.
When executed on 2D or 3D data, the *sin* commands take up to four arguments, e.g. sinm <row> <procno> n y, process the specified row and store it under the specified procno. The last two arguments are optional: n prevents changing the display to the output 1D data, y causes a possibly existing data to be overwritten without warning.
When executed on a dataset with 2D or 3D raw data but 1D processed data (usually a result of rsr, rsc or a previous 1D processing command on that 2D or 3D data), the sin* commands take one argument sinm <row> to process the specified row and store it under the current procno.
sinm same process the same row as the previous processing command and store it under the current procno. The same option is automatically used by the AU program macros *SIN*. When used on a regular 1D dataset (i.e. with 1D raw data) it has no effect.
The wm command can be used on 1D or 2D data. It recognizes the data dimensionality and opens a dialog box with the appropriate options and parameters.


## INPUT PARAMETERS

Set from the wm dialog box, with edp or by typing ssb, gb etc.:
SSB - sine bell shift
GB - Gaussian broadening factor (input of sinc and qsinc)
Set by the acquisition, can be viewed with dpa or s aq:
AQ - Acquisition time (input of sinm and qsin)


## INPUT FILES

<dir>/data/<user>/nmr/<name>/<expno>/
fid - raw data (input if 1r, 1i do not exist or are Fourier transformed)
acqus - acquisition status parameters
<dir>/data/<user>/nmr/<name>/<expno>/pdata/<procno>/
1r, 1i - processed data (input if they exist but are not Fourier transformed)
proc - processing parameters


## OUTPUT FILES

<dir>/data/<user>/nmr/<name>/<expno>/pdata/<procno>/
1r, 1i - processed 1D data (real, imaginary)
procs - processing status parameters
auditp.txt - processing audit trail


## USAGE IN AU PROGRAMS

SINM
QSIN
SINC
QSINC


## SEE ALSO

em, gm, wm, qf, qfp, tm, traf, trafs
© 2025 Bruker BioSpin GmbH & Co. KG
