# ptrace

**Category:** Commands > Manage > Commands

## NAME

**ptrace** - Display messages from various log files time sorted


## DESCRIPTION

The command ptrace (like hist) displays the TopSpin protocol and history files time sorted:
 
These files only contain valuable information if the protocol function is active. You can switch on this function as follows:
1. Click Setup preferences  or enter set.
2. Click the Miscellaneous group in the left part of the dialog box.
3. Check the item Record commands in protocol file.
The protocol file contains TopSpin startup information and command information on interface level. The history file contains command information on the level of the command interpreter and application modules. It also contains error messages.
Note that the files history and protocol are emptied when you restart TopSpin which means the history of the previous TopSpin session is lost. In case of problems, you should first make a copy of these files before you restart TopSpin. Note that a long TopSpin session, especially with automation can create very large history and protocol files. Therefore, it is useful to regularly check the size of the files or simply restart TopSpin after each (automation) session.


## OUTPUT FILES

<tshome>/prog/curdir/<user>/
history - TopSpin history file
history_i.txt - TopSpin protocol file
history.traffic.txt - network traffic log
stdout.dataserver.<number>.txt – data server output file
<userhome>/<.topspin-hostname>/prop/
protocol.txt - TopSpin protocol file (if TopSpin was started as topspin -client)


## SEE ALSO

hist
© 2025 Bruker BioSpin GmbH & Co. KG
