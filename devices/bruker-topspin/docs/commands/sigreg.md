# sigreg

**Category:** Commands > Analyze > Integrate

## NAME

**sigreg** - Automatic signal region detection in 1D 1H spectra


## DESCRIPTION

The processing command sigreg finds signal regions in proton spectra using a machine learning approach. The algorithm was developed and tested for 1D 1H spectra without solvent suppression.
To ensure optimal performance the spectrum should be phase- and baseline corrected before running sigreg. 
 
In case that the width of the signal regions detected by sigreg is not satisfactory, the command can be customized using the -add, -expand, and -setsize options.
1. The -add option extends signal regions on both sides by a given amount of Hz or ppm.
2. The -expand option extends all signal regions narrower than a given amount of Hz or ppm to that value of Hz or ppm. All signal regions broader than the given value remain untouched.
3. The -setsize option sets the size of all signal regions to a given amount of Hz or ppm.
 
If the requested extension of the signal regions would cause adjacent regions to overlap, they are not merged, but kept separate, with the center of the overlap defining the limit of the two regions. As a result, the left and the right side of these two regions are extended by different values causing their centers to be shifted. This behavior can be prevented by using the -symm option that forces the changes to be symmetric with respect to the center of the signal region, and thus ensuring that the centers of all signal regions remain unchanged (example: sigreg -setsize 0.1ppm -symm).
 
By default, the signal regions are detected using sigreg before modification. By using the 
-mod option, it is possible to suppress this initial detection of signal regions, in order to apply the requested modifications to previously defined signal regions instead (example: sigreg -add=0.15ppm -symm -mod). 
 
### USAGE

sigreg: detects signal regions in 1D 1H spectra.
sigreg -add <value>Hz|ppm: detects signal regions in 1D 1H spectra and extends them on both sides by <value> Hz|ppm.
sigreg -expand <value>Hz|ppm: detects signal regions in 1D 1H spectra and extends all signal regions narrower than <value>Hz|ppm to <value> Hz|ppm.
sigreg -setsize <value>Hz|ppm: detects signal regions in 1D 1H spectra and sets their size to <value> Hz|ppm.
sigreg -add|-expand|-setsize <value>Hz|ppm -symm: detects signal regions in 1D 1H spectra, performs the -add|-expand|-setsize option, and forces the changes to be symmetric with respect to the center of the signal regions.
sigreg -add|-expand|-setsize <value>Hz|ppm -mod: performs the -add|-expand|-setsize option on existing signal regions.
sigreg -add|-expand|-setsize <value>Hz|ppm -symm -mod: performs the -add|-expand|-setsize option on existing signal regions, and forces the changes to be symmetric with respect to the center of the signal region.
Note:
1. sigreg -add accepts both positive and negative values, while sigreg -expand and sigreg -setsize accept only positive values.
2. When using these options, all required information must be specified by command line arguments. The -add, -expand, and -setsize options must be followed by (1) the value for the modification of the signal regions and (2) the unit (Hz or ppm). Between the numerical value and the unit there must not be any space, while the numerical value can be separated by the option using a space (example: sigreg -add 10Hz) or an equal sign (example: sigreg -expand=1ppm).


## INPUT FILES

<dir>/<name>/<expno>/pdata/<procno>/
1r, 1i - processed 1D data (frequency domain)


## OUTPUT FILES

<dir >/<name>/<expno>/pdata/<procno>/
intrng - integral regions 
auditp.txt - processing audit trail


## USAGE IN AU PROGRAMS

SIGREG


## SEE ALSO

abs, int, apbk
© 2025 Bruker BioSpin GmbH & Co. KG
