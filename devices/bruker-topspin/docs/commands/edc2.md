# edc2

**Category:** Commands > Miscellaneous > Dataset Handling

## NAME

**edc2** - Define second and third data set


## DESCRIPTION

The command edc2 opens a dialog box in which you can define the second and third data set:
 
You can define the NAME, EXPNO, PROCNO and DIR (disk unit). Note that these are all parts of the data path name:
<dir>\<name>\<expno>\pdata\<procno>
The second data set is used by 1D commands like add, duadd, mul, div and addfid and by 2D commands like add2d, mul2d and addser. The second data set is, however, usually set from the add/multiply dialog box (command adsu).
The third data set is used by the 1D command add when entered from the command line and in various AU programs (macro DATASET3).
### INPUT AND OUTPUT FILES

<dir>/data/<user>/nmr/<name>/<expno>/pdata/<procno>/
curdat2 - definition of the second data set


## SEE ALSO

add, duadd, addfid, addc, adsu
© 2025 Bruker BioSpin GmbH & Co. KG
