# psf, wspf

**Category:** Commands > Analyze > Line Shapes

## NAME

**psf** - Generate Point Spread Function (1D, 2D, 3D)

**wpsf** - Write 1r file into point spread function file (1D)


## DESCRIPTION

These commands generate a Point Spread Function for the deconvolution of an NMR spectrum with command maxent. A PSF is basically the lineshape of a single line or peak of a region in an NMR spectrum. In 1D, it can also be the sum of several lineshapes defining a more complex peak or peak group, which can only be generated with the command wpsf. The editor maxed provides parameters to customize the lineshape for the command wpsf. Command wpsf copies the 1r file into a PSF file.
### REQUIRED PARAMETERS

The following parameters are required when executing psf:
1. Number of points defining the lineshape (PSF)
- This number will be reduced to be at most equal to the number of points in the region of the NMR spectrum to deconvolve. In case of reduction, the selected points are chosen with respect to the center of the PSF. 
2. Symmetrical or asymmetrical lineshape
- In case of an asymmetrical lineshape, the distribution and the half width will be asked twice, namely once for the right and once for the left.
3. Line shape distribution. Example values are:
1. 0 : 100% Gaussian
2. 0.6 : 60% Lorentz, 40% Gauss
3. 1 : 100% Lorentzian
4. 1.4 : 60% Lorentz, 40% Winged
5. 2 : 100% Winged
4. Half width at half height
- When designing a PSF for a certain region of the NMR spectrum you should measure the half width of a peak in the spectrum in Hz using the mouse cursor. The selected peak should be a single peak not overlapping with other peaks and the peak should be representative for the region you want to deconvolve. Note that the lineshape is split into two halves.
5. Write destination
6. p to only write into file mem.psf , r to only write into files 1r (not only in 1D), and b for both. If the 1r file is overwritten, then the dataset should not be used anymore as second or third data set in edc2 for a maxent run, because the sizes, SW and Hz/Pt in the status processing parameters no longer match with the original NMR spectrum.


## INPUT PARAMETERS

<dir>/data/<user>/nmr/<name>/<expno>/pdata/<procno>/
SF - Spectrometer frequency (Hz)
SI - size of the processed data
SW_p - Processing spectral width
NC_proc - intensity scaling factor
F1P - low field (left) limit of the plot region in ppm


## OUTPUT FILES

<dir>/data/<user>/nmr/<name>/<expno>/pdata/<procno>/
mem.log - if the selected destination is p or b
1r - if the selected destination is r or b
1i - if the selected destination is r or b


## SEE ALSO

maxed, maxent, maxinf, maxres, xline
© 2025 Bruker BioSpin GmbH & Co. KG
