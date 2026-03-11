# delf, dels, delser, del2d, deli

**Category:** Commands > Miscellaneous > Dataset Handling

## NAME

**delf** - Delete acquired (raw) data (1D)

**dels** - Delete processed data (1D)

**delser** - Delete acquired (raw) data (2D, 3D)

**del2d** - Delete processed data (2D, 3D)

**deli** - Delete imaginary processed data (nD)

**delete** - Open the delete commands dialog box (nD)


## DESCRIPTION

Delete commands can be started from the command line or from the delete dialog box. The latter is opened with the command delete:
 
This dialog box has several options, each of which selects a certain command for execution.
The commands delf, dels, delser, del2d and deli display a list of data sets. Such a list only includes data sets which contain data files. As opposed to commands like del and dela, they do not show empty data sets. You can select one or more data sets to mark them for deletion and then click OK to actually delete them.
### 1D raw data

This option selects the command delf for execution. It lists 1D datasets which contain raw data showing a separate entry for each experiment number (expno). Each entry shows the dataset NAME, EXPNO, ACQU.DATA and SIZE. To delete data, select one or more data sets and check one of the following check boxes: 
1. Delete selected EXPNOs to delete the expno directory.
2. Delete raw data files of the selected EXPNOs.
 
### 1D processed data

This option selects the command dels for execution. It lists 1D datasets which contain processed data showing a separate entry for each processed data number (procno). Each entry contains the data set NAME, EXPNO, PROCNO, PROC.DATA and SIZE. To delete data, select one or more data sets and check one of the following check boxes:
1. Delete the selected PROCNOs to delete the procno directories.
2. Delete processed data files of the selected PROCNOs.
### 2D/3D raw data

This option selects the command delser for execution. It lists 2D and 3D data sets which contain raw data showing a separate entry for each experiment number (expno). Each entry shows the data set NAME, EXPNO, ACQU.DATA and SIZE. To delete data, select one or more data sets and check one of the following check boxes: 
1. Delete selected EXPNOs to delete the expno directory.
2. Delete raw data files of the selected EXPNOs.
### 2D processed data

This option selects the command del2d for execution. It lists 2D data sets which contain processed data showing a separate entry for each processed data number (procno). Each entry shows the data set NAME, EXPNO, PROCNO, PROC.DATA and SIZE. To delete data, select one or more data sets and check one of the following check boxes: 
1. Delete selected PROCNOs to delete the procno directories.
2. Delete processed data files of the selected PROCNOs.
### Imaginary processed data

This option selects the command deli for execution. It lists data sets which contain 1D, 2D or 3D imaginary data showing a separate entry for each processed data number (procno). Each entry shows the dataset NAME, EXPNO, PROCNO, PROC.DATA and SIZE. Only the imaginary processed data files are deleted. Raw data, processed data and parameter files are kept. To delete data, mark one or more data sets and check:
Delete imaginary processed data of the selected PROCNOs. 
When started from the command line, del* commands can take one argument which may contain wild cards. Examples:
delf exam1d* 
List all data sets whose name starts with exam1d 
delf exam1d???
List all data sets whose name is exam1d plus three extra characters
del* commands only list and delete the data sets of current user. The current user here refers to the user part of the data path of the currently selected data set. Please distinguish: 
1. The user part of the data path.
2. The owner of the dataset.
3. The user who runs TopSpin.
Usually these three things are the same, i.e. a user works on his own data. However, the user part of the data path can be any character string and does not have to correspond to a user account on the computer. Furthermore, the user who runs TopSpin might work on someone else’s data. In this case, he/she may or may not have the permission to delete this data set. In the latter case, the del* commands will not delete the data set but show an error message instead.


## OUTPUT FILES

### For delf/delser: Delete raw data files of the selected EXPNOs:

<dir>/data/<user>/nmr/<name>/<expno>/
audita.txt - acquisition audit trail
### For dels/del2d/deli: Delete processed data files of the selected PROCNOs:

<dir>/data/<user>/nmr/<name>/<expno>/pdata/<procno>/
auditp.txt - processing audit trail


## SEE ALSO

del, dela  
© 2025 Bruker BioSpin GmbH & Co. KG
