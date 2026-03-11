# cmdindex

**Category:** Commands > Miscellaneous > TopSpin Interface

## NAME

**cmdindex** - Open the command index


## DESCRIPTION

The command cmdindex opens a command index dialog box:
 
It displays all TopSpin commands which can be entered from the command line with a one-line description for each command. Select one or more commands for further actions. The following actions are available:
Help 
Open the HTML Help page of the selected command. This is equivalent to double-clicking the command.
Execute
Execute the selected command or commands.
New Macro
Create a new macro and append commands from the list or enter commands manually.
Append
Append the (first) selected command to the command line. The appended command can be edited and executed. Useful for commands with many arguments such as re.
Save Macro
The selected command(s) are stored as a macro. You will be prompted for the macro name. To edit this macro, enter edmac <macro-name>. To execute it, just enter the name on the command line.
Find
Find a character string in the command index.


## INPUT FILES

<tshome>/classes/prop
cmdindex_main.prop - command index properties file
<tshome>/prog/docu>/english/xwinproc/html
*.html - TopSpin command help files


## OUTPUT FILES

<tshome>/exp/stan/nmr/lists/mac/
* - Macros (created by cmdindex and Save Macro..)


## SEE ALSO

cmdhist 
© 2025 Bruker BioSpin GmbH & Co. KG
