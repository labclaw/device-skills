# f2projn, f2projp, f1projn, f1projp

**Category:** Commands > Process > Advanced

## NAME

**f2projn** - Calculate negative partial projection in F2 (2D)

**f2projp** - Calculate positive partial projection in F2 (2D)

**f1projn** - Calculate negative partial projection in F1 (2D)

**f1projp** - Calculate positive partial projection in F1 (2D)

**proj** - Open the projection commands dialog box (2D, 3D)


## DESCRIPTION

The proj command open the projection commands dialog box.
 
This dialog box has several options, each of which selects a certain command for execution.
### Calculate positive projection (of rows)

This option selects the command f2projp for execution. It calculates the positive partial 1D projection of the 2D dataset in the F2 direction
### Calculate positive projection (of columns)

This option selects the command f1projp for execution. It calculates the positive partial 1D projection of the 2D dataset in the F1 direction
### Calculate negative projection (of rows)

This option selects the command f2projn for execution. It calculates the negative partial 1D projection of the 2D dataset in the F2 direction
### Calculate negative projection (of columns)

This option selects the command f1projn for execution. It calculates the negative partial 1D projection of the 2D dataset in the F1 direction
The calculated projection is stored under the specified Destination procno.
The Required parameter Display projection can be set to:
1. on 2D to display the calculated projection with the 2D dataset. The current 2D dataset remains the active dataset. 
2. as 1D to display the calculated projection as a 1D dataset. The active dataset changes to the destination PRONCNO.
The required parameters can also be specified as arguments on the command line. As an example we use the command f2projn here. 
f2projn <firstrow> prompts for lastrow and stores the projection under data name ~TEMP
f2projn <firstrow> <lastrow> stores the specified projection under data name ~TEMP
f2projn <firstrow> <lastrow> <procno> stores the specified projection under the specified procno of the current data name
f2projn <firstrow> <lastrow> <procno> n stores the specified projection under the specified procno of the current data name but does not change the display to this procno
A projection is a 1D trace where every point has the highest intensity of all points of the corresponding orthogonal trace in the 2D spectrum. Partial means that only a specified range of rows (or columns) is are evaluated, i.e. only a part of the orthogonal trace is scanned for the highest intensity. Negative projections contain only negative intensities, positive projections contain only positive intensities. 
A special case is the command f1projp or f1projn on a hypercomplex 2D dataset (MC2 ≠ QF) that has been processed in F2 only. Suppose you would perform the following command sequence:
xf2 - to process the data in F2 only.
s si - to check the F1 size of the 2D data, click Cancel.
s mc2 - to check status MC2 (≠ QF), click Cancel.
f1projp - to store the F1 projection in ~TEMP and change to that dataset.
s si - to check the size of the resulting 1D dataset, click Cancel .
You will see that the size of the 1D data is only half the F1 size of the 2D data. The reason is that f1projp unshuffles the input data (file 2rr). As such, f1projp behaves like the command rsc. If you want to prevent the unshuffling of the input data (file 2rr), you can use the following trick. Set the status parameter MC2 to QF before you run f1projp:
s mc2  , click QF
Then, the size of the 1D data will be the same as the F1 size of the 2D data.


## INPUT FILES

<dir>/data/<user>/nmr/<name>/<expno>/pdata/<procno>/
2rr - processed data


## OUTPUT FILES

<dir>/data/<user>/nmr/<name>/<expno>/pdata/<procno>/
f2projn - ascii file specifying the range of rows and the 1D data path
f2projp - ascii file specifying the range of rows and the 1D data path
f1projn - ascii file specifying the range of columns and the 1D data path
f1projp - ascii file specifying the range of columns and the 1D data path
<dir>/data/<user>/nmr/<name>/<expno>/pdata/<procno>/
1r - 1D spectrum containing the projection
auditp.txt - processing audit trail
If the commands are used with less than three arguments, the files are stored in:
<dir>/data/<user>/nmr/~TEMP/1/pdata/1/


## USAGE IN AU PROGRAMS

F2PROJN(firstrow, lastrow, procno)
F2PROJP(firstrow, lastrow, procno)
F1PROJN(firstcol, lastcol, procno)
F1PROJP(firstcol, lastcol, procno)
For all these macros counts that if procno = -1, the projection is written to the dataset ~TEMP


## SEE ALSO

f2disco, f1disco, f2sum, f1sum, rhpp, rhnp
© 2025 Bruker BioSpin GmbH & Co. KG
