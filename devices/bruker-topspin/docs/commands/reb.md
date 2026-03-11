# reb

**Category:** Commands > Miscellaneous > Dataset Handling

## NAME

**reb** - Open a data browser at the level of data names (nD)


## DESCRIPTION

The command reb opens a file browser:
 
Here you see a list of data set names under the same <dir> and <user> as the currently selected data set. Note that TopSpin data are stored in a directory:
<dir>/data/<user>/nmr/<name>/<expno>/pdata/<procno>
From the browser, you can:
1. Select the data name to be displayed in the current data window
2. Move up in the data directory tree to select a different user and/or dir
3. Double-click a data name to move down the directory tree and select a desired expno/procno.
Once you have selected the desired name, expno or procno, click Display or hit Enter to display the data set in the current data window.
reb allows opening data sets stored in the following directories structures:
<mydata>/<dataname>/<expno>/pdata/<procno>
Note that this will create a copy the data set in the standard TopSpin data path:
<tshome>/data/<user>/nmr/<dataname>/<expno>/pdata/<procno>
Where <user> is the current internal TopSpin user. This copy can be processed, deleted or overwritten, even if the original data set is write protected. The original data set remains unchanged.


## SEE ALSO

open, re, rep, new, find, search
© 2025 Bruker BioSpin GmbH & Co. KG
