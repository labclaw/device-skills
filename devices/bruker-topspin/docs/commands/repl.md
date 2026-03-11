# rel, repl

**Category:** Commands > Miscellaneous > Dataset Handling

## NAME

**rel** - Open a list of expnos / procnos in current dataset (nD)

**repl** - Open a list of procnos in the current expno (nD)


## DESCRIPTION

The command rel lists the available expnos/procnos under the current data set and allows to select and open one:
 
If the current data set contains only one expno/procno combination, it is automatically opened.
The dialog offers the following buttons:
Open : Open the highlighted dataset (equivalent to pressing the Enter key)
Print  : Print the dialog contents
Save : Print the dialog contents to a text file
Cancel : Close the dialog
The command repl works like rel, except that it lists the available procnos under the current expno.
Another dateset can also be selected directly on the command line, e.g.: 
rel 2 - selects the expno 2 of the current dataset. 
repl 2 - selects the procno 2 of the current dataset.
 
If no data set is open, rel refers to the last active dataset. If no data set has been open yet during the current TopSpin session, an error message is displayed.


## SEE ALSO

re, rep commandr, new
© 2025 Bruker BioSpin GmbH & Co. KG
