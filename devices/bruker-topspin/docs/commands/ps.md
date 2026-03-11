# ps

**Category:** Commands > Process > Adjust Phase

## NAME

**ps** - Calculate power spectrum (1D)


## DESCRIPTION

The command ps calculates the power spectrum of the 1D current dataset, replacing the intensity of each data point i according to the formula:
PS(i) = R(i)2 + I(I)2
Where R and I are the real and imaginary part of the spectrum, respectively. If no processed input data exist, ps works on the raw data. The result is always stored as the real processed data.
ps can also be started from the phase correction dialog box which is opened with ph.
If ps is typed on a 2D or 3D spectrum, the following warning message is displayed. Enter the appropriate values.


## INPUT FILES

<dir>/data/<user>/nmr/<name>/<expno>/
fid - raw data (input if no processed data exist)
<dir>/data/<user>/nmr/<name>/<expno>/pdata/<procno>/
1r, 1i - processed 1D data (real, imaginary)


## OUTPUT FILES

<dir>/data/<user>/nmr/<name>/<expno>/pdata/<procno>/
1r, 1i - processed 1D data (real, imaginary)
auditp.txt - processing audit trail


## USAGE IN AU PROGRAMS

PS


## SEE ALSO

mc, apk, apks, apkm, apkf, ph, trf, trfp
© 2025 Bruker BioSpin GmbH & Co. KG
