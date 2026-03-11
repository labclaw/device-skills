# xpy

**Category:** Commands > Miscellaneous > Run a Program

## NAME

**xpy** - Execute Jython program


## DESCRIPTION

The command xpy opens a dialog where you can select the desired Jython program:
 
Path 
Field where you can enter the full path name of the Jython program. Click Execute to run it.
Browse 
Button to open a file browser where you can enter or select the Jython program. Click Execute to run it.
 
Browse in database
Button to open a dialog showing the available Jython programs in the database:
 
Select the desired macro and click Execute. Jython programs are stored in a database. xpy opens the same dialog as the corresponding commands edpy. For more details, see the description of this command.
Jython programs can also be executed from the command line by entering the macro name, e.g.:
ExamCmd4.py
or
xpy  ExamCmd4.py
The difference is that using the xpy command searches for Jython programs only, whereas only entering just the name searches for a TopSpin command, AU program, Jython program or macro of that name.


## SEE ALSO

edpul, edcpde, delpul, delcpdd, xmac
© 2025 Bruker BioSpin GmbH & Co. KG
