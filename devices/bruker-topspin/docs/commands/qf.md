# qf, qfp

**Category:** Commands > Process > Advanced > Special Transforms

## NAME

**qf** - Sine squared window multiplication + Fourier transform (1D)

**qfp** - Sine squared window multiplication + FT + phase correction (1D)


## DESCRIPTION

The composite processing command qf is a combination of qsin and ft, i.e. it performs a Sine squared window multiplication and a Fourier transform.
qfp is a combination of qsin, ft and pk, i.e. it does the same as qf but, in addition, performs a phase correction.
qf and qfp automatically perform an FID baseline correction according to BC_mod.
All composite processing commands can be found under the menu Process | Advanced | Special Transforms.
### INPUT AND OUTPUT PARAMETERS

See qsin, ft and pk


## INPUT FILES

<dir>/data/<user>/nmr/<name>/<expno>/
fid - raw data (input if 1r, 1i do not exist or are Fourier transformed)
acqus - acquisition status parameters
<dir>/data/<user>/nmr/<name>/<expno>/pdata/<procno>/
1r, 1i - processed data (input if they exist but are not Fourier transformed)
proc - processing parameters


## OUTPUT FILES

<dir>/data/<user>/nmr/<name>/<expno>/pdata/<procno>/
1r, 1i - processed 1D data (real, imaginary)
procs - processing status parameters
auditp.txt - processing audit trail


## USAGE IN AU PROGRAMS

GF
GFP


## SEE ALSO

ef, efp, gf, gfp, sinm, qsin, sinc, qsinc, fp, fmc
© 2025 Bruker BioSpin GmbH & Co. KG
