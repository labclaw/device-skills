# accumulate

**Category:** Commands > Process > Advanced

## NAME

**accumulate** - Accumulate 1D datasets ppm/Hz-wise (1D)


## DESCRIPTION

The command accumulate accumulates 1D datasets. It adds a specified processed dataset to the current dataset. accumulate has the following features:
1. the specified data can be shifted and scaled with respect to the current data.
2. addition can be performed ppm-wise or hz-wise
3. the specified data can overwrite the current data or can be added to the current data
All required information must be specified by command line arguments. As such, accumulate takes 4 to 9 arguments. Here are some examples of its usage:
accumulate <offset> <scale> ppm |hz <procno>
Add the processed data of the specified procno to the current procno as follows:
1. shift the added data by <offset> ppm 
2. scale added data by the value <scale> 
3. perform the addition ppm-wise or hz-wise as specified
Example: accumulate 0.0 1.0 ppm 3
accumulate start <offset> <scale> ppm |hz <procno>
Same as above, except that the processed data of the specified procno are copied to the current procno, overwriting possibly existing data.
Example: accumulate start 0.0 1.0 ppm 3
Note that here, the arguments offset and ppm |hz do not affect the data but do affect the status parameter OFFSET. 
In the examples above, the accumulated dataset has the same datapath as the original data except for the procno. To accumulate data with a different datapath, you can specify other parts of the datapath as arguments. Parts that are not specified are taken from the current dataset.
Examples:
accumulate <offset> <scale> ppm |hz <procno> <expno>
accumulate start <offset> <scale> ppm |hz <procno> <expno> <user> <dir>
accumulate works like the command duadd, except that all information is specified on the command line. accumulate is typically used repeatedly to accumulate a series of 1D processed data. The first instance of accumulate overwrites the current data with the specified data, defining the accumulation start. All further instances add the specified data to the current data.
### OUTPUT PARAMETERS

OFFSET - the ppm value of the first data point of the spectrum


## INPUT FILES

<dir>/data/<user>/nmr/<name>/<expno>/pdata/<procno>/
1r, 1i - current processed data
proc - processing parameters
<dir2>/data/<user2>/nmr/<name2>/<expno2>/pdata/<procno2>/
1r, 1i - second processed data


## OUTPUT FILES

<dir>/data/<user>/nmr/<name>/<expno>/pdata/<procno>/
1r, 1i - current processed data
procs - processing status parameters 
auditp.txt - processing audit trail


## SEE ALSO

add, duadd, addfid, addc, adsu
© 2025 Bruker BioSpin GmbH & Co. KG
