# xfb, ftf

**Category:** Commands > Process > Processing Spectrum

## NAME

**xfb** - Process data, including FT, in F2 and F1 (2D)

**ftf** - Open the Fourier transform command dialog box (1D, 2D)


## DESCRIPTION

The command xfb processes a 2D dataset or a plane of a dataset with dimension ≥ 3. It can be started from the command line or from the Fourier transform dialog box. The latter is opened with the command ftf. 
 
The ftf command recognizes the data dimensionality and opens a dialog box with the appropriate options and parameters. For 2D data, two options appear, both of which select the xfb command for execution, provided the F2 and F1 direction are both enabled.
Standard Fourier transform
This option only allows to set the parameter SI, the size of the real spectrum. 
Advanced Fourier transform
This option allows to set all Fourier transform related parameters. 
xfb Fourier transforms time domain data into frequency domain data. Depending on the processing parameters BC_mod, WDW, ME_mod and PH_mod, xfb also performs baseline correction, window multiplication, linear prediction and spectrum phase correction.
The processing steps done by xfb can be described as follows: 
1. Baseline correction of the 2D time domain data. Each row and/or column is baseline corrected according to BC_mod. This parameter takes the value no, single, quad, spol, qpol sfil or qfil.
2. Linear prediction of the 2D time domain data. Linear prediction is done according to ME_mod. This parameter takes the value no, LPfr, LPfc, LPbr, LPbc, LPmifr or LPmifc. Usually, ME_mod = no, which means no prediction is done. Forward prediction (LPfr, LPfc, LPmifr or LPmifc) can, for example, be used to extend truncated FIDs. Backward prediction (LPbr or LPbc) can be used to improve the initial data points of the FID. Linear prediction is only performed for NCOEF > 0. Furthermore, LPBIN and, for backward prediction, TDoff play a role.
3. Window multiplication of the 2D time domain data. Each row and/or column is multiplied with a window function according to WDW. This parameter takes the value em, gm, sine, qsine, trap, user, sinc, qsinc, traf or trafs.
4. Fourier transform of the 2D time domain data. Each row is Fourier transformed according to the acquisition status parameter AQ_mod as shown in the table below. Each column (F1) is Fourier transformed according to the acquisition status parameter FnMODE as shown in the table below. xfb does not evaluate the processing parameter FT_mod! However, it stores the Fourier transform mode as it was evaluated from AQ_mod (F2) or FnMODE (F1) in the processing status parameter FT_mod. If, for some reason, you want to Fourier transform a spectrum with a different mode, you can set the processing parameter FT_mod (with edp) and use the command xtrf (see xtrf). 
5. Phase correction of the 2D spectrum according to PH_mod. This parameter takes the value no, pk, mc or ps. For PH_mod = pk, xfb applies the values of PHC0 and PHC1. This is only useful if the phase values are known. If they are not, you can do an interactive phase correction in Phase correction mode after xfb has finished.
F2 AQ_mod
Fourier transform mode
F2 status FT_mod
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
F1 FnMODE
Fourier transform mode
F1 status FT_mod
QF 
forward, quad, complex
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
4. 0 < TDoff < TD: the first TDoff raw data points are cut off at the beginning and TDoff zeroes are appended at the end (corresponds to left shift).
5. TDoff < 0: -TDoff zeroes are prepended at the beginning. Note that:
1. for SI < (TD-TDoff)/2 raw data are cut off at the end
2. for DIGMOD=digital, the zeroes would be prepended to the group delay which does not make sense. You can avoid that by converting the raw data with convdta before you process them.
6. 0 < STSR < SI: only the processed data between STSR and STSR+STSI are stored (if STSI = 0, STSR is ignored and SI points are stored)
7. 0 < STSI < SI: only the processed data between STSR and STSR+STSI are stored.
### NOTE

Note that only in the first case the processed data contain the total information of the raw data. In all other cases, information is lost.
xfb performs a quad spike correction, which means that the central data point of the spectrum is replaced by the average of the neighbouring data points in the F1 direction. Note that the quad spike correction is also done if you process the data with the sequence xf2 - xf1.
xfb evaluates the parameter FCOR. The first point of the FIDs is multiplied with the value of FCOR which lies between 0.0 and 2.0. For digitally filtered Avance data, FCOR is only used in the F1 direction. In F2, it has no effect because the first point is part of the group delay and, as such, is zero. However, A*X data or Avance data measured with DIGMOD = analog, FCOR is used in F1 and F2.
xfb evaluates the F2 parameter PKNL. On A*X spectrometers, PKNL = true causes a non linear 5th order phase correction of the raw data. This corrects possible errors caused by non linear behaviour of the analog filters. On Avance spectrometers, PKNL must always be set to TRUE. For digitally filtered data, it causes xfb to handle the group delay of the FID. For analog data it has no effect.
xfb evaluates the F2 and F1 parameter REVERSE. If REVERSE = TRUE, the spectrum will be reversed in the corresponding direction, i.e. the first data point becomes the last and the last data point becomes the first. The same effect can be obtained with the commands rev2 and/or rev1 after xfb.
USAGE:
xfb is normally used without options. There are, however, several options available:
1. n 
1. xfb normally stores real and imaginary processed data. However, the imaginary data are only needed for phase correction. If the parameters PHC0 and PHC1 are set correctly, then you don’t need to store the imaginary data. The option n allows to do that. This will save processing time and disk space. If you still want to do a phase correction, you can create imaginary data from the real data with a Hilbert transform (see xht2 and xht1).
2. nc_proc value 
1. xfb scales the data such that, i.e. the highest intensity of the spectrum lies between 228 and 229. The intensity scaling factor is stored in the processing status parameter NC_proc and can be viewed with dpp. The option nc_proc causes xfb to use a specific scaling factor. However, you can only scale down the data by entering a greater (more positive) value than the one xfb would use without this option. If you enter a smaller (more negative) value, the option will be ignored to prevent data overflow. The option nc_proc last causes xfb to use the current value of the status processing parameter NC_proc, i.e. the value set by the previous processing step on this dataset. 
3. raw/proc 
1. xfb works on raw data if no processed data exist or if processed data exist and have been Fourier transformed in F2 and/or F1. One of them is usually true, i.e. the data have not been processed yet or they have been processed, for example with xfb. If, however, the data have been processed with xtrf with FT_mod = no, they are not Fourier transformed and a subsequent xfb will work on the processed data. The raw option causes xfb to work on the raw data, no matter what. The proc option causes xfb to work on the processed data. If these do not exist or are Fourier transformed, the command stops and displays an error message. In other words, the option proc prevents xfb to work on raw data. 
4. big/little 
1. xfb stores the data in the data byte order (big or little endian) of the computer it runs on e.g. little endian on Windows PCs. Note that TopSpin’s predecessor XWIN-NMR on SGI UNIX workstations stores data in big endian. The byte order is stored in the processing status parameter BYTORDP which can be viewed with s bytordp. The option big or little allows to predefine the byte order. This, for example, is used to read processed data with third party software which cannot interpret BYTORDP. This option is only evaluated when xfb works on the raw data.
5. xdim 
1. Large 2D spectra are stored in the so-called submatrix format. The size of the submatrices are calculated by xfb and depend on the size of the spectrum and the available memory. The option xdim allows to use predefined submatrix sizes. It causes xfb to interpret the F2 and F1 processing parameter XDIM which can be set by entering xdim on the command line. The used submatrix sizes, whether predefined or calculated, are stored as the F2 and F1 processing status parameter XDIM and can be viewed with dpp. Predefining submatrix sizes is, for example, used to read the processed data with third party software which cannot interpret the processing status parameter XDIM. This option is only evaluated when xfb works on the raw data.
Normally, xfb stores the entire spectral region as determined by the spectral width. You can, however, do a so-called strip transform which means that only a certain region of the spectrum is stored. This can be done by setting the parameters STSR and STSI which represent the strip start and strip size, respectively. They both can take a value between 0 and SI. The values which are actually used can be a little different. STSI is always rounded to the next multiple of 16. Furthermore, when the data are stored in submatrix format (see below), STSI is rounded to the next higher multiple of the submatrix size. Type dpp to check this; if XDIM is smaller than SI, then the data are stored in submatrix format and STSI is a multiple of XDIM.
Depending on size of the processed data and the available computer memory, xfb stores the data in sequential or submatrix format. Sequential format is used when the entire dataset fits in memory, otherwise submatrix format is used. xfb automatically calculates the submatrix sizes such that one row (F2) of submatrices fits in the available memory. The calculated submatrix sizes are stored in the processing status parameter XDIM (type dpp). The next two tables show the alignment of the data points for sequential and submatrix format, respectively. This example shows a dataset with the following sizes: F2 SI = 16, F1 SI = 16, F2 XDIM = 8, F1 XDIM = 4. The storage handling is completely transparent to the user and is only of interest when the data are interpreted by third party software.2D data in sequential storage format
 2D data in 8*4 submatrix storage format
 
As can be seen in the second table F1 FnMODE of this chapter, the acquisition mode in F1 (FnMODE) determines the Fourier transform mode. Furthermore, FnMODE determines the data storage mode. The description below demonstrates the difference in data storage between a data set with FnMODE = QF and one with FnMODE ≠ QF.
### FnMODE = QF

xfb performs complex (two-quadrant) processing. In F2 the data are acquired phase sensitive, in F1 non-phase sensitive. In the example below, the following parameter settings are used:
  In F2: TD = 8, SI is 4
  In F1: TD = 2, SI = 2 
Furthermore, the following notation is used for individual data points:
  rncm : point n of FID m. This point is real in F2 and complex in F1
  incm : point n of FID m. This point is imaginary in F2 and complex in F1 
### Input F2 processing (raw data)

For F2 processing, r1c1 i1c1 is the first complex input point, r2c1 i2c1 the second etc.
### Output F2 processing = Input F1 processing

Below, the F1 input data are simply redisplayed in vertical order, with the first complex input point in bold. 
### Input F1 processing

### Output F1 processing

### FnMODE ≠ QF

xfb performs hypercomplex (four-quadrant) processing. Both in F2 and F1, the data are acquired phase sensitive. In the example below, the following parameters settings are used:
  In F2: TD = 8, SI is 4
  In F1: TD = 4, SI = 2 
Furthermore, the following notation is used for individual data points:
1. rnrm : point n of FID m. This point is real in F2 and F1
2. inrm : point n of FID m. This point is imaginary in F2 and real in F1
3. rnim: point n of FID m. This point is real in F2 and imaginary in F1
4. inim : point n of FID m. This point is imaginary in F2 and F1
### Input F2 processing (raw data)

For F2 processing, r1r1 i1r1 is the first hypercomplex input data point, r2r1 i2r1 the second etc. Output F2 processing = Input F1 processing
Below, the F1 input data are simply redisplayed, with the first F1 complex input points in bold. 
### Input F1 processing

### Output F1 processing

### FnMODE = Echo-Antiecho

xfb performs hypercomplex (four-quadrant) processing. Both in F2 and F1, the data are acquired phase sensitive. In the example below, the following parameters settings are used:
  In F2: TD = 8, SI is 4
  In F1: TD = 4, SI = 2 
Furthermore, the following notation is used for individual data points:
1. rnrm : point n of FID m. This point is real in F2 and F1
2. inrm : point n of FID m. This point is imaginary in F2 and real in F1
3. rnim: point n of FID m. This point is real in F2 and imaginary in F1
4. inim : point n of FID m. This point is imaginary in F2 and F1
### Input F2 processing (raw data)

For F2 processing, r1r1 i1r1 is the first hyper complex input data point, r2r1 i2r1 the second etc.
### Output F2 processing = Input F1 processing

Below, the F1 input data are simply redisplayed, with the first F1 complex input points in bold.
### Input F1 processing

### Output F1 processing

Note that:
1. For FnMODE ≠ QF, zero filling once in F1 is done when SI = TD. For FnMODE = QF, zero filling once in F1 is done when SI = 2*TD. 
2. FnMODE = QF is normally used on magnitude or power data. For this purpose, the F1 processing parameter PH_mod must be set to MC or PS, respectively. Note that in these cases, no imaginary data are stored after F1 processing.
3. FnMODE = Echo-Antiecho is equivalent to FnMODE = States, except that two consecutive FIDs (rows of the 2D raw data) are linearly combined according to the following rules: 
1. re0 = -im1 - im0
2. im0 = re1 + re0
3. re1 = re1 - re0
4. im1 = im1 - im0
4. xfb n does not store imaginary data after F1 processing.
### 2D PROCESSING OF 3D DATA

xfb can also be used to process one 2D plane of a 3D spectrum. This can be a plane in the F3-F2 or in the F3-F1 direction. The output 2D data are stored in a separate procno. When the current dataset is a 3D, xfb will prompt you for the plane axis direction, the plane number, the output procno and, if applicable, for the permission to overwrite existing data. Alternatively, you can enter this information as arguments on the command line, for example: 
  xfb s23 17 2 y 
Will read the F3-F2 plane number 17 and store it under procno 2, overwriting possibly existing data. Furthermore, you can use the nodisp argument to prevent opening/displaying the destination dataset, e.g.:
  xfb s23 17 2 y nodisp 
For 2D processing of 3D echo-antiecho (EA) data the option eao is available. This option ensures EA calculation when:
1. the 3D raw data are EA in either F2 or F1 (the acquisition status parameter FnMODE = Echo-Antiecho in F2 or F1, respectively)
2. the processed plane does not include the EA direction
For example, to process F2-F3 plane 17 of a 3D dataset which is EA in F1, enter:
  xfb eao s23 17 2 y 
If you omit the eao option, the plane is still processed but no EA calculation is done. Using the eao option allows to determine the correct phase values for EA data or compare the processed plane with a plane extracted from a 3D processed data. Note that if the processed plane includes the EA direction, or if the 3D data are not EA in any direction, the option eao has no effect.
When executed on a dataset with 3D raw data but 2D processed data (usually a result of a previous 2D processing command on that 3D dataset), xfb takes one argument:
  xfb <plane> 
Process the specified plane and store it under the current procno.
  xfb same 
Process the same plane as the previous processing command and store it under the current procno. The same option is automatically used by the AU program macro XFB. When used on a regular 2D dataset (i.e. with 2D raw data), it has no effect.


## INPUT PARAMETERS

F2 and F1 parameters
Set from the ftf dialog box, with edp or by typing bc_mod, bcfw etc.
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
SI - size of the processed data
STSR - strip start: first output point of strip transform
STSI - strip size: number of output points of strip transform
TDeff - number of raw data points to be used for processing 
TDoff - first point of the FID used for processing (default 0)
FCOR - first (FID) data point multiplication factor (0.0-2.0, default 0.5)
REVERSE - flag indicating to reverse the spectrum
XDIM - submatrix size (only used for the command xfb xdim)
Set by the acquisition, can be viewed with dpa or by typing s td :
TD - time domain; number of raw data points
F2 parameters
Set from the ftf dialog box, with edp or by typing pknl :
PKNL - group delay compensation (Avance) or filter correction (A*X)
Set by the acquisition, can be viewed with dpa or by typing s aq_mod.:
AQ_mod - acquisition mode (determines the Fourier transform mode)
BYTORDA - byteorder or the raw data
NC - normalization constant
F1 parameters
Set by the acquisition, can be viewed with dpa or by typing s fnmode :
FnMODE - F1 Acquisition transform mode
Set by the user with edp or by typing mc2 :
MC2 - FT mode in F1 (only used if F1-FnMODE = undefined)
### OUTPUT PARAMETERS

F2 and F1 parameters
Can be viewed with dpp or by typing s si, s tdeff etc.:
SI - size of the processed data
TDeff - number of raw data points that were used for processing
FTSIZE - Fourier transform size
STSR - strip start: first output point of strip transform 
STSI - strip size: number of output points of strip transform
XDIM - submatrix size
FT_mod - Fourier transform mode
F2 parameters
Can be viewed with dpp or by typing s ymax_p, s ymin_p etc.:
YMAX_p - maximum intensity of the processed data
YMIN_p - minimum intensity of the processed data
S_DEV - standard deviation of the processed data
NC_proc - intensity scaling factor
BYTORDP - byte order of the processed data


## INPUT FILES

<dir>/data/<user>/nmr/<name>/<expno>/
  ser - raw data (input if 2rr does not exit or is Fourier transformed)
<dir>/data/<user>/nmr/<name>/<expno>/pdata/<procno>/
  2rr - real processed 2D data (input if it exists but is not Fourier transformed)
  proc - F2 processing parameters
  proc2 - F1 processing parameters
  acqus - F2 acquisition status parameters
  acqu2s - F1 acquisition status parameters
### NOTE

Note that if 2rr is input, then 2ir and 2ri can also be input, depending on the processing status of the data.


## OUTPUT FILES

<dir>/data/<user>/nmr/<name>/<expno>/pdata/<procno>/
For FnMODE  QF:
  2rr - real processed 2D data 
  2ir - second quadrant imaginary processed data 
  2ri - third quadrant imaginary processed data 
  2ii - fourth quadrant imaginary processed data
For FnMODE = QF:
  2rr - real processed 2D data 
  2ii - second quadrant imaginary processed data
For all values of FnMODE:
  procs - F2 processing status parameters
  proc2s - F1 processing status parameters
  auditp.txt - processing audit trail


## USAGE IN AU PROGRAMS

XFB
If you want to use XFB with an option, you can do that with XCMD, e.g.
XCMD("xfb raw")


## SEE ALSO

xf1, xf2, xfbm, xf2m, xf1m, xfbp, xf2p, xf1p, xfbps, xf2ps, xf1ps, xtrf, xtrf2
© 2025 Bruker BioSpin GmbH & Co. KG
