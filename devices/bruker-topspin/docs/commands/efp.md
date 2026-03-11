# ef, efp

**Category:** Commands > Process > Advanced > Special Transforms

## NAME

**ef** - Exponential window multiplication + Fourier transform (1D)

**efp** - Exponential window multiplication + FT + phase correction (1D)


## DESCRIPTION

The composite processing command ef is a combination of em and ft, i.e. it performs an exponential window multiplication and a Fourier transform. 
efp is a combination of em, ft and pk, i.e. it does the same as ef but, in addition, performs a phase correction. 
ef and efp automatically perform an FID baseline correction according to BC_mod.
All composite processing commands can be found in the menu: 
Process | Advanced | Special Transforms


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

EF
EFP


## SEE ALSO

gf, gfp, fp, fmc, qf, qfp
© 2025 Bruker BioSpin GmbH & Co. KG
