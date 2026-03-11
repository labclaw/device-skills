# apk0, apk1, apk0f, ph

**Category:** Commands > Process > Adjust Phase > Automatic Phasing Options

## NAME

**apk0** - Zero-order automatic phase correction (1D)

**apk1** - First-order automatic phase correction (1D)

**apk0f** - Customized zero-order automatic phase correction (1D)

**ph** - Open phase correction command dialog box (1D, 2D)


## DESCRIPTION

Phase correction commands can be entered on the command line or started from the phase correction dialog box:
 
This dialog is opened with the command ph. It offers several options, each of which selects a certain command for execution.
### Automatic phasing, 0th order only

This option selects the command apk0 for execution. It works like apk, except that it only performs the zero order phase correction. 
### Automatic phasing, 1st order only

This option selects the command apk1 for execution. It works like apk, except that it only performs the first order phase correction.
### Automatic zero order phasing, selected region order only

This option selects the command apk0f for execution. It works like apkf, except that it only performs the zero order phase correction.
If you run a command like apk0f from the command line, you have to make sure that the required parameters are already set. Click the Procpars tab or enter edp to do that.
If automatic phase correction does not give satisfactory results, you can perform interactive phase correction. This can be started with the entry Manual phasing in the ph dialog box, by clicking the  button in the toolbar or by entering .ph on the command line.
The ph command can be used on 1D, 2D or 3D data. It recognizes the data dimensionality and opens a dialog box with the appropriate options and parameters.


## INPUT PARAMETERS

Set from the ph dialog box, with edp or by typing absf1, absf2 etc.:
ABSF1 - low field (left) limit of the region used by apk0f
ABSF2 - high field (right) limit of the region used by apk0f
### OUTPUT PARAMETERS

Can be viewed with edp, dpp or by typing phc0, sphc0 etc.:
PHC0 - zero order phase correction value (output of apk0 and apk0f) 
PHC1 - first order phase correction value (output of apk1)
Note that this is one of the rare cases where the output parameters of a command are stored as processing (edp) and as processing status parameters (dpp).


## INPUT FILES

<dir>/data/<user>/nmr/<name>/<expno>/pdata/<procno>/
1r, 1i - processed 1D data (real, imaginary)
proc - processing parameters


## OUTPUT FILES

<dir>/data/<user>/nmr/<name>/<expno>/pdata/<procno>/
1r, 1i - processed 1D data (real, imaginary)
proc - processing parameters
procs - processing status parameters 
auditp.txt - processing audit trail


## USAGE IN AU PROGRAMS

APK0
APK1
APK0F


## SEE ALSO

apk, apks, mc, ps; apbk
© 2025 Bruker BioSpin GmbH & Co. KG
