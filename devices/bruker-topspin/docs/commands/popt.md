# popt

**Category:** Commands > Acquire > Run

## NAME

**popt** - Open the parameter optimization window


## DESCRIPTION

The command popt allows you to optimize acquisition parameters like pulses and delays (see the next figure).
 
Before you start an optimization, you must run one acquisition with the acquisition parameters as they are (not optimized) and process the data. On the resulting spectrum, you must define the spectral range (a peak or group of peaks) to be used for optimization. To do that, click-hold the left mouse button at one edge of the desired region and drag the cursor to the other edge. The TopSpin display will automatically be adjusted to show the selected region only. You must now store this region with a right-mouse click in the spectrum window and select Save Display Region to … or by entering dpl.
The popt dialog box allows you to create an entry for each parameter you want to optimize. By default, it shows only one entry; more parameters can be added by clicking the button Add parameter. Furthermore, the following fields are offered:
1. OPTIMIZE : Optimization of the parameters in the group.
1. Step by Step
- The parameters of a group are optimized one after the other. NEXP can be different for each parameter. The total number of experiments is the sum of the NEXP value of each parameter. The result of each parameter optimization is stored in a separate PROCNO. 
2. Simultaneous 
- The parameters of a group a optimized simultaneously. NEXP must be the same for each parameter and represents the total number of experiments. The result of the parameter optimization is stored in one PROCNO.
3. Array
- The parameters of a group a optimized according to an N-dimensional array (N is the number of parameters in a group). NEXP can be different for each parameter. The total number of experiments is the product of the NEXP value of each parameter. The result of the parameter optimization is stored in one PROCNO.
4. No Optimization
- The parameter is not optimized. 
2. GROUP: group number. Optimization starts with the lowest group number.
3. PARAMETER: The parameter to be optimized. If OPTIMIZE is set to No Optimization, the parameter will be stored as comment in the optimization setup.
4. OPTIMUM: Optimization criterion (see below).
5. STARTVAL: First value of the parameter.
6. ENDVAL: Last value of the parameter.
7. NEXP: Number of experiments.
8. VARMOD: Parameter variation mode: linear or logarithmic.
9. INC: Parameter increment value. Unused for VARMOD = log.
 
The optimization criterion OPTIMUM can take the following values:
1. POSMAX - the maximum value of a positive peak.
2. NEGMAX - the maximum value of a negative peak.
3. ZERO - zero intensity of a peak.
4. MAGMAX - the maximum magnitude value of a peak.
5. MAGMIN - the minimum magnitude value of a peak.
 
At the bottom of the dialog box you will find the following buttons:
1. Start optimize - start the optimization for all checked parameters.
2. Skip current optimization - stop the optimization for the current parameter.
3. Show protocol - show the optimization result. A dialog appears with a list of protocol files: 
1. popt.protocol : the entire optimization result.
2. popt.protocol.999 : the optimization result in PROCNO 999.
3. popt.protocol.998: the optimization result in PROCNO 998.
4. etc.
4. Add parameter - add a parameter entry.
5. Restore - restore the last saved optimization setup.
6. Save - save the current optimization setup to current dataset EXPNO.
7. Read array file - read optimization setup.
8. Save array file as.. - save current optimization setup for general usage.
9. Stop optimization - stop the optimization for all checked parameters.
10. Delete parameter - delete the selected parameter.
11. Display Dataset – Display the current dataset
12. Update ProcPars – Update Processing Parameters
13. Help - open the popt help page.
 
Clicking the button Start optimize will start the optimization process.
### NOTE

Note that it runs on the current dataset. For each parameter/group, a series of acquisitions will be performed. The result of this is a series of spectra (actually spectral regions) that are displayed in one screen and show the optimum parameter value. They are stored as one or more processed data files under the current dataset name and experiment number, but under different processing numbers. For the first parameter/group that is optimized this is PROCNO 999, for the second parameter/group PROCNO 998 etc. As such, you must start popt on a dataset with PROCNO < 900. The result will also be stored in the so-called protocol file (see OUTPUT FILES) 
 
Please note that the popt command is especially useful for 90° pulse length calibration. Also for pulse power optimization or any other pulse (decoupling, indirect pulses etc.) popt can be a useful tool. 
 
At the top of the dialog box you will find the following check buttons:
1. Store as 2D data (ser file).
- If checked, the result of the optimization (a series of 1D spectra) will be stored as a 2D dataset in EXPNO 899. However, if the source dataset PROCNO is greater than 100, the EXPNO of the destination 2D data will be
- PROCNO - 100. 
2. The AU program specified in AUNM will be executed.
- If checked, the AU program defined by AUNM will be executed instead of the command zg. 
3. Perform automatic baseline correction (ABSF) 
- If checked, the output data will be baseline corrected with absf.
- 
### NOTE

Note that this command corrects the selected region (determined by the processing parameters ABSF1 and ABSF2).
4. Overwrite existing files (disable confirmation message).
- If checked, the output PROCNO, if it exists, will be overwritten without warning.
5. Stop sample spinning at the end of optimization (mash)
6. Run optimization in background 
- If checked, the foreground dataset will remain the same during the optimization. If it is not checked, the TopSpin display will change to PROCNO 999 where the optimization result is displayed.
7. No display of estimated running time
8. Calculate optimum after POPT has finished, but do not store in dataset
9. Correlate 2D Container with experiment 
To the right of the above check buttons, the current values of the parameters WDW (window multiplication mode), PH_mod (phase correction mode) and FT_mod (Fourier Transform mode) are displayed.
If you want to rerun an optimization, you must first return to the starting PROCNO.


## INPUT FILES

1. <tshome>/exp/stan/nmr/lists/popt/
1. <name> - parameter optimization setup for general usage (input of Read array file..)
2. <dir>/data/<user>/nmr/<name>/<expno>/
1. acqu - acquisition parameters
2. popt.array - parameter optimization setup (input of Restore)
3. popt.protocol - parameter optimization result (input of Show protocol)
3. <dir>/data/<user>/nmr/<name>/<expno>/pdata/<procno>/
1. proc - processing parameters
4. <tshome>/prog/au/bin/
1. poptau - AU program that runs the optimization (executable)
2. popthalt - AU program that halts the current optimization (executable)


## OUTPUT FILES

1. <tshome>/exp/stan/nmr/lists/popt/
1. <name> - parameter optimization setup for general usage (output of Save array file as..)
2. <dir>/data/<user>/nmr/<name>/<expno>/pdata/999
1. 1r - processed data containing the optimization result of the first parameter/group
3. <dir>/data/<user>/nmr/<name>/<expno>/pdata/998
1. 1r - processed data containing the optimization result of the 2nd parameter/group 
4. <dir>/data/<user>/nmr/<name>/<expno>/
1. popt.array - parameter optimization setup (output of Save)
2. popt.protocol - parameter optimization result (output of Start optimize)
5. <dir>/data/<user>/nmr/<name>/899/
1. ser - 2D raw data containing the optimization result


## SEE ALSO

gs, zg
© 2025 Bruker BioSpin GmbH & Co. KG
