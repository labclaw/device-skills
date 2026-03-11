# genfid

**Category:** Commands > Process > Advanced

## NAME

**genfid** - Generate pseudo-raw data (1D)


## DESCRIPTION

The command genfid generates pseudo-raw data from processed data. When entered without arguments, it opens a dialog box where you can specify the destination dataset.
 
genfid is normally used in combination with the command ift which performs an inverse Fourier transform, converting a spectrum into an FID. Actually, ift transforms processed frequency domain data into processed time domain data. genfid converts these processed time domain data into pseudo-raw time domain data and stores them under a new name or experiment number (expno).
Note that genfid does not modify the data, but only stores them in a different format. The number of data points of the pseudo-raw data is twice the size (SI) of the processed data they are created from. The acquisition status parameter TD (types s td or dpa) is set; accordingly, TD = 2*SI.
genfid takes arguments and can be used as follows:
1. genfid <expno>
2. The FID will be stored under the specified expno.
3. genfid <expno> <name> y
4. The FID will be stored under the specified name and expno. The last argument (y) causes genfid to overwrite possibly existing data.
You can use any other combination of arguments as long they are entered in the correct order. The processed data number (procno) of the output dataset is always set to 1.
genfid can be used if you want to reprocess a 1D spectrum, for example with different processing parameters, but the raw data do not exist anymore. An example of such a procedure is: 
ift (if the data are Fourier transformed)
genfid (to create the pseudo-raw data)
edp (to set the processing parameters)
ef (to process the pseudo-raw data)
If the input data are processed but not Fourier transformed, you can skip the first step.


## INPUT FILES

<dir>/data/<user>/nmr/<name>/<expno>/pdata/<procno>/
1r, 1i - processed time domain data (real, imaginary)


## OUTPUT FILES

<dir>/data/<user>/nmr/<name>/<expno>/
fid - pseudo-raw data
audita.txt - acquisition audit trail


## USAGE IN AU PROGRAMS

GENFID(expno)
Overwrites possibly existing raw data in the specified expno


## SEE ALSO

ift, genser
© 2025 Bruker BioSpin GmbH & Co. KG
