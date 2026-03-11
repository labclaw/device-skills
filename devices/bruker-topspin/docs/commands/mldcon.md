# mldcon

**Category:** Commands > Analyze > Line Shapes


## DESCRIPTION

The command mldcon deconvolves a 1D spectrum by fitting a mixed Lorentzian/Gaussian function to the peaks. The algorithm was developed to work on 1H 1D spectra, and it is based on a deep learning algorithm trained for peak detection. The algorithm requires a phase and baseline corrected 1D spectrum as input, and outputs a list of peaks that can be used to describe the spectrum. The algorithm works based on two deconvolution steps performed automatically: (i) initial peaks detection and peak parameters guess using deep learning, and (ii) accurate fit of peaks position, amplitude, width and line shape to match spectrum amplitudes.
The algorithm automatically optimizes the mixed Lorentzian/Gaussian ratio of each peak to obtain the best possible fit to the input data. The percentage of Gaussian contribution to the line shape is expressed by the lineshape parameter, and it can range from 0 (pure Lorentzian – line shape parameter equal to 0) to 100% (pure Gaussian – line shape parameter equal to 1). The ability to fit both Lorentzian and Gaussian line shapes makes the algorithm suitable to deconvolve spectra that can be described by either line shape or by a mix of the two.
The algorithm stores the deconvolution results as mldcon.csv file in the corresponding PROCNO directory. For each detected peak, the mldcon.csv file reports peak frequency in ppm, intensity in absolute values, full width at half maximum in Hz, line shape as ratio of Gaussian contribution to the total line shape, and absolute area. The peak positions and intensities are also stored as peaklist.xml file, to allow visualization of the predicted peak positions in the spectrum and for the Plot Editor. 
After successful completion of the deconvolution algorithm, mldcon displays by default the result in a deconvolution visualization window. An example of the deconvolution visualization window is shown in the figure below. This window displays the input spectrum (in blue), the detected peaks (in grey), their sum (reconstructed spectrum, in red), and the difference between the input and the reconstructed spectrum (residuals, in black).
Use the command mldcon -d (or mldcon -display) to display the visualization window without running the deconvolution algorithm. This option builds a deconvolution visualization window using the results stored in the mldcon.csv file (i.e., it shows the results of a previous mldcon run). Use the -s (or -silent) option to run the deconvolution command silently, without automatically opening the deconvolution visualization window (for more details, see USAGE below).
The reconstructed spectrum is not saved by default. It is possible to store the reconstructed spectrum using the command mldcon -sr (or -store), which would run the deconvolution and save the reconstructed spectrum in the PROCNO 999 directory of the corresponding EXPNO. Use the additional -procno and -o options to respectively change the PROCNO directory and force overwriting (for more details, see USAGE below). 
Note that the algorithm offers a range of options that can be used to tailor your results and personalize your workflow. Examples are: deconvolve only a given part of the spectrum, run the deconvolution using an existing user-defined guess instead of the deep learning prediction (starts from a peaklist.xml or mldcon.csv file), increase the number of fit iterations to have a more accurate fitting, and more. Many of these options can also be combined together. An overview of all the options is given in the USAGE paragraph below.
### USAGE

The following options run the full deconvolution algorithm (deep learning initial guess + accurate fitting). A slash separates matching options. 
mldcon - Run the deconvolution and display the results in a deconvolution visualization window.
mldcon -s/-silent - Run the deconvolution silently (without opening the deconvolution visualization window).
mldcon -r=<value1>,<value2>/-range=<value1>,<value2> – Run the deconvolution in the region of the spectrum between <value1> and <value2> ppm. The -r/-range option cannot be combined with the -intrng and -e/-exclude options. For optimal results, include the full signal regions in the range by extending the range to hit the baseline on both sides (region with only noise).
mldcon -e=<value1>,<value2>/-exclude=<value1>,<value2> – Run the deconvolution for the full spectrum leaving out the region between <value1> and <value2> ppm. The -e/-exclude option cannot be combined with the -r/-range and -intrng options.
mldcon -intrng – Run the deconvolution in the integral regions. The - intrng option cannot be combined with the -r/-range and -e/-exclude options. For optimal results, include the full signal regions in the integral regions by extending the edges to hit the baseline on both sides (region with only noise).
mldcon -sr/-store – Run the deconvolution, display the results in a deconvolution visualization window, store the reconstructed spectrum in PROCNO 999.
mldcon -sr/-store -procno=<value> – Run the deconvolution, display the results in a deconvolution visualization window, store the reconstructed spectrum as PROCNO <value>. <value> must be a positive integer higher than 0.
mldcon -sr/-store -o – Run the deconvolution, display the results in a deconvolution visualization window, store the reconstructed spectrum in PROCNO 999 and force overwriting if the PROCNO directory already exists. The -o option can also be combined with the -procno.
mldcon -sino=<value> – Run the deconvolution, filter out peaks smaller than <value> times the noise level, display the results in a deconvolution visualization window. The default -sino value is 5. Note that the noise level is roughly estimated by the algorithm, and it might slightly deviate from the correct value. Note also that the -sino parameter cannot be used in combination with -csv and -pp in order to preserve the number of user defined peaks.
mldcon -fit=<value> – Run the deconvolution using <value> times the number of fitting iterations of the accurate fitting, display the results. Use this option to get a more accurate fitting if the default result has a large residual. <value> must be a positive integer higher than 0. (example: mldcon -fit=2 will double the number of fitting iterations)
mldcon -f – Force the deconvolution algorithm to run on spectra that are not 1H spectra. 
The following options run only the accurate fitting part of the deconvolution algorithm and allow users to define the initial peak parameters guess. A slash separates matching options. 
mldcon -pp – Read the content of the peaklist.xml file (created e.g. using the manual peak picking window), run the deconvolution using peaks at the positions defined in the peaklist.xml file as initial guess, display the results. Note that if the peak positions are changed during the fitting, the peaklist.xml file will be updated. 
mldcon -csv – Read the content of the mldcon.csv file, run the accurate fitting using the peaks defined in mldcon.csv as initial guess, display the results. Note that if the peak parameters are changed during the fitting the mldcon.csv file will be updated.
mldcon -pp/-csv -tolppm=<value> – Run the deconvolution restricting the chemical shift adjustment made by the accurate fitting to <value> ppm from the initial guess, display the results. This option can be combined with both -csv and -pp. (example mldcon -pp -tolppm=0.01: deviates peak positions max 0.01ppm from the input guess)
mldcon -csv -tolamp=<value> – Run the deconvolution restricting the amplitudes adjustment made by the accurate fitting to <value>% of the initial guess, display the results. This option can be combined with -csv only. (example mldcon -csv -tolamp=10: deviates peak amplitudes max 10% from the input guess)
mldcon -csv -tolwidth=<value> – Run the deconvolution restricting the line width adjustment made by the accurate fitting to <value>% of the initial guess, display the results. This option can be combined with -csv only. (example mldcon -csv -tolwidth=10: deviates peak line widths max 10% from the input guess)
mldcon -csv -tolls=<value> – Run the deconvolution restricting the lineshape parameter adjustment made by the accurate fitting to <value> units from the initial guess, display the results. This option can be combined with -csv only. (example mldcon -csv -tolls=0.1: deviates peak lineshape parameters max 0.1 units from the input guess)
The following options do not run the deconvolution algorithm. A slash separates equivalent options.
mldcon -d/-display – Open a deconvolution visualization window with the results stored in the mldcon.csv file. 
mldcon -srcsv/-storecsv – Reconstruct the spectrum from the peak list in the mldcon.csv file, and store it as PROCNO 999. This option can be combined with the -procno and -o options to respectively change the PROCNO directory and force overwriting.
Note that most of the options can be used together to combine their results.


## INPUT FILES

<dir>/<name>/<expno>/pdata/<procno>/
1r, 1i - processed 1D data (frequency domain)
mldcon.csv (input of mldcon -csv and mldcon -srcsv/storecsv)
peaklist.xml (input of mldcon -pp)


## OUTPUT FILES

<dir >/<name>/<expno>/pdata/<procno>/
mldcon.csv – peak list created by mldcon
peaklist.xml – peak list for the plot editor
auditp.txt – processing audit trail
1r – real processed 1D data of the reconstructed spectrum (output of mldcon -sr/-store and mldcon -srcsv/storecsv)


## USAGE IN AU PROGRAMS

MLDCON(option_string)
All the options in the USAGE paragraph can be used in automation and passed as option_string (const char*). Example MLDCON(“-range=4,5 -fit=2”). Note that the function always requires an option string, so the default mldcon command can be used in AU programs using MLDCON(“”).


## SEE ALSO

dcon2d, dcon
© 2025 Bruker BioSpin GmbH & Co. KG
