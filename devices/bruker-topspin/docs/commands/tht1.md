# tht3, tht2, tht1

**Category:** Commands > Process > Advanced > Special Transforms

## NAME

**tht3** - Hilbert transform in F3 (3D)

**tht2** - Hilbert transform in F2 (3D)

**tht1** - Hilbert transform in F1 (3D)


## DESCRIPTION

tht3 performs a Hilbert transform in the F3 direction creating imaginary data from the real data. The resulting imaginary data can then be used for phase correction with tf3p.
tht2 performs a Hilbert transform in the F2 direction creating imaginary data from the real data. The resulting imaginary data can then be used for phase correction with tf2p.
tht1 performs a Hilbert transform in the F1 direction creating imaginary data from the real data. The resulting imaginary data can then be used for phase correction with tf1p.
Note that Hilbert Transform is only useful when the real data have been created from zero filled raw data, with SI ≥ TD.
Normally, the imaginary data are created during Fourier transform. If, however, the imaginary data are missing or do not match the real data and you want to do a phase correction, you can (re)create them with Hilbert transform. Imaginary data do not match the real data if the latter have been manipulated after the Fourier transform, for example by baseline correction or third party software.


## INPUT FILES

<dir>/data/<user>/nmr/<name>/<expno>/pdata/<procno>/
3rrr - real processed 3D data


## OUTPUT FILES

<dir>/data/<user>/nmr/<name>/<expno>/pdata/<procno>/
3irr - F3 imaginary processed data (output of tht3)
3rir - F2 imaginary processed data (output of tht2)
3rri - F1-imaginary processed data (output of tht1)
auditp.txt - processing audit trail


## SEE ALSO

tf3, tf2, tf1
© 2025 Bruker BioSpin GmbH & Co. KG
