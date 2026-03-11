# edau, xau, delau, xauw

**Category:** Commands > Miscellaneous > Run a Program

## NAME

**edau** - Edit an AU program

**xau** - Execute an AU program

**delau** - Delete an AU program

**xauw** - Execute an AU program and wait for it to finish (no parallel actions possible)


## DESCRIPTION

When entered without arguments, the AU program commands edau, xau and delau all open the AU program dialog box:
 
The dialog offers the following buttons:
Edit 
Edit the selected AU program. Equivalent to double-clicking the AU program name or entering edau <name> on the command line.
Compile 
Compile the selected AU program. Equivalent to entering cplbruk <name> on the command line.
Execute 
Execute the selected AU program. Equivalent to entering <name> or xau <name> on the command line.
Close 
Close the dialog.
The AU programs are selected from the Source directory as selected at the upper right of the dialog. Note that:
<tshome>\exp\stan\nmr\au\src - contains all Bruker AU programs
<tshome>\exp\stan\nmr\au\src\user - contains all user defined AU programs
### The File menu

The File menu offers the following functions:
New...
Create a new AU program. Note that new AU programs can only be stored in user defined directories.
Save as...
Save the selected AU program under a new name. A dialog will appear where you can specify the AU program name and destination directory.
Delete...
Delete the selected AU program. Note that both the source and binary AU program are deleted.
Rename...
Rename the selected AU program. Note that both the source and binary AU program are deleted. Note that only user defined AU programs can be renamed.
Export...
Export the selected AU program to an arbitrary directory. A file dialog will appear where you can select/specify the destination directory.
Import...
Import an AU program from an arbitrary directory. A file dialog will appear where you can select/specify the AU program.
### The Options menu

 
The Options menu offers the following functions:
Show Comment
Toggles between displaying AU programs with/without comments.
Show Date
Toggles between displaying AU programs with/without date.
Sort by Date
Sort AU programs by date when selected.
Manage Source Directories
Add/modify AU programs source directories. AU programs will be searched for in the order of the directories specified.
Export Sources...
Opens a dialog to export an entire AU program library to a user defined directory. Note the difference to the Export function under the File menu (see below).
When you edit a Bruker AU program, it is shown in view mode which means it cannot be modified. However, if you click Save as.. and store it under a different name, the stored file is automatically opened in edit mode. When you edit a User defined AU program, it is opened in edit mode and can be modified.
When edau is entered on the command line with an argument, the corresponding AU program will be opened. If it does not exist it will be created. If the argument contains wildcards, the AU dialog box is opened showing the matching AU programs. For example, edau a* displays all AU programs which start with a.
Bruker AU programs must be installed once with expinstall before they can be opened with edau. The installation must be repeated when a new version of TopSpin is installed.
edau uses the editor which is defined in the TopSpin User Preferences. To change it, enter set, click Miscellaneous and select or change the editor.
AU programs are usually executed simply by entering their names. The command xau is only needed in three cases:
1. The AU program has not been compiled yet.
2. A TopSpin command with the same name exists.
3. To call an Au program from another AU program (using the macro XAU).
AU programs run in background and several of them can run simultaneously. The command kill can be used to stop a running (or hanging) AU program.
For details on writing, compiling, and executing AU programs please refer to the AU reference manual:
In the menu click Help | Manuals | Programming Manuals | AU programming
 
### INPUT/OUTPUT FILES

<tshome>/exp/stan/nmr/au/src/* 
AU program source files.
<tshome>/prog/au/bin/* 
AU program executable binary files


## SEE ALSO

compileall, cplbruk, cpluser, (expinstall)
© 2025 Bruker BioSpin GmbH & Co. KG
