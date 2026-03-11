# tf1

**Category:** Commands > Process > Advanced > Special Transforms

## NAME

**tf1** - Process data, including FT, in F1 (3D)


## DESCRIPTION

The command tf1 processes a 3D dataset in the F1 direction. This involves a Fourier transform which transforms time domain data (FID) into frequency domain data (spectrum). Depending on the processing parameters BC_mod, WDW, ME_mod and PH_mod, tf1 also performs baseline correction, window multiplication, linear prediction, and spectrum phase correction. 
The processing steps done by tf1 can be described as follows: 
tf1 only works on data which have already been processed with tf3 and possibly with tf2. It performs the following processing steps: 
1. Baseline correction of the F1 time domain data
2. Each tube is baseline corrected according to BC_mod. This parameter takes the value no, single, quad, spol, qpol sfil or qfil.
3. Linear prediction of the F1 time domain data
4. Linear prediction is done according to ME_mod. This parameter takes the value no, LPfr, LPfc, LPbr, LPbc, LPmifr, LPmifc. Usually, ME_mod = no, which means no prediction is done. Forward prediction in F1 (LPfr, LPfc, LPmifr or LPmifc) can, for example, be used to extend truncated FIDs. Backward prediction (LPbr or LPbc) is not used very often in F1. Linear prediction is only performed for NCOEF > 0. Furthermore, LPBIN and, for backward prediction, TDoff play a role.
5. Window multiplication of the F1 time domain data
6. Each tube is multiplied with a window function according to WDW. This parameter takes the value em, gm, sine, qsine, trap, user, sinc, qsinc, traf or trafs.
7. Fourier transform of the F1 time domain data. Each tube is Fourier transformed according to the F1 processing status parameter MC2. tf1 does not evaluate the processing parameter FT_mod! Instead, it evaluates the F1 processing status parameter MC2, which was set by tf3 to the value of the F1 acquisition status parameter FnMODE (if FnMODE = undefined, tf3 sets processing status MC2 to processing MC2). tf1 stores the corresponding Fourier transform mode as the processing status parameter FT_mod (type dpp).
8. Phase correction of the F1 frequency domain data. 
9. Each column is phase corrected according to PH_mod. This parameter takes the value no, pk, mc or ps. For PH_mod = pk, tf1 applies the values of PHC0 and PHC1. This is only useful if the phase values are known. You can determine them by typing xfb on the 3D data to process a 13 or 12 plane, do a phase correction on the resulting the 2D dataset and store the phase values to 3D.
F1 MC2
Fourier transform mode
status FT_mod
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
 
The F1 processing parameter SI determines the size of the processed data in the F1 direction. This must, however, be set before tf3 is done and cannot be changed after tf3. See tf3 for the role of TD, TDeff and TDoff. 
tf1 can do a strip transform according to the F1 parameters STSR and STSI (see tf3). 
tf1 evaluates the F1 parameter FCOR. The first point of the FIDs is multiplied with the value of FCOR which is a value between 0.0 and 2.0. As such, FCOR allows to control the DC offset of the spectrum.
tf1 evaluates the F1 parameter REVERSE. If REVERSE=TRUE, the spectrum will be reversed in F1, i.e. the first data point becomes the last and the last data point becomes the first.
tf1 evaluates the F1 status parameter MC2. For MC2 ≠ QF, tf1 uses the file 3rrr as input and the files 3rrr and 3rri as output. For MC2 = QF, tf1 uses the files 3rrr and 3iii as input and output. The role of MC2 is described in detail for the 2D processing command xfb.


## INPUT PARAMETERS

### F1 parameters

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
PH_mod - phase correction mode
PHC0 - zero order phase correction value for PH_mod = pk
PHC1 - first order phase correction value for PH_mod = pk
FCOR - first (FID) data point multiplication factor (0.0-2.0, default 0.5)
REVERSE - flag indicating to reverse the spectrum
### F3, F2 and F1 parameters

Set by tf3, can be viewed with dpp or by typing s si, s stsi etc.:
SI - size of the processed data
STSR - strip start: first output point of strip transform
STSI - strip size: number of output points of strip transform
TDeff - number of raw data points to be used for processing
TDoff - first point of the FID used for processing (default 0)
### F1 parameters

Set by the tf3, can be viewed with dpp or by typing s mc2 :
MC2 - Fourier transform mode
### OUTPUT PARAMETERS

### F1 parameters

can be viewed with dpp or by typing s ft_mod :
FT_mod - Fourier transform mode
FTSIZE - Fourier transform size
### F3 parameters

Can be viewed with dpp or by typing s ymax_p etc.:
YMAX_p - maximum intensity of the processed data
YMIN_p - minimum intensity of the processed data
S_DEV - standard deviation of the processed data
NC_proc - intensity scaling factor


## INPUT FILES

<dir>/data/<user>/nmr/<name>/<expno>/
acqu3s - F1 acquisition status parameters
<dir>/data/<user>/nmr/<name>/<expno>/pdata/<procno>/
3rrr - processed 3D data (Fourier transformed in F1) 
3iii - real/imaginary processed data (if MC2 = QF)
proc3 - F1 processing parameters


## OUTPUT FILES

<dir>/data/<user>/nmr/<name>/<expno>/pdata/<procno>/
3rrr - real processed 3D data 
3rir - real/imaginary data (if MC2 ≠ QF)
3iii - real/imaginary processed data (if MC2 = QF)
proc3s - F1 processing status parameters
auditp.txt - processing audit trail


## USAGE IN AU PROGRAMS

TF1(store_imag)
Where store_image can be y or n


## SEE ALSO

tf3, tf2
© 2025 Bruker BioSpin GmbH & Co. KG
