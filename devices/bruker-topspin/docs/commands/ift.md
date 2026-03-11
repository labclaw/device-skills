# ift

**Category:** Commands > Process > Advanced > Special Transforms

## NAME

**ift** - Inverse Fourier transform (1D)


## DESCRIPTION

The command ift performs an inverse Fourier transform of a 1D spectrum, thus creating an artificial FID. Normally, ift is done when the raw data do not exist anymore. If, however, raw data do exist, they are not overwritten. ift stores the resulting FID as processed data, i.e. it overwrites the current spectrum. 
After ift, you can create pseudo-raw data with the command genfid which creates a new dataset. Note that the number of data points of the pseudo-raw data, is twice the size of the processed data they are created from. The acquisition status parameter TD (dpa) is set; accordingly, TD = 2*SI.


## INPUT FILES

<dir>/data/<user>/nmr/<name>/<expno>/pdata/<procno>/
1r, 1i - processed 1D data (frequency domain)


## OUTPUT FILES

<dir>/data/<user>/nmr/<name>/<expno>/pdata/<procno>/
1r, 1i - processed 1D data (time domain)
auditp.txt - processing audit trail


## USAGE IN AU PROGRAMS

IFT


## SEE ALSO

ft, ftf, trf, trfp
© 2025 Bruker BioSpin GmbH & Co. KG
