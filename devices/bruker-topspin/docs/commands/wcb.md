# wcb

**Category:** Commands > Process > Advanced

## NAME

**wcb** - Write 3D data to a cube of data ≥ 4D


## DESCRIPTION

The command wcb replaces a cube of processed data with dimension ≥ 4D with a 3D processed dataset. It is usually, but not necessarily, used to write back a cube that was extracted with rcb. This cube can be modified and/or written back to a different cube number.
wcb takes up to three arguments. As an example, we take a cube written to a 4D dataset:
<cube axis orientation> : 234, 134, 124, 123, 432, ..., 321 etc.
The digits refer to the F4, F3, F2 and F1 axes of the 4D data. Note that the order of the three digits is relevant:
the first digit is the 4D axis that corresponds to the 3D-F1 axis
the last digit is the 4D axis that corresponds to the 3D-F3-axis
<cube number> : 1 - SI
SI is the 4D size in the direction orthogonal to the cube axis orientation
<procno>
destination 4D procno (source 4D procno if wcb is entered on the destination 3D dataset).
wcb can be entered on the 3D source dataset or on the destination 4D dataset. The number of required arguments is different (see below).
### wcb entered on the source 3D dataset

In this case, wcb prompts the user for two arguments only, the cube number and the 4D destination procno. The cube axis orientation is taken from the 3D dataset (used_from file). The two arguments can also be specified on the command line. If, however, you specify three arguments, the plane axis orientation is taken from the first argument rather than from the 3D dataset.
Examples:
wcb
prompt the user for the cube number and destination 4D procno, take the cube axis orientation from the current 3D dataset and write the cube accordingly.
wcb 11 1
write the current 3D data to cube 11 of the 4D dataset in procno 1. Take the cube axis orientation from the current 2D dataset.
wcb 432 11 2
write the current 4D data to F2-F3-F4 cube number 11 of the 4D data in procno 2, exchanging the F2 and F4 axes.
Note that if the source 3D dataset does not contain a used_from file, for example because it is not an extracted plane, wcb will prompt the user for the cube axis orientation.
### Entering wcb on the destination 4D dataset

In this case, wcb prompts the user for three arguments. Alternatively, these can be entered on the command line.
Examples:
wcb 234 10 999
Write the 3D data in procno 999 to F2-F3-F4 cube 10 of the current 4D data.
wcb 234 32 101
Write the 3D data in procno 101, to the F2-F3-F4 cube 32 of the current 4D data
wcb 234
Prompt the user for the procno of the source 3D dataset and the cube number. Write the 3D dataset to the specified F2-F3-F4 cube accordingly.
### Entering wcb on a 5D dataset

On a data with dimension > 4, wcb works the same as on a 4D dataset, except that there are more cube axis orientations.


## INPUT FILES

<dir>/data/<user>/nmr/<name>/<expno>/pdata/<procno>/
3rrr, 3iii - processed 3D data
used_from - data path of the source 4D data and the cube number


## OUTPUT FILES

<dir>/data/<user>/nmr/<name>/<expno>/pdata/<procno>/
4rrrr, - processed data (wcb on 4D data)
5r, 5i - processed data (wcb on 5D data)
auditp.txt - processing audit trail


## SEE ALSO

rcb, rpl, rtr, wtr, rser, wser, wserp
© 2025 Bruker BioSpin GmbH & Co. KG
