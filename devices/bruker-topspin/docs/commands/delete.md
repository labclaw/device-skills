# del, dela, delp, deldat, delete

**Category:** Commands > Miscellaneous > Dataset Handling

## NAME

**del** - Delete a complete dataset (nD)

**dela** - Delete acquired (raw) data (nD)

**delp** - Delete processed data (nD)

**deldat** - Delete acquired data (possibly together with processed data) from certain dates (nD)

**delete** - Open the delete commands dialog box (nD)


## DESCRIPTION

Delete commands can be started from the command line or from the delete dialog box. The latter is opened with the command delete:
 
This dialog box has several options, each of which selects a certain command for execution.
The commands del, dela, delp and deldat allow you to display a list of datasets. Such a list includes datasets containing raw and/or processed data as well as empty datasets which only contain parameter files. You can select one or more datasets in the list to mark them for deletion and then click OK to delete them.
### An entire dataset with all expnos/procnos

This option selects the command del for execution. It lists datasets, only showing the dataset name. To delete data, select one or more datasets and click OK. The marked datasets are entirely deleted, including data files, parameter files and the data name directory.
 
### Acquisition data

This option selects the command dela for execution. It. It lists datasets showing a separate entry for each experiment number (expno). Each entry shows the dataset NAME, EXPNO, ACQU.DATA and SIZE. Datasets which do not contain raw data are displayed with ACQU.DATA none. To delete data, select one or more datasets and check one of the following check boxes:
1. Delete the selected EXPNOs with all their PROCNOs to delete the expno directory.
2. Delete the raw data files of the selected EXPNOs.
### Processed data

This option selects the command delp for execution. It lists datasets showing a separate entry for each processed data number (procno). Each entry shows the dataset NAME, EXPNO, PROCNO, PROC.DATA and SIZE. Datasets which do not contain processed data are displayed with PROC.DATA none. To delete data, select one or more data sets and check one of the following check boxes: 
1. Delete the selected PROCNOs to delete the procno directories.
2. Delete the processed data files of the selected PROCNOs.
 
### Data acquired at certain dates

This option selects the command deldat for execution and lists all data sets chronologically.
When started from the command line, del* commands can take one argument which may contain wild cards. Examples:
dela exam1d* - List all data sets whose name starts with exam1d 
dela exam1d??? - List all data sets whose name is exam1d plus three extra characters
del* commands only list and delete the datasets of current user. The current user here refers to the user part of the data path of the currently selected dataset.
Please distinguish:
1. The user part of the data path.
2. The owner of the data set.
3. The user who runs TopSpin.
Usually these three things are the same, i.e. a user works on his own data. However, the user part of the data path can be any character string and does not have to correspond to a user account on the computer. Furthermore, the user who runs TopSpin might work on someone else’s data. In this case, he/she may or may not have the permission to delete this dataset. In the latter case, the del* commands will not delete the dataset but show an error message instead.


## OUTPUT FILES

### For dela: Delete raw data files of the selected EXPNOs:

<dir>/data/<user>/nmr/<name>/<expno>/
audita.txt - acquisition audit trail
### For delp: Delete processed data files of the selected PROCNOs:

<dir>/data/<user>/nmr/<name>/<expno>/pdata/<procno>/
auditp.txt - processing audit trail


## SEE ALSO

delf, dels  
© 2025 Bruker BioSpin GmbH & Co. KG
