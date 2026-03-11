# xaua, xaup

**Category:** Commands > Acquire > Run

## NAME

**xaua** - Execute the AU program specified with AUNM

**xaup** - Execute the AU program specified with AUNMP


## DESCRIPTION

The commands xaua and xaup execute the AU program which is specified by the parameters AUNM and AUNMP, respectively. In all Bruker parameter sets, these parameters are set to relevant Bruker AU programs. For example, in the parameter set PROTON, AUNM = au_zg and AUNMP = proc_1d. When parameter sets are used in automation (IconNMR), the AU programs specified by AUNM and AUNMP perform the acquisition and the processing, respectively.
For details on writing, compiling, and executing AU programs please refer to the TopSpin AU Programming manual (click Help | Manuals | Programming Manuals | AU Programming).


## INPUT PARAMETERS

1. Set by the user with eda or by typing aunm :
1. AUNM - acquisition AU program name for xaua
2. Set by the user with edp or by typing aunmp :
1. AUNMP - processing AU program name for xaup


## INPUT FILES

1. <tshome>/exp/stan/nmr/au/src/
1. AU program source files (only input if the AU program is not compiled yet)
2. <tshome>/prog/au/bin/
1. AU program binary executables
3. <dir>/data/<user>/<name>/nmr/<expno>/
1. acqu - acquisition parameters (input file for xaua)
4. <dir>/data/<user>/<name>/nmr/<expno>/pdata/<procno>/
1. proc - processing parameters (input file for xaup)


## USAGE IN AU PROGRAMS

1. XAUA
2. XAUP
3. XAUPW 
XAUPW waits until the AU program has finished before the next statement is executed whereas XAUP does not. XAUA works like XAUPW is this respect.


## SEE ALSO

edau, xau, delau, xauw, expinstall, 
© 2025 Bruker BioSpin GmbH & Co. KG
