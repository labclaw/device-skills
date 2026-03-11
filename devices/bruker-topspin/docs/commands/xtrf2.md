# xtrf, xtrf2

**Category:** Commands > Process > Advanced > Special Transforms

## NAME

**xtrf** - Custom processing of raw data in F2 and F1 (2D)

**xtrf2** - Custom processing of raw data in F2 (2D)


## DESCRIPTION

The command xtrf performs customized processing of the raw data in both the F2 and F1 direction. It processes data according to the processing parameters BC_mod, WDW, ME_mod, FT_mod and PH_mod. xtrf works like xfb, except for the following differences:
1. The Fourier transform is performed according to the processing parameter FT_mod, whereas the acquisition status parameter AQ_mod is ignored. This, for example, allows to process the data without Fourier transform (FT_mod = no). Furthermore, you can choose a Fourier transform mode different from the one that would be evaluated from the acquisition mode. This feature is not used very often because the Fourier transform as evaluated from the acquisition mode is usually the correct one. If, however, you want to manipulate the acquisition mode of the raw data, you can Fourier transform the data with one FT_mod, inverse Fourier transform them with a different FT_mod. Then you can use genser to create pseudo-raw data with a different acquisition mode than the original raw data. The table below shows a list of values of FT_mod.
2. A baseline correction is performed according to BC_mod. This parameter can take the value no, single, quad, spol, qpol, sfil or qfil. xtrf evaluates BC_mod for the baseline correction mode (e.g. quad, qpol or qfil) and for the detection mode (e.g. single or quad, spol or qpol, sfil or qfil). Note that xfb evaluates the acquisition status parameter AQ_mod for the detection mode.
3. When all parameters mentioned above are set to no, no processing is done but the raw data are still stored as processed data and displayed on the screen. This means the raw data are converted to submatrix format (files 2rr, 2ir, 2ri and 2ii) and scaled according to the vertical resolution. The intensity scaling factor is stored in the processing status parameter NC_proc and can be viewed with dpp. The size of these processed data and the number of raw data points which are used are determined by the parameters SI, TDeff and TDoff, as described for the command xfb. For example, if 0 < TDeff < TD, the processed data are truncated. This allows to create pseudo-raw data with a smaller size than the original raw data (see also genser).
FT_mod
Fourier transform mode
no
no Fourier transform
fsr
forward, single channel, real
fqr
forward, quadrature, real
fsc
forward, single channel, complex
fqc
forward, quadrature, complex
isr
inverse, single channel, real
iqr
inverse, quadrature, real
isc
inverse, single channel, complex
iqc
inverse, quadrature, complex
 
The F1 Fourier transform mode and data storage mode depends on the F1 acquisition mode (see INPUT PARAMETERS below and the description of xfb). 
xtrf2 works like xtrf, except that it only works in the F2 direction.
xtrf and xtrf2 take the same options as xfb.
xtrf can be used to do a combination of forward and backward prediction.
Run xtrf with ME_mod = LPfc and xtrfp (or xfb) with ME_mod = LPbc.


## INPUT PARAMETERS

F2 and F1 direction 
Set by the user with edp or by typing si, bc_mod, bcfw etc.:
SI - size of the processed data
TDeff - number of raw data points to be used for processing 
TDoff - first point of the FID used for processing (default 0)
FCOR - first (FID) data point multiplication factor (0.0-2.0, default 0.5)
BC_mod - FID baseline correction mode
  BCFW - filter width for BC_mod = sfil or qfil
  COROFFS - correction offset for BC_mod = spol/qpol or sfil/qfil
ME_mod - FID linear prediction mode
  NCOEF - number of linear prediction coefficients 
  LPBIN - number of points for linear prediction 
  TDoff - number of raw data points predicted for ME_mod = LPb*
WDW - FID window multiplication mode
  LB - Lorentzian broadening factor for WDW = em or gm
  GB - Gaussian broadening factor for WDW = gm, sinc or qsinc
  SSB - Sine bell shift for WDW = sine, qsine, sinc or qsinc
  TM1, TM2 - limits of the trapezoidal window for WDW = trap
FT_mod - Fourier transform mode
  STSR - strip start: first output point of strip transform
  STSI - strip size: number of output points of strip transform
  REVERSE - flag indicating to reverse the spectrum
  PKNL - group delay compensation (Avance) or filter correction (A*X)
PH_mod - phase correction mode
  PHC0 - zero order phase correction value for PH_mod = pk
  PHC1 - first order phase correction value for PH_mod = pk
Set by the acquisition, can be viewed with dpa or by typing s td :
TD - time domain; number of raw data points
F2 direction 
Set by the acquisition, can be viewed with dpa or by typing s bytorda:
BYTORDA - byteorder or the raw data
NC - normalization constant
F1 direction 
Set by the acquisition, can be viewed with dpa or by typing s fnmode:
FnMODE - Acquisition mode
### OUTPUT PARAMETERS

F2 and F1 parameters
Can be viewed with dpp or by typing s si etc.:
SI - size of the processed data
TDeff - number of raw data points that were used for processing
STSR - strip start: first output point of strip transform 
STSI - strip size: number of output points of strip transform
XDIM - submatrix size
F2 parameters
Can be viewed with dpp or by typing s ymax_p, s ymin_p etc.:
YMAX_p - maximum intensity of the processed data
YMIN_p - minimum intensity of the processed data
S_DEV - standard deviation of the processed data
NC_proc - intensity scaling factor
BYTORDP - byte order of the processed data


## INPUT FILES

<dir>/data/<user>/nmr/<name>/<expno>/
  ser - raw data
  acqus - F2 acquisition status parameters
  acqu2s - F1 acquisition status parameters
<dir>/data/<user>/nmr/<name>/<expno>/pdata/<procno>/
  proc - F2 processing parameters
  proc2 - F1 processing parameters


## OUTPUT FILES

<dir>/data/<user>/nmr/<name>/<expno>/pdata/<procno>/
  2rr, 2ir, 2ri, 2ii - processed 2D data
  procs - processing status parameters
  proc2s - processing status parameters
  auditp.txt - processing audit trail


## USAGE IN AU PROGRAMS

XTRF
XTRF2


## SEE ALSO

xtrfp, xtrfp2, xfb, ftf, xf2, xf1
© 2025 Bruker BioSpin GmbH & Co. KG
