# bcm

**Category:** Commands > Process > Baseline

## NAME

**bcm** - User-defined spectrum baseline correction (1D)


## DESCRIPTION

The command bcm performs a spectrum baseline correction by subtracting a polynomial, sine or exponential function.
This involves the following steps: 
1. Click  or enter.basl to change to baseline correction mode.
2. Fit the baseline of the spectrum with a polynomial, exponential or sine function. Click-hold the button A and move the mouse to determine the zero order correction. Do the same with the buttons B, C etc. for higher order corrections until the line matches the baseline of the spectrum. 
3. Click  to return. The command bcm is automatically executed.
The interactively determined baseline function is stored in the file base_info. This file can be stored for general usage with the command wmisc. After that, you can read it with rmisc on another dataset and run bcm to perform the same baseline correction.In this case, bcm can be started from the command line or from the baseline dialog box which is opened with the command bas.


## INPUT FILES

<dir>/data/<user>/nmr/<name>/<expno>/pdata/<procno>/
1r - real processed 1D data
proc - processing parameters
base_info - baseline correction coefficients


## OUTPUT FILES

<dir>/data/<user>/nmr/<name>/<expno>/pdata/<procno>/
1r - real processed 1D data
procs - processing status parameters
auditp.txt - processing audit trail


## USAGE IN AU PROGRAMS

BCM


## SEE ALSO

abs, absf , sab
© 2025 Bruker BioSpin GmbH & Co. KG
