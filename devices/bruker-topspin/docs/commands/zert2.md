# zert2, zert1, zert

**Category:** Commands > Process > Advanced > Miscellaneous Operations

## NAME

**zert2** - Zero a trapezoidal region of each row (2D)

**zert1** - Zero a trapezoidal region of each column (2D)

**zert** - Open zero region parameter dialog box (2D)


## DESCRIPTION

The zero region commands can be started from the command line or from the zero region parameter dialog box. The latter is opened with the command zert.
 
This dialog box offers only one option which can be used in the F2 or F1 direction.
Zero trapezoidal region in F2
This option selects the command zert2 for execution. The trapezoidal region to be zeroed is defined as follows: 
1. Only the rows between F1-ABSF2 and F1-ABSF1 are zeroed. 
2. The part (region) of each row which is zeroed shifts from row to row. The first row is zeroed between F2-ABSF2 and F2-ABSF1. The last row is zeroed between F2-SIGF2 and F2-SIGF1. For intermediate rows, the low field limit is an interpolation of F2-ABSF2 and F2-SIGF2 and the high field limit is an interpolation of F2-ABSF1 and F2-SIGF1.
zert2 works exactly like abst2, except that the data points are zeroed instead of baseline corrected.
Zero trapezoidal region in F1
This option selects the command zert1 for execution. The trapezoidal region to be zeroed is defined as follows: 
1. Only the columns between F2-ABSF2 and F2-ABSF1 are zeroed. 
2. The part (region) of each column which is zeroed shifts from column to column. The first column is zeroed between F1-ABSF2 and F1-ABSF1. The last column is zeroed between F1-SIGF2 and F1-SIGF1. For intermediate columns, the low field limit is an interpolation of F1-ABSF2 and F1-SIGF2 and the high field limit is an interpolation of F1-ABSF1 and F1-SIGF1.
zert1 works exactly like abst1, except that the data points are zeroed instead of baseline corrected.


## INPUT PARAMETERS

Set from the zert dialog box, with edp or by typing absf1, absf2 etc.: 
ABSF1 - low field limit of the zero region in the first row
ABSF2 - high field limit of the zero region in the first row
SIGF1 - low field limit of the zero region in the last row
SIGF2 - high field limit of the zero region in the last row


## INPUT FILES

<dir>/data/<user>/nmr/<name>/<expno>/pdata/<procno>/
  2rr - real processed 2D data
  proc2 - F1 processing parameters


## OUTPUT FILES

<dir>/data/<user>/nmr/<name>/<expno>/pdata/<procno>/
  2rr - real processed 2D data
  proc2s - F1 processing status parameters
  auditp.txt - processing audit trail


## USAGE IN AU PROGRAMS

ZERT2
ZERT1


## SEE ALSO

abs2, abst2 commanda, abs, absf, absd, absn, bas
© 2025 Bruker BioSpin GmbH & Co. KG
