# rpl

**Category:** Commands > Process > Advanced

## NAME

**rpl** - Read plane from data ≥ 3D and store as 2D data


## DESCRIPTION

The command rpl reads a plane from processed data with dimension ≥ 3D and stores it as a 2D dataset in a different procno. 
rpl takes up to five arguments. As an example, we take a plane read from a 3D dataset:
<plane   axis   orientation>  : 23, 13, 12, 32, 31 or 21 
The digits refer to the F3, F2 and F1 axes of the 3D data. Note that the order of the two digits is relevant:
1. the first digit is the 3D axis that corresponds to the 2D-F1 axis
2. the last digit is the 3D axis that corresponds to the 2D-F2-axis
This means that for the values 21, 31 and 32, the axes are exchanged, storing rows as columns and vice versa (see below).
<plane number> : 1 - SI
SI is the 3D size in the direction orthogonal to the plane orientation
<procno> : 
Destination 2D procno (source 3D procno if rpl is entered on the destination 2D dataset)
<inmem> : optional argument for usage in AU programs only
Improves performance by data caching. Caution: nD data must not be modified by any command other than wpl between two consecutive rpl inmem or wpl inmem commands.
n : optional argument
Prevents the destination dataset from being displayed/activated 
Obligatory arguments which are not specified on the command line will be prompted for.
rpl can be entered on the source 3D dataset or, if it already exists, on the destination 2D dataset. The number of required arguments is different (see below).
### rpl entered on a source 3D dataset

In this case, rpl prompts the user for three arguments. Alternatively, these can be entered on the command line.
Here are some examples: 
rpl 
Prompt the user for the plane axis orientation, the plane number and source 3D procno and read the plane accordingly.
rpl 23 10 999
Read F2-F3 plane 10 and store it in procno 999. 
rpl 32 10 999
Read F2-F3 plane 10 and store it in procno 999, exchanging the F2 and F3 axes.
rpl 12 64 101
Read F1-F2 plane 64 and store it in procno 101.
rpl 12 64 
Read F1-F2 plane 64, prompt the user for the destination procno
rpl 31 1 10 n
Read an F1-F3 plane number 1 and store it in procno 10, exchanging the F1 and F3 axes. Do not display/activate the destination dataset. 
### rpl entered on a destination 2D dataset

This is typically done on a 2D dataset which is a plane extracted by a previous rpl command, which was entered on the source 3D dataset. In that case, rpl requires only one argument; the plane number. By default, the same plane axis orientation and source 3D dataset (procno) are used as with the previous rpl command (as defined in the used_from file of the 2D dataset). You can, however, use two or three arguments to specify a different plane axis orientation and/or 3D source procno. On a regular 2D dataset (not a plane from a 3D), rpl requires three arguments.
Here are some examples of rpl executed on a 2D dataset, where the 2D dataset is a plane from a 3D dataset:
rpl 
Prompt the user for the plane number, use the plane axis orientation and source 3D procno as defined in the current 2D dataset and read the plane accordingly.
rpl 11
Read plane 11. Use the plane axis orientation and source 3D procno as defined in current 2D dataset.
rpl 31 11 
Read F1-F3 plane 11, exchanging the F1 and F3 axes. Use the source 3D procno as defined in current 2D dataset.
rpl 13 11 2 
Read F1-F3 plane 11 from the 3D dataset under procno 2
As described above, the rpl argument plane axis orientation determines whether the axes are exchanged. This is sometimes required to match nuclei when you compare a 3D plane with a 2D dataset. Example: you have a 3D NOESYHSQC (F3-1H, F2-13C, F1-1H) and want to compare an F2-F1 plane with a 2D HSQC (F2-1H, F1-13C). Now compare the following actions:
rpl 12: The plane is stored as a 2D dataset with F2-13C, F1-1H which cannot be directly compared with the a HSQC. 
rpl 21: The plane is stored as a 2D dataset with F2-1H, F1-13C which can be directly compared with the a HSQC. 
In special cases, rpl results in a 2D dataset which is not Fourier transformed in F2. This occurs, for example, if you run rpl 12 on a 3D dataset which has only been transformed in F3. rpl unshuffles the output data, storing the odd and even points in separate data files (2rr and 2ir). As a result the size in F2 (parameter SI) is only half the size of the corresponding direction in the 3D dataset. If, for some reason, you want keep the same size, you can use rpl with the option keepsize. The output data are then zero filled once in F2. Here is an example:
rpl 12 1 10 keepsize 
Note that a plane read with keepsize cannot be written back to the source dataset because the sizes do not match.
The behaviour of the command rpl is similar to the commands rsr and rsc, in the sense that it can be entered from the source and destination dataset.
On a data with dimension > 3, rpl works the same as on a 3D dataset, except that there are more plane axis orientations. For example on 4D dataset, possible orientations are 34, 24, 14, 23, 13, 12, 43, 42, 41, 32, 31 and 21.
For an example if the inmem option, see the AU program ift3d.


## INPUT FILES

<dir>/data/<user>/nmr/<name>/<expno>/pdata/<procno>/
3rrr, 3irr, 3rir, 3rri, 3iii - processed data (rpl on 3D data)
4rrrr, 4iiii - processed data (rpl on 4D data)


## OUTPUT FILES

<dir>/data/<user>/nmr/<name>/<expno>/pdata/<procno>/
2rr, 2ir, 2ri, 2ii - processed 2D data
auditp.txt - processing audit trail
used_from - data path of the source 3D data and the plane number


## SEE ALSO

wpl, rtr, wtr, rcb, wser, wserp, rser2d
© 2025 Bruker BioSpin GmbH & Co. KG
