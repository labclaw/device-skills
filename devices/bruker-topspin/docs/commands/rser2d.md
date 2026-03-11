# rser2d

**Category:** Commands > Process > Advanced

## NAME

**rser2d** - Read plane from raw 3D data and store as a 2D (3D)


## DESCRIPTION

The command rser2d reads a plane from 3D raw data (a series of FIDs) and stores it as a pseudo raw 2D data set. When entered without arguments, it opens the following dialog box:
 
Here you can specify three required parameters:
1. Plane orientation: F1-F3 or F2-F3 (must contain acquisition (F3) direction)
2. Plane number: the maximum plane number is the TD value in the direction orthogonal to the plane orientation
3. Destination EXPNO: the expno where the output 2D dataset is stored
The parameters can also be entered as arguments on the command line. In that case, the command is executed without opening the dialog box. For example, rser2d s23 10 999 reads an F3-F2 plane number 10 and stores it in expno 999
In contrast to rser, rser2d can only be entered on the source dataset, not on the destination dataset.


## INPUT FILES

<dir>/data/<user>/nmr/<name>/<expno>/
ser - 3D raw data


## OUTPUT FILES

<dir>/data/<user>/nmr/<name>/<expno>/
ser - 2D pseudo raw data
audita.txt - acquisition audit trail
<dir>/data/<user>/nmr/<name>/<expno2>/pdata/1/
used_from - data path of the source 3D data and the plane number


## USAGE IN AU PROGRAMS

RSER2D (direction, plane, expno)


## SEE ALSO

wser, wserp, rpl, wpl
© 2025 Bruker BioSpin GmbH & Co. KG
