# edshape, delshape

**Category:** Commands > Parameter Handling

## NAME

**edshape** - Edit shape files

**delshape** - Delete shape files


## DESCRIPTION

When entered without arguments, the Shape File commands edshape and delshape all open the AU program dialog box:
 
On the top right of the upcoming window, you can find the sources where the listed Shape files are stored. With pull-down menu and click on the respective Source you can change the Shape file source to let them be listed in this dialog. 
 
The AU programs are selected from the Source directory as selected at the upper right of the dialog. Note that:
<tshome>\exp\stan\nmr\lists\wave contains all Bruker Shape files.
<tshome>\exp\stan\nmr\lists\wave\user contains all user defined Shape files.
The dialog offers the following buttons: 
Close
Close the dialog.
Edit
Edit the selected Shape file. Equivalent to double-clicking the Shape file name or entering edshape <name> on the command line.
 
Display
Display the selected Shape file. The Shape Tool will be opened for display the current Shape file. The result can be seen in the following figure:
 
### The File menu

The File menu offers the following functions:
New...
Create a new Shape file. Note that new Shape files can only be stored in user defined directories.
Save as...
Save the selected Shape files under a new name. A dialog will appear where you can specify the Shape file name and destination directory.
Delete...
Delete the selected Shape file.
Rename...
Rename the selected Shape file. Note that only user defined Shape files can be renamed.
Export...
Export the selected Shape file to an arbitrary directory. A file dialog will appear where you can select/specify the destination directory.
Import...
Import a Shape file from an arbitrary directory. A file dialog will appear where you can select/specify the Shape file.
Close 
Close the Shape file lists.
### The Options menu

The Options menu offers the following functions:
Show Comment
Toggles between displaying Shape file with/without comments (see the figure below).
Show Date
Toggles between displaying Shape file with/without date (see figure below).
Sort by Date
Sort Shape files by date when selected:
 
### Manage Source Directories

Add/modify Shape files source directories. Shape files will be searched in the order of the specified directories.
### INPUT/OUTPUT FILES

The default directory for user-defined files is:
<tshome>/exp/stan/nmr/lists/<listname>/user


## SEE ALSO

edlist, dellist command
© 2025 Bruker BioSpin GmbH & Co. KG
