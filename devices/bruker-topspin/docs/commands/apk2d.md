# apk2d

**Category:** Commands > Process > Adjust Phase > Automatic Phasing Options

## NAME

**apk2d** - Automatic Phase Correction


## DESCRIPTION

This command heuristically searches for the optimal value of the four phase correction parameters PHC0(F1), PHC0(F2), PHC1(F1), PHC1(F2). This is done by running a 4D conjugate gradient method 9 times, starting from 9 fixed initial locations. Each gradient search aims at minimizing the number of spectrum points that are beyond 2.5 times the spectrum noise level. The inner minimization algorithm framework is the same as for command apkm, but uses a different objective function and a different input dimension. We denote the above-described phase correction process as the hypercomplex variant. The module also has a "pseudo 2D" variant, where the algorithm instead performs a 1D phase correction from command apkm on the row of the spectrum with the highest intensity value, then apply this phase correction to every row of the spectrum.
 
### COMMAND OPTIONS

1. pseudo2d
- This option enables thempseudo 2D variant of the phase correction process. Note that by default, apk2d always select the hypercomplex variant, even for 2.5D datasets, namely when the acquisition parameter FnMode has value QF(no frequency). For such dataset, the option pseudo2d must be selected by the user.
2. cosy / nocosy
- By default, if the processing parameter SPECTYP" has one of the values COSY, ECOSY or DQFCOSY, then the hypercomplex algorithm is set to the cosy. In this setting, the optimized 0th order phase corrections PHC0(F1) and PHC0(F2) are shifted by 90°. Option cosy resp. forces the hypercomplex in the cosy mod resp. out of it.
3. nopp
- By default, the hypercomplex algorithm looks for a pulse program with name pulseprogram in the same directory as file auditp.txt. If such a file exists, it is read and the value of the phase correction parameters PHC0(F1), PHC0(F2), PHC1(F1), PHC1(F2) will be taken over during the minimization process. Option nopp disables the reading of the pulse program file. 
- A phase correction parameter, e.g. PHC0(F1), can be specified in a pulse program with ;PHC0(F1): $value, where $value represents the desired phase correction in degrees.
4. log
Write apk2d process information to a file with name apkm.log in the same folder as file auditp.txt.
1. nn / n0 / n1 / 0n / 00 / 01 / 1n / 10 / 11
- These options specify which phase correction values are to be optimized. For each direction, value n means that the direction should not be optimized, 1 means that the direction should be optimized, and 0 means that only the 0th order.
### OUTPUT PARAMETERS

Can be viewed with edp, dpp or by typing phc0, s phc0 etc.:
PHC0 - zero order phase correction values (frequency independent)
PHC1 - first order phase correction values (frequency dependent)
Note that this is one of the rare cases where the output parameters of a command are stored as processing (edp) and as processing status parameters (dpp).


## INPUT FILES

<dir>/data/<user>/nmr/<name>/<expno>/pdata/<procno>/
2rr, 2ri, 2ir, 2ii - processed 2D data (real, imaginary)
proc, proc2 - processing parameters


## OUTPUT FILES

<dir>/data/<user>/nmr/<name>/<expno>/pdata/<procno>/
2rr, 2ri, 2ir, 2ii - processed 2D data (real, imaginary)
proc, proc2 - processing parameters
procs, proc2s - processing status parameters
auditp.txt - processing audit trail


## SEE ALSO

apk, apks, apkm, apkf, ph
© 2025 Bruker BioSpin GmbH & Co. KG
