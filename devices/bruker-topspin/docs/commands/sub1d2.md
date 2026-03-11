# sub2, sub1, sub1d2, sub1d1

**Category:** Commands > Process > Advanced

## NAME

**sub2** - Subtract 1D data from 2D data rows, keep sign (2D)

**sub1** - Subtract 1D data from 2D data columns, keep sign (2D)

**sub1d2** - Subtract 1D data from 2D data rows (2D)

**sub1d1** - Subtract 1D data from 2D data columns (2D)

**adsu** - Open add/subtract/multiply workflow button bar (1D, 2D)


## DESCRIPTION

Subtracting a 1D data from a 2D data can be started from the command line or from the add/subtract workflow button bar. The latter is opened with the command adsu.
 
This workflow button bar offers several options, each of which selects a certain command for execution. 
### Subtract a 1D spectrum from each row, retain sign

This option selects the command sub2 for execution. It subtracts a 1D dataset from each row of the current 2D spectrum. It first compares the intensity of each data point of the 1D spectrum with the intensity of the corresponding data point in the 2D spectrum. If they have opposite signs, no subtraction is done and the 2D data point remains unchanged. If they have the same sign and the 1D data point is smaller than the 2D data point, the subtraction is done. If the 1D data point is greater than the 2D data point, the latter is set to zero. As such, the sign of the 2D data points always remains the same.
### Subtract a 1D spectrum from each column, retain sign

This option selects the command sub1 for execution. It works like sub2, except that it subtracts the 1D second dataset from each column of the current 2D spectrum.
### Subtract a 1D spectrum from each row

This option selects the command sub1d2 for execution. It subtracts a 1D dataset from each row of the current 2D spectrum. Unlike sub2, it does not compare intensities.
### Subtract a 1D spectrum from each column

This option selects the command sub1d1 for execution. It subtracts a 1D dataset from each column of the current 2D spectrum. Unlike sub1, it does not compare intensities.
The sub* commands only work on the real data. After using them, the imaginary data no longer match the real data and cannot be used for phase correction.
If the second dataset has not been defined yet, the sub* commands open the add/subtract (adsu) dialog box. 
The adsu command can be used on 1D or 2D data. It recognizes the data dimensionality and opens a dialog box with the appropriate options and parameters.


## INPUT FILES

<dir>/data/<user>/nmr/<name>/<expno>/pdata/<procno>/
2rr - real processed 2D data
<dir2>/data/<user2>/nmr/<name2>/<expno2>/pdata/<procno2>/
1r - real processed 1D data


## OUTPUT FILES

<dir>/data/<user>/nmr/<name>/<expno>/pdata/<procno>/
2rr - real processed 2D data
auditp.txt - processing audit trail


## USAGE IN AU PROGRAMS

SUB2
SUB1
SUB1D2
SUB1D1


## SEE ALSO

add2d, mul2d, addser
© 2025 Bruker BioSpin GmbH & Co. KG
