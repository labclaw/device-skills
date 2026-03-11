# projplp, projpln, sumpl

**Category:** Commands > Process > Advanced

## NAME

**projplp** - Calculate positive projection (nD)

**projpln** - Calculate negative projection (nD)

**sumpl** - Calculate sum projection (nD)


## DESCRIPTION

The commands projplp, projpln and sumpl calculate the 2D positive, negative and sum projection, respectively. When entered without arguments, they all open the same dialog:
 
Here you can select the desired command in the Options section and specify the plane orientation, first and last row/column and output PROCNO in the Parameter section. 
The parameters can also be specified as arguments. Up to 5 arguments can be used:
<plane orientation>   
23, 13, 12 (3D data) 
34, 24, 14, 23, 13, 12, 43, ..., 21 (4D data) 
<first plane> 
The plane included in the calculation.
<last plane> 
The last plane included in the calculation.
<dest. procno> 
The procno where the 2D output data are stored.
n 
Prevents the destination dataset from being displayed/activated (optional)
Here is an example:
projplp 13 10 128 998 n   
Calculates the positive F1-F3 projection of the planes 10 to 128 along F2 and stores it under PROCNO 998.
Instead of specifying the first and last plane, you can also use the argument all for all cubes. For example:
projplp 23 all 10 
Calculates the positive F2-F3 projection of all planes along F1 and stores it under PROCNO 10.
projplp, projpln and sumpl work on data of dimension ≥3D. On 4D and 5D data, the dialog shown in the figure above does not appear. Instead, the arguments are prompted for one at a time, if they are not specified on the command line.


## INPUT FILES

<dir>/data/<user>/nmr/<name>/<expno>/pdata/<procno>/
3rrr - real processed 3D data


## OUTPUT FILES

<dir>/data/<user>/nmr/<name>/<expno>/pdata/<procno>/
2rr - real processed 2D data


## SEE ALSO

rpl, wpl, rser2d
© 2025 Bruker BioSpin GmbH & Co. KG
