# xht2, xht1

**Category:** Commands > Process > Advanced > Special Transforms

## NAME

**xht2** - Hilbert transform in F2 (2D)

**xht1** - Hilbert transform in F1 (2D)


## DESCRIPTION

The command xht2 performs a Hilbert transform of 2D data in the F2 direction. 
The command xht1 performs a Hilbert transform of 2D data in the F1 direction. 
Hilbert transform creates imaginary data from the real data. Imaginary data are required for phase correction. They are normally created during Fourier transform with xfb, xf2 or xf1. If, however, the imaginary data were not stored (xfb n) or have been deleted (deli), you can (re)create them with xht2 or xht1.
Note that Hilbert Transform is only useful when the real data have been created from zero filled raw data, with SI ≥ TD.
Hilbert transform can also be used if the imaginary data exist but do not match the real data. This is the case when the latter have been manipulated after Fourier transform, for example by abs1, abs2, sub*, sym or third party software.


## INPUT FILES

<dir>/data/<user>/nmr/<name>/<expno>/pdata/<procno>/
  2rr - real processed 2D data
  2ir - second quadrant imaginary data (if existing, input of xht1)
  2ri - third quadrant imaginary data (if existing, input of xht2)


## OUTPUT FILES

<dir>/data/<user>/nmr/<name>/<expno>/pdata/<procno>/
  2rr - real processed 2D data
  2ir - second quadrant imaginary data (output of xht2, created from 2rr)
  2ri - third quadrant imaginary data (output of xht1, created from 2rr)
  2ii - fourth quadrant imaginary data
  auditp.txt - processing audit trail


## USAGE IN AU PROGRAMS

XHT2
XHT1


## SEE ALSO

xfb, ftf, xf2, xf1
© 2025 Bruker BioSpin GmbH & Co. KG
