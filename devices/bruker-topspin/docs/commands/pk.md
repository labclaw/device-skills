# pk

**Category:** Commands > Process > Adjust Phase

## NAME

**pk** - Phase correction according to PHC0 / PHC1 (1D)


## DESCRIPTION

The command pk performs a zero and first order phase correction according to user defined phase values. These phase values are read from the processing parameters PHC0 and PHC1. 
The data, consisting of real points R(i) and imaginary points I(i) are phase corrected according to the formula:
R0(i) = R(i) cos[ a(i) ]- I(i) sin[ a(i) ]
I0(i) = I(i) cos[ a(i) ]+ R(i) sin[ a(i) ]
Where:
a(i) = PHC0 + (i-1)PHC1
Where i > 0, R0 and I0 represent the corrected values and PHC0 and PHC1 are processing parameters.
pk does not calculate the phase values but uses the preset values. Therefore, pk is only useful when these values are known. They can be determined, interactively, in Phase correction mode or, automatically, with apk or apks.
pk is typically used in a series of experiments where the first spectrum is corrected with apk and each successive spectrum with pk, using the same values (see for example AU program proc_noe).
pk applies but does not change the processing parameters PHC0 and PHC1 (edp). It does, however, change the corresponding processing status parameters PHC0 and PHC1 (dpp), by adding the applied phase values. 
pk is a part of the composite processing commands efp, fp and gfp.
pk can also be used to perform a phase correction on an FID rather than a spectrum. This is automatically done if you enter pk on a dataset which does not contain processed data. Phase correction on an FID is used prior to Fourier transform to induce a shift in the resulting spectrum. The spectrum is shifted according to the value of PHC1; one real data point to the left for each 360°. A negative value of PHC1 causes a right shift. The points which are cut off on one side of the spectrum are appended on the other side. Note the difference with performing a left shift (ls) or right shift (rs) after Fourier transform. This appends zeroes at the opposite side. If processed data do exist and you still want to do a phase correction on the FID, you can do this with the command trf.
The command pk can also be started from the phase correction dialog box which is opened with ph.


## INPUT PARAMETERS

Set from the ph dialog box, with edp or by typing phc0, phc1 etc.: 
PHC0 - zero order phase correction value (frequency independent) 
PHC1 - first order phase correction value (frequency dependent) 
### OUTPUT PARAMETERS

Can be viewed with dpp or by typing s phc0, s phc1 etc.: 
PHC0 - zero order phase correction value (frequency independent) 
PHC1 - first order phase correction value (frequency dependent)


## INPUT FILES

<dir>/data/<user>/nmr/<name>/<expno>/
fid - raw data (input if no processed data exist)
<dir>/data/<user>/nmr/<name>/<expno>/pdata/<procno>/
1r, 1i - processed 1D data (input if they exist)
proc - processing parameters


## OUTPUT FILES

<dir>/data/<user>/nmr/<name>/<expno>/pdata/<procno>/
1r, 1i - processed 1D data (real, imaginary)
procs - processing status parameters
auditp.txt - processing audit trail


## USAGE IN AU PROGRAMS

PK


## SEE ALSO

mc, ps, apk, apks, apkm, apkf, ph, trf, trfp
© 2025 Bruker BioSpin GmbH & Co. KG
