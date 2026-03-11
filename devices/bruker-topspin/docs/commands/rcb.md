# rcb

**Category:** Commands > Process > Advanced

## NAME

**rcb** - Read cube from data ≥ 4D and store as 3D data


## DESCRIPTION

The command rcb reads a cube from processed data of dimension ≥ 4. It stores the extracted cube in a different procno as a 3D dataset.
 
rcb takes up to five arguments:
<cube axis orientation>  : 234, 134, 124, ..., 432, 321 etc. 
The digits refer to the F4, F3, F2 and F1 axes of the 4D data. Note that the order of the three digits is relevant:
1. The first digit is the 4D axis that corresponds to the 3D-F1 axis.
2. The second digit is the 4D axis that corresponds to the 3D-F2 axis.
3. The last digit is the 4D axis that corresponds to the 3D-F3-axis.
This means that for values like 234, 134, 124 etc. the axis order or the 3D cube and the 4D dataset are the same. For values like 432, 423, 143 etc., they are different. 
<cube number> : 1 - SI
SI is the 4D size in the direction orthogonal to the cube orientation
<procno> : 
Destination 3D procno (source 4D procno if rcb is entered on the destination 3D dataset)
xdim : optional argument
Sets the subcube sizes according to the processing parameter XDIM in the respective directions. This parameter must be set in the source 4D dataset before rcb is executed. 
n : optional argument
Prevents the destination dataset from being displayed/activated 
Arguments which are not specified on the command line will be prompted for, except for xdim and n argument.
rcb can be entered on the source 4D dataset or, if this already exists, on the destination 3D dataset. The number of required arguments is different (see below).
### rcb entered on a source 4D dataset

In this case, rcb prompts the user for three arguments. Alternatively, these can be entered on the command line.
Here are some examples: 
rcb 
Prompt the user for the cube axis orientation, the cube number and destination 3D procno and read the cube accordingly.
rcb 234 10 999
Read F2-F3-F4 cube 10 and store it in procno 999. 
rcb 324 10 999
Read F2-F3-F4 plane 10 and store it in procno 999, exchanging the F2 and F3 axes 
rcb 124 64 101 xdim
Read F1-F2-F4 plane 64 with subcube sizes according to the respective XDIM values and store it in procno 101.
rcb 124 64 
Read F1-F2-F4 plane 64, prompt the user for the destination procno
rcb 214 1 10 n
Read an F1-F2-F4 plane number 1 and store it in procno 10, exchanging the F2 and F1 axes. Do not display/activate the destination dataset. 
### rcb entered on a destination 3D dataset

This is typically done on a 3D dataset which is a cube extracted by a previous rcb command, which was entered on the source 4D dataset. In that case, rcb requires only one argument; the cube number. By default, the same cube axis orientation and source 4D dataset (procno) are used as with the previous rcb command (as defined in the used_from file of the 3D dataset). You can, however, use two or three arguments to specify a different cube axis orientation and/or 4D source procno. On a regular 3D dataset (not a plane from a 3D), rcb requires three arguments.
Here are some examples of rcb executed on a 3D dataset, where the 3D dataset is a cube from a 4D dataset:
rcb 
Prompt the user for the cube number. Use the cube axis orientation and source 4D procno as defined in the current 3D dataset.
rcb 11
Read cube 11. Use the cube axis orientation and Source 4D procno as defined in current 3D dataset.
rcb 123 11
Read F1-F2-F3 plane 11. Use the source 4D procno as defined in current 3D dataset.
rcb 123 11 2
Read F1-F2-F3 plane 11 from the 4D dataset under procno 2
As described above, the rcb argument cube axis orientation determines whether the axes are exchanged. Axes exchange is sometimes required to match nuclei when you compare a 4D cube with a 3D dataset.


## INPUT FILES

<dir>/data/<user>/nmr/<name>/<expno>/pdata/<procno>/
4rrrr, 4iiii - processed 4D data


## OUTPUT FILES

<dir>/data/<user>/nmr/<name>/<expno>/pdata/<procno>/
3rrr, 3iii - processed 3D data
auditp.txt - processing audit trail
used_from - data path of the source 4D data and the cube axis orientation


## SEE ALSO

rpl, wpl, rtr, wtr
© 2025 Bruker BioSpin GmbH & Co. KG
