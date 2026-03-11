# int2d, int3d, int

**Category:** Commands > Analyze > Integrate

## NAME

**int2d** - Calculate integrals (2D)

**int3d** - Calculate integrals (2D)

**int** - Open integral dialog box (1D, 2D, 3D)


## DESCRIPTION

The command int2d calculates 2D integrals. It opens the following dialog box:
 
Here you can set the minimum threshold for integration. You can enter:
1. Enter the relative intensity: value between 0.0 and 1.0 
2. Enter the absolute intensity: value between 0.0 and YMax_p (processing status parameter). 
3. Click Set to... and choose from one of the following options:
1. lowest contour level - value of the lowest contour level (see edlev) 
2. value stored in MI - value of the processing parameter MI (see edp)
3. most recent MI used - value used by last  int2d command on any dataset 
If you enter a relative value, the absolute value is automatically adjusted and vice versa. Setting the most recent MI used allows to compare integral value, e.g. of the NOE peak of a series of 2D spectra. Obviously, this only makes sense for spectra that are measured and processing under similar conditions.
The calculated integrals will be marked in the data field and can be listed by clicking the Integrals tab.
int3d is the same as int2d, except that it works on 3D data.
The int command can be used on 1D, 2D or 3D data. It recognizes the data dimensionality and opens a dialog box with the appropriate options and parameters. In particular on 1D data sets, it offers some special functionality to integrate spectra.
The following figure shows a region of peaks after peak picking.
 
The next figure shows the same region after 2D integration. Here you can see the integral labels and areas. The area color can be set in the user preferences (command set) as Color of 3rd 1D spectrum.


## INPUT FILES

<dir>/data/<user>/nmr/<name>/<expno>/pdata/<procno>/
2rr - real processed 2D data (input of  int2d)
3rrr - real processed 3D data (input of  int3d)


## OUTPUT FILES

<dir>/data/<user>/nmr/<name>/<expno>/pdata/<procno>/
integ_points.txt - data points of integral regions
integrals.txt - peaks, integral regions and integral values


## SEE ALSO

li, lipp, lippf, int
© 2025 Bruker BioSpin GmbH & Co. KG
