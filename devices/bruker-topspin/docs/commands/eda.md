# eda

**Category:** Commands > Miscellaneous > Graphical User Interface

## NAME

**eda** - Edit acquisition parameters


## DESCRIPTION

The command eda opens a dialog box in which you can set all acquisition parameters (see the next figure).
 
Entering eda on the command line is equivalent to clicking ACQUPARS in the Tab Bar of the data window.
The following buttons are available:
 Undo the last modification. Can be used repeatedly.
 Show pulse program parameters.
 Switch to acquisition status parameters.
 Set probe/solvent dependant parameters.
 Open and set the nuclei and routing.
 Show the status of the nuclei and routing information (edasp-s). 
 Change raw dataset dimensionality (parameter PARMODE).
Collapse/expand all parameter sections.
Search for the parameter specified in the search field.
 
Inside the parameter editor, you can do the following actions:
1. Select an acquisition parameter submenu, e.g Experiment, at the left of the dialog box. The submenu is highlighted, and the corresponding parameters will appear in the right part of the dialog box.
2. Click in a parameter field, e.g. TD, to set the parameter value. It is automatically stored.
3. Hit the Tab key to jump to the next parameter field.
4. Hit Shift-Tab to jump to the previous parameter field.
5. Use the scroll bar at the right of the dialog box to move to parameters further up or down in the dialog box.
### NOTE

Note that the buttons to the right of the PULPROG parameter allow you to show the pulse program list or edit the current pulse program, respectively. This applies to all parameters that refer to a filename.
Parameters can also be set by entering their names on the command line. A dialog window will appear where you can enter the parameter value(s). For example:
td 
On a 1D data set.
 
or on a 2D data set:
 
Alternatively, you can specify the parameter value as an argument on the command line, For example; 
td 8k 
The time domain will be set to 8k.
### INPUT AND OUTPUT PARAMETERS

All acquisition parameters.


## INPUT FILES

1. <tshome>/classes/prop/
1. pared.prop - parameter properties file.
2. <tshome>/exp/stan/nmr/form/
1. acqu.e - format file for eda.
### INPUT AND OUTPUT FILES

1. <dir>/data/<user>/<name>/nmr/<expno>/
1. acqu - acquisition parameters for the acquisition (direct) direction.
2. acqu2 - acquisition parameters for F1 (2D) or F2 (3D) indirect direction.
3. acqu3 - acquisition parameters for the F1 direction (3D).


## SEE ALSO

dpa, edp
© 2025 Bruker BioSpin GmbH & Co. KG
