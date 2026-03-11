# hist

**Category:** Commands > Manage > Commands

## NAME

**hist** - Show the TopSpin history and protocol


## DESCRIPTION

The command hist (like ptrace) displays the TopSpin protocol and history files. These files only contain information if the protocol function is active. You can switch on this function as follows:
1. Click Setup preferences  or enter set.
2. Click the Miscellaneous group in the left part of the dialog box.
3. Check the item Record commands in protocol file.
The protocol file contains TopSpin startup information and command information on interface level. The history file contains command information on the level of the command interpreter and application modules. It also contains error messages.
 
Note that the history files and most protocol files are emptied when you restart TopSpin. The old content of the history and history_j files are copied to history.old and history_j.old so that after a second restart of TopSpin the history of the previous TopSpin session is lost. In case of problems, you should first make a copy of these files before you restart TopSpin. Note that a long TopSpin session, especially with automation, can create very large history and protocol files. Therefore, it is useful to regularly check the size of the files or simply restart TopSpin after each (automation) session.


## OUTPUT FILES

<tshome>/prog/curdir/<user>/
history - TopSpin history file
history_i.txt - TopSpin protocol file


## SEE ALSO

ptrace
© 2025 Bruker BioSpin GmbH & Co. KG
