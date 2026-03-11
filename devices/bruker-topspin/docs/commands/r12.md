# r12, r13, r23, slice

**Category:** Commands > Process > Advanced

## NAME

**r12** - Read F1-F2 plane from 3D data and store as 2D data

**r13** - Read F1-F3 plane from 3D data and store as 2D data

**r23** - Read F2-F3 plane from 3D data and store as 2D data

**slice** - Open the read slice/plane command dialog box (2D, 3D)


## DESCRIPTION

The commands r12, r13 and r23 read a plane from 3D processed data and store it as a 2D data set. 
When entered without arguments, they open the dialog box shown:
 
This dialog box offers several options, each of which selects a certain command for execution. Furthermore, you must specify three parameters:
1. Plane orientation: F1-F2, F1-F3 or F2-F3. This parameter determines which of the commands r12, r13 or r23 is executed.
2. Plane number: The maximum plane number is the SI value in the direction orthogonal to the plane orientation.
3. Destination procno: The procno where the output 2D dataset is stored.
For each option described below, a table shows how the processing state of the output 2D data relates to the processing state of the input 3D data. This table can be interpreted as follows:
1. FID: Data have not been Fourier transformed (time domain data)
2. Real:- Data have been Fourier transformed but imaginary data do not exist 
3. real+imag: Data have been Fourier transformed and imaginary data exist
Depending on the processing state, an extracted plane can be further processed with 2D processing commands like xf2, xf1, xf2p etc.
### Extract an orthogonal spectrum plane in F1-F2

This option selects the command r12 for execution. It reads an F1-F2 plane from a 3D data set and stores it as a 2D data set:
3D data 
processed with 
3D input data
2D output data
F3
F2
F1
F2
F1
tf3
real+imag
FID
FID
FID
FID
tf3, tf2
real
real+imag
FID
real+imag
FID
tf3, tf2, tf1
real
real
real+imag
real
real+imag
tf3, tf1, tf2
real
real+imag
real
real+imag
real
r12 input/output data
### Extract an orthogonal spectrum plane in F1-F3

This option selects the command r13 for execution. It reads an F1-F3 plane from a 3D data set and stores it as a 2D data set:
3D data 
processed with 
3D input data
2D output data
F3
F2
F1
F2
F1
tf3
real+imag
FID
FID
real+imag
FID
tf3, tf2
real
real+imag
FID
real
FID
tf3, tf2, tf1
real
real
real+imag
real
real+imag
tf3, tf1, tf2
real
real+imag
real
real
real
r13 input/output data
### Extract an orthogonal spectrum plane in F2-F3

This option selects the command r23 for execution. It reads an F2-F3 plane from a 3D data set and stores it as a 2D data set:
3D data 
processed with 
3D input data
2D output data
F3
F2
F1
F2
F1
tf3
real+imag
FID
FID
real+imag
FID
tf3, tf2
real
real+imag
FID
real
real+imag
tf3, tf2, tf1
real
real
real+imag
real
real
tf3, tf1, tf2
real
real+imag
real
real
real+imag
r23 input/output data
 
The parameters required by r12, r13 and r23 can also be entered as arguments on the command line. In that case, the command is executed without opening the dialog box. For example, r12 10 999 reads an F1-F2 plane number 10 and stores it in procno 999. Note that the Plane orientation is not specified as an argument but part of the command name. 
The commands r12, r13 and r23 are equivalent to the commands rpl 12, rpl 13 and rpl 23, respectively (see the description of rpl).


## INPUT FILES

<dir>/data/<user>/nmr/<name>/<expno>/pdata/<procno>/
3rrr, 3irr, 3rir, 3rri, 3iii - processed 3D data


## OUTPUT FILES

<dir>/data/<user>/nmr/<name>/<expno>/pdata/<procno>/
2rr, 2ir, 2ri, 2ii - processed 2D data
auditp.txt - processing audit trail


## USAGE IN AU PROGRAMS

R12(plane, procno). For example R12(64, 1)
R13(plane, procno). For example R13(64, 1)
R23(plane, procno). For example R23(64, 1)
© 2025 Bruker BioSpin GmbH & Co. KG
