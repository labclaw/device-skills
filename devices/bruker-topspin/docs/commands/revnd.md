# revnd

**Category:** Commands > Process > Advanced > Miscellaneous Operations

## NAME

**revnd** - Reverse of an nD spectrum along a dimension (≥ 3D)


## DESCRIPTION

The command revnd reverses an nD spectrum in the specified dimension. This means, each row along this dimension is mirrored about its center. Calling this command firstly opens the following dialog box to choose the dimension:
 
Note that the spectrum can also be reversed during ftnd by setting the processing parameter REVERSE to TRUE for the desired dimension.


## INPUT FILES

<dir>/data/<user>/nmr/<name>/<expno>/pdata/<procno>/
3rrr - processed data


## OUTPUT FILES

<dir>/data/<user>/nmr/<name>/<expno>/pdata/<procno>/
3rrr - processed data
auditp.txt - processing audit data


## USAGE IN AU PROGRAMS

REVND - processed 3D data


## SEE ALSO

rv, rev2, rev1
© 2025 Bruker BioSpin GmbH & Co. KG
