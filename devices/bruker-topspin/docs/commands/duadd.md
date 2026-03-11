# add, duadd, addfid, addc, adsu

**Category:** Commands > Process > Advanced

## NAME

**add** - Add two data sets point-wise, multiply 2nd with DC (1D)

**duadd** - Add two data sets ppm/Hz-wise, mult. 2nd with DC (1D)

**addfid** - Add two FIDs, multiply 2nd with DC (1D)

**addc** - Add the constant DC to the current data set

**adsu** - Open add/subtract/multiply workflow button bar (1D, 2D)


## DESCRIPTION

Addition commands can be entered on the command line or started from the add/subtract/multiply workflow button bar. The latter is opened with the command adsu.
This workflow button bar offers several options, each of which selects a certain command for execution.

 
### Add a 1D spectrum point-wise

This option selects the command add for execution. It adds the second data set, multiplied with the constant DC, to the current data set. add performs a point-to-point addition which is independent of the spectrum calibration. The result is stored in the current data set. DC can be set by entering dc on the command line or in the Procpars pane. If the second data set has not been defined yet, the add/subtract dialog box is opened. Here you can define the second data set and start the add command. add works on raw or on processed data, depending on the value of DATMOD. For DATMOD = raw, add adds the raw data of the current and second data set but stores the result as processed data in the current data set. The raw data of the current data set are not overwritten.
### Add a 1D spectrum ppm/Hz-wise

This option selects the command duadd for execution. It works like add, except that it adds two data sets according to their chemical shift values. Each ppm value of one data set is added to the same ppm value of a second data set. 
duadd is useful when the two input spectra are:
1. of different size
2. referenced differently
3. acquired with different frequencies (i.e. on different spectrometers)
 
For data with equal size, reference, and spectrometer frequency, add and duadd give the same result.
Furthermore, duadd allows to shift the second spectrum by a user defined number of ppm. The parameter ppm or hz is only relevant if the input data were acquired with different basic frequencies, i.e. when they come from different spectrometers. duadd only works on processed data, independent of the value of DATMOD.
### Add an FID

This option selects the command addfid for execution. It adds two 1D raw data sets multiplying one of them with the factor DC. The result is stored in the current data set. It works like add with DATMOD = raw, except that it overwrites the raw data.
### Add a constant

This option selects the command addc for execution. It adds the value of DC to the current data set. It works on raw or processed data, depending on the value of DATMOD. The result is stored as processed data in the current data set.
If you run a command like add from the command line, it behaves slightly different. It adds the second and the third data set, as specified with edc2 and stores the result in the current data set. You have to make sure that the required parameters are already set. Click the Procpars tab or enter edp to do that.
The adsu command can be used on 1D or 2D data. It recognizes the data dimensionality and opens a workflow button bar with the appropriate options and parameters.


## INPUT PARAMETERS

Set from the adsu workflow button bar, with edp or by typing dc, datmod etc.:
DC - multiplication factor
DATMOD - data mode: work on raw or processed data


## INPUT FILES

<dir>/data/<user>/nmr/<name>/<expno>/
fid - current raw data (input of add/addc if DATMOD = raw)
<dir>/data/<user>/nmr/<name>/<expno>/pdata/<procno>/
1r, 1i - current processed data (input of add/addc if DATMOD = proc)
proc - processing parameters
curdat2 - definition of the second data set
<dir2>/data/<user2>/nmr/<name2>/<expno2>/
fid - second raw data (input of add if DATMOD = raw, addfid)
<dir2>/data/<user2>/nmr/<name2>/<expno2>/pdata/<procno2>/
1r, 1i - second processed data (input of add if DATMOD = proc)


## OUTPUT FILES

<dir>/data/<user>/nmr/<name>/<expno>/
fid - current raw data (output of addfid)
audita.txt - acquisition audit trail (output of addfid)
<dir>/data/<user>/nmr/<name>/<expno>/pdata/<procno>/
1r, 1i - current processed data (output of add and addc)
procs - processing status parameters 
auditp.txt - processing audit trail (output of add and addc)


## USAGE IN AU PROGRAMS

ADD
ADDFID
ADDC
© 2025 Bruker BioSpin GmbH & Co. KG
