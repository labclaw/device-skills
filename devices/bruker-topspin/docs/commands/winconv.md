# winconv

**Category:** Commands > Miscellaneous > Dataset Handling

## NAME

**winconv** - Convert WINNMR type data to TopSpin data (1D)


## DESCRIPTION

The command winconv converts Bruker Win-nmr data to TopSpin format. It opens a browser where you can navigate to the Win-NMR input datasets. A Win-nmr dataset is a directory with several files. Each file has:
1. A number as file name.
2. The extension .FID, .1R, .1I, .AQS or .FQS for raw data, processed real data, processed imaginary data, acquisition parameters and processing parameters, respectively. 
Just select any of these files and click convert. This will open the dialog box shown:
 
Here you can specify the TopSpin destination dataset. The data path fields are initialized as follows:
NAME - the Win-nmr data directory
EXPNO - the first three digits of the Win-nmr data name
PROCNO - the second three digits of the Win-nmr data name
DIR - DIR of the active TopSpin data set
USER - USER of the active TopSpin data set
Specify a data path or accept the initial values and click OK to start the conversion. To display the data set, open it from the TopSpin browser or use the command re.


## INPUT FILES

<name>/ 
num.FID - Win-nmr raw data
num.1R - Win-nmr real processed data
num.1I - Win-nmr imaginary processed data
num.1I - Win-nmr imaginary processed data
num.AQS - Win-nmr acquisition parameters
num.FQS - Win-nmr processing parameters
num.TIT - Win-nmr title


## OUTPUT FILES

<dir>/data/<user>/nmr/<name>/<expno>/
fid - TopSpin 1D raw data
acqu - TopSpin acquisition parameters
acqus - TopSpin acquisition status parameters
 
<dir>/data/<user>/nmr/<name>/<expno>/pdata/1
1r - real processed data
1i - imaginary processed data
proc - TopSpin processing parameters
procs - TopSpin processing status parameters


## SEE ALSO

conv, fconv, jconv, vconv, convdta
© 2025 Bruker BioSpin GmbH & Co. KG
