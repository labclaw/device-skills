# edpul, edcpd, edpy, edpy3, edmac

**Category:** Commands > Parameter Handling

## NAME

**edpul** - Edit any pulse program

**edcpd** - Edit composite pulse decoupling (CPD) programs

**edpy** - Edit Jython programs

**edpy3** - Edit Python 3 programs

**edmac** - Edit macros


## DESCRIPTION

The commands edpul, edcpd, edpy and edmac open a dialog that lists pulse programs, CPD programs, Python programs and macros, respectively. The dialog offers various functions like edit, create, search, delete, import, and export. These programs are stored in a database.
The dialog for the command edpul is shown in the figure below. The dialogs for edcpd, edpy and edmac have the same menu but can offer different buttons.
 
Search List Box
Database items can be searched in two possible ways, as can be chosen from the list box at the upper left of the dialog:
1. Search in names - to search for a string in the item names.
2. Search in text - to search for a string in item text contents.
Search Text Field
Here you can enter one or more characters of the item name or contents. The following wildcards can be used:
* : for zero or more occurrences of any character
? : for a single occurrence of any character
Here are some examples:
1. *xxx* finds all occurrences of xxx.
2. ??xxx* finds all occurrences of xxx preceded by two arbitrary characters.
A search mask for item names can also be specified on the command line, e.g. edpul ??cos*
Conditional List boxes
These list boxes are only offered if the selected item has the corresponding item defined. For example, most high-resolution pulse programs have a Class and Dim definition but not Type or SubType definition.
Class
Allows to show a particular class of items or all items (any).
Dim
Allows to show items of a particular dataset dimension or all items (any).
Type
Allows to show a particular type of items or all items (any).
SubType
Allows to show items of a particular subtype of items or all items (any).
### Available Buttons

All 
Show items of all classes, dimensions, types, and subtypes.
Edit 
Opens the selected item (pulse program, CPD program, ...) in the TopSpin text editor or viewer, depending on whether the selected item is writable for the current user or not (see below). Writable items can be modified in the editor. They can be saved from the editor as follows:
In the menu click File | Save [Ctrl-s]
Write-protected items can be saved under a different name as follows:
In the menu click File | Save as..
The new item is owned by and writable for the current TopSpin user.
Items can also be created /modified with an external (non-TopSpin) editor. They can then be imported in the database as described below.
Graphical Edit (for pulse programs only)
Opens a symbolic graphical display of the selected pulse program, with the possibility of graphical editing.
Set PULPROG (for pulse programs only)
Sets the acquisition parameter PULPPROG to the name of the selected pulse program.
### The Options menu

The Options menu offers the following functions:
Show Comment 
Toggles between displaying items with/without comments.
Show Date 
Toggles between displaying items with/without date.
Sort by Date 
Sort items by date when selected.
Manage Source Directories
Add/modify item source directories. Items will be searched for in the order of the directories specified.
Export Sources... 
Opens a dialog to export an entire item library to a user defined directory. Note the difference to the Export function under the File menu (see below).
### The File menu

The File menu offers the following functions:
New 
Opens an empty editor for creating a new item, e.g. a pulse program. Saving the text will prompt you for the item name and will store it in the database. The owner of the item will be the current TopSpin user.
Save As...
Saves the selected item under a new name. Opens a dialog where you can select a source directory and specify a filename.
Delete... 
Deletes all selected items from the database (if not write protected). You will be prompted to confirm deletion.
Rename...
Allows to rename the selected item in the database (if not write protected).
Export...
Exports one or more items to text files. To do that:
1. Mark one or more items in the dialog.
2. Click File | Export 
3. Select or enter the storage directory and click Export...
The selected item(s) will be stored under their original names, provided there is write permission.
Import...
Imports external item (e.g. pulse program) files into the database and lists it in the dialog. First, it opens a file browser where you can navigate to a directory containing your text files (which may have been created outside of TopSpin). Select or enter the desired files in the browser and click Import. The dialog will be updated showing the imported item. Please note that:
1. The owner of imported items is the current TopSpin user.
2. Write-protected items in the database cannot be overwritten by importing items with the same name.
3. Writable items with the same name are only overwritten by import, after user confirmation.
4. 
Close 
Close the dialog
### Current TopSpin User

The current TopSpin user can be one of the following users:
1. The system login user, i.e. the user who started TopSpin. This is the case if TopSpin internal login/logoffis disabled.
2. The current internal TopSpin user. This is the case if TopSpin internal login/logoff is enabled.
To enable/disable TopSpin internal login/logoff, enter set and click Change to the right of the item Setup users for internal....
### Write Protection

An item (e.g. pulse program) in the database is write-protected (cannot be modified or deleted), if its owner is Bruker or if its owner is not the current TopSpin user.
### Owner

Each item (e.g. pulse program) in the database has an assigned owner. Please note the following aspects:
1. For all items (e.g. pulse programs) delivered by Bruker, the owner is Bruker.
2. The description of the Edit, New and Import functions above shows how an owner is assigned to an item.
3. Bruker-owned items are write protected (cannot be changed/deleted). They may, however, be copied to a new name (see Edit above).
4. Pulse programs names MUST be unique across all owners! The database cannot contain two pulse programs with same name, even if their assigned owners are different.
### Using Pulse/CPD Programs from a User-defined Directory

When you run an acquisition, using commands like zg, gs, .., the required pulse or CPD program is normally taken from the database. You might, however, want to use pulse programs from an arbitrary, user-defined directory, e.g. for development purposes. You can do this by setting the operating system environment variables PULPPROG_DIR and CPDPROG_DIR. They can be set in two different ways, with or without a minus sign, determining the item search order.
Examples:
1. PULPPROG_DIR=c:\mydir 
2. Will cause zg, gs... to search for the pulse program in the database and then, if it did not find it there, in c:\mydir. So the database is searched first, then the defined directory.
3. PULPPROG_DIR=-c:\mydir 
4. Will cause zg, gs... to search for the pulse program in c:\mydir, and then, if it did not find it there, in the database. So the directory is searched first, then the database.
Each time a pulse or CPD program is taken from a directory (rather than from the database), a message is written into the history file (to be viewed with command hist).
Please note:
1. The commands edpul and edcpd do not evaluate the above environment variables.
2. When TopSpin is running as a client that controls a remote spectrometer, the remote environment variables are evaluated.
### About Macros

Macros are text files which contain a sequence of TopSpin commands and/or Jython commands. A simple macro for processing and plotting the current dataset is: 
# 1D processing macro
em
ft
apk
sref
autoplot # plot according to Plot Editor layout
TopSpin commands can be inserted in lower or uppercase letters. Jython commands must be entered as follows:
xpy <name> 
All text behind a # character is treated as comment. 
### About Jython and Python3 programs

Python programming is extensively described in a separate document available under:
Click Help | Manuals | Programming Manuals | Python programming
### INPUT AND OUTPUT FILES

The default directories for pulse programs, CPD programs, Macros and Python programs are listed below, just like Bruker default directories:
<tshome>/exp/stan/nmr/lists/pp/* - Bruker pulse programs
<tshome>/exp/stan/nmr/lists/pp/user/* - User defined pulse programs
<tshome>/exp/stan/nmr/lists/cpd/* - Bruker/CPD programs
<tshome>/exp/stan/nmr/lists/cpd/user/* - User CPD programs
<tshome>/exp/stan/nmr/lists/mac/* - Bruker TopSpin macros
<tshome>/exp/stan/nmr/lists/mac/user/* - User TopSpin macros
<tshome>/exp/stan/nmr/py/* - Bruker Jython programs
<tshome>/exp/stan/nmr/py/user/* - User Jython programs


## SEE ALSO

edlist, dellist, delpul, delcpdd, xmac, xpy, xpy3
© 2025 Bruker BioSpin GmbH & Co. KG
