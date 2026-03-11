# pp2dml

**Category:** Commands > Analyze > Pick Peaks

## NAME

**pp2dml** - Peak picking and annotation using machine learning based algorithm (2D)


## DESCRIPTION

The command pp2dml performs automated peak picking followed by peak annotation on a 2D spectrum. The peak picking is based on a deep learning model to identify all NMR peaks. A rule-based algorithm is then used to annotate peaks into five main categories: Compound (C), impurity (I), solvent (S), TMS, and different types of artifacts (A). The network and annotation algorithm are tailored to COSY, HSQC and HMBC spectra, but can be forced to run on other experiments using the command pp2dml -f.
During the peak picking part, peak candidates are identified. A pretrained neural network then evaluates based on intensity, local environment, and symmetry in the spectrum, if a given peak candidate is a real peak. Peaks appearing as shoulders are optionally identified and external 1D experiments (external projections) can be used to filter the peak list. 
In the peak annotation part, peaks in COSY, HSQC or HMBC spectra are labeled as:
1. Compound [C]: Peak from the main compound in the sample.
2. Impurity [I]: Peak from an impurity in the sample.
3. Solvent [S]: Peak from the solvent.
4. Water Residual [S(H2O)]: Peak from residual water in the solvent.
5. Contaminant [S(C)]: Peak from known contaminant in the solvent.
6. Reference (TMS) [TMS]: Peak from the TMS reference.
7. Axial edge artifact [A(AXE)]: Peak along the edges of the spectrum in F1 (zero frequency artifact).
Additional annotations specific to COSY spectra:
1. Diagonal Compound [C(D)]: Diagonal peak corresponding to the main compound in the sample.
2. Diagonal Impurity [I(D)]: Diagonal peak corresponding to an impurity in the sample.
3. Slope 2 Artifact [A(S2)]: Peak along lines with a slope of ±2 (rapid pulsing artifacts).
4. Antidiagonal Artifact [A(AD)]: Peak along the antidiagonal, without a symmetric counterpart.
5. Axial Middle Artifact [A(AXM)]: Peak along the middle of the spectrum in F1 (zero frequency artifact).
Additional annotations specific to HSQC spectra:
1. COSY Artifact [A(COSY)]: Weak peak resulting from a multiple bond correlation between a proton and a carbon (3J artifact, long-range coupling).
2. Decoupling Side Band Artifact [A(DSB)]: Peak from a decoupling side band, typical of composite-pulse decoupling (CPD) methods such as WALTZ and GARP.
Additional annotation specific to HMBC spectra:
1. HMQC Response Artifact [A(1J)]: Peak from a one-bond HMQC response (1J artifact).
The type of spectrum is identified using the SPECTYPE variable in the processing parameter tab. Alternatively, it is extracted from the name of the pulse sequence.
The identification of peaks from the compound or from impurities is based on their intensity relative to the most intense peak, excluding solvent or diagonal peaks in COSY spectra.
The solvent peaks are identified using a database of chemical shifts. Their identification relies on a correct referencing of the spectrum.
By default, only the abbreviations (in square brackets) are displayed as annotations. Use the -fulllabel argument to display the full names as annotations. 
### USAGE

The command can be run using the different arguments described below. Different arguments can be combined.
pp2dml - Run the peak picking and peak classification algorithms and display the annotated picked peaks on the spectrum.
pp2dml -f - Force the command to run on spectra other than a COSY, HSQC or HMBC. In this case, no peak annotation is available. 
pp2dml -shoulder - Include peaks that appear as shoulder to other, more intense peaks, in the peak picking procedure.
pp2dml -useprojection - Use the selected external projections (1D experiments) in F2 and/or F1 as filters to identify real NMR peaks, only retaining peaks with corresponding peaks in the 1D experiments. The external projections are analyzed using the deconvolution method mldcon. The 1D spectra will be internally aligned to the 2D spectrum prior to the filtering, but the resulting shift will not be applied to the TopSpin dataset.
pp2dml -mi=<value> - Minimum intensity of a peak relative to the most intense peak. All peaks identified with a lower intensity will be discarded. This ignores the signs of the peaks. Default value: 0.0.
pp2dml -maxi=<value> - Maximum intensity of a peak relative to the most intense peak. All peaks identified with a higher intensity will be discarded. This ignores the signs of the peaks. Default value: 1.0.
pp2dml -psign=<value> - Sign of the peaks to pick. “pos” for only positive peaks, “neg” for only negative peaks, and “both” for both positive and negative peaks. Default value: “both”.
pp2dml -rangeF2=<value1>,<value2> - Run the peak picking algorithm in the region of the spectrum between <value1> and <value2> ppm in F2. This command can be combined with the option -rangeF1 to specify a region both in F2 and F1 direction.
pp2dml -rangeF1=<value1>,<value2> - Run the peak picking algorithm in the region of the spectrum between <value1> and <value2> ppm in F1. This command can be combined with the option -rangeF2 to specify a region both in F2 and F1 direction.
pp2dml -ppdiag=<value> - Tolerance to identify and discard a peak on the diagonal (number of points). A value of 0 will not filter out diagonal peaks. Default value: 0.
pp2dml -ppmpnum=<value> - Maximum number of peaks to pick. If set, only the defined number of most intense peaks will be retained. A value of 0 corresponds to no limit on the number of peaks. 
pp2dml -ppfilter - Use the values in the Peak panel of the processing parameters tab. If set, the values in the Peak panel take precedence over the values defined using the -mi, -maxi, -psign, -rangeF2, -rangeF1, -ppdiag, and -ppmpnum arguments.
pp2dml -fulllabel - Display full peak labels as annotations instead of one-letter abbreviations.
pp2dml -onlycompound - Only pick peaks identified as the main compound in the sample, the solvent, residual water, or TMS.
pp2dml -noannotation - Only run the peak picker, prevents running the peak annotation step.
pp2dml -nosymmetryfilter - Disable the symmetry filter in COSY spectra, enabling the identification of peaks that have no symmetric counterpart.
pp2dml -getnoise - Return the noise level in the peaklist.xml file. The noise level is computed as the difference between the 84th and 16th percentiles of all spectral amplitudes. This corresponds to two standard deviations of a normal distribution describing the histogram of amplitudes in the spectrum.


## INPUT FILES

<dir>/data/<user>/nmr/<name>/<expno>/
acqu - F2 acquisition parameters
acqu2 - F1 acquisition parameters
<dir>/data/<user>/nmr/<name>/<expno>/pdata/<procno>/
2rr - Real processed 2D data
proc - F2 processing parameters, including peak picking parameters
proc2 - F1 processing parameters
curdat2 - Reference to the external projections


## OUTPUT FILES

<dir>/<name>/<expno>/pdata/<procno>/
peaklist.xml - 2D peak list in XML format


## USAGE IN AU PROGRAMS

PP2DML


## SEE ALSO

Other peak picking algorithms:
pps, ppf, ppl, pph, ppj, ppd, pp2d, pp, pp3d
Other ML commands:
apbk, sigreg, mldcon
© 2025 Bruker BioSpin GmbH & Co. KG
