# abs, absf, absd, absn, bas

**Category:** Commands > Process > Baseline

## NAME

**abs** - Automatic baseline correction (1D)

**absf** - Automatic baseline correction of the plot region (1D)

**absd** - Automatic baseline correction, special algorithm (1D)

**absn** - Automatic baseline correction, without integration (1D)

**bas** - Open baseline correction dialog box (1D, 2D)


## DESCRIPTION

Baseline correction commands can be started on the command line or from the baseline correction dialog box.
 
The latter is opened with the command bas.
This dialog box offers several options, each of which selects a certain command for execution.
### Auto-correct baseline using polynomial

This option selects the command abs for execution. It performs an automatic baseline correction of the spectrum by subtracting a polynomial. The degree of the polynomial is determined by the parameter ABSG which has a value between 0 and 5, with a default of 5. abs first determines which parts of the spectrum contain spectral information and stores the result in the file intrng (integral regions). The remaining part of the spectrum is considered baseline and used to fit the polynomial function.
abs also interprets the parameters ABSL, AZFW, AZFE and ISEN. Since these parameters apply to integration rather than baseline correction, they do not appear in the bas dialog box. They do appear in the integration dialog box (command int). Data points greater than ABSL*(standard deviation) are considered spectral information, all other points are considered noise. If two peaks are more than AZFW apart, they are treated independently. If they are less than AZFW ppm apart, they are considered to be overlapping. Integral regions are extended at both sides by AZFE ppm. If this extension causes adjacent regions to overlap, the centre of the overlap is used as the limit of the two regions. Only regions whose integrals are larger (area) than the largest integral divided by ISEN are considered. 
abs n does not store the integral regions.
The command abs only stores the integral regions of positive peaks. To store the integral regions of both positive and negative peaks, following command sequence can be used: ef, mc, abs, efp, abs n.
### Auto-correct spectral range ABSF1 .. ABSF2 only

This option selects the command absf for execution. It works like abs, except that it only corrects the spectral region which is determined by the processing parameters ABSF1 and ABSF2. 
### Auto-correct baseline, alternate algorithm

This option selects the command absd for execution. It works like abs, except that it uses a different algorithm (It uses the same algorithm as the command abs in DISNMR). It is, for example, used when a small peak lies on the foot of a large peak. In that case, absd allows to correct the baseline around the small peak which can then be integrated. Usually absd is followed by abs.
To display the integral regions determined by one of the above commands: 
1. Right-click inside the data window and select Display Properties
2. Check the entry Integrals and click OK
The integral regions are also used by various commands which calculate spectral integrals like li, lipp and plot. 
If you run a command like abs from the command line, you have to make sure that the required parameters are already set. Click the Procpars tab or enter edp to do that.
If automatic baseline correction does not give satisfactory results, you can apply an interactively determined polynomial, exponential, sine or spline baseline correction. This can be started with the first entry of the bas dialog box, by clicking the  button in the toolbar or by entering .basl on the command line.
The bas command can be used on 1D or 2D data. It recognizes the data dimensionality and opens a dialog box with the appropriate options and parameters.


## INPUT PARAMETERS

Set from the bas dialog box, with edp or by typing absg, absf1 etc.:
ABSG - degree of the polynomial (input of abs, absf, absd)
ABSF1 - low field (left) limit of the region corrected by absf
ABSF2 - high field (right) limit of the region corrected by absf
Set from the int dialog box, with edp or by typing absl, azfw etc.:
ABSL - integral sensitivity factor with reference to the noise
AZFW - minimum distance between peaks for independent integration
AZFE - integral extension factor
ISEN - integral sensitivity factor with reference to the largest integral


## INPUT FILES

<dir>/data/<user>/nmr/<name>/<expno>/pdata/<procno>/
1r - real processed 1D data 
proc - processing parameters


## OUTPUT FILES

<dir>/data/<user>/nmr/<name>/<expno>/pdata/<procno>/
1r - real processed 1D data 
procs - processing status parameters
intrng - integral regions (output of abs, absf, absd) 
auditp.txt - processing audit trail


## USAGE IN AU PROGRAMS

ABS
ABSD
ABSF


## SEE ALSO

bcm, sab, bc; apbk, sigreg
© 2025 Bruker BioSpin GmbH & Co. KG
