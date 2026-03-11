# li, lipp, lippf, int

**Category:** Commands > Analyze > Integrate

## NAME

**li** - List integrals (1D)

**lipp** - List integrals and peaks within F1P-F2P (1D)

**lippf** - List integrals and peaks of the full spectrum (1D)

**int** - Open integral dialog box (1D, 2D, 3D)


## DESCRIPTION

Integral commands can be started from the command line or from the integration dialog box.
 
The latter is opened with the command int.
This dialog box has several options, each of which selects a certain command for execution.
### Auto-find regions, integrate & display results

This option executes the command sequence abs - li. The command abs determines the integral regions creating the intrng file. The command li calculates the integral value for each integral region and shows the result in on the screen.
### Integrate existing regions and display results

This option executes the command li. This command calculates the integral value for each integral region and shows the result in on the screen.
### List peaks and integrals within the displayed region

This option executes the command lipp. It works like li, except that it also performs peak picking and shows a list of integral regions and peaks within the region F1P - F2P.
### List peaks and integrals of the entire spectrum

This option executes the command lippf. It works like lipp, except that it only determines the integrals and peaks over the entire spectrum.
The li* commands evaluates the parameter INTSCL if the regions have been determined interactively. For INTSCL ≠ –1, the current dataset is defined as reference dataset for integral scaling. For INTSCL = –1, the integrals of the current dataset are scaled relative to the reference dataset. As such, you can compare the areas of peaks in a series of experiments. Furthermore, the parameter INTBC is evaluated. For INTBC = yes, an automatic baseline correction (slope and bias) of the integrals is performed. This, however, is only done when the integral regions were determined with abs, not if they were determined interactively.
The int command can be used on 1D, 2D or 3D data. It recognizes the data dimensionality and opens a dialog box with the appropriate options and parameters.


## INPUT PARAMETERS

Set with edp, from the int dialog box or by typing intscl, intbc etc.:
INTSCL - scale 1D integrals relative to a reference data set
INTBC - automatic baseline correction of integrals created by  abs 
F1P - low field (left) limit of the plot region in ppm (input for lipp)
F2P - high field (right) limit of the plot region in ppm (input for lipp)


## INPUT FILES

<dir>/data/<user>/nmr/<name>/<expno>/pdata/<procno>/
1r - real processed 1D data
intrng - 1D integral regions (created by abs or interactive integration)


## OUTPUT FILES

<dir>/data/<user>/nmr/<name>/<expno>/pdata/<procno>/
integrals.txt - ascii file containing the output of li
integrals_lipp.txt - ascii file containing the output of lipp integrals_lippf.txt - ascii file containing the output of lippf


## USAGE IN AU PROGRAMS

LI
LIPP
LIPPF


## SEE ALSO

int2d, int3d, int
© 2025 Bruker BioSpin GmbH & Co. KG
