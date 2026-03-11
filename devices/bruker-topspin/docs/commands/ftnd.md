# ftnd

**Category:** Commands > Process > Processing Spectrum

## NAME

**ftnd** - nD processing including Fourier transform (≥ 3D)


## DESCRIPTION

The command ftnd processes nD data performing fid baseline correction, linear prediction, window multiplication, Fourier transform and phase correction. The command automatically recognizes the data dimensionality and handles data of dimension ≥3D. In TopSpin, ftnd has been tested by Bruker on 3D, 4D, 5D and 6Ddata. Note that 3D data can also be processed with the conventional commands tf3, tf2, tf1 and ft3d. 
As an example, ftnd is described here for a 4D dataset. It takes the following three arguments:
<direction> 
the direction(s) to be processed. Allowed values are:
0 : all directions, in the order defined by AQSEQ
4321, 4312, 4231, 4213, 4132, 4123 : all directions in specified order
4, 3, 2, or 1 : F4, F3, F2 or F1, respectively. 
<procno> 
Output procno of the processed data. Optional argument, normally unused. In special cases, however, the data cannot be processed in-place, and must be stored in a different procno. ftnd will then prompt you for an output procno.
dlp 
Delayed linear prediction. Optional argument, only applicable when all directions are processed. This argument ensures that when linear prediction is performed in a certain direction, all other directions are already Fourier transformed (see below).
If the arguments are not specified on the command line, ftnd will normally only prompt you for the direction. The output procno is only prompted for if inplace operation is not possible. 
### Examples

ftnd 0
Process the data in all directions in the order defined by the acquisition status parameter AQSEQ
ftnd 4
Process data in direction F4
ftnd 4312 999
Process the data in all directions, in the order F4-F3-F1-F2 and store the result in procno 999
ftnd 0 dlp
Process the data in all directions, in the order defined by AQSEQ, performing delayed linear prediction according to ME_MOD and NCOEF.
ftnd 4 nc_proc 8
Process data in direction F4, while using NC_proc = 8. Note the value of NC_proc is only relevant on the first processing command, for the acquisition direction. Namely in 4D, the commands ftnd 3, ftnd 2, and ftnd 1 will use the same NC_proc value as the preceding call.
ftnd 4.
Missing arguments are prompted for, except for the dlp argument. Note that for the first argument, the direction, only the allowed directions are displayed, and the next logical direction is suggested. The figure below shows the dialog opened by ftnd on a 4D dataset that has already been processed in F4 and F3.
 
### Extract 1D, 2D or 3D data from 4D, 5D,... processed data.

To view the result of 4D processing, open the dataset (procno) where the processed data are stored and read a 3D-cube, 2D-plane or 1D trace. This can be done with the commands rcb, rpl and rtr, respectively. These commands automatically switch to the destination dataset showing the 3D, 2D or 1D dataset, respectively (see the description of these commands for more information). Furthermore, you can extract positive, negative or sum cube projections with the commands projcbp, projcbn and sumcb, respectively. Similarly, you can extract plane projections with the commands projplp, projpln and sumpl, respectively.
Instead of processing the entire 4D dataset and reading a certain plane or trace, you can also process single 2D-planes or 1D fids of the 4D raw data. To process a plane, just enter xfb, xf2 or xtrf and specify the requested plane axis orientation, plane number and output procno. To process a trace, just enter a 1D processing command like ft or trf and specify the requested fid number and output procno. Obviously, 1D/2D processing commands can also be used to further process or reprocess traces/planes or processed 4D data. For example:
1. Open a 4D dataset
2. ftnd 4 - Perform 4D processing in the F4 direction
3. rpl 34 1 999 - Read F3-F4 plane 1 and store it in procno 999. Note that the plane is stored as a F2-processed 2D dataset. 
4. xf1 - Perform 2D processing in the F1-direction.
### Processing the four directions in separate steps

Normally, ftnd with the argument 0 or one of the arguments 4321, 4312, .. etc. to process all directions. In some cases, you may want to process the different directions in individual steps and perform the sequence ftnd 4, ftnd 3, .. etc. The first direction to be processed must be F4, the other three directions can be processed in any order. Note that every order in which the data are processed in F3, F2 an and F1 gives the same result, unless linear prediction is done (ME_mod and NCOEF ≠ 0) 
### Delayed linear prediction

Linear prediction is a valuable method for improving the resolution of nD data with small TD values and often truncated FIDs. The effect of linear prediction in one direction can, however, be distorted by modulations introduced by other, untransformed, directions. The dlp argument allows to perform linear prediction in a certain direction while all other directions have already been Fourier transformed. Let’s take an example to see how this works. Suppose you have a 4D dataset with acquisition order 4321 (parameter AQSEQ), which you want to processed in all 4 directions including Window Multiplication (WM) and Fourier transform (FT). Furthermore, you want to increase the resolution with linear prediction (LP) in the third (F2) and fourth (F1) direction. As such, you have set the parameters WDW, and, in F2 and F1, ME_mod and NCOEF, to appropriate values. If you use the command ftnd 0 the following happens: 
1. Processing in F4 (WM - FT)
2. Processing in F3 (WM - FT
3. Processing in F2 (LP - WM - FT
4. Processing in F1 (LP - WM - FT
So when linear prediction is done in F2, data have not been Fourier transformed yet in F1, which can cause distortions.
If, however, you use the command ftnd 0 dlp for delayed linear prediction, the following happens:
1. Processing in F4 (WM - FT) 
2. Processing in F3 (WM - FT) 
3. Processing in F2 (FT) 
4. Processing in F1 (LP - WM - FT) 
5. Processing in F2 (IFT - inverse Fourier transform, including Hilbert Transform to create temporary imaginary data)
6. Processing in F2 (LP - WM - FT) 
Now when linear prediction is done in F2, the data are Fourier transformed in F1 (and all other directions). For the F1 direction, linear prediction does not have to be delayed because F1 is the last direction being processed. Note that ftnd also performs fid baseline correction and spectrum phase correction if the parameters BC_mod and PH_mod, respectively, are set.
Delayed linear prediction can also be performed in two steps. The command: 
ftnd 0 dlp (with F2-ME_mod ≠ 0 and NCOEF ≠0)
is equivalent with the command sequence:
1. ftnd 0 (with F2-ME_mod = 0) and WDW = 0
2. lpnd 2 (with F2-ME_mod ≠ 0, NCOEF ≠ 0 and WDW ≠ 0) 
### In-place operation

Normally, ftnd can perform an in-place operation, which means the processed data are stored in the current procno. In special cases, however, in-place operation is not possible and the processed data must be stored in a different procno. ftnd will prompt the user for the output procno. When processing is finished, the display will automatically change to the destination PROCNO. 
Whether or not in-place operation is possible depends on the direction being processed and the zero-filling conditions. In-place operation is done:
1. In the first direction: always
2. In the second direction: always as long as all directions are processed with one command, e.g. with ftnd 0. 
3. In the third, fourth etc. directions: if at least single zero filling (SI ≥ TD and (STSI = 0 or STSI ≥ TD)). 
Note that if a procno is specified on the command line, it is used, i.e. the processed data of the last two directions are stored there.
Restrictions nD processing
The command ftnd has the following restrictions:
1. Raw and processed data have the same dimensionality, i.e. the values of the status parameters PARMODE and PPARMOD must be the same. Note that 2D processing commands like xfb also work on datasets with different raw and processed data dimensionality, e.g. 3D raw and 2D processed data.
2. If dimension > 3 and the acquisition mode (acquisition status parameter FnMODE) is QF in one direction, it must be QF in all directions. In other words, you cannot process mixed single detection/hypercomplex data for dimension > 3.
3. For data of dimension ≥ 5D, only the natural acquisition order (AQSEQ = 0) is supported.
4. Simultaneous echo-antiecho not supported; the acquisition status parameter FnMODE must not be echo-antiecho in more than 1 direction.
Note that the values of parameters which use a predefined list are stored as integers. The first value of the list is always stored as 0, the second value as 1 etc. The table below shows the values of the parameter PH_mod as an example: 
Parameter value
Integer stored in the proc(s) file
no 
0
pk
1
mc
2
ps
3


## INPUT PARAMETERS

### F4, F3, F2 and F1 parameters

Set by the user with edp or by typing si, stsr etc.:
SI - size of the processed data
STSR - strip start: first output point of strip transform
STSI - number of output points of strip transform
TDeff - number of raw data points to be used for processing 
TDoff - first point of the FID used for processing (default 0)
FCOR - first (FID) data point multiplication factor (0.0-2.0, default 0.5)
REVERSE - flag indicating to reverse the spectrum
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
Set by the acquisition, can be viewed with dpa or s aq_mod etc.:
TD - time domain; number of raw data points
### F4 parameters

Set by the user with edp or by typing aqorder, pknl etc.:
AQORDER - Acquisition order
PKNL - group delay compensation (Avance) or filter correction (A*X)
Set by the acquisition, can be viewed with dpa or s aq_mod etc.:
AQ_mod - acquisition mode (determines the status FT_mod)
AQSEQ - acquisition sequence (3-2-1 or 3-1-2)
BYTORDA - byteorder or the raw data
NC - normalization constant
### F3, F2 and F1 parameters

Set by the acquisition, can be viewed with dpa or by typing s fnmode etc.:
FnMODE - Fourier transform mode
### OUTPUT PARAMETERS

### F4, F3, F2 and F1

Can be viewed with dpp or by typing s si, s stsi etc.:
SI - size of the processed data
STSR - strip start: first output point of strip transform
STSI - strip size: number of output points of strip transform
TDeff - number of raw data points that were used for processing 
TDoff - first point of the FID used for processing (default 0)
XDIM - subcube size
FT_mod - Fourier transform mode
FTSIZE - Fourier transform size
### F4 parameters

Can be viewed with dpp or by typing s si, s tdeff etc.:
AQORDER - Acquisition order
YMAX_p - maximum intensity of the processed data
YMIN_p - minimum intensity of the processed data
S_DEV - standard deviation of the processed data
NC_proc - intensity scaling factor
BYTORDP - byte order of the processed data
### F3, F2 and F1 parameters

Can be viewed with dpp or by typing s mc2 etc.:
MC2 - Fourier transform mode


## INPUT FILES

### For 4D data:

<dir>/data/<user>/nmr/<name>/<expno>/
ser - raw data
acqus - F4 acquisition status parameters
acqu2s - F3 acquisition status parameters
acqu3s - F2 acquisition status parameters
acqu4s - F1 acquisition status parameters
<dir>/data/<user>/nmr/<name>/<expno>/pdata/<procno>/
proc - F4 processing parameters
proc2 - F3 processing parameters
proc3 - F2 processing parameters
proc4 - F1 processing parameters
For 3D data proc4s does not exist. For data of dimension n where n ≥ 5 the additional files proc5,...,etc. exist.


## OUTPUT FILES

### For 4D data:

<dir>/data/<user>/nmr/<name>/<expno>/pdata/<procno>/
4rrrr - processed 4D data
procs - F4 processing status parameters
proc2s - F3 processing status parameters
proc3s - F2 processing status parameters
proc4s - F1 processing status parameters
For 3D data, the output data file is 3rrr whereas proc4s does not exist. For data of dimension n where n ≥ 5, processed data files are named nr and ni, e.g. 5r, 5i, 6r, 6i etc. and the additional files proc5s,..., etc. exist.


## SEE ALSO

absnd, lpnd, pknd, projcbp, projcbn, sumcb, projplp, projpln, sumpl
© 2025 Bruker BioSpin GmbH & Co. KG
