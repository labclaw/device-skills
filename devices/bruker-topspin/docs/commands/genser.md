# genser

**Category:** Commands > Process > Advanced

## NAME

**genser** - Generate pseudo-raw data (2D)


## DESCRIPTION

The command genser generates pseudo-raw data from processed 2D data. When entered without arguments, genser opens the following dialog box: 
 
Here, you specify the output dataset and click OK to execute the command. genser is normally used in combination with xif2 and xif1. These commands perform an inverse Fourier transform, converting processed frequency domain data into processed time domain data. genser converts these processed time domain data into pseudo-raw time domain data and stores them under a new name or experiment number (expno).
### NOTE

Note that genser does not modify the data, but only stores them in a different format. The number of data points of the pseudo-raw data is twice the size (SI) of the processed data they are created from. The acquisition status parameter TD (type dpa) is set; accordingly, TD = 2*SI. This counts for both the F2 and F1 direction.
genser takes three arguments and can be used as follows: 
1. genser opens a dialog box where you can specify the output data.
2. genser <expno> stores the output under the specified expno and opens a new data window displaying this expno.
3. genser <expno> n stores the output under the specified expno, but does not open and display this expno. 
If the specified expno already exists, you will be prompted to overwrite it or not. You can force the overwrite by specifying the extra argument y on the command line: 
1. genser <expno> y n stores the output under the specified expno, overwriting it if it exists, but does not open and display this expno. 
The processed data number (procno) of the new dataset is always set to 1.
genser can be useful if you want to reprocess a 2D spectrum, for example with different processing parameters, but the raw data do not exist any longer. An example of such a procedure is: 
xif2 (if the data are Fourier transformed in F2)
xif1 (if the data are Fourier transformed in F1)
genser (to create the pseudo-raw data)
edp (to set the processing parameters)
xfb (to process the pseudo-raw data)
If the input data are processed but not Fourier transformed, you can skip the first two steps.


## INPUT FILES

<dir>/data/<user>/nmr/<name>/<expno>/pdata/<procno>/
2rr, 2ir, 2ri, 2ii - processed time domain data


## OUTPUT FILES

<dir>/data/<user>/nmr/<name>/<expno>/
ser - pseudo-raw time domain data
audita.txt - acquisition audit trail


## USAGE IN AU PROGRAMS

GENSER(expno)


## SEE ALSO

genfid, xif2, xif1
© 2025 Bruker BioSpin GmbH & Co. KG
