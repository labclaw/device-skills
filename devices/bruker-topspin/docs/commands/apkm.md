# apk, apks, apkm, apkf, ph

**Category:** Commands > Process > Adjust Phase > Automatic Phasing Options

## NAME

**apk** - Automatic phase correction (1D)

**apks** - Automatic phase correction with a different algorithm (1D)

**apkm** - Automatic phase correction with a different algorithm 2 (1D)

**apkf** - Customized automatic phase correction (1D)

**ph** - Open phase correction command dialog box (1D, 2D)


## DESCRIPTION

Phase correction commands can be entered on the command line or started from the phase correction dialog box. This dialog is opened with the command ph. It offers several options, each of which selects a certain command for execution.
 
### Automatic phasing

This option selects the command apk for execution. It calculates the zero and first order phase values and then corrects the spectrum according to these values. The phase values are stored in the parameters PHC0 and PHC1, respectively. Note that apk stores the calculated phase values both as processing parameters (edp) and as processing status parameters (dpp). 
### Automatic phasing, alternate algorithm

This option selects the command apks for execution. It works like apk, except that it uses a different algorithm which gives better results on certain spectra, for instance polymer spectra where peaks are concentrated only in one area.
### Automatic phasing, alternate algorithm 2

This option selects the command apkm for execution. It uses symmetric isolated peaks, regions with positive/negative signals and regions of flat baseline for automated phase correction of 1D NMR spectra. The automated phasing is performed by means of minimization of certain penalty function with four terms. The first term is responsible for phases of symmetric isolated peaks, the second accounts for regions with positive/negative signals, the third accounts for baseline regions, and the fourth gives additional penalty for large values of first-order phase correction parameter PHC1.
### Automatic phasing, selected region only

This option selects the command apkf for execution. It works like apk, except that it uses only a certain region of the spectrum for the calculation of the phase values. This region is determined by the parameters ABSF1 and ABSF2. The calculated phase values are then applied to the entire spectrum. Note that the parameters ABSF1 and ABSF2 are also used by the command absf.
If you run a command like apkf from the command line, you have to make sure that the required parameters are already set. Click the Procpars tab or enter edp to do that.
If automatic phase correction does not give satisfactory results, you can perform interactive phase correction. This can be started with the entry Manual phasing in the ph dialog box, by clicking the  button in the toolbar or by entering .ph on the command line.
The ph command can be used on 1D or 2D data. It recognizes the data dimensionality and opens a dialog box with the appropriate options and parameters.


## INPUT PARAMETERS

Set from the ph dialog box, with edp or by typing absf1, absf2 etc.:
ABSF1 - low field (left) limit of the region used by apkf
ABSF2 - high field (right) limit of the region used by apkf
### OUTPUT PARAMETERS

Can be viewed with edp, dpp or by typing phc0, s phc0 etc.:
PHC0 - zero order phase correction value (frequency independent) 
PHC1 - first order phase correction value (frequency dependent)
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

APK
APKF
APKS


## SEE ALSO

apk0, apk1, apk0f, ph; apbk
© 2025 Bruker BioSpin GmbH & Co. KG
