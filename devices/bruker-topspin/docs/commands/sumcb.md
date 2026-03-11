# projcbp, projcbn, sumcb

**Category:** Commands > Process > Advanced

## NAME

**projcbp** - Calculate positive 3D projection

**projcbn** - Calculate negative 3D projection

**sumcb** - Calculate sum 3D projection


## DESCRIPTION

The commands projcbp, projcbn and sumcb calculate the positive, negative and sum 3D projection, respectively, from a dataset of dimension ≥ 4.
They require take up to 5 arguments:
1. <cube orientation>  : 234, 134, 124, ..., 432, 321 etc. 
2. <first cube> : the first cube included in the calculation
3. <last cube> : the last cube included in the calculation
4. <dest. procno> : the procno where the 3D output data are stored
5. xdim : sets the subcube sizes according to XDIM (optional)
6. n : prevents the destination dataset from being displayed/activated (optional)
Here is an example of the usage of a 3D projection command:
projcbp 234 1 32 999 n
Calculates the positive F2-F3-F4 3D projection of cube 1 to 32 along the F1 direction, stores it under PROCNO 999 but does not change the display to the output data. 
Instead of specifying the first and last cube, you can also use the argument all for all cubes. For example:
projcbp 234 all 10
Calculates the positive F2-F3-F4 3D projection of all cubes along F1 and stores it under PROCNO 10.
Missing arguments (except for the optional ones) will be prompted for. For example, entering projcbp without any arguments will display the dialog:
 
Note the following aspects:
1. The maximum first and last cube is determined by the size of the data in the direction not included cube orientation, i.e. the direction along which the projection is calculated.
2. XDIM is a processing parameter which must be set in each direction included cube orientation when with the xdim argument is used.
3. The numerical arguments must be specified in the above order, whereas the arguments all, xdim and n can be specified at any position.


## INPUT FILES

For a 4D dataset:
<dir>/data/<user>/nmr/<name>/<expno>/pdata/<procno>/
4rrrr - real processed 4D data


## OUTPUT FILES

<dir>/data/<user>/nmr/<name>/<expno>/pdata/<procno>/
3rrr - real processed 3D data
procs - F3 processing status parameters
proc2s - F2 processing status parameters
proc3s - F1 processing status parameters
auditp.txt - processing audit trail


## SEE ALSO

projplp, projpln, sumpl
© 2025 Bruker BioSpin GmbH & Co. KG
