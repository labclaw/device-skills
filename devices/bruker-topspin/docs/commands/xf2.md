# xf2

**Category:** Commands > Process > Processing Spectrum

## NAME

**xf2** - Process data, including FT, in F2 (2D)


## DESCRIPTION

The command xf2 processes a 2D dataset in the F2 direction. It can be started from the command line or from the Fourier transform dialog box. The latter is opened with the command ftf. 
xf2 Fourier transforms time domain data (FID) into frequency domain data (spectrum). Depending on the F2 processing parameters BC_mod, WDW, ME_mod and PH_mod, xf2 also performs baseline correction, window multiplication, linear prediction and phase correction, respectively. These steps are described in detail for the command xfb. 
Normally, 2D data are processed with the command xfb which performs a Fourier transform in both directions, F2 and F1. In some cases, however, 2D data must only be processed in the F2 direction. Examples are T1, T2 or Dosy data, or a 2D dataset which has been created from a series on 1D datasets. 
Even if a 2D dataset must be processed in both directions, it is sometimes useful to do that in two separate steps using the sequence xf2 - xf1. The result is exactly the same as with xfb with one exception; xfb performs a quad spike correction (see xfb) and the sequence xf2 - xf1 does not. 
xf2 takes the same options as xfb. Furthermore, xf2 takes the special option nd2d converting an nD dataset (n>2) to a 2D dataset processing it in the acquisition direction. The size in the orthogonal direction (F1-SI) of the destination 2D dataset, is the product of the TD values of the source nD dataset.
xf2 can also be used to process one 2D plane of a 3D spectrum (see xfb).


## INPUT PARAMETERS

F2 and F1 parameters
Set from the ftf dialog box, with edp or by typing si, stsr etc.:
  SI - size of the processed data
  STSR - strip start: first output point of strip transform
  STSI - strip size: number of output points of strip transform
  TDeff - number of raw data points to be used for processing 
  TDoff - first point of the FID used for processing (default 0)
  XDIM - submatrix size (only used for the command xf2 xdim)
Set by the acquisition, can be viewed with dpa or by typing s td:
  TD - time domain; number of raw data points
F2 parameters
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
Set by the acquisition, can be viewed with dpa or by typing s aq_mod:
  AQ_mod - acquisition mode (determines the Fourier transform mode)
  BYTORDA - byteorder or the raw data
  NC - normalization constant
F1 parameters
Set by the acquisition, can be viewed with dpa or by typing s fnmode :
  FnMODE - Fourier transform mode
### OUTPUT PARAMETERS

F2 and F1 parameters
Can be viewed with dpp or by typing s si, s tdeff etc.:
  SI - size of the processed data
  TDeff - number of raw data points that were used for processing
  STSR - strip start: first output point of strip transform 
  STSI - strip size: number of output points of strip transform
  FTSIZE - Fourier transform size
  XDIM - submatrix size
F2 parameters
Can be viewed with dpp or by typing s ft_mod, s ymax_p etc.:
  FT_mod - Fourier transform mode
  YMAX_p - maximum intensity of the processed data
  YMIN_p - minimum intensity of the processed data
  S_DEV - standard deviation of the processed data
  NC_proc - intensity scaling factor
  BYTORDP - byte order of the processed data
F1 parameters
Set by the acquisition, can be viewed with dpp or by typing s mc2 :
  MC2 - Fourier transform mode


## INPUT FILES

<dir>/data/<user>/nmr/<name>/<expno>/
  ser - raw data (input if 2rr does not exist or is Fourier transformed in F2) 
  acqus - F2 acquisition status parameters
  acqu2s - F1 acquisition parameters
<dir>/data/<user>/nmr/<name>/<expno>/pdata/<procno>/
  2rr - processed data (input if it exists but is not Fourier transformed in F2)
  proc - F2 processing parameters
  proc2 - F1 processing parameters
### NOTE

Note that if 2rr is input, 2ri is also input if xf1 has been done.


## OUTPUT FILES

<dir>/data/<user>/nmr/<name>/<expno>/pdata/<procno>/
  2rr - first quadrant real processed data
  2ir - second quadrant imaginary processed data (output if FnMODE ≠ QF)
  2ii - second quadrant imaginary processed data (output if FnMODE = QF) 
  procs - F2 processing status parameters
  auditp.txt - processing audit trail


## USAGE IN AU PROGRAMS

XF2


## SEE ALSO

xf1, xfb, ftf, xtrf, xtrf2
© 2025 Bruker BioSpin GmbH & Co. KG
