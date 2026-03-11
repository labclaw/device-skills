# wpl

**Category:** Commands > Process > Advanced

## NAME

**wpl** - Write 2D data to a plane of data ≥ 3D


## DESCRIPTION

The command wpl replaces a plane of processed data with dimension ≥ 3D with a 2D processed data set. It is usually, but not necessarily, used to write back a plane that was extracted with rpl. This plane can be modified and/or written back to a different plane number. 
 
wpl takes up to four arguments. As an example we take a plane written to a 3D data set:
<plane axis orientation> : 12, 13, 23, 21, 31 or 32
The digits refer to the F3, F2 and F1 axes of the 3D data. Note that the order of the two digits is relevant:
1. the first digit is the 3D axis that corresponds to the 2D-F1 axis
2. the last digit is the 3D axis that corresponds to the 2D-F2-axis
This means that for the values 21, 31 and 32, the axes are exchanged, i.e. rows are stored as columns and vice versa (see below).
<plane number> : 1 - SI
SI is the 3D size in the direction orthogonal to the plane axis orientation
<procno> 
Destination 3D procno (source 3D procno if wpl is entered on the destination 2D data set)
<inmem> : optional argument for usage in AU programs only
Improves performance by data caching. Caution: nD data must not be modified by any command other than wpl between two consecutive rpl inmem or wpl inmem commands.
n 
Do not write imaginary data. Only the real data plane is written to the real destination data. This option prevents wpl to abort when nD destination data exist, but 2D source data do not. Caution: this options makes the nD imaginary data inconsistent.
wpl can be entered on the 2D source dataset or on the destination 3D data set. The number of required arguments is different (see below).
### wpl entered on the source 2D data set

In this case, wpl prompts the user for two arguments only, the plane number and the 3D destination procno. The plane axis orientation is taken from the 2D data set (used_from file). The two arguments can also be specified on the command line. If, however, you specify three arguments, the plane axis orientation is taken from the first argument rather than from the 2D data set. 
Examples:
wpl 
Prompt the user for the plane number and destination 3D procno, take the plane axis orientation from the current 2D data set and write the plane accordingly.
wpl 11 1 
Write the current 2D data to plane 11 of the 3D dataset in procno 1. Take the plane axis orientation from the current 2D data set.
wpl 31 11 2 
Write the current 2D data to F1-F3 plane number 11 of the 3D data in procno 2, exchanging the F1 and F3 axes.
Note that if the source 2D data set does not contain a used_from file, for example because it is not an extracted plane, wpl will prompt the user for the plane axis orientation. 
### Entering wpl on the destination 3D dataset

In this case, wpl prompts the user for three arguments. Alternatively, these can be entered on the command line.
Examples:
wpl 23 10 999 
Write the 2D data in procno 999 to F2-F3 plane 10 of the current 3D data.
wpl 12 32 101 
Write the 2D data in procno 101, to the F1-F2 plane 32 of the current 3D data
wpl 12 
Prompt the user for the procno of the source 2D dataset and the plane number. Write the 2D dataset to the specified F1-F2 plane accordingly.
### Entering wpl on a 4D dataset

On a data with dimension > 3, wpl works the same as on a 3D data set, except that there are more plane axis orientations. For example on 4D data set, possible orientations are 12, 13, 14, 23, 24, 34, 21, 31, 32, 41, 42 and 43.


## INPUT FILES

<dir>/data/<user>/nmr/<name>/<expno>/pdata/<procno>/
2rr, 2ir, 2ri, 2ii - processed 2D data
used_from - data path of the source 3D data and the plane number


## OUTPUT FILES

<dir>/data/<user>/nmr/<name>/<expno>/pdata/<procno>/
3rrr, 3irr, 3rir, 3rri, 3iii - processed data (wpl on 3D data)
4rrrr, 4iiii - processed data (wpl on 4D data)
auditp.txt - processing audit trail


## SEE ALSO

rpl, rtr, wtr, rcb, wser, wserp
© 2025 Bruker BioSpin GmbH & Co. KG
