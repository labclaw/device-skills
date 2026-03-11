# run

**Category:** Commands > Miscellaneous > Run a Program

## NAME

**run** - Open dialog for starting macro, AU, Jython or serial


## DESCRIPTION

The command run opens the run dialog window:
 
This dialog box has various options, each of which selects a certain command for execution.
### Open the file explorer

This option selects the command expl for execution. It opens the File Explorer showing the processed data files (the files in the procno directory) of the active data set. Under Linux the KDE konqueror will be opened. If no data set is open in the TopSpin data area, the Explorer will show the users home directory. expl allows you access to the current data files as well as the entire data directory tree.
An alternative way to access data files is to right-click inside the data window and select Files in the appearing popup menu.
### Open Command Prompt/Shell

This option selects the command shell for execution. It opens a Windows Command Prompt or Linux Shell, depending on your operating system.
### Serial Processing

This option selects the command serial for execution. It opens a dialog window where you can set up and start data processing of a series of data sets using TopSpin commands, macros or Jython programs.
### Execute an AU program

This option selects the command xau for execution. It opens the AU dialog box showing a list of available AU program. Here you can select an AU program and click Execute to execute it. xau can also be entered on the command line in which case you can specify the AU program as an argument.
### Execute a Jython program

This option selects the command xpy for execution. It prompts you for the path name of a Jython program. Enter this path name and click OK to execute the Jython program.
### Execute a Macro

This option selects the command xmac for execution. It opens the Macro dialog box showing a list of available macros. Here you can select macro and click Execute to execute it. xmac can also be entered on the command line in which case you can specify the macro as an argument.
### Open a text editor

This option selects the command edtext for execution. It opens an empty text file with the TopSpin editor. The file can be stored in any directory.


## SEE ALSO

expl, shell, edau, xau, xpy, xmac, edtext
© 2025 Bruker BioSpin GmbH & Co. KG
