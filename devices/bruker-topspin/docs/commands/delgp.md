# delpar, delgp, delsh

**Category:** Commands > Acquire > Shim

## NAME

**delpar** - Delete parameter sets

**delgp** - Delete gradient programs

**delsh** - Delete shim files


## DESCRIPTION

The del* commands without argument open a dialog box with a list of the available entries. They are equivalent to the respective edit commands rpar, edgp and rsh. From the dialog box, you can select entries and click Delete to delete them. Alternatively, you can use the del* command with one argument, for example:
delpar myparset
Deletes the parameter set myparset. 
 
### NOTE

Note that only user defined entries can be removed.
### INPUT FOLDERS

1. <tshome>/exp/stan/nmr/par - Bruker and user defined parameter sets.
2. <tshome>/exp/stan/nmr/lists/gp - Bruker and user defined gradient programs.
3. <tshome>/exp/stan/nmr/lists/bsms - shim files.


## USAGE IN AU PROGRAMS

1. DELPAR(name).
2. No AU macros are available for the other del* commands.


## SEE ALSO

edlist, dellist
© 2025 Bruker BioSpin GmbH & Co. KG
