# ft, ftf

**Category:** Commands > Process > Processing Spectrum

## NAME

**ft** - Fourier transform (1D)

**ftf** - Open the Fourier transform command dialog box (1D, 2D)


## DESCRIPTION

The command ft Fourier transforms a 1D dataset or a row of a dataset with dimension ≥ 2. It can be started from the command line or from the Fourier transform dialog box. The latter is opened with the command ftf 
 
This dialog box offers two options both of which select the ft command for execution.
### Standard Fourier Transform

This option only allows to set the parameter SI, the size of the real spectrum. 
### Advanced Fourier Transform

This option allows to set all FT related parameters. 
Fourier transform is the main step in processing NMR data. The time domain data (FID) which are created by acquisition are transformed into frequency domain data (spectrum). Usually, Fourier transform is preceded by other processing steps like FID baseline correction (bc) and window multiplication (em, gm, etc.) and followed by steps like phase correction (apk) and spectrum baseline correction (abs).
The size of the resulting spectrum is determined by the parameter SI. An FID of TD time domain points is transformed to a spectrum of SI real and SI imaginary data points. A typical value for SI is TD/2. In that case, all points of the FID are used by the Fourier transform and no zero filling is done. 
The size of the spectrum and the number of FID points which are used can be determined in the following ways: 
1. SI > TD/2: the FID is zero filled
2. SI < TD/2: only the first 2*SI points of the FID are used
3. 0 < TDeff < TD: only the first TDeff points of the FID are used
In the latter two cases, the spectrum will contain less information than the FID. Note that the parameter TDoff only plays a role for linear prediction and in 2D and 3D Fourier transform.
You can also perform a so-called strip transform which means that only a certain region of the spectrum is stored. This can be done by setting the parameters STSR and STSI which represent the strip start and strip size, respectively. They can take values between 0 and SI. The processing status parameters STSI and SI are both set to this value. You can check this by entering dpp or clicking the Procpars tab.
The Fourier transform mode depends on the acquisition mode; single, sequential or simultaneous. For this purpose, ft evaluates the acquisition status parameter AQ_mod as shown in the table below: 
AQ_mod
FT_mod
Fourier transform mode
qf
fsr
forward, single channel, real
qsim
fqc
forward, quadrature, complex
qseq
fqr
forward, quadrature, real
DQD
fqc
forward, quadrature, complex
 
Note that ft does not evaluate the processing parameter FT_mod but it does store the Fourier transform mode, as evaluated from the acquisition mode, in the processing status parameter FT_mod. However, the command trf determines the Fourier transform mode from the processing parameter FT_mod and not from the acquisition mode (see trf). 
ft evaluates the parameter FCOR. The first point of the FID is multiplied with FCOR which is a value between 0.0 and 2.0. However, on Avance spectrometers, the FID of digitally filtered data starts with a group delay of which the first points are zero so that the value of FCOR is irrelevant. On A*X data, FCOR allows to control the DC offset of the spectrum.
ft evaluates the parameter PKNL. On A*X spectrometers, PKNL = true causes a nonlinear 5th order phase correction of the raw data. This corrects possible errors caused by nonlinear behaviour of the analog filters. On Avance spectrometers, PKNL must always be set to TRUE. For digitally filtered data, it causes ft to handle the group delay of the FID. For analog data it has no effect.
ft evaluates the parameter REVERSE. If REVERSE = TRUE, the spectrum will be reversed, i.e. the first output data point becomes the last and the last point becomes the first. The same effect is attained by using the command rv after ft.
ft automatically performs an FID baseline correction according to BC_mod.
ft performs linear prediction according to ME_mod. This parameter can take the following values: 
no : no linear prediction
LPfr : forward LP on real data
LPfc : forward LP on complex data
LPbr : backward LP on real data
LPbc : backward LP on complex data
LPmifr : mirror image forward LP on real data
LPmifc : mirror image forward LP on complex data
Forward prediction can, for example, be used to extend truncated FIDs. Backward prediction can be used to improve the initial data points of the FID. ft determines the detection mode (real or complex) from the acquisition status parameter AQ_mod, not from ME_mod. As such, ft does not distinguish between ME_mod = LPfr and ME_mod = LPfc. The same counts for backward prediction. Note that the command trf does determine the detection mode from ME_mod. Linear prediction is only performed for NCOEF > 0. Furthermore, LPBIN and, for backward prediction, TDoff play a role. By default, ME_mod is set to no which means no linear prediction is done.
When executed on a 2D or 3D dataset, ft takes up to four arguments, e.g. ft <row> <procno> y n, process the specified row and store it under the specified procno. The last two arguments are optional: y causes a possibly existing data to be overwritten without warning, n prevents TopSpin from changing to the destination dataset. Note that the oder of the last two arguments, y and n, is irrelevant. 
If you run a command like ft from the command line, make sure that the required parameters are already set. Click the Procpars tab or enter edp to do that.
The ft command can be used on multidimensional data. In that case it automatically recognizes the dimensionality of the data and prompts for the row to be processed and the output procno. It only applies to the acquisition direction. 
The ftf command can be used on 1D and 2D data. It recognizes the data dimensionality and opens a dialog box with the appropriate options and parameters.


## INPUT PARAMETERS

Set from the ftf dialog box, with edp or by typing si, stsr etc.: 
SI - size of the processed data
STSR - strip start: first output point of strip transform
STSI - strip size: number of output points of strip transform
TDeff - number of raw data points to be used for processing
FCOR - first (FID) data point multiplication factor (0.0-2.0, default 0.5)
REVERSE - flag indicating to reverse the spectrum
PKNL - group delay compensation (Avance) or filter correction (A*X)
ME_mod - FID linear prediction mode
NCOEF - number of linear prediction coefficients
LPBIN - number of points for linear prediction
TDoff - number of raw data points predicted for ME_mod = LPb*
Set by the acquisition, can be viewed with dpa or by typing s aq_mod etc.:
AQ_mod - acquisition mode (determines the Fourier transform mode)
TD - time domain; number of raw data points
BYTORDA - byteorder or the raw data
NC - normalization constant
### OUTPUT PARAMETERS

Can be viewed with dpp or by typing s ft_mod, s tdeff etc.:
FT_mod - Fourier transform mode
TDeff - number of raw data points that were used for processing
STSR - strip start: first output point of strip transform
STSI - strip size: number of output points of strip transform
NC_proc - intensity scaling factor
YMAX_p - maximum intensity of the processed data
YMIN_p - minimum intensity of the processed data
BYTORDP - data storage order


## INPUT FILES

<dir>/data/<user>/nmr/<name>/<expno>/
fid - raw data (input if 1r, 1i do not exist or are Fourier transformed)
acqus - acquisition status parameters
<dir>/data/<user>/nmr/<name>/<expno>/pdata/<procno>/
1r, 1i - processed data (input if they exist but are not Fourier transformed)
proc - processing parameters


## OUTPUT FILES

1r, 1i - processed 1D data (real, imaginary)
procs - processing status parameters
auditp.txt - processing audit trail


## USAGE IN AU PROGRAMS

FT


## SEE ALSO

ift, ht, trf, trfp
© 2025 Bruker BioSpin GmbH & Co. KG
