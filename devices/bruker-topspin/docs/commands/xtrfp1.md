# xtrfp, xtrfp2, xtrfp1

**Category:** Commands > Process > Advanced > Special Transforms

## NAME

**xtrfp** - Custom processing of processed data in F2 and F1 (2D)

**xtrfp2** - Custom processing of processed data in F2 (2D)

**xtrfp1** - Custom processing of processed data in F1 (2D)


## DESCRIPTION

The command xtrfp performs customized processing of processed data both the F2 and F1 direction. It works like xtrf, except that it only works on processed data. If processed data do not exist, an error message is displayed. If processed data do exist, they are further processed according to the parameters BC_mod, WDW, ME_mod, FT_mod and PH_mod as described for xtrf.
xtrfp2 works like xtrfp, except that it only works in the F2 direction.
xtrfp1 works like xtrfp, except that it only works in the F1 direction.
The xtrfp* commands can, for example, be used to perform multiple additive baseline corrections. This can be necessary if the raw data contain multiple frequency baseline distortions. You cannot do this with xfb or xtrf because these commands always work on the raw data, i.e. they are not additive.
xtrfp, xtrfp2 and xtrfp1 can also be used for inverse Fourier transform. To do that: 
1. Type dpp to check the status FT_mod 
2. Type edp to set the processing parameters; set BC_mod, WDW, ME_mod and PH_mod to no and FT_mod to the inverse equivalent of the status FT_mod
3. Perform xtrfp, xtrfp2 or xtrfp1
As an alternative way to perform an inverse Fourier transform use the commands xif2 and xif1.


## INPUT PARAMETERS

F2 and F1 parameters
Set by the user with edp or by typing bc_mod, bcfw etc.:
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
PH_mod - phase correction mode
  PHC0 - zero order phase correction value for PH_mod = pk
  PHC1 - first order phase correction value for PH_mod = pk
FCOR - first (FID) data point multiplication factor (0.0-2.0, default 0.5)
REVERSE - flag indicating to reverse the spectrum
Set by a previous processing command, e.g. xtrf, can be viewed with dpp :
SI - size of the processed data
STSR - strip start: first output point of strip transform
STSI - strip size: number of output points of strip transform
TDeff - number of raw data points to be used for processing 
TDoff - first point of the FID used for processing (default 0)
F1 parameters
Set by a previous processing command, e.g. xtrf, can be viewed with dpp :
MC2 - Fourier transform mode
### OUTPUT PARAMETERS

F2 parameters
Can be viewed with dpp or by typing s ymax_p, s ymin_p etc.:
YMAX_p - maximum intensity of the processed data
YMIN_p - minimum intensity of the processed data
S_DEV - standard deviation of the processed data
NC_proc - intensity scaling factor
BYTORDP - byte order of the processed data


## INPUT FILES

<dir>/data/<user>/nmr/<name>/<expno>/pdata/<procno>/
  2rr, 2ir, 2ri, 2ii - processed 2D data
  proc - F2 processing parameters
  proc2 - F1 processing parameters


## OUTPUT FILES

<dir>/data/<user>/nmr/<name>/<expno>/pdata/<procno>/
  2rr, 2ir, 2ri, 2ii - processed 2D data
  procs - F2 processing status parameters
  proc2s - F1 processing status parameters
  auditp.txt - processing audit trail


## USAGE IN AU PROGRAMS

XTRFP
XTRFP2
XTRFP1


## SEE ALSO

xtrf, xtrf2, xfb, ftf, xf2, xf1
© 2025 Bruker BioSpin GmbH & Co. KG
