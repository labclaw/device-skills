# fconv

**Category:** Commands > Miscellaneous > Dataset Handling

## NAME

**fconv** - Convert Felix type data to Bruker TopSpin type data (1D)


## DESCRIPTION

The command fconv converts Felix data to TopSpin format. It opens a dialog window where you can navigate to the Felix input data file. Just select the desired file and click convert. 
 
This will open the dialog box shown:
 
Here you can specify the TopSpin destination data set and click OK to start the conversion.
The fconv source and destination data can also be entered on the command line. Here are some examples:
fconv <path>/fdata 
When the specified input data are found, the dialog window shown above will appear. Here, you can specify the output data set.
fconv fdata <name> <expno> <dir> <user> 
Here, the destination data set is specified as command line arguments. The procno is automatically set to 1. If the data set specification is incomplete, the dialog window shown above will appear.
fconv can convert raw and processed Felix data.
Note that fconv converts 1D data only.


## INPUT FILES

<fdata_name> - Felix data file


## OUTPUT FILES

<dir>/data/<user>/nmr/<name>/<expno>/
fid - TopSpin 1D raw data
acqu - TopSpin acquisition parameters
acqus - TopSpin acquisition status parameters
audita.txt - acquisition audit trail
 
<dir>/data/<user>/nmr/<name>/<expno>/pdata/1/
proc - TopSpin processing parameters
procs - TopSpin processing status parameters


## SEE ALSO

vconv, jconv, conv, winconv, convdta
© 2025 Bruker BioSpin GmbH & Co. KG
