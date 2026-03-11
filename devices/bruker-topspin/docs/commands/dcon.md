# dcon2d, dcon

**Category:** Commands > Analyze > Line Shapes

## NAME

**dcon2d** - Open deconvolution workflow button bar (1D, 2D)

**dcon** - Open deconvolution workflow button bar (1D, 2D)


## DESCRIPTION

1. Deconvolution based on a Levenberg-Marquardt algorithm, command dcon
2. Deconvolution based on a machine learning algorithm, command mldcon
3. Fit Dynamic NMR Models, command dnmr
4. Fit Solids NMR Models, command sola
Only the command dcon will be described in this manual, the other commands and methods are described in separate manuals.
1. For mldcon, click Help | Manuals | Acquisition & Processing Parameters | Proc. Commands and Parameters or enter help mldcon
2. For dnmr, click Help | Manuals | Analysis and Simulation | Structure Analysis Tools 
3. The manual under Help | Manuals | Analysis and Simulation | DNMR is an older version and additionally describes the theoretical background of the method.
4. For sola, click Help | Manuals | Analysis and Simulation | Structure Analysis Tools.
 
The command dcon opens its own workflow button bar with the logical order of the steps used to perform the deconvolution.
 
Click Destination to define where the result will be stored. The following dialog box will appear:
 
Click Def. Peaks to define the peaks to be deconvoluted.
The display changes to manual peak picking mode. Select the peaks as described in 1D Interactive Peak Picking. Here, eight peaks were defined. 6 came from automatic peak picking, the center peak was removed and replaced with two manually defined peaks. This is justified, because the larger half width of the center peak suggests that two peaks close to each other overlap here (see screenshot below).
 
When done, click  and in the list, select Save Peaklist for Deconvolution. This will save the list of peaks in the files peaklist and peaklist.xml. Exit from manual peak picking mode before you start the deconvolution. 
1. Click View Peaks to inspect the peak list (file peaklist). Here you may enter individual values for half width and the Lorentz / Gauss percentage for the fitted peaks.
2. Click Params and in the list, select values for the computation range per line [AZFW] and the integral scaling factor [CY].
3. Click Start Fit to start the fitting process. The peaks will be fitted, and the resulting spectrum will be stored in the defined PROCNO. 
TopSpin shows the deconvolution result, i.e. peak positions, line widths and integrals on the screen and stores it in the file dconpeaks.txt within the respective procno of the dataset, see screenshot below.
 
TopSpin will also automatically switch to multiple display mode and show original spectrum and the sum of the computed line shapes superimposed. 
 
All multiple display functionality is available to visualize and compare the two spectra. Additionally, more display options are available from the workflow bar.
Click View Fit for further display options:
View Fit Overlayed to switch to multiple display.
View Numerical Result to display the result again.
View Fitted Shapes to display all deconvoluted lines individually. Note that this opens a separate, simple, overlay presentation in its own window without the multiple display functionality.
 
Note that the results of deconvolution are approximated achievements to interpret complex spectra. These amounts are according to reality if the signal is an ideal Gauss- or Lorentzian shape and if the complete region of the signals has been deconvolved. Also note that indeed two lines could be fitted to the center peak.


## INPUT FILES

<dir>/data/<user>/nmr/<name>/<expno>/pdata/<procno>/
2rr - real processed 2D data
peaklist.xml - peak list
proc - processing parameters


## OUTPUT FILES

<dir>/data/<user>/nmr/<name>/<expno>/pdata/1000/
2rr - deconvolved processed 2D data (first individual peak)
dcon2dpeaks.txt - deconvolution parameters and peaks
procs - processing status parameters
<dir>/data/<user>/nmr/<name>/<expno>/pdata/1001/
2rr - deconvolved processed 2D data (second individual peak)
dcon2dpeaks.txt - deconvolution parameters and peaks
procs - processing status parameters
etc.


## SEE ALSO

mldcon
© 2025 Bruker BioSpin GmbH & Co. KG
