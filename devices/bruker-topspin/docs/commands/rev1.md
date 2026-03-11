# rev2, rev1

**Category:** Commands > Process > Advanced > Miscellaneous Operations

## NAME

**rev2** - Reverse spectrum in F2 (2D)

**rev1** - Reverse spectrum in F1 (2D)


## DESCRIPTION

The command rev2 reverses the spectrum in the F2 direction. This means, each row is mirrored about the central column.
The command rev1 reverses the spectrum in the F1 direction. This means, each column is mirrored about the central row.
Note that the spectrum can also be reversed by during xfb by setting the F2 and/or F1 processing parameter REVERSE to TRUE.


## INPUT FILES

<dir>/data/<user>/nmr/<name>/<expno>/pdata/<procno>/
2rr, 2ir, 2ri, 2ii - processed data


## OUTPUT FILES

<dir>/data/<user>/nmr/<name>/<expno>/pdata/<procno>/
2rr, 2ir, 2ri, 2ii - processed data
auditp.txt - processing audit trail


## USAGE IN AU PROGRAMS

REV2
REV1


## SEE ALSO

rv 
© 2025 Bruker BioSpin GmbH & Co. KG
