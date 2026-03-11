# mc

**Category:** Commands > Process > Adjust Phase

## NAME

**mc** - Magnitude calculation (1D)


## DESCRIPTION

The command mc calculates the magnitude spectrum of a 1D dataset. The intensity of each point i is replaced by its absolute value according to the formula:

Where R and I are the real and imaginary part of the spectrum, respectively. If no processed input data exist, mc works on the raw data.
mc can also be started from the phase correction dialog box which is opened with ph.


## INPUT FILES

<dir>/data/<user>/nmr/<name>/<expno>/
fid - raw 1D data (input if 1r, 1i do not exist)
<dir>/data/<user>/nmr/<name>/<expno>/pdata/<procno>/
1r, 1i - processed 1D data (input if they exist)


## OUTPUT FILES

<dir>/data/<user>/nmr/<name>/<expno>/pdata/<procno>/
1r, 1i - processed 1D data (real, imaginary)
auditp.txt - processing audit trail


## USAGE IN AU PROGRAMS

MC


## SEE ALSO

ps, apk, apks, apkm, apkf, ph, trf, trfp
© 2025 Bruker BioSpin GmbH & Co. KG
