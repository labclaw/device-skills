# wpar, edpar

**Category:** Commands > Parameter Handling

## NAME

**wpar** - Write a parameter set (nD)

**edpar** - Read, write, rename and delete a parameter set combined in one command


## DESCRIPTION

The command wpar stores the parameters of the current data set in a parameter set. It opens a dialog box where you can select an experiment name and then click Write.. to store it or click Write New... to store them under a new name:
 
A newly created parameter set can now be stored with additional meta-information (Sample Class etc.). When reading or writing parameter sets, this information can be used as a filter to reduce the number of shown parameter sets. 
The command edpar opens a similar dialog as the rpar and wpar commands. The difference to wpar and rpar is that with edpar parameter sets can be read, written, written new and edited, whereas rpar only offer reading possibilities for parameter sets and wpar gives the possibility to write and create (button Write New ...) parameter sets. Same possibilities as edpar offers the command delpar.
The following buttons are available:
Write... 
Write the parameters of the current data set to the selected parameter set. 
Write New... 
Write the parameters of the current data set to a new experiment name. You will be prompted to enter this name. 
Close 
Close the wpar dialog.
The parameters are written to the Source directory as selected at the upper right of the dialog.
wpar can be used with arguments:
1. wpar <name> 
2. Opens a dialog box where you can select individual parameter files of the parameter set <name>. Upon clicking OK, this file is copied to the current data set.
3. wpar <name> acqu
4. Reads the acquisition parameters (file acqu) of the parameter set <name> to the current data set.
5. wpar <name> proc
6. Reads the processing parameters (file proc) of the parameter set <name> to the current data set.
7. wpar <name> acqu proc
8. Reads the acquisition and processing parameters (files acqu and proc) of the parameter set <name> to the current data set.
9. wpar <name> all
10. Reads all parameter files of the parameter set <name> to the current data set.
The first argument may contain wildcards, e.g.:
1. wpar C* shows all parameter sets beginning with the letter C
Bruker standard experiment names should not be used when storing your own experiments with wpar. The reason is that they are overwritten when a new version of TopSpin is installed.
wpar is often used in the following way:
1. Define a new data set with the command new.
2. Enter rpar to read a Bruker parameter set which defines the experiment you want to do. 
3. Modify the acquisition parameters (with eda) to your preference and run the acquisition.
4. Modify processing parameters (with edp) to your preference and process the data.
5. Store the parameters with wpar under a new experiment name for general usage.
The reason is that is that rpar with two arguments is used in automation.


## INPUT FILES

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


## OUTPUT FILES

<tshome>/exp/stan/nmr/par/user/<1D parameter set>
acqu - acquisition parameters
proc - processing parameters
outd - output device parameters
<tshome>/exp/stan/nmr/par/user/<2D parameter set>
acqu - F2 acquisition parameters
acqu2- F1 acquisition parameters
proc - F2 processing parameters
proc2 - F1 processing parameters
outd - output device parameters
clevels - 2D contour levels
3D parameter sets also contain the files acqu3 and proc3 for the third direction.
Note that in TopSpin 2.0 and older, the user subdirectory does not exist and user defined parameter sets are stored in:
<tshome>/exp/stan/nmr/par
The same location as Bruker parameter sets.


## USAGE IN AU PROGRAMS

WPAR(name, type)


## SEE ALSO

rpar, expinstall
© 2025 Bruker BioSpin GmbH & Co. KG
