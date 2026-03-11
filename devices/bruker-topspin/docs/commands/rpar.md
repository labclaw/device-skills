# rpar

**Category:** Commands > Parameter Handling

## NAME

**rpar** - Read a parameter set (nD)


## DESCRIPTION

The command rpar reads a parameter set (experiment) to the current data set. When it is entered without arguments, rpar opens a dialog box with a list of available parameter sets. All Bruker parameter sets now have a description that is automatically shown together with the name. There are new filter options to reduce the number of shown parameter sets to those matching the filter criteria. The values for each filter criterion are stored in the parameter set directory in the file comment.txt. As an example, for the parameter set C13APT the following values are stored.
$COMMENT=13C Attached Proton Test
$SAMPLE_CLASS=Small Molecules , Polymers, Peptides
$APPLICATION=Structure Characterization
$DIM=1D
$PHYSICAL_AGGREGATION=Liquid
$OBS_NUCLEI=13C
$OTHER_NUCLEI=1H
$EXPERIMENT_TYPE=APT
$EXPERIMENT_SPECIFIC_TAGS=Edited
$RECOMMEND=yes
 
Here you can select a Source directory at the upper right of the dialog, then select a parameter set and click Read... to read it to the current data set. This will open the dialog:
 
In this dialog, you can select the file types to be read, or just click OK to read all types.
The following buttons are available:
Read... 
Read the parameters of the selected parameter set to the current data set.
Close 
Close the rpar dialog.
rpar can be used with arguments:
1. rpar <name> 
2. Opens a dialog box where you can select individual parameter files of the parameter set <name>. Upon clicking OK, this file is copied to the current data set.
3. rpar <name> acqu 
4. Reads the acquisition parameters (file acqu) of the parameter set <name> to the current data set.
5. rpar <name> proc 
6. Reads the processing parameters (file proc) of the parameter set <name> to the current data set.
7. rpar <name> acqu proc 
8. Reads the acquisition and processing parameters (files acqu and proc) of the parameter set <name> to the current data set.
9. rpar <name> all 
10. Reads all parameter files of the parameter set <name> to the current data set.
11. rpar <name> all remove=yes 
12. Reads all parameter files of the parameter set <name> to the current data set, deleting all data files and all status parameters.
The first argument may contain wildcards, e.g.:
1. rpar C* shows all parameter sets beginning with the letter C.
The remove=yes argument can be used together with any other argument.
After reading a parameter set with rpar, you can modify parameters of the various types with the commands:
1. eda - acqu parameters
2. edp - processing parameters
Note that Bruker parameter sets contain all parameter types, but user defined parameter sets contain only those parameter types that were stored when the parameter set was created (see wpar). Usually, however, user defined parameter sets are also stored with all parameter types.
Bruker parameter sets are delivered with TopSpin and installed with the command expinstall.
User defined parameter sets are created with wpar, which stores the parameters of the current data set under a new or existing parameter set name.
rpar allows to read parameters sets of various dimensionalities, 1D, 2D, etc. If the dimensionality of the current data set and the parameter set you want to read are the same, e.g. both 1D, the current parameter files are overwritten. If the current data set contains data (raw and/or processed data), these are kept. Furthermore, the status parameters are kept so you still have a consistent data set. However, as soon as you process the data, the new processing parameters are used, the processed data files are overwritten, and the processing status parameters are updated. When you start an acquisition, the new acquisition parameters are used, the raw data are overwritten, and the acquisition status parameters are updated. 
If the dimensionality of the current data set and the parameter set you want to read are different, the current parameter files are overwritten, all data files are deleted, and status parameters are kept. If the dimensionality is reduced, the superfluous parameter files are deleted.


## INPUT FILES

<tshome>/exp/stan/nmr/par/<1D parameter set>/
acqu - acquisition parameters
proc - processing parameters
outd - output device parameters
<tshome>/exp/stan/nmr/par/<2D parameter set>/
acqu - F2 acquisition parameters
acqu2- F1 acquisition parameters
proc - F2 processing parameters
proc2 - F1 processing parameters
outd - output device parameters
clevels - 2D contour levels
3D parameter sets also contain the files acqu3 and proc3 for the third direction.


## OUTPUT FILES

<dir>/data/<user>/nmr/<1D data name>/<expno>/
acqu - acquisition parameters
<dir>/data/<user>/nmr/<1D data name>/<expno>/pdata/<procno>/
proc - processing parameters
outd - output device parameters
<dir>/data/<user>/nmr/<2D data name>/<expno>/
acqu - F2 acquisition parameters
acqu2 - F1 acquisition parameters
<dir>/data/<user>/nmr/<2D data name>/<expno>/pdata/<procno>/
proc - F2 processing parameters
proc2 - F1 processing parameters
outd - output device parameters
clevels - 2D contour levels
The default directory for user defined parameter sets is:
<tshome>/exp/stan/nmr/par/user


## USAGE IN AU PROGRAMS

RPAR(name, type)


## SEE ALSO

wpar, edpar commande, delpar, expinstall
© 2025 Bruker BioSpin GmbH & Co. KG
