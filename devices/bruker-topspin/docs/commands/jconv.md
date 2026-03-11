# jconv

**Category:** Commands > Miscellaneous > Dataset Handling

## NAME

**jconv** - Convert Jeol type data to Bruker TopSpin data (1D, 2D, 3D)


## DESCRIPTION

The command jconv converts Jeol raw data to TopSpin format. It opens a dialog window where you can navigate to the Jeol input data file. 
 
Just select the desired file and click JNMR data conversion. This will open the dialog box shown:
Here you can specify the TopSpin destination data set and click OK to start the conversion.
The jconv source and destination data can also be entered on the command line. Here are some examples:
jconv jdata.<ext>
Searches for jdata.<ext> in the directory defined by the environment variable JNMR (can be set with the TopSpin command env set JNMR=<path>). When the specified input data are found, the dialog window shown in the figure above will appear. Here, you can specify the output data set.
 
jconv <path>/jdata.<ext>
As above, except that the source data are searched for in the directory <path> 
 
jconv jdata.<ext> <name> <expno> <dir> <user>
Here, the destination dataset is specified as command line arguments. The procno is automatically set to 1. If the data set specification is incomplete, the dialog window shown in the figure above will appear.
jconv can handle Jeol EX, GX and ALPHA raw data and works on 1D, 2D and 3D data. Processed data cannot be converted. The conversion of FX FID data has been implemented. FX data must have a numerical extension (like in proton.1) and the name must be specified on the command line, e.g. jconv proton.1. No parameter file is needed for the conversion, the most relevant parameters are extracted from the header of the data file.
Data type
Extension of data file
Extension of parameter file
EX
.gxd
.gxp
GX
.gxd
.gxp
ALPHA
.nmf
.txt
DELTA(new)
.jdf
.jdf
DELTA(old)
.bin
.hdr
FX
.num (an integer number)
no parameter file
 
jconv converts all Jnmr parameters which have a TopSpin equivalent. First, the Jnmr parameter EXMOD is interpreted. If it is set to a certain name, jconv checks the existence of a TopSpin parameter set with that name. If it exists, it is copied to the destination data set. If it does not exist, a standard parameter set (standard1D for 1D data) is copied. Then jconv converts all Jnmr parameters which have a TopSpin equivalent and overwrites the values of the parameter set which was previously copied. The parameters of the TopSpin parameter set which do not have a Jnmr equivalent keep their original values. If you frequently convert Jnmr data, with typical values of EXMOD, you might want to create the TopSpin parameter sets with the corresponding names. This can be done by reading a standard parameter set with rpar, modify it with eda and edp and then store it with wpar.


## INPUT FILES

<jdata.ext> - Jeol raw data


## OUTPUT FILES

<dir>/data/<user>/nmr/<name>/<expno>/
fid - TopSpin 1D raw data
acqu - TopSpin acquisition parameters
acqus - TopSpin acquisition status parameters
audita.txt - acquisition audit trail
 
<dir>/data/<user>/nmr/<name>/<expno>/pdata/1/
proc - TopSpin processing parameters
procs - TopSpin processing status parameters
jnm original Jeol parameter file
For 2D and 3D data, the raw data are stored in the file ser and the additional parameter files acqu2(s), acqu3(s), proc2(s) and proc3(s) are created.


## USAGE IN AU PROGRAMS

JCONV(jname, uxname, uxexp, uxdisk, uxuser)


## SEE ALSO

vconv, fconv, conv, winconv, convdta
© 2025 Bruker BioSpin GmbH & Co. KG
