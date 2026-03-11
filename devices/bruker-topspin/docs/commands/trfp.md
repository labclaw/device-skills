# trf, trfp

**Category:** Commands > Process > Advanced > Special Transforms

## NAME

**trf** - User-defined processing of raw data (1D)

**trfp** - User-defined processing of processed data (1D)


## DESCRIPTION

The command trf processes the raw data performing the following steps:
1. baseline correction according to BC_mod
2. linear prediction according to ME_mod
3. window multiplication according to WDW
4. Fourier transform according to FT_mod
5. phase correction according to PH_mod
trf offers the following features: 
1. when all parameters mentioned above are set to no, the raw data (file fid) are simply stored as processed data (files 1r, 1i). The even points are stored as real data (file 1r) and the odd points as imaginary data (file 1i). The size of these processed data and the number of input FID points are determined by the parameters SI and TDeff, as described for the command ft. For example, if 0 < TDeff < TD, the processed data are truncated. This allows to create an FID with a smaller size than the original one (see also the command genfid genfid).
2. trf evaluates BC_mod for the baseline correction mode (e.g. quad, qpol or qfil) and detection mode (e.g. single or quad, spol or qpol, sfil or qfil). Note that the command bc evaluates the acquisition status parameter AQ_mod for the detection mode and ignores the BC_mod detection mode (see parameter BC_mod).
3. trf evaluates WDW for the window multiplication mode (em, gm, sine, qsine, trap, user, sinc, qsinc, traf or trafs). This allows to vary the window multiplication by varying the value of WDW rather than the window multiplication command. This can be useful in AU programs.
4. the Fourier transform is performed according to FT_mod. Normally, the Fourier transform is done with the command ft which determines the Fourier transform mode from acquisition status parameter AQ_mod. However, for some datasets, no value of AQ_mod translates to a correct Fourier transform mode. An example of this is when you read a column (with rsc) from a 2D dataset which was measured with FnMODE (or MC2) = States-TPPI and Fourier transformed in the F2 direction only. The resulting FID can only be Fourier transformed correctly with trf. The parameter FT_mod is automatically set to the correct value by the rsc command. trf can also be used manipulate the acquisition mode of raw data by Fourier transforming the data with one FT_mod and inverse Fourier transforming them with a different FT_mod. From the resulting data you could create pseudo-raw data (using genfid) with a different acquisition mode than the original raw data. Finally, trf allows to process the data without Fourier transform (FT_mod = no). The following table shows a list of FT_mod values:
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
 
The command trfp works like trf, except that it always works on processed data. If no processed data exist, trfp stops with an error message. 
trfp can be used to perform multiple additive baseline corrections, to remove multiple frequency baseline distortions. This cannot be done with bc or trf because these commands always work on the raw data, i.e. they are not additive. Note that the window multiplication commands (e.g. em, gm, sine etc.) are additive. The same counts for linear prediction (part of ft) and phase correction (pk). 
trf can be used to do a combination of forward and backward prediction. Just run trf with ME_mod = LPfc and then trfp (or ft) with ME_mod = LPbc.
When executed on a 2D or 3D dataset, trf takes up to four arguments: 
trf <row> <procno> n y 
process the specified row and store it under the specified procno. The last two arguments are optional: n prevents changing the display to the output 1D data, y causes a possibly existing data to be overwritten without warning.
When executed on a dataset with 2D or 3D raw data but 1D processed data (usually a result of rsr, rsc or a previous 1D processing command on that 2D or 3D data), trf takes one argument trf <row> process the specified row and store it under the current procno.
trf same process the same row as the previous processing command and store it under the current procno. The same option is automatically used by the AU program macro TRF. When used on a regular 1D dataset (i.e. with 1D raw data), it has no effect.


## INPUT PARAMETERS

Set by the user with edp or by typing si, tdeff etc.: 
SI - size of the processed data
TDeff - number of raw data points to be used for processing
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
  REVERSE - flag indicating to reverse the spectrum
  PKNL - group delay compensation (Avance) or filter correction (A*X)
  STSR - strip start: first output point of strip transform
  STSI - strip size: number of output points of strip transform
PH_mod - phase correction mode
  PHC0 - zero order phase correction value for PH_mod = pk
  PHC1 - first order phase correction value for PH_mod = pk
Set by the acquisition, can be viewed with dpa or by typing s td :
TD - time domain; number of raw data points
### OUTPUT PARAMETERS

Can be viewed with dpp or by typing s tdeff etc.: 
TDeff - number of raw data points that were used for processing
STSR - strip start: first output point of strip transform
STSI - strip size: number of output points of strip transform
NC_proc - intensity scaling factor
YMAX_p - maximum intensity of the processed data
YMIN_p - minimum intensity of the processed data
BYTORDP - data storage order


## INPUT FILES

<dir>/data/<user>/nmr/<name>/<expno>/
fid - raw data (input of trf)
acqus - F2 acquisition status parameters
<dir>/data/<user>/nmr/<name>/<expno>/pdata/<procno>/
1r, 1i - processed 1D data (input of trfp)
proc - processing parameters


## OUTPUT FILES

<dir>/data/<user>/nmr/<name>/<expno>/pdata/<procno>/
1r, 1i - processed 1D data
procs - processing status parameters
auditp.txt - processing audit trail


## USAGE IN AU PROGRAMS

TRF
TRFP


## SEE ALSO

bc, em, gm, ft, ftf
© 2025 Bruker BioSpin GmbH & Co. KG
