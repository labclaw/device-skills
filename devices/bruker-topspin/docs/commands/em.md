# em, gm, wm

**Category:** Commands > Process > Processing Spectrum

## NAME

**em** - Exponential window multiplication of the FID (1D)

**gm** - Gaussian window multiplication of the FID (1D)

**wm** - Open window function dialog box (1D, 2D)


## DESCRIPTION

Window multiplication commands can be entered on the command line or started from the window function dialog box. The latter is opened with the command wm.
 
The parameter section of this dialog box offers several window functions, each of which selects a certain command for execution.
### Exponential multiplication

This function selects the command em for execution. It performs an exponential window multiplication of the FID. It is the most used window function for NMR spectra. em multiplies each data point i with the factor:

Where LB (the line broadening factor) is a processing parameter and SWH (the spectral width) an acquisition status parameter. 
### Gaussian multiplication

This function selects the command gm for execution. It performs a Gaussian window multiplication of the FID. The result is a Gaussian line shape after Fourier transform. This line shape has sharper edges than the line shape caused by em. gm multiplies the FID with the function:

Where t is the acquisition time in seconds and the parameters a and b are defined by:
In this equation, LB and GB are processing parameters which represent the exponential broadening factor and the Gaussian broadening factor, respectively. AQ is an acquisition status parameter which represents the acquisition time.
gm allows to separate overlapping peaks. The quality of the separation depends on the choice of the parameters LB and GB. Suitable values can be determined with Manual window adjustment. The value of LB must be negative, typically the half line width of the spectral peaks. Note that for exponential window multiplication (em), LB must be positive. The value of GB must lie between 0 and 1. It determines the position of the top of the Gaussian function. For example, for GB = 0.5 the top lies in the middle of the FID. Note that for large values of GB (close to 1), peaks can become negative at the edges which can impair quantitative analysis of the spectrum.
em and gm implicitly perform a baseline correction of the FID, according to the processing parameter BC_mod. Furthermore, they perform linear prediction according to the parameters ME_mod, NCOEF and LPBIN.
When executed on 2D or 3D data, em and gm take up to four arguments, e.g. em <row> <procno> n y process the specified row and store it under the specified procno. The last two arguments are optional: n prevents changing the display to the output 1D data, y causes a possibly existing data to be overwritten without warning.
When executed on a dataset with 2D or 3D raw data but 1D processed data (usually a result of rsr, rsc or a previous 1D processing command on that 2D or 3D data, em and gm take one argument, e.g. em <row> processes the specified row and stores it under the current procno.
em same processes the same row as the previous processing command and stores it under the current procno. The same option is automatically used by the AU program macros EM and GM. When used on a regular 1D dataset (i.e. with 1D raw data) it has no effect.
If you run a command like em from the command line, you have to make sure that the required parameters are already set. Click the Procpars tab or enter edp to do that.
The wm command can be used on 1D or 2D data. It recognizes the data dimensionality and opens a dialog box with the appropriate options and parameters.


## INPUT PARAMETERS

Set from the wm dialog box, with edp or by typing lb, bc_mod etc.:
LB - Lorentzian broadening factor
GB - Gaussian broadening factor
BC_mod - FID baseline correction mode
Set by the acquisition, can be viewed with dpa or s swh:
SWH - spectral width


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

EM
GM


## SEE ALSO

tm, traf, trafs
© 2025 Bruker BioSpin GmbH & Co. KG
