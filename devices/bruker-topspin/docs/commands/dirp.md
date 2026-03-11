# dir, dira, dirp, dirdat, browse

**Category:** Commands > Miscellaneous > Dataset Handling

## NAME

**dir** - List all dataset names from current data directory (nD)

**dira** - List acquired (raw) data (nD)

**dirp** - List processed data (nD)

**dirdat** - List data acquired at certain dates (nD)

**browse** - Open the data directory commands dialog box (nD)


## DESCRIPTION

Commands to list data directories can be started from the command line or from the directory dialog box. The latter is opened with the command browse:
 
This dialog box has several options, each of which selects a certain command for execution.
The commands dir, dira, dirp and dirdat display all data sets containing raw and/or processed data as well as empty data sets which only contain parameter files. You can mark one or more entries in the list and click:
Display selected data - to display the data in the current data window.
or 
Display selected data in a new window - to display the data in a new data window.
When multiple entries were marked, they will be shown in one data window in multi-display mode.
### An entire data set with all EXPNOs/PROCNOs

This option selects the command dir for execution. It lists data sets, showing the data names only.
 
### Acquisition data

This option selects the command dira for execution. It lists data sets showing a separate entry for each expno. Each entry shows the data set NAME, EXPNO, ACQU.DATA and SIZE. The entry file refers to the data files and can be fid (1D raw data), ser (2D or 3D raw data) or no raw data.
 
### Processed data

This option selects the command dirp for execution. It lists data sets showing a separate entry for each processed data number (procno). Each entry shows the data set NAME, EXPNO, PROCNO, PROC.DATA and SIZE. The type refers to the name of the data files and can be 1r 1i (processed 1D data), 2rr 2ir 2ri 2ii (2D raw data), 3rrr, 3rri, .. (processed 3D data) or no processed data.
 
### Data acquired at certain dates

This option selects the command dirdat for execution and lists all data sets chronologically.
 
When started from the command line, dir* commands can take one argument which may contain wild cards. Examples:
dir exam1d*
List all data sets whose name starts with exam1d.
dir exam1d???
List all data sets whose name is exam1d plus three extra characters.


## INPUT FILES

<dir>/data/<user>/nmr/<name>/<expno>/
fid - 1D raw data
ser - 2D or 3D raw data 
<dir>/data/<user>/nmr/<name>/<expno>/pdata/<procno>/
1r, 1i - processed 1D data
2rr, 2ir, 2ri, 2ii - processed 2D data
3rrr, 3irr, 3rir, 3iir - processed 3D data


## SEE ALSO

dirf, dirs, dirser, dir2d, browse, find, search, open, re, rep, rew, repw, reb
© 2025 Bruker BioSpin GmbH & Co. KG
