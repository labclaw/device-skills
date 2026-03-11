# ft3d

**Category:** Commands > Process > Processing Spectrum

## NAME

**ft3d** - Process data, including FT, in the F3, F2 and F1 direction (3D)


## DESCRIPTION

The command ft3d processes a 3D dataset in all three directions F3, F2 and F1. It is equivalent to the command sequence tf3-tf2-tf1 or tf3-tf1-tf2 (see below). 
ft3d performs a Fourier transform which transforms time domain data (FID) into frequency domain data (spectrum). Depending on the processing parameters BC_mod, WDW, ME_mod and PH_mod, it also performs baseline correction, window multiplication, linear prediction and spectrum phase correction. 
ft3d executes the following processing steps: 
1. Baseline correction
- The time domain data are baseline corrected according to BC_mod. This parameter takes the value no, single, quad, spol, qpol sfil or qfil. 
2. Linear prediction
- Linear prediction is done according to ME_mod. This parameter takes the value no, LPfr, LPfc, LPbr, LPbc, LPmifr or LPmifc. Usually, ME_mod = no, which means no prediction is done. Forward prediction (LPfr, LPfc, LPmifr or LPmifc) can, for example, be used to extend truncated FIDs. Backward prediction (LPbr or LPbc) is usually only done in F3, e.g. improve the initial data points of the FID. Linear prediction is only performed if NCOEF > 0. Furthermore, the parameters LPBIN and, for backward prediction, TDoff are evaluated.
3. Window multiplication
- The time domain data are multiplied with a window function according to WDW. This parameter takes the value em, gm, sine, qsine, trap, user, sinc, qsinc, traf or trafs.
4. Fourier transform
- The time domain data are Fourier transformed in F3 according to the acquisition status parameter AQ_mod (see AQ_mod table below). 
- In F2 and F1, they are Fourier transformed according to the acquisition status parameter FnMODE (if FnMODE = undefined, ft3d evaluates the processing parameter MC2). 
- The Fourier transform mode is stored in the processing status parameter FT_mod. Note that ft3d does not evaluate the processing parameter FT_mod! 
5. Phase correction
- The frequency domain data are phase corrected according to PH_mod. This parameter takes the value no, pk, mc or ps. For PH_mod = pk, ft3d applies the values of PHC0 and PHC1. This is only useful if the phase values are known. You can determine them by typing xfb on the 3D data to process a 23 or 13 plane, do a phase correction on the resulting the 2D dataset and store the phase values to 3D.
status AQ_mod
Fourier transform mode
status FT_mod
qf 
forward, single, real
fsr
qsim
forward, quad, complex
fqc
qseq 
forward, quad, real
fqr 
DQD
forward, quad, complex
fqc
 
 
 
FnMODE
Fourier transform mode
status FT_mod
undefined
according to MC2
 
QF 
forward, quad, real
fqc
QSEQ
forward, quad, real
fqr
TPPI 
forward, single, real
fsr
States
forward, quad, complex
fqc
States-TPPI
forward, single, complex
fsc
Echo-AntiEcho
forward, quad, complex
fqc
 
The size of the processed data is determined by the processing parameter SI; SI real and SI imaginary points are created. A typical value for SI is TD/2 in which case, all raw data points are used and no zero filling is done. In fact, several parameters control the number of input and output data points, for example:
1. SI > TD/2: the raw data are zero filled before the Fourier transform
2. SI < TD/2: only the first 2*SI raw data points are used
3. 0 < TDeff < TD: only the first TDeff raw data points are used
4. 0 < TDoff < TD: the first TDoff raw data points are cut off and TDoff zeroes are appended at the end 
5. TDoff < 0: -TDoff zeroes are prepended at the beginning. Note that:
1. for SI < (TD-TDoff)/2 raw data are cut off at the end
2. for DIGMOD=digital, the zeroes would be prepended to the group delay which does not make sense. You can avoid that by converting the raw data with convdta before you process them.
6. 0 < STSR < SI: only the processed data between STSR and STSR+STSI are stored (if STSI = 0, STSR is ignored and SI points are stored)
7. 0 < STSI < SI: only the processed data between STSR and STSR+STSI are stored. 
Note that only in the first case the processed data contain the total information of the raw data. In all other cases, information is lost. Before you run ft3d, you must set the processing parameter SI in all three directions F3, F2 and F1.
ft3d evaluates the acquisition status parameter AQSEQ, which defines the storage order of the raw data. Raw data can be stored in the order 3-2-1 or 3-1-2. Processed data, however, are always stored in the order 3-2-1. For AQSEQ=321, ft3d is equivalent to the command sequence tf3-tf2-tf1. For AQSEQ=312, it is equivalent to tf3-tf1-tf2. Note, however, that for magnitude or power data, the processing order is independent of AQSEQ. ft3d then behave as follows: 
1. for F1-PH_mod = mc / ps, tf3-tf2-tf1 is executed
2. for F2-PH_mod = mc / ps, tf3-tf1-tf2 is executed
Note that PH_mod = mc/ps is only allowed in either F2 or F1, not in both and also not in F3. 
ft3d evaluates the processing parameter FCOR. The first point of the FIDs is multiplied with the value of FCOR which lies between 0.0 and 2.0. For digitally filtered Avance data, FCOR has no effect in F3 because the first point is part of the group delay and, as such, is zero. In that case, it only plays a role in the F2 and F1 direction. However, on A*X data or Avance data measured with DIGMOD = analog, there is no group delay and FCOR also plays a role in F3.
ft3d evaluates the processing parameter PKNL. On A*X spectrometers, PKNL = true causes a nonlinear 5th order phase correction of the raw data. This corrects possible errors caused by nonlinear behavior of the analog filters. On Avance spectrometers, PKNL must always be set to TRUE. For digitally filtered data, it causes ft3d to handle the group delay of the FID. For analog data it has no effect.
ft3d evaluates the processing parameter REVERSE. If REVERSE = TRUE, the spectrum will be reversed, i.e. the first data point becomes the last and the last data point becomes the first.
ft3d can be used with the following command line arguments:
n 
ft3d will not store the imaginary data. Imaginary data are only needed for phase correction in last processed direction. If the phase values are already known and PHC0 and PHC1 have been set accordingly, ft3d will perform phase correction and there is no need to store the imaginary data. This will save processing time and disk space. If you still need to do a phase correction after ft3d, you can create imaginary data from the real data with a Hilbert transform (see tht1). Note that if the n option is omitted, imaginary data are only stored in the last processed direction.
21 or 12 
ft3d 21 is equivalent to the command sequence tf3-tf2-tf1, whereas ft3d 12 is equivalent to tf3-tf1-tf2.
xdim 
3D spectra are stored in the so-called subcube format. The size of the subcubes is calculated by ft3d and depends on the size of the spectrum and the available memory. The option xdim allows to use predefined subcube sizes. It causes ft3d to interpret the F3, F2 and F1 processing parameter XDIM which can be set by entering xdim on the command line. Note that XDIM = 0, is evaluated as XDIM = SI. The used subcube sizes, whether predefined or calculated, are stored as the F3, F2 and F1 processing status parameter XDIM and can be viewed with dpp. Predefining subcube sizes is, for example, used to read the processed data with third party software which cannot interpret the processing status parameter XDIM.
big/little 
ft3d stores the data in the data storage order of the computer it runs on, e.g. little endian on Windows PCs. Note that TopSpin’s predecessor XWIN-NMR on SGI UNIX workstations stores data in big endian. The storage order is stored in the processing status parameter BYTORDP (type s bytordp). If, however, you want to read the processed data with third party software which cannot interpret this parameter, you can use the big/little option to predefine the storage order.
p<du> 
The option p allows to store the processed data on a different top level data directory, typically a different disk. The rest of the data directory path is the same as that of the raw data. If the specified top level directory does not exist, it will be created.
Normally, ft3d stores the entire spectral region as determined by the spectral width. However, you can do a so-called strip transform which means that only a certain region of the spectrum is stored. This can be done by setting the parameters STSR and STSI which represent the strip start and strip size, respectively. They both can take a value between 0 and SI. The values which are used can be a little different. STSI is always rounded to the next higher multiple of 16. Furthermore, when the data are stored in subcube format (see below), STSI is rounded to the next multiple of the subcube size. Type dpp to check this; if XDIM is smaller than SI, then the data are stored in subcube format and STSI is a multiple of XDIM.
ft3d stores the data in subcube format. It automatically calculates the subcube sizes such that one row (F3) of subcubes fits in the available memory. Furthermore, one column (F2) and one tube (F1) of subcubes must fit in the available memory. The calculated subcube sizes are stored in the processing status parameter XDIM (type dpp). The alignment of the data points subcube format is the extension of the alignment in a 2D dataset as it is shown in 2D data in 8*4 submatrix storage format. The storage handling is completely transparent to the user and is only of interest when the data are interpreted by third party software.


## INPUT PARAMETERS

### F3, F2 and F1 parameters

Set by the acquisition, can be viewed with dpa or s td:
TD - time domain; number of raw data points
 
Set by the user with edp or by typing si, stsr etc.:
SI - size of the processed data
STSR - strip start: first output point of strip transform
STSI - number of output points of strip transform
TDeff - number of raw data points to be used for processing 
TDoff - first point of the FID used for processing (default 0)
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
### F3 parameters

Set by the acquisition, can be viewed with dpa or s aq_mod etc.:
AQ_mod - acquisition mode (determines the status FT_mod)
AQSEQ - acquisition sequence (3-2-1 or 3-1-2)
BYTORDA - byteorder or the raw data
NC - normalization constant
### F2 and F1 parameters

Set by the acquisition, can be viewed with dpa or by typing s fnmode:
FnMODE - Fourier transform mode
### OUTPUT PARAMETERS

### F3, F2 and F1 parameters

Can be viewed with dpp or by typing s si, s stsr etc.:
SI - size of the processed data
STSR - strip start: first output point of strip transform 
STSI - strip size: number of output points of strip transform
FTSIZE - Fourier transform size
TDeff - number of raw data points that were used for processing 
TDoff - first point of the FID used for processing (default 0)
XDIM - subcube size
FT_mod - Fourier transform mode
### F3 parameters

Can be viewed with dpp or by typing s ymax_p etc.:
YMAX_p - maximum intensity of the processed data
YMIN_p - minimum intensity of the processed data
S_DEV - standard deviation of the processed data
NC_proc - intensity scaling factor
BYTORDP - byte order of the processed data
### F2 and F1 parameters

Can be viewed with dpp or by typing s mc2:
MC2 - Fourier transform mode


## INPUT FILES

<dir>/data/<user>/nmr/<name>/<expno>/
ser - raw data
acqus - F3 acquisition status parameters
acqu2s - F2 acquisition status parameters
acqu3s - F1 acquisition status parameters
<dir>/data/<user>/nmr/<name>/<expno>/pdata/<procno>/
proc - F3 processing parameters
proc2 - F2 processing parameters
proc3 - F1 processing parameters


## OUTPUT FILES

<dir>/data/<user>/nmr/<name>/<expno>/pdata/<procno>/
3rrr - real processed 3D data 
3rri - real/imaginary processed data (for AQSEQ =321, FnMODE ≠ QF)
3rir - real/imaginary processed data (for AQSEQ =312, FnMODE ≠ QF)
3iii - imaginary processed data (for FnMODE = QF)
procs - F3 processing status parameters
proc2s - F2 processing status parameters
proc3s - F1 processing status parameters
auditp.txt - processing audit trail


## USAGE IN AU PROGRAMS

FT3D


## SEE ALSO

tf3, tf2, tf1
© 2025 Bruker BioSpin GmbH & Co. KG
