# rhpp, rhnp, rvpp, rvnp

**Category:** Commands > Process > Advanced

## NAME

**rhpp** - Calculate horizontal (F2) positive projection (2D)

**rhnp** - Calculate horizontal (F2) negative projection (2D)

**rvpp** - Calculate vertical (F1) positive projection (2D)

**rvnp** - Calculate vertical (F1) negative projection (2D)

**proj** - Open the projection commands dialog box (2D, 3D)


## DESCRIPTION

The projection commands can be started from the command line or from the projection dialog box selecting the corresponding command.
 
This dialog box has several options, each of which selects a certain command for execution.
### Read positive projection (on rows)

This option selects the command rhpp for execution. It calculates the full positive projection of a 2D spectrum in the F2 direction and stores it as a 1D dataset.
### Read positive projection (on columns)

This option selects the command rvpp for execution. It calculates the full positive projection of a 2D spectrum in the F1 direction and stores it as a 1D dataset.
### Read negative projection (on rows)

This option selects the command rhnp for execution. It calculates the full negative projection of a 2D spectrum in the F2 direction and stores it as a 1D dataset.
### Read negative projection (on columns)

This option selects the command rvnp for execution. It calculates the full negative projection of a 2D spectrum in the F1 direction and stores it as a 1D dataset.
 
A projection is a 1D trace where every point has the highest intensity of all points of the corresponding orthogonal trace in the 2D spectrum. 
r*p commands only take the projection of the first quadrant data (file 2rr) and store it as real 1D data (file 1r)
r*p commands can be started from the command line. When entered without arguments, a dialog window is displayed: 
 
The required arguments can also be specified on the command line. 
rhpp <procno> stores the projection under the specified procno of the current data name
rhpp <procno> n stores the projection under the specified procno but does not change the display to that procno
The three other r*p command have the same syntax.
A special case is the command rvpp or rvnp on a hypercomplex 2D dataset (MC2 ≠ QF) that has been processed in F2 only. Suppose you would perform the following command sequence:
xf2 - to process the data in F2 only
s si - to check the F1 size of the 2D data, click Cancel.
s mc2 - to check status MC2 (≠ QF), click Cancel.
rvpp - to store the F1 projection in ~TEMP and change to that dataset.
s si - to check the size of the resulting 1D dataset, click Cancel .
You will see that the size of the 1D data is only half the F1 size of the 2D data. The reason is that rvpp unshuffles the input data (file 2rr). As such, rvpp behaves like the command rsc. If you want to prevent the unshuffling of the input data (file 2rr), you can use the following trick. Set the status parameter MC2 to QF before you run rvpp :
s mc2  , click QF
Then, the size of the 1D data will be the same as the F1 size of the 2D data.


## INPUT FILES

<dir>/data/<user>/nmr/<name>/<expno>/pdata/<procno>/
2rr - real processed 2D data


## OUTPUT FILES

<dir>/data/<user>/nmr/<name>/<expno>/pdata/<procno>/
1r - 1D spectrum containing the projection
auditp.txt - processing audit trail
If the commands are used without arguments, the files are stored in:
<dir>/data/<user>/nmr/~TEMP/1/pdata/1/


## USAGE IN AU PROGRAMS

RHPP(procno)
RHNP(procno)
RVPP(procno)
RVNP(procno)
For all these macros counts that if procno = -1, the projection is written to the dataset ~TEMP


## SEE ALSO

f2projn, f2projp, f2sum, f1sum, f2disco, f1disco
© 2025 Bruker BioSpin GmbH & Co. KG
