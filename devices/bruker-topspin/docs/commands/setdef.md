# setdef

**Category:** General Information

## NAME

**setdef** - Configure acknowledgment of dialog windows


## DESCRIPTION

With the command setdef the settings for automatic dialog acknowledgement can be changed.
### USAGE

Display a help message
1. xcpr setdef
Display a dialog with the available sub commands.
2. xcpr setdef <sub command>
Display a dialog with the available options for the specified sub command, where <sub command> is one of ackn, beep, quest, stderr, stdout.
Sub command ackn
This defines how standard dialog windows with a simple OK button are handled.
1. setdef ackn no
Program execution continues without acknowledgment.
2. setdef ackn ok
Program execution continues only after acknowledgment.
3. setdef ackn hide
Program execution continues without acknowledgment. In addition, the dialog window is not displayed.
Sub command beep
Obsolete. There is no action related to this sub command. 
Sub command quest
This defines how question windows with an OK and a CANCEL button are handled. 
1. setdef quest ok
Program execution continues without acknowledgment assuming OK.
2. setdef quest can
Program execution continues without acknowledgment assuming CANCEL.
3. setdef quest no
Program execution continues only after acknowledgment.
Sub command stderr
This defines whether stderr (error messages from program execution) are written to a file.
1. setdef stderr off
Program error messages are not written to a file.
2. setdef stderr on
Program error messages are written to a file.
Sub command stdout
This defines whether stdout (standard messages from program execution) are written to a file.
1. setdef stdout off
Program standard messages are not written to a file.
2. setdef stdout on
Program standard messages are written to a file.
### DEFAULTS

At TopSpin start all of these settings are reset to their defaults, namely
1. setdef ackn ok
2. setdef quest no
3. setdef stderr on
4. setdef stdout on


## OUTPUT FILES

If program standard and/or error messages are written to a file, the files are in the directory
<tshome>/prog/curdir/<user>
and have the names
stdout.<pid> - standard TopSpin output file 
stderr.<pid> - standard TopSpin error file
### PROGRAMMING GUIDE

In AU programs the current state of each sub command option can be queried with
int result = CPR_exec(“setdef <sub command> ?”);
The result is 
1. sub command ackn: ‘n’ for no, ‘o’ for ok
2. sub command quest: 0 for ok, 1 for can, -1 for no
3. sub command stdout and stderr: ‘y’ for on, ‘n’ for off
4. sub command beep: ‘y’ for yes, ‘n’ for no.
© 2025 Bruker BioSpin GmbH & Co. KG
