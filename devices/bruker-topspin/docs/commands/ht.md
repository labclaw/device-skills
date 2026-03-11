# ht

**Category:** Commands > Process > Advanced > Special Transforms

## NAME

**ht** - Hilbert transform (1D)


## DESCRIPTION

The command ht performs a Hilbert transform which means the imaginary part of a spectrum is calculated from the real part. This is only useful when the real data have been created from zero filled raw data, with SI ≥ TD. Only then they will contain the entire spectral information.
Imaginary data are required for phase correction. They are normally created together with the real data by Fourier transform. Directly after the Fourier transform, real and imaginary data are consistent and can be used for phase correction. If, however, the real data are manipulated, e.g. by abs, they are no longer consistent with the imaginary data. In that case, or when the imaginary data have been deleted, ht can be used to create new imaginary data.
Hilbert transform is based on the so-called dispersion relations or Kramers-Kronig relations (see, for example, R. R. Ernst, G. Bodenhausen and A. Wokaun, Principles of nuclear magnetic resonance in one and two dimensions, Clarendon Press, Oxford, 1987).


## INPUT FILES

<dir>/data/<user>/nmr/<name>/<expno>/pdata/<procno>
1r - real processed 1D data


## OUTPUT FILES

<dir>/data/<user>/nmr/<name>/<expno>/pdata/<procno>/
1i - imaginary processed data
auditp.txt - processing audit trail


## USAGE IN AU PROGRAMS

HT


## SEE ALSO

ift, ft, ftf, trf, trfp
© 2025 Bruker BioSpin GmbH & Co. KG
