# maxed, maxent, maxinf, maxres, xline

**Category:** Commands > Analyze > Line Shapes

## NAME

**maxed** - Open maxent parameters control window

**maxent** - Execute maximum entropy based deconvolution (1D, 2D, 3D)

**maxinf** - Show short version of maxent report

**maxres** - Show maxent report

**xline** - Show quantification results


## DESCRIPTION

The purpose of maxent is to derive spectral features such as line positions and peak widths from NMR data by using the maximum entropy method from probability theory. Maximum entropy is a procedure for inferring positive distributions from limited data. This method generates the most probable spectrum, best fitting the experimental data, as well as diverse statistics to assess the reliability of the result.
Before running maxent, the following must be defined:
1. a second and third data set for the output files (using command edc2).
2. the region of interest in the NMR spectrum.
3. if parameter PSFDEF is set to free-form, the user-defined PSF must have been generated into file mem.psf beforehand, e.g. using command psf.
After the maxent run, the second data set will contain the deconvolution result as well as all generated single peaks. The mock data in the third data set will contain the multiplication of the deconvolution result with the PSF. The mock data is most useful for controlling the quality of the deconvolution, i.e. how similar are deconvolved and original data.
The command maxent writes a report for all iteration steps into the mem.log file which can be inspected at any time during or after the run. The following parameters are important:
1. Omega
- Convergence criterion, written at each iteration. Convergence is reached when Omega is 1. Checking Omega during a maxent run gives an indication of the progress of the iteration.
2. Good
- Number of points with accurate measurement, written at each iteration. A high value indicates a reliable deconvolution.
3. Evidence (= Log10Pr)
- Logarithm of the likelihood of the deconvolution result, written at the end of the report. A value close to zero indicates a probable and reliable result. This value can be used as a baseline comparison of two runs of maxent using different parameters or a different point spread function (PSF).
4. Csigma
- Statistical noise value, written at the end of the report. It must be set in maxed to have an exact comparison of two runs using two different PSFs.
5. Npeaks
- Number of peaks in the spectrum
- The other parameters are written at each iteration and are not important for the user. In the following description, the input refers to the state at the beginning of a maxent iteration:
6. Entropy
- Opposite of the entropy of the input. This value should move closer to zero.
7. Alpha
- Regularization constant, which is a factor of the entropy function.
8. Scale
- Scaling factor for the noise.
9. Ntrans
- Number of transform calls
10. Chisq
- Chi squared of the gaussian error. At the end of the run, Chisq should be roughly equal to the number of inaccurate measurements.
11. Test
- Equals 1 - cos(T) for the input, where T is the angle between the gradients of entropy and Chisq. Test helps finding a fast trajectory to the optimum, as the next iteration should move a state close to where Test equals 0.
12. Code (1 digit)
- Equals 0 if and only if the parameter Good was found within acceptable tolerance, and 1 otherwise.
13. Code (6 digits)
- Contains 6 different codes, each equal to 0 if a corresponding criterion is satisfied at the end of the iteration, and 1 otherwise. The maxent run stops once Code = 000000.
1. digit 1: whether the cloud mismatch was found within acceptable tolerance.
2. digit 2: whether Test is lower or equal to 1.
3. digit 3: whether Alpha did not change in the last iteration.
4. digit 4: whether no distance penalty was imposed to "Alpha" in the last iteration.
5. digit 5: whether convergence is reached within acceptable tolerance, namely Omega is close to 1.
6. digit 6: whether the cloud overlap criterion was met.


## INPUT PARAMETERS

Set in the maxent parameters tab by running command maxed, or by clicking on the M in the PROCPARS parameters tab:
1. NITER
- Number of iterations.
- Can be set to any number. The default value 99 is usually sufficient to lead to convergence. Otherwise, the PSF is probably unrealistic.
2. STEPRES
- Generate step results
- If STEPRES is set to yes, the output information is written to disk after each iteration.
3. MOCKDAT
- Write mock data
- If set yes, it will write the mock data to the third data set. Otherwise, the mock data will not be saved.
4. IPOSNEG
- Amplitude sign of the peaks to be deconvolved
- If set to positive, only peaks with positive amplitude will deconvolved. If set to pos/neg,, all peaks will be deconvolved.
5. SIGMA
- Estimated data noise level
- To compare two PSF functions, SIGMA must be set to an estimated noise value. Typically, SIGMA is set to: 
1. 0, then the statistical noise is used. 
2. the CSIGMA value calculated by maxent at the end of a run (see maxres) 
3. the noise value generated by command xcpr noie, using 1 as the order of difference.
4. the noise value generated by command sino, selecting NOISF1, NOISF2, SIGF1 and SIGF2 to roughly fit the region to deconvolve.
- F1P, F2P, F1, F2 - Left and right field limits of the deconvolution region, low and high field deconvolution limits.
- These values are only used for 1D data sets. To deconvolve only a part of a nD matrix, the strip transform feature should be used to get the region of interest.
6. PSFDEF
- Type of Point Spread Function
- Can be set to free-form in 1D to use a user-defined PSF instead of an automatically generated parametric PSF. A user-defined PSF should be generated beforehand with command psf or wpsf. A parametric PSF is defined by the parameters ASYM, PSFWI and PSFSH, which values should fit the required inputs for a psf call.
All other parameters should be modified only by a user with detailed knowledge of the maximum entropy method.


## INPUT FILES

<dir>/data/<user>/nmr/<name>/<expno>/pdata/<procno>/
curdat2 - Path to the second and third datasets
1r - real part of the processed data


## OUTPUT FILES

<dir>/data/<user>/nmr/<name>/<expno>/pdata/<procno>/
mem.quant - Maxent quantification results, generated by maxent.
mem.log - Maxent statistical results, generated by maxent and displayed by maxres.
mem.log.sho - Short maxent statistical results, generated and displayed from mem.log by maxinf.
mem.par - Parameter values of the last maxent run.
mem.quant.xl - Formatted quantification results, generated and displayed from mem.par by xline.
auditp.txt - processing audit trail


## SEE ALSO

psf, wpsf, sino, ed2c
© 2025 Bruker BioSpin GmbH & Co. KG
