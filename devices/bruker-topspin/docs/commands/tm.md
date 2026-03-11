# tm, traf, trafs

**Category:** Commands > Process > Processing Spectrum

## NAME

**tm** - Trapezoidal window multiplication of the FID (1D)

**traf** - Traficante window multiplication of the FID (1D)

**trafs** - Similar to traf, but additionally retains optimum signal-to-noise

**wm** - Open window function dialog box (1D, 2D)


## DESCRIPTION

Window multiplication can be executed from the command line or from the window function dialog box. The latter is opened with the command wm:
 
This dialog box offers several window functions, each of which selects a certain command for execution.
### Trapezoid

This function selects the command tm for execution. It performs a trapezoidal window multiplication of the FID. The rising and falling edge of this function are defined by the processing parameters TM1 and TM2. These represent a fraction of the acquisition time as displayed below. 
 
 
### Traficante and trafic.s/n

This function selects the commands traf and trafs , respectively, for execution. The algorithms used by these commands are described by D. D. Traficante and G. A. Nemeth in J. Magn. Res., 71, 237 (1987).
tm, traf and trafs implicitly perform a baseline correction of the FID, according to the processing parameter BC_mod. Furthermore, they perform linear prediction according to the parameters ME_mod, NCOEF and LPBIN.
When executed on 2D or 3D data, tm and traf* take up to four arguments, e.g. tm <row> <procno> n y process the specified row and store it under the specified procno. The last two arguments are optional: n prevents changing the display to the output 1D data, y causes a possibly existing data to be overwritten without warning.
If you run a command like tm from the command line, you have to make sure that the required parameters are already set. Click the Procpars tab or enter edp to do that.
When executed on a dataset with 2D or 3D raw data but 1D processed data (usually a result of rsr, rsc or a previous 1D processing command on that 2D or 3D data), tm and traf* take one argument, e.g. tm <row> process the specified row and store it under the current procno.
tm same process the same row as the previous processing command and store it under the current procno. The same option is automatically used by the AU program macro TM. When used on a regular 1D dataset (i.e. with 1D raw data) it has no effect.
The wm command can be used on 1D or 2D data. It recognizes the data dimensionality and opens a dialog box with the appropriate options and parameters.


## INPUT PARAMETERS

Set from the wm dialog box, with edp or by typing tm1, lb etc.:
TM1 - the end of the rising edge of a trapeziodal window (input of tm)
TM2 - the start of the falling edge of a trapezoidal window (input of tm)
LB - Lorentzian broadening factor (input of traf*)
Set by the acquisition, can be viewed with dpa or s aq:
AQ - acquisition time (input of tm)


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

TM


## SEE ALSO

em, gm, wm 
© 2025 Bruker BioSpin GmbH & Co. KG
