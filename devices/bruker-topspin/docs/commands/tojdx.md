# tojdx

**Category:** Commands > Miscellaneous > Dataset Handling

## NAME

**tojdx** - Convert dataset to JCAMP-DX format (1D, 2D)


## DESCRIPTION

The command todjx converts a TopSpin data set to JCAMP-DX format. JCAMP-DX is a standard ascii exchange format for spectroscopic data.
When tojdx is entered without argument, it will open a dialog box in which you can enter the required information.
 
This dialog box includes:
### Name of the archive file

The file name should have the extension .dx. This allows you to open it in TopSpin with drop & drag. Default is the data set name with the extension .dx.
### Directory of the archive file

Any directory. Default is the users home directory.
### Type of archive file

For JCAMP format, you can choose between the following archive types:
1. FIX (=0): Table format.
2. PACKED (=1): No spaces between the intensity values.
3. SQUEEZED (=2): The sign of the intensity values is encoded in the first digit.
4. DIFF/DUP (=3): The difference between successive values is encoded, suppressing repetition of successive equal values.
The default value is DIFF/DUP.
### Include these data types

For the included data types, you have the following choices:
1. FID (=0): Raw data.
2. RSPEC (=1): Real processed data.
3. RSPEC+ISPEC (=2): Real and imaginary processed data.
4. PARAMS (=3): Parameter files.
5. FID+RSPEC+ISPEC (=4): Raw data + real and imaginary processed data.
6. FID+ALL_PROCNOS (=5): Raw data +real and imaginary processed data of all PROCNO’s under the current EXPNO.
7. ALL_EXPNOS_DIM_1_2 (=6): Raw data +real and imaginary processed data of all EXPNO’s under the current NAME.
8. FID+RSPEC+ISPEC (=4): Raw and real + imaginary processed data.
9. ALL PROCNOS (=5): All procnos under current expno.
10. ALL EXPNOS (=6): All expnos under current name.
The default value is RSPEC+ISPEC (=2)
The above information can be entered as arguments of tojdx as follows:
tojdx <path> <data> <file> <title> <origin> <owner>
Note that in this case three extra arguments are required. The arguments have the following meaning:
<path>: Name and directory of the archive file.
<data>: Data types included.
<file>: Type of archive file.
<title>: The title as it appears in the output file: enter a character string.
<origin>: The origin as it appears in the output file: enter a character string.
<owner>: The owner as it appears in the output file: enter a character string.
 
The default title is the plot title as defined with edti. If no plot title is defined the data name is taken as default. The default origin and owner are taken from the acquisition status parameter files (acqus). If you enter an * character as argument, the default value will be used. 
Here are some examples:
tojdx C:\temp\mydata.dx 0 2 mytitle BRUKER guest
tojdx D:\nmr\mydata.dx 0 2 mytitle * *
tojdx * 1 * mytitle MYORIGIN joe 
tojdx F:\users\guest\mydata.dx * * * * *


## INPUT FILES

### For 1D and 2D data:

<tshome>/prog/curdir/<user>/
curdat - current data definition
### For 1D data:

<dir>/data/<user>/nmr/<name>/<expno>/
fid - 1D raw data
acqus - acquisition status parameters
 
<dir>/data/<user>/nmr/<name>/<expno>/pdata/<procno>
1r - real processed 1D data
1i - imaginary processed 1D data
proc - processing status parameters
procs - processing status parameters
### For 2D data:

<dir>/data/<user>/nmr/<name>/<expno>/
ser - 2D raw data
acqus - F2 acquisition status parameters
acqu2s - F1 acquisition status parameters
 
<dir>/data/<user>/nmr/<name>/<expno>/pdata/<procno>
2rr - real processed 2D data
proc - F2 processing parameters
proc2 - F1 processing parameters
procs - F2 processing status parameters
proc2s - F1 processing status parameters


## OUTPUT FILES

<path name>/<mydata.dx> - TopSpin data in JCAMP-DX format


## USAGE IN AU PROGRAMS

TOJDX(name, data, mode, title, origin, owner) 
For example TOJDX("/tmp/mydata.dx", 0, 2, "mytitle", "BRUKER", "joe")


## SEE ALSO

fromjdx, tozip, totxt
© 2025 Bruker BioSpin GmbH & Co. KG
