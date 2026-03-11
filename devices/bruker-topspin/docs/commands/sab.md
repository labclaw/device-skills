# sab

**Category:** Commands > Process > Baseline

## NAME

**sab** - Spline baseline correction (1D)


## DESCRIPTION

The command sab performs a spline baseline correction. This is based on a predefined set of data points which are considered to be a part of the baseline. The regions between these points are individually fitted. In order to execute sab, the baseline points must have been determined. You can do this as follows: 
1. Click  or enter .basl to change to baseline correction mode.
2. Click  to switch to Define baseline points mode
3. (if the baseline points have been defined before, you are first prompted to append to (a) or overwrite (o) the existing list of points)
4. Move the cursor along the spectrum and click left at several positions which are part of the baseline.
5. Click  to return. The command sab is automatically executed.
The set of baseline points is saved in the file baslpnts. This file can be stored for general usage with the command wmisc. After that, you can read it with rmisc on another dataset and run sab to perform the same baseline correction.
sab can be started from the command line or from the baseline dialog box which is opened with the command bas.


## INPUT FILES

<dir>/data/<user>/nmr/<name>/<expno>/pdata/<procno>/
1r - real processed 1D data
baslpnts - baseline points (points and ppm values)


## OUTPUT FILES

<dir>/data/<user>/nmr/<name>/<expno>/pdata/<procno>/
1r - real processed 1D data
auditp.txt - processing audit trail


## USAGE IN AU PROGRAMS

SAB


## SEE ALSO

bcm
© 2025 Bruker BioSpin GmbH & Co. KG
