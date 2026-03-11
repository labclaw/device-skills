# fp, fmc

**Category:** Commands > Process > Advanced > Special Transforms

## NAME

**fp** - Fourier transform + phase correction (1D)

**fmc** - Fourier transform + magnitude calculation (1D)


## DESCRIPTION

The composite processing command fp is a combination of ft and pk, i.e. it performs a 1D Fourier transform and a phase correction. 
fmc is a combination of ft and mc, i.e. it performs a 1D Fourier transform and a magnitude calculation. 
fp and fmc automatically perform an FID baseline correction according to BC_mod.
All composite processing commands can be found in the menu:
Process | Advanced | Special Transforms 
### INPUT AND OUTPUT PARAMETERS

See the commands ft, pk and mc.


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

FP
FMC


## SEE ALSO

ef, efp, gf, gfp, qf, qfp
© 2025 Bruker BioSpin GmbH & Co. KG
