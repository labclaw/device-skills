# xif2, xif1

**Category:** Commands > Process > Advanced > Special Transforms

## NAME

**xif2** - Inverse Fourier transform in F2 (2D)

**xif1** - Inverse Fourier transform in F1 (2D)


## DESCRIPTION

The command xif2 performs an inverse Fourier transform in the F2 direction. This means frequency domain data (spectrum) are transformed into time domain data (FID).
xif1 performs an inverse Fourier transform in the F1 direction. 
### NOTE

Note that after xif2 or xif1 (or both), the data are still stored as processed data, i.e. the raw data are not overwritten. You can, however, create pseudo-raw data with the command genser which creates a new dataset.
Inverse Fourier transform can also be done with the commands xtrfp, xtrfp2 and xtrfp1. To do that: 
1. Type dpp and check the status FT_mod.
2. Type edp to set the processing parameters; set BC_mod, WDW, ME_mod and PH_mod to no and FT_mod to the inverse equivalent of the status FT_mod.
3. Perform xtrfp, xtrfp2 or xtrfp1.


## INPUT FILES

<dir>/data/<user>/nmr/<name>/<expno>/pdata/<procno>/
  2rr, ir, 2ri, 2ii - processed 2D data


## OUTPUT FILES

<dir>/data/<user>/nmr/<name>/<expno>/pdata/<procno>/
  2rr, ir, 2ri, 2ii - processed 2D data
  auditp.txt - processing audit trail


## USAGE IN AU PROGRAMS

XIF2
XIF1


## SEE ALSO

xtrfp, xtrfp2
© 2025 Bruker BioSpin GmbH & Co. KG
