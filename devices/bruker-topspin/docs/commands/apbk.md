# apbk

**Category:** Commands > Process > Adjust Phase > Automatic Phasing Options


## DESCRIPTION

The command apbk provides simultaneous linear phase and baseline correction of 1D spectra. The apbk algorithm was developed and tested for 1H, 11B, 13C, 15N, 19F, 29Si, and 31P spectra in solution state, and 1H, 13C, 15N, and 29Si spectra in solid state. The parameters of the algorithm are adjusted per nucleus and per state of the sample (solution- or solid-state) to give the best performance for each category of spectra. If the algorithm does not contain parameters for a given spectrum, they are estimated from the spectrum. Estimation of parameters can also be triggered for any spectrum using the -estimate option, which might improve results for atypical spectra (see ADVANCED USAGE).
The algorithm uses a model-free baseline correction method. For proton spectra in solution state, baseline detection is performed using a deep neural network.
The algorithm is able to correct spectra that contain out-of-phase peaks due to solvent suppression, as well as spectra with negative peaks (see ADVANCED USAGE). The processing audit trail (<dir>/<name>/<expno>/pdata/<procno>/auditp.txt) can be consulted to examine the details and options the algorithm was run with.
The standard python program <TopSpin>/python/examples/tsapbk.py provides a boiler plate to run apbk with custom options based on the dataset and its pulse program name.
### BASIC USAGE

apbk - Correct the phase and baseline
apbk -bo - Only correct the baseline.
apbk -po - Only correct the phase.
apbk -apk0 - Restrict the phase correction to zero-order (PHC0).
### ADVANCED USAGE

apbk -solid – Enable solid mode. In this mode, the algorithm is tuned to better handle the typical linewidths encountered in solid-state spectra. In addition, the MAS rate (status parameter MASR) is used to better detect low-intensity spinning sidebands. Solid mode is enabled by default for some solid-state-specific Bruker pulse programs (see NOTES).
apbk -solid=<masr> – Enable solid mode and manually set the MAS rate (in Hz). Example: for a solid-state spectrum measured at 15 kHz MAS rate, the command should be apbk -solid=15000.
apbk -nosolid –Disable solid mode.
apbk -supp – Enable suppression mode. In this mode, the region around the suppression frequencies is ignored since the corresponding residual signal may be out of phase. The suppression frequencies are identified from the file <dir>/<name>/<expno>/solvents.f1list or status parameter O1P. Suppression mode is enabled by default for some suppression-specific Bruker pulse programs (see NOTES).
apbk -supp=<f1>(,<f2>,…) – Enable suppression mode and manually set the suppression frequency/frequencies. Example: for a spectrum with suppression frequency at 4.7 ppm, the command should be apbk -supp=4.7. For two suppression frequencies at 4.7 and 3.5 ppm, the command should be apbk -supp=4.7,3.5.
apbk -nosupp – Disable suppression mode.
apbk -neg – Enable negative mode. In this mode, the phase correction accounts for the possibility of negative peaks. The final phase relationship is set such that most peaks are positive. Negative mode is enabled by default for some Bruker pulse programs (see NOTES).
apbk -noneg – Disable negative mode.
apbk -storeb=<procno> – Run the phase and baseline correction and store the baseline to the defined procno. Example: To store the baseline to procno 999, the command is apbk -storeb=999. If the destination procno already exists, it can be overwritten by adding the option -o.
apbk -phc1max=<value> – Restrict the first-order phase correction value (PHC1) to a given absolute value. Example: to restrict PHC1 to ±100°, the command is apbk -phc1max=100.
apbk -estimate – Estimate algorithm parameters directly from the input spectrum instead of using the pre-defined parameters which are general for a given nucleus. This can improve results for atypical spectra. This option is experimental and must be combined with -f.
apbk -f – Enable experimental options.
apbk -intrng – Use the currently defined integration regions to determine signal and baseline regions. Everything within the integration regions will be considered signal and used for phasing, and everything outside will be considered baseline.
apbk -w – Write the detected signal regions as integration regions to disk.
INPUT FILES
<dir>/<name>/<expno>/pdata/<procno>/
1r, 1i - processed 1D data (frequency domain)
acqus – acquisition parameters
OUTPUT FILES
<dir>/<name>/<expno>/pdata/<procno>/
1r, 1i – processed 1D data (real, imaginary)
proc – processing parameters
procs – processing status parameters
intrng – integral regions
auditp.txt – processing audit trail
<dir>/<name>/<expno>/pdata/<procno2>/
1r – real processed 1D data of the baseline


## USAGE IN AU PROGRAMS

APBK – Run the command without options.
APBK_ARGS(option_string) – Run the command with options. Any option described above can be passed as option_string (const char*). Example APBK_ARGS(“-supp=4.7 -neg”).
### NOTES

Solid mode is enabled by default for the following pulse programs: cp, cp90, cppi, hahnecho, hC.cp, hpdec, hX.cp, solidecho. 
Suppression mode is enabled by default for the following pulse programs: noesygppr1d, noesygppr1d.2, noesygpps1d, noesypr1d, noesyprigld1d, npt_zggppr, p11, p1331, p3919fpgp, p3919gp, stebpesgp1s1d, stebpgp1s191d, wet, wet0, wetdc0, wetdc2, wetdcps0, wetdw, wetps0, zg0pr, zgcpdcps, zgcpfqpr, zgcpgppr, zgcppr, zgcxesgp, zgcxgp19, zgesfpgp, zgesgp, zgesgppe, zggpjrse, zggppeso, zggppewg, zggppr, zggpso, zggpw5, zggpwg, zgpr, zgps, zgpurge.
Negative mode is enabled by default for the following pulse programs: cppi, dept135, deptcp135, deptq135, deptqgpsp, deptqgpsp.2, deptqsp, deptsp135.


## SEE ALSO

abs, absf, absd, absn, bas, apk, apks, apkm, apkf, ph
© 2025 Bruker BioSpin GmbH & Co. KG
