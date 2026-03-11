# f2disco, f1disco

**Category:** Commands > Process > Advanced

## NAME

**f2disco** - Calculate disco projection in F2 (2D)

**f1disco** - Calculate disco projection in F1 (2D)

**proj** - Open the projection commands dialog box (2D, 3D)


## DESCRIPTION

The proj command open the projection commands dialog box:
 
This dialog box has several options, each of which selects a certain command for execution.
### Calculate disco sum (of rows)

This option selects the command f2disco for execution. Like f2sum, it calculates the sum of all rows between firstrow and lastrow. However, for each row, the intensity at the intersection with the reference column is determined. If this intensity is positive, the row is added to the total. If it is negative, the row is subtracted from the total. 
### Calculate disco sum (of columns)

This option selects the command f1disco for execution. It works like f2disco, except that it calculates the sum of the specified columns considering the intensities at the intersections with a reference row.
The calculated disco sum is stored under the specified Destination procno.
The Required parameter Display projection can be set to:
1. on 2D to display the calculated projection with the 2D dataset. The current 2D dataset remains the active dataset. 
2. as 1D to display the calculated projection as a 1D dataset. The active dataset changes to the destination procno.
The required parameters can also be specified as arguments on the command line. As an example, we use the command f2disco here. 
f2disco <firstrow> prompts for lastrow and refrow and stores the disco projection under data name ~TEMP
f2disco <firstrow> <lastrow> <refrow> stores the specified disco projection under data name ~TEMP
f2disco <firstrow> <lastrow> <refrow> <procno> stores the specified disco projection under the specified procno of the current data name
f2disco <firstrow> <lastrow> <refcol> <procno> n stores the specified disco projection under the specified procno of the current data name but does not change the display to this procno


## INPUT FILES

<dir>/data/<user>/nmr/<name>/<expno>/pdata/<procno>/
2rr, 2ir, 2ri, 2ii - processed data


## OUTPUT FILES

<dir>/data/<user>/nmr/<name>/<expno>/pdata/<procno>/
1r, 1i- 1D spectrum containing the F1 disco projection
auditp.txt - processing audit trail


## USAGE IN AU PROGRAMS

F2DISCO(firstrow, lastrow, refcol, procno)
F1DISCO(firstcol, lastcol, refrow, procno) 
For procno = -1, the disco projection is written to the dataset ~TEMP


## SEE ALSO

f2projn, f2projp, f2sum, f1sum, rhpp, rhnp
© 2025 Bruker BioSpin GmbH & Co. KG
