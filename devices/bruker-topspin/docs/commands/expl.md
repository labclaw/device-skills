# expl

**Category:** Commands > Miscellaneous > Run a Program

## NAME

**expl** - Open File Explorer showing files of current processing data directory


## DESCRIPTION

The command expl opens the Explorer (Windows) or Konqueror/Nautilus (Linux) showing the processed data files (the files in the procno directory) of the active dataset.
 
If no data set is open in the TopSpin data area, the users home directory will be shown. 
expl allows you to access to the current data files as well as the entire data directory tree. An alternative way to access the processed data files is to right-click in the data window and select Files...
The command can also be used with one argument:
expl top
Opens the TopSpin home directory
expl home
Opens the User home directory
expl spect
Opens the directory <tshome>/conf/instr/<curinst>
expl prop
Opens the User properties directory
expl <absolute_path>
Opens the directory <absolute_path>
 
expl can also be started from File | Run a Program.


## SEE ALSO

run 
© 2025 Bruker BioSpin GmbH & Co. KG
