# gf, gfp

**Category:** Commands > Process > Advanced > Special Transforms

## NAME

**gf** - Gaussian window multiplication + Fourier transform (1D)

**gfp** - Gaussian window multiplication + FT + phase correction (1D)


## DESCRIPTION

The composite processing command gf is a combination of gm and ft, i.e. it performs a Gaussian window multiplication and a Fourier transform. 
gfp is a combination of gm, ft and pk, i.e. it does the same as gf but, in addition, performs a phase correction. 
gf and gfp automatically perform an FID baseline correction according to BC_mod.
All composite processing commands can be found under the menu: 
Process | Advanced | Special Transforms
### INPUT AND OUTPUT PARAMETERS

See gm, ft and pk


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

ef, efp, fp, fmc, qf, qfp 
© 2025 Bruker BioSpin GmbH & Co. KG
