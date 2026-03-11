# dirf, dirs, dirser, dir2d, browse

**Category:** Commands > Miscellaneous > Dataset Handling

## NAME

**dirf** - List acquired (raw) data (1D)

**dirs** - List processed data (1D)

**dirser** - List acquired (raw) data (2D, 3D)

**dir2d** - List processed data (2D, 3D)

**browse** - Open the data directory commands dialog box (nD)


## DESCRIPTION

The dir* commands display a list of data sets according to certain criteria. They can be started from the command line or from the browse dialog box:
 
1. Click OK to display the raw data.
 
The commands dirf, dirs, dirser and dir2d display a list of data sets. This list only includes data sets which contain certain data files. As opposed to commands like dir and dira, they do not show empty data sets. You can mark one or more datasets in the list and click:
Display 
To display the data in the current data window.
or
Display in new window 
To display the data in a new data window.
When multiple entries were marked, they will be shown in one data window in multi-display mode.
### 1D raw data

This option selects the command dirf for execution. It lists 1D data sets which contain raw data showing a separate entry for each experiment number (expno). Each entry shows the data set NAME, EXPNO, ACQU.DATA and SIZE.
### 1D processed data

This option selects the command dirs for execution. It lists 1D data sets which contain processed data showing a separate entry for each processed data number (procno). Each entry shows the data set NAME, EXPNO, PROCNO, PROC.DATA and SIZE.
### 2D/3D raw data

This option selects the command dirser for execution. It lists 2D and 3D data sets which contain raw data showing a separate entry for each experiment number (expno). Each entry shows the data set NAME, EXPNO, ACQU.DATA and SIZE.
### 2D processed data

This option selects the command dir2d for execution. It lists 2D data sets which contain processed data showing a separate entry for each processed data number (procno). Each entry shows the data set NAME, EXPNO, PROCNO, PROC.DATA and SIZE.


## INPUT FILES

<dir>/data/<user>/nmr/<name>/<expno>/
fid - 1D raw data
ser - 2D or 3D raw data
<dir>/data/<user>/nmr/<name>/<expno>/pdata/<procno>/
1r, 1i - processed 1D data
2rr, 2ir, 2ri, 2ii - processed 2D data
3rrr, 3irr, 3rir, 3iir - processed 3D data


## SEE ALSO

dir, dira, dirp, dirdat, browse, find, search, re, rep, rew, repw, reb
© 2025 Bruker BioSpin GmbH & Co. KG
