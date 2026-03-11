# pknd

**Category:** Commands > Process > Adjust Phase

## NAME

**pknd** - nD phase correction (≥ 3D)


## DESCRIPTION

The command pknd performs a phase correction of data of dimension ≥3D, applying the values of PHC0 and PHC1. It takes one argument, the direction to be corrected. If no argument is specified on the command line, it is requested:
 
Before you execute pknd, the phase values must first be determined, for example on a 2D plane. You can do that by typing xfb on the nD data to process a plane, do a phase correction on the resulting the 2D dataset and store the phase values in the nD dataset.
Note that phase correction normally requires the existence of imaginary data. Usually, however these do not exist for data of dimension ≥ 4. Therefore, pknd automatically creates temporary imaginary data using Hilbert transform. Actually, the command processes 2D planes of an nD dataset, performing a series of xht2 - xf2p or xht1 - xf1 commands.
On 3D data, the commands pknd 3, pknd 2 and pknd 1 are equivalent to tf3p, tf2p and tf1p, respectively.


## INPUT PARAMETERS

Set by the user with edp or by typing phc0, phc1 etc.
PHC0 - zero order phase correction value (frequency independent) 
PHC1 - first order phase correction value (frequency dependent) 
### OUTPUT PARAMETERS

Can be viewed with dpp or by typing s phc0, s phc1 etc.:
PHC0 - zero order phase correction value (frequency independent) 
PHC1 - first order phase correction value (frequency dependent)


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

tf1, tf2, tf3, xfbp, xf2p, xf1p, xht2, xht1
© 2025 Bruker BioSpin GmbH & Co. KG
