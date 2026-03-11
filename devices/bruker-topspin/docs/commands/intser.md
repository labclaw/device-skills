# intser

**Category:** Commands > Process > Advanced

## NAME

**intser** - Integrate a series of datasets


## DESCRIPTION

The command intser integrates a series of 1D or 2D data. 
1. Click Process | Advanced | Integrate Spectra List.
This will open the following workflow button bar:
 
Click Select List to define the list of data sets on which you want to perform the series of integrations. This list must have been previously created manually or can be created by clicking on the arrow key on the Select List button and selecting the command Build dataset list using find. The latter will open a dialogue window as shown below.
 
Enter appropriate values for the various list items to find the data sets you want to work with. A completed list may look like the one shown below. Click on Define List button and select Edit Dataset List.
 
The first data set in the list serves as reference data set. Its PROCNO directory must contain an intrng file with the spectral regions to be integrated. This file is created by automatic integration (command abs) or by interactive integration (command .int). The next step is to set up the parameters for the serial integration. Clicking on Define Parameters will open the following dialogue box.
 
There are two options:
1. Calibrate the integrals in the series of spectra to a certain reference value. In the first (reference) spectrum, the indicated Number of region to calibrate is calibrated to the Value of region to calibrate. All integrals in the series of experiments will then be scaled with the same scaling factor. This allows to immediately compare the integrals within the series of experiments.
2. Normalize the sum of integrals. Works like the calibration, but instead of scaling the reference region to a certain value, the sum of all integrals in the reference spectrum is scaled to the Normalization value. All integrals in the series of experiments will then be scaled with the same scaling factor. This allows to immediately compare the integrals within the series of experiments.
### Global scaling

Takes the value yes or no. For yes, all integrals of all spectra in the list will be scaled relative to the normalization region of the reference spectrum. For no, all integrals of one spectrum will be scaled relative to the normalization region of the same spectrum. The normalization region number and value are same for each spectrum (the specified values).
To start the calculation, click on Execute.
The integration result is stored in a text file whose contents are shown on the screen. Its format is demonstrated by the following example. Lines beginning with a # are comment lines. The format is suitable to be imported into a spreadsheet program such as Excel for further processing. The example is the result of integrating the 3 defined regions of 3 data sets. The first region is the reference region and all integrals in all spectra were integrated with the same scaling factor.
# Result of 'intser'
# Date/time = Wed Feb 21 11:42:55 CET 2018
# Data set list (full path) = C:\Bruker\examdata\topspin-dataset-list.txt
# Region to calibrate = 0
# Value of region to calibrate = 1.0
# Global scaling = yes
 
# --- Integral info --- 
# A 1.0 #regions in PPM
# # low field high field bias slope
# 2.999042477377031 2.9053223999589988 -0.0 -0.0 # for region 1
# 2.824990905029257 2.747337126597173 -0.0 -0.0 # for region 2
# 2.01899823923418 1.895823280341909 -0.0 -0.0 # for region 3
 
# Spectrum#; Integral 0; Integral 1; Integral 2;
0;1.0;0.9944740153680266;1.012183456123523;
1;0.774737126457184;0.7625343796353649;0.7993500292763215;
2;0.6126474881645066;0.4877583034349917;0.6854909593010602;
 
With the parameters set as below the result of the integration will look like this.
 
# Result of 'intser'
# Date/time = Wed Feb 21 11:52:40 CET 2018
# Data set list (full path) = C:\Bruker\examdata\topspin-dataset-list.txt
# Normalization value = 100.0
# Global scaling = no
 
# --- Integral info --- 
# A 1.0 #regions in PPM
# # low field high field bias slope
# 2.999042477377031 2.9053223999589988 -0.0 -0.0 # for region 1
# 2.824990905029257 2.747337126597173 -0.0 -0.0 # for region 2
# 2.01899823923418 1.895823280341909 -0.0 -0.0 # for region 3
 
# Spectrum#; Integral 0; Integral 1; Integral 2;
0;33.259525219675844;33.07573359444518;33.664741185878974;
1;33.15629487831799;32.63405596897349;34.20964915270852;
2;34.30475406014218;27.311674271708828;38.383571668148996;
 
Particularly, in this example, the last three lines with the integration results are important. 
The command intser can also be used to integrate a series of 2D data. Note that in this case the file containing the integral regions is int2drng.


## SEE ALSO

serial 
© 2025 Bruker BioSpin GmbH & Co. KG
