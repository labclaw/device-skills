# edtune

**Category:** Commands > Acquire > Shim

## NAME

**edtune** - Edit tune file for automatic shimming with the tune command


## DESCRIPTION

The command edtune opens a dialog box where you can edit an existing tune file or create a new one (see the next figure). The tune files you see listed here are delivered with TopSpin.
 
The following buttons are available:
1. Edit probe tunefile
1. Edit the probe specific tune file as it was created with edprosol.
2. Edit
1. Edit the selected tune file. The file will be opened in an editable window which offers a Save and a Save as button. The latter one allows you to save the tune file under a different name, i.e. create a new tune file.
3. Execute
1. Execute the selected tune file. This will run the command tune.
4. Delete
1. Delete the selected tune file.
5. Cancel
1. Quit the edtune dialog box.
Tune files are used by the tune command which performs automatic shimming.
1. edtune can take one argument and can be used as follows:
1. edtune <name>
- Edits the specified tune file. If the specified file does not exist, an error message will appear.
- The format of a tune file is described for the tune command.
### INPUT AND OUTPUT FILES

1. <tshome>/exp/stan/nmr/lists/group/
1. example - standard tune file
2. my_tunefile - user defined tune file
2. <tshome>/conf/instr/<instrum>/prosol/<probeID>/
1. tunefile - probe dependent tune file (input for edtune => Probe tunefile)


## SEE ALSO

tune, rsh, wsh, vish, delpar, delgp, delsh
© 2025 Bruker BioSpin GmbH & Co. KG
