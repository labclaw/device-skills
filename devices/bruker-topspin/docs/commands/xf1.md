# xf1

**Category:** Commands > Process > Processing Spectrum

## NAME

**xf1** - Process data, including FT, in F1 (2D)


## DESCRIPTION

The command xf1 processes a 2D dataset in the F1 direction. It can be started from the command line or from the Fourier transform dialog box. The latter is opened with the command ftf.
xf1 Fourier transforms time domain data (FID) into frequency domain data (spectrum). Depending on the F1 processing parameters BC_mod, WDW, ME_mod and PH_mod, xf1 also performs baseline correction, window multiplication, linear prediction and phase correction, respectively. These steps are described in detail for the command xfb. 
Normally, 2D data are processed with the command xfb which performs a Fourier transform in both directions, F2 and F1. In some cases, however, it is useful to process the data in two separate steps using the sequence xf2 - xf1, for example to view the data after processing them in F2 only.
If you run xf1 without running xf2 first, a warning that the F2 transform has not been done will appear. When the command has finished the data are in the time domain in F2 and in the frequency domain in F1. The opposite case, however, is more usual, i.e. data which have only been processed with xf2.
xf1 takes the same options as xfb.
The F1 Fourier transform mode and data storage mode depends on the F1 acquisition mode (see INPUT PARAMETERS below and the description of xfb).


## INPUT PARAMETERS

F2 and F1 parameters
Set by xf2, can be viewed with dpp or by typing s si, s stsr etc.:
  SI - size of the processed data
  STSR - strip start: first output point of strip transform
  STSI - strip size: number of output points of strip transform
  TDeff - number of raw data points to be used for processing 
  TDoff - first point of the FID used for processing (default 0)
If xf2 has not been done, xf1 uses the edp parameters set by the user.
F1 parameters
Set from the ftf dialog box, with edp or by typing bc_mod etc.
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
PH_mod - phase correction mode
  PHC0 - zero order phase correction value for PH_mod = pk
  PHC1 - first order phase correction value for PH_mod = pk
FCOR - first (FID) data point multiplication factor (0.0-2.0, default 0.5)
REVERSE - flag indicating to reverse the spectrum
Set by the xf2, can be viewed with dpp or by typing s mc2 :
  MC2 - Fourier transform mode (input of xf1 on processed data)
Set by the acquisition, can be viewed with dpa or by typing s fnmode:
  FnMODE - Acquisition mode (input of xf1 on raw data)
### OUTPUT PARAMETERS

F1 parameters
Can be viewed with dpp or by typing s ft_mod etc.:
  FT_mod - Fourier transform mode
  FTSIZE - Fourier transform size
F2 parameters
Can be viewed with dpp or by typing s ymax_p, s ymin_p etc.:
  YMAX_p - maximum intensity of the processed data
  YMIN_p - minimum intensity of the processed data
  S_DEV - standard deviation of the processed data
  NC_proc - intensity scaling factor


## INPUT FILES

<dir>/data/<user>/nmr/<name>/<expno>/
  ser - raw data (input if 2rr does not exist or is Fourier transformed in F1)
  acqu2s - F1 acquisition status parameters
<dir>/data/<user>/nmr/<name>/<expno>/pdata/<procno>/
  2rr - real processed data (input if it exists but is not processed in F1) 
  2ir - second quadrant imaginary processed data (input if FnMODE ≠ QF)
  2ii - second quadrant imaginary processed data (input if FnMODE = QF)
  proc - F2 processing parameters
  proc2 - F1 processing parameters


## OUTPUT FILES

<dir>/data/<user>/nmr/<name>/<expno>/pdata/<procno>/
  2rr - real processed data
  2ir - third quadrant imaginary processed data (output if FnMODE ≠ QF)
  2ii - fourth quadrant imaginary processed data (output if FnMODE ≠ QF)
  2ii - second quadrant imaginary processed data (output if FnMODE = QF)
  procs - F2 processing status parameters
  proc2s - F1 processing status parameters
  auditp.txt - processing audit trail


## USAGE IN AU PROGRAMS

XF1


## SEE ALSO

xf2, xfb, ftf, xfb, ftf, xtrf, xtrf2, xtrfp, xtrfp2, xtrfp1
© 2025 Bruker BioSpin GmbH & Co. KG
