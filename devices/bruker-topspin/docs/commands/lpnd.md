# lpnd

**Category:** Commands > Process > Advanced

## NAME

**lpnd** - nD linear prediction (≥ 3D)


## DESCRIPTION

The command lpnd performs a linear prediction of data with dimension ≥3D. It takes one argument, the direction to be processed. If no argument is specified on the command line, it is requested:
 
lpnd works on data that have already been Fourier transformed in the specified direction, e.g. with ftnd. Since linear prediction is normally performed on a unfiltered FID, the data should first be processed with ftnd with WDW = no, and then with lpnd while WDW is set to the desired window function.
lpnd performs the following steps in the specified direction:
1. Inverse Fourier transform (if imaginary data do not exist, they are automatically created with Hilbert transform).
2. Regular processing including:
1. Linear prediction according to ME_mod, NCOEF
2. Window multiplication according to WDW
3. Fourier transform
Linear prediction is a valuable method for improving the resolution of nD data with small TD values and often truncated FIDs. The effect of linear prediction in one direction can, however, be distorted by modulations introduced by other, untransformed, directions. Therefore, it is a good idea to first process the data in all directions and then perform lpnd. This entire procedure, including the correct window handling, is automatically performed by the command ftnd dlp (delayed linear prediction). However, if you want both backward and forward prediction, the latter must be done with lpnd. In this case, you have to perform the following steps:
1. Backward prediction with ftnd while ME_mod=LPbr or LPbc and WDW=no.
2. Forward prediction with lpnd while ME_mod=LPfr or LPfc and WDW set to the desired window function. 
For more information, see the description of ftnd.
### INPUT AND OUTPUT PARAMETERS

See ftnd


## INPUT FILES

### For 4D data:

<dir>/data/<user>/nmr/<name>/<expno>/pdata/<procno>/
4rrrr - processed 4D data
proc - F4 processing parameters
proc2 - F3 processing parameters
proc3 - F2 processing parameters
proc4 - F1 processing parameters
For 3D data, the input data file is 3rrr whereas the proc4 does not exist. For data of dimension n where n ≥ 5, input data files are named nr and ni, e.g. 5r, 5i, 6r, 6i etc.


## OUTPUT FILES

### For 4D data:

<dir>/data/<user>/nmr/<name>/<expno>/pdata/<procno>/
4rrrr - processed 4D data
procs - F4 processing status parameters
proc2s - F3 processing status parameters 
proc3s - F2 processing status parameters
proc4s - F1 processing status parameters
For 3D data, the output data file is 3rrr whereas proc4s does not exist. For data of dimension n where n ≥ 5, output data files are named nr and ni, e.g. 5r, 5i, 6r, 6i etc.


## SEE ALSO

ftnd 
© 2025 Bruker BioSpin GmbH & Co. KG
