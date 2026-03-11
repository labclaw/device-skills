# find, search

**Category:** Commands > Miscellaneous > Dataset Handling

## NAME

**find** - Find data according to specified criteria (nD)

**search** - Find data according to specified criteria (nD)


## DESCRIPTION

The commands find and search (or Ctrl+f) allow to find TopSpin data according to various criteria. The easiest way to find data is to enter (part of) the data set name directly in the search field in the browser window.
1. Use the Show Filters function to restrict the search according to certain filter criteria. 
 
1. Enter the search items in the upper part of the dialog. Note that:
1. It will be searched for items containing the specified EXPNO, PROCNO or matching strings of title and pulse program.
2. The search is restricted to data created between the specified dates. Note that this refers to the acquisition date.
3. The Reset mask button resets the default criteria.
2. Select the Data directories to be searched in the lower part of the dialog. If no directories are selected, all will be searched.
3. Click OK to start the search and display the result.
 
Note: when exiting TopSpin, the search criteria will be saved as default.
### How to Display one of the Found Data Sets

In the search result window:
1. Click one or more data sets to select them.
2. Click Display to display the selected data set(s) in the current data window. If multiple data sets are selected they are displayed in the new data window in multiple display mode.
The search result window offers a right-click context menu with various options:
 
Display 
Display the selected data set(s) in the current data window. If multiple data sets are selected they are displayed in the same data window in multiple display mode. Equivalent to clicking the Display button or pressing Enter.
Display in New Window 
Display the selected data set(s) in a new window. If multiple data sets are selected they are displayed in the one new data window in multiple display mode.
Display as 2D Projection
Display the selected data set as a projection of the current 2D data set. A dialog will appear allowing you to choose F1-projection, F2-projection or both. If multiple data sets are selected, only the first one is considered. If the current data set is not a 2D data set, nothing happens.
Save Selection to File..
Save the list of selected data sets in a text file. First opens a file dialog where you can select or specify a file name. The saved data set list can, for example, be used for serial processing (command serial, see also Process Selected Data sets below).
Add Selection to data set group..
Add the list of selected data sets to a data set group. You will be prompted to enter the group name. The created or modified group can be accessed from the browser.
File properties
Show main data set parameters like Dimension, Pulse program, Acquisition Date, Nuclei, Spectrometer frequency and Solvent.
Files 
Show the files in the processed data directory of the selected data set.
Process Selected Data sets
Perform serial processing on the selected data sets. Opens a dialog where you can change or edit the data set list and specify the command, macro or Jython program to be executed (starts the command serial).
The Close button allows you to close the search result dialog.


## INPUT FILES

<dir>/data/<user>/nmr/<name>/<expno>/
fid - 1D raw data 
acqu - acquisition parameters
acqus - acquisition status parameters
<dir>/data/<user>/nmr/<name>/<expno>/pdata/<procno>/
1r, 1i - processed 1D data
proc - processing parameters
procs - processing status parameters
Note that these are only the main 1D data files.


## SEE ALSO

dir, dira, dirp, dirdat, browse, new, open, re, rep, rew, repw, reb
© 2025 Bruker BioSpin GmbH & Co. KG
