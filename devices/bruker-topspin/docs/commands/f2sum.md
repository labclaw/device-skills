# f2sum, f1sum, proj

**Category:** Commands > Process > Advanced

## NAME

**f2sum** - Calculate partial sum in F2 (2D)

**f1sum** - Calculate partial sum in F1 (2D)

**proj** - Open the projection commands dialog box (2D, 3D)


## DESCRIPTION

The proj command open the projection commands dialog box.
 
This dialog box has several options, each of which selects a certain command for execution.
### Calculate sum (of rows)

This option selects the command f2sum for execution. It calculates the sum of all rows within a region specified by the parameters. The result is divided by the number of rows. This means, that in the fact a mean row is calculated.
### Calculate sum (of columns)

This option selects the command f1sum for execution. It calculates the sum of all columns within a region specified by the parameters. The result is divided by the number of columns. This means, that in the fact a mean column is calculated.
The calculated column is stored under the specified Destination procno.
The Required parameter Display projection can be set to:
1. on 2D to display the calculated projection with the 2D dataset. The current 2D dataset remains the active dataset. 
2. as 1D to display the calculated projection as a 1D dataset. The active dataset changes to the destination procno. 
The required parameters can also be specified as arguments on the command line. As an example we use the command f2sum here. 
f2sum <firstrow> prompts for lastrow and stores the sum under data name ~TEMP
f2sum <firstrow> <lastrow> stores the specified sum under data name ~TEMP
f2sum <firstrow> <lastrow> <procno> stores the specified sum under the specified procno of the current data name
f2sum <firstrow> <lastrow> <procno> n stores the specified sum under the specified procno of the current data name but does not change the display to this procno


## INPUT FILES

<dir>/data/<user>/nmr/<name>/<expno>/pdata/<procno>/
2rr, 2ir, 2ri, 2ii - processed data


## OUTPUT FILES

<dir>/data/<user>/nmr/<name>/<expno>/pdata/<procno>/
1r, 1i- 1D spectrum containing the sum
auditp.txt - processing audit trail


## USAGE IN AU PROGRAMS

F2SUM(firstrow, lastrow, procno)
F1SUM(firstcol, lastcol, procno)
For both macros counts that if procno = -1, the sum is written to the dataset ~TEMP


## SEE ALSO

f2disco, f1disco, f2projn, f2projp, f1projn, f1projp, rhpp, rhnp, rvpp, rvnp
© 2025 Bruker BioSpin GmbH & Co. KG
