# compileall, cplbruk, cpluser

**Category:** Commands > Miscellaneous > Run a Program

## NAME

**compileall** - Compile all Bruker and User AU programs

**cplbruk** - Compile Bruker AU programs

**cpluser** - Compile user defined AU programs


## DESCRIPTION

The command compileall compiles all Bruker and User AU programs. In order to compile Bruker AU programs, these must have been installed. This can be achieved using the command expinstall.
The command cplbruk allows to compile one or more Bruker AU programs. 
 
Before you can use it, the command expinstall must have been executed once, with the option "Install Bruker library AU programs" enabled. Then you can use cplbruk in three different ways:
1. cplbruk <name> - compile the Bruker AU program <name>
2. cplbruk all - compile all Bruker AU programs
3. cplbruk - lists Bruker AU programs; double-click one to compile it
If you specify an argument, then it may contain wildcards; for example:
1. cplbruk a* compiles all Bruker AU programs which start with a.
2. cpluser works like cplbruk, except that it compiles user defined AU programs.
For more information on AU programs please refer to the AU reference manual.


## INPUT FILES

<tshome>/exp/stan/nmr/au/src/*
AU programs (source files)


## OUTPUT FILES

<tshome>/prog/au/bin/* 
AU programs (executable files)


## SEE ALSO

(expinstall), edau, xau, (xaua, xaup)
© 2025 Bruker BioSpin GmbH & Co. KG
