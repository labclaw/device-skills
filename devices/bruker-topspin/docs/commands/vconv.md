# vconv

**Category:** Commands > Miscellaneous > Dataset Handling

## NAME

**vconv** - Convert Varian type data to TopSpin data (1D, 2D, 3D)


## DESCRIPTION

The command vconv converts Varian data, which were measured with the Vnmr program, to TopSpin format. 
 
It opens a browser where you can navigate to the Varian input data file. Just select the desired file and click VNMR data conversion. This will open the dialog box shown:
Here you can specify the TopSpin destination dataset and click OK to start the conversion. 
The vconv source and destination data can also be entered on the command line. Here are some examples:
vconv vdata.fid 
searches for vdata.fid in the directory defined by the environment variable VNMR (can be set with the TopSpin command env set VNMR=<path>). When the specified input data are found, the dialog window shown in the figure above will appear. Here, you can specify the output data set.
vconv <path>/vdata.fid 
as above, except that the source data are searched for in the directory <path> 
vconv vdata.fid <name> <expno> <dir> <user> 
Here, the destination data set is specified as command line arguments. The procno is automatically set to 1. If the data set specification is incomplete, the dialog window shown in the figure above will appear.
Note that the extension .fid of the Vnmr dataset is not obligatory.
vconv converts all Vnmr parameters which have a TopSpin equivalent. First, the Vnmr parameter SEQFIL is interpreted. If it is set to a certain name, vconv checks the existence of a TopSpin parameter set with that name. If it exists, it is copied to the destination dataset. If it does not exist, a standard parameter set (standard1D for 1D data) is copied. Then vconv converts all Vnmr parameters which have a TopSpin equivalent and overwrites the values of the parameter set which was previously copied. The parameters of the TopSpin parameter set which do not have a Vnmr equivalent keep their original values. If you frequently convert Vnmr data, with typical values of SEQFIL, you might want to create the TopSpin parameter sets with the corresponding names. This can be done by reading a standard parameter set with rpar, modify it with eda and edp and then store it with wpar.
### NMR parameter equivalence between Bruker and Varian software

VNMR 
XWIN-NMR / TopSpin
VNMR 
XWIN-NMR / TopSpin
ct
NS(status)
rfl/rfp
OFFSET
d1
D1
rfl1/rfp1
OFFSET(2D)
date
DATE
rfl2/rfp2
OFFSET(3D)
dfrq
BF2
rp
PHC0
dfrq2
BF3
rp/lp
PHC0/PHC1
dmf
P31
rp1/lp1
PHC0/PHC1(2D)
dn
DECNUC
rp2/lp2
PHC0/PHC1(3D)
dn2
DECBNUC
seqfil
PULPROG
dof
O2
sfrq
BF1
dof2
O3
solvent
SOLVENT
fb
FW
spin
RO
fn
SI
ss
DS
lp
PHC1
sw
SW_h
np
TD
sw1
SW_h(2D)
nt
NS(foreground)
sw2
SW_h(3D)
pp
P3
temp
TE
pslabel
AUNM
tn
NUCLEUS
pw
P0
tof
O1
pw90
P1
 
 
 
The original Vnmr parameter file procpar is stored in the TopSpin processed data directory. You can check this ascii file for possible parameters which could not be converted.
The table above shows the Varian parameters and their TopSpin equivalent.
vconv can handle Unity and Gemini data acquired with Vnmr 4.1 or newer. Data from older Varian spectrometers or acquired with older software versions might also work but have not been tested by Bruker.


## INPUT FILES

<dir>/data/<user>/nmr/<vdata>.fid
or 
<VNMR>/<vdata>.fid/
fid - the Vnmr raw data
procpar - the parameters
text - title file


## OUTPUT FILES

<dir>/data/<user>/nmr/<name>/<expno>/
fid - TopSpin 1D raw data
acqu - TopSpin acquisition parameters
acqus - TopSpin acquisition status parameters
audita.txt - acquisition audit trail
<dir>/data/<user>/nmr/<name>/<expno>/pdata/1
proc - TopSpin processing parameters
procs - TopSpin processing status parameters
procpar - Vnmr parameter file
For 2D and 3D data, the raw data are stored in the file ser and the additional parameter files acqu2(s), acqu3(s), proc2(s) and proc3(s)are created.


## USAGE IN AU PROGRAMS

VCONV(vname, xwname, xwexpno, xwdisk, xwuser)


## SEE ALSO

jconv, fconv, conv
© 2025 Bruker BioSpin GmbH & Co. KG
