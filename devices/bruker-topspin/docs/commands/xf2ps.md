# xfbps, xf2ps, xf1ps

**Category:** Commands > Process > Adjust Phase

## NAME

**xfbps** - Calculate power spectrum in F2 and F1 (2D)

**xf2ps** - Calculate power spectrum in F2 (2D)

**xf1ps** - Calculate power spectrum in F1 (2D)

**ph** - Open phase correction command dialog box (1D, 2D)


## DESCRIPTION

The commands xf*ps calculate the magnitude spectrum. They can be started from the command line or from the phase correction dialog box. The latter is started with the command ph.
 
This dialog box offers several options, each of which selects a certain command for execution.
### Power spectrum in F2

This option selects the command xf2ps for execution. It recalculates the real and F2-imaginary data according to: 

### Power spectrum (F1)

This option selects the command xf1ps for execution. It recalculates the real and F1-imaginary data according to:

### Power spectrum (F2 and F1)

This option selects the command xfbps for execution. It recalculates the real according to: 

Where:
  rr = real data (2rr file)
  ir = F2-imaginary data (2ir file) 
  ri = F1- imaginary data (2ri file)
  ii = F2/F1-imaginary data (2ii file)
The commands xf*ps is, for example, used in special cases to convert a phase sensitive spectrum to a power spectrum. This is useful for data which cannot be phased properly or data which are not phase sensitive but have been acquired as such.
The ph command can be used on 1D or 2D data. It recognizes the data dimensionality and opens a dialog box with the appropriate options and parameters.


## INPUT FILES

<dir>/data/<user>/nmr/<name>/<expno>/pdata/<procno>/
  2rr, 2ir, 2ri, 2ii - processed 2D data


## OUTPUT FILES

<dir>/data/<user>/nmr/<name>/<expno>/pdata/<procno>/
  2rr, 2ir, 2ri, 2ii - processed 2D data
  auditp.txt - processing audit trail


## USAGE IN AU PROGRAMS

XFBPS
XF2PS
XF1PS


## SEE ALSO

xfbm, xf2m, xf1m
© 2025 Bruker BioSpin GmbH & Co. KG
