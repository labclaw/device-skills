# dalias

**Category:** Commands > Miscellaneous > Dataset Handling

## NAME

**dalias** - Create an alias name for a dataset (nD)


## DESCRIPTION

The Alias Tab in Topspin allows to work with short dataset names (aliases) for frequently used data. Each alias is linked to one dataset with fixed EXPNO and PROCNO. 
Please note, that the Alias Tab can be switched on or off in Set/Browser Settings.
The aliases may be managed through the GUI - a popup menu on the Alias Tab. An alternative option is the dalias command.
The aliases given for single datasets are different handled from the aliases in the Data Tab. They are only a placeholder for complete directories.
 
Entering the command dalias without arguments displays a help message with a summary of all options:
 
The command requires various arguments and can be used as follows:
### Create alias name for a dataset

dalias add <alias> <name> <eno> <pno> <dir>
or
dalias add <alias> <pathname> 
Note: the alias name must start with a letter!
Create the alias name <alias> for the specified dataset, e.g.:
dalias add e1h exam1d_1H 1 1 C:/bio
or
dalias add e1h C:/bio/data/guest/nmr/exam1d_1H/1/pdata/1
### Show dataset path or name behind alisases

dalias pr <alias>
Print the name, expno, procno and dir of the specified alias name.
dalias prgen <alias>
Print the full pathname of the specified alias name.
dalias prall
Print the name, expno, procno, dir of all alias names.
dalias prallgen
Print the full data path of all alias names.
### Remove alias names

dalias rm <alias>
Remove the specified alias name.
dalias rmall
Remove all alias names.
Note: Removing aliases does not remove corresponding data from disk.


## SEE ALSO

re, rep commandr
© 2025 Bruker BioSpin GmbH & Co. KG
