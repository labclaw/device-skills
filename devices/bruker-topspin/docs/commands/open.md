# open

**Category:** Commands > Miscellaneous > Dataset Handling

## NAME

**open** - Open a dataset, pulse program, AU program etc. (nD)


## DESCRIPTION

Opening data, parameters, lists and various other files can be started from the command line or from the open dialog box. The latter is opened with the command open [Ctrl-o]:
 
This dialog box has three options each with several file types. Each file type selects a certain command for execution.
### Open NMR data stored in standard Bruker format

This option allows you to open Bruker format data in the following ways:
1. File chooser [reb]
2. RE dialog [re]
3. PROCNO dialog [rep]
### Open NMR data stored in special formats

This option allows you to open the following NMR data types (formats):
1. JCAMP-DX [fromjdx]
2. Zipped TopSpin [fromzip]
3. WIN-NMR [winconv]
4. A3000 [conv]
5. VNMR [vconv]
6. JNMR [jconv]
7. Felix [fconv]
### Open other file:

This option allows you to open the following lists and programs: 
1. Pulse programs [edpul]
2. Au programs [edau]
3. Gradient programs [edgp]
4. CPD programs [edcpd]
5. Parameter set [rpar]
6. Miscellaneous files [edmisc] 
7. Parameter lists [edlist]
8. Jython program [edpy]
9. Macro [edmac]
The corresponding command line commands are specified in square brackets.
After clicking OK, a new dialog box will appear according to the selected option and file type.


## SEE ALSO

conv, edau, xau, delau, xauw, edlist, dellist, edmisc, rmisc, wmisc, delmisc, edpul, edcpd, edpy, edpy3, edmac, fconv, fromjdx, fromzip, jconv, re, rep, rew, repw, reb, reb, vconv, winconv
© 2025 Bruker BioSpin GmbH & Co. KG
