# sref, cal

**Category:** Commands > Process > Calibrate Axis

## NAME

**sref** - Calibrate the spectrum; set the TMS signal to 0 ppm (1D, 2D)

**cal** - Open axis calibration commands dialog box (1D, 2D)


## DESCRIPTION

Spectrum calibration can be started from the command line with sref or from the calibration dialog box which is opened with the cal command.
 
This dialog box offers two options, one for manual and one for automatic calibration.
### Manual calibration

This option selects the .cal command for execution. This is equivalent to clicking  in the toolbar and switches to interactive calibration mode. Click inside the data window at the reference peak, enter the frequency value in the appearing dialog box and click OK.
### Automatic calibration

This option selects the sref command for execution. It calibrates the spectrum by setting the TMS signal of a spectrum to exactly 0 ppm. It works on 1D and 2D spectra.
sref makes use of the lock table. This must be set up once after installing TopSpin with the command edlock.
On 1D spectra, sref involves three steps which are discussed below. 
During the first step sref sets the value of the processing parameter SF according to the formula:
SF=BF1/(1.0+RShift * 1e-6) 
Where RShift is taken from the edlock table and BF1 is an acquisition status parameter. Changing SF automatically changes the processing parameters SR, the spectral reference, and OFFSET, the ppm value of the first data point, according to the following relations:
1. SR = SF - BF1 - where BF1 is an acquisition status parameter.
2. OFFSET = (SFO1/SF-1) * 1.0e6 + 0.5 * SW * SFO1/SF - where SW and SFO1 are acquisition status parameters
Actually, the relation for OFFSET depends on the acquisition mode. When the acquisition status parameter AQ_mod is qsim, qseq or DQD, which is usually the case, the above relation count. When AQ_mod is qf, the relation OFFSET = (SFO1/SF-1) * 1.0e6 is used.
sref then calculates which data point (between 0 and SI) in your spectrum corresponds to the ppm value Ref. from the edlock table. This data point will be used in the second step. The first step is independent of a reference substance.
During the second step, sref scans a region around the data point found in the first step for a peak. It will normally find the signal of the reference substance. The width of the scanned region is defined by the parameter Width in edlock table, so this region is Ref. +/- 0.5*Width ppm. This step is necessary because the lock substance (solvent) will not always resonate at exactly the same position relative to the reference shift. The absolute chemical shift of the lock substance (solvent) differs because of differences in susceptibility, temperature, concentration or pH, for instance.
The third step depends on whether or not a peak was found in the second step. If a peak was found, sref determines the interpolated peak top and shifts its ppm value to the  ref. value from the edlock table. The processing parameters OFFSET, SF and SR are changed accordingly. As such, the result of the default (step 1) is slightly corrected in order to set the peak of the reference substance exactly to 0. You can check this by putting the cursor on this peak. If no peak was found, you will get the message: sref: no peak found default calibration done. The result of the default calibration (step 1) is stored without any further correction.
The three cases below show the calibration of a 1H, 13C and 31P spectrum with C6D6 as a solvent. The following table shows the corresponding entry in the edlock table:
Solvent
Field
Lockpower
Nucleus
Distance
[ppm]
Ref.
[ppm]
Width
[ppm]
Rshift
[ppm]
C6D6
-150
-15.0
 
 
 
 
 
 
 
 
1H
7.28
0.0
0.5
0.000
 
 
 
2H
7.28
0.0
0.5
0.000
 
 
 
13C
128.0
0.0
5.0
0.220
 
 
 
31P
0.00
10.5
5.0
13.356
 
Case #1 - Calibration of a 1H spectrum: A spectrum was acquired while being locked on C6D6. sref will do a default calibration and look for a signal at 0.0 ppm ( Ref.) in a window of +/- 0.25 ppm. If a peak is found, its chemical shift will be set to 0 ppm. 
Case #2 - Calibration of a 13C spectrum: A spectrum was acquired while being locked on C6D6. sref will do a default calibration and look for a signal at 0.0 ppm ( Ref.) in a window of +/- 2.5 ppm. If a peak is found, its chemical shift will be set to 0 ppm. 
Case #3 - Calibration of a 31P spectrum: A spectrum was acquired while being locked on C6D6. sref will do a default calibration and look for a signal at 10.5 ppm ( Ref.) in a window of +/- 2.5 ppm. If a peak is found, its chemical shift will be set to exactly 10.5 ppm.
On 2D spectra, sref calibrates the F2 and F1 direction and this involves the same steps as described above for 1D spectra.
Please note that the purpose of RShift is the following: 
1. If TMS (or any other reference substance) is found, the value is ignored. 
2. If there is no TMS (or any other reference substance), than sref sets SR to 0, which basically makes BF1 = SF. This is normally pragmatic, but in special cases it is necessary to enter a different value, in order to get a useful resulting chemical shift. Entering a value here will correct the chemical shift by the amount specified.


## INPUT PARAMETERS

Set by the acquisition, can be viewed with dpa or by typing s solvent etc.: 
SOLVENT - the solvent of the sample 
INSTRUM - configuration name (entered during cf) of the spectrometer
LOCNUC - lock nucleus
SFO1 - spectral frequency
NUC1 - measured nucleus
SW - sweep width
### OUTPUT PARAMETERS

Processing parameters which can be viewed with edp
Processing status parameters which can be viewed with dpp
SF - spectral reference frequency
OFFSET - the ppm value of the first data point of the spectrum
SR - spectral reference


## INPUT FILES

<tshome>/conf/instr/<instrum>/
2Hlock - edlock table for 2H locked samples
19Flock - edlock table for 19F locked samples


## OUTPUT FILES

<dir>/data/<user>/nmr/<name>/<expno>/pdata/<procno>/
proc - processing parameters
procs - processing status parameters


## USAGE IN AU PROGRAMS

SREF
© 2025 Bruker BioSpin GmbH & Co. KG
