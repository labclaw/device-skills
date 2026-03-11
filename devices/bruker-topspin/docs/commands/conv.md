# conv

**Category:** Commands > Miscellaneous > Dataset Handling

## NAME

**conv** - Convert Aspect 2000/3000 data to TopSpin format (1D, 2D, 3D)


## DESCRIPTION

The command conv converts DISNMR/DISMSL data (data from an Aspect 2000/3000) to the TopSpin format. It opens a file browser where you can:
1. Navigate to the input directory where the DISNMR/DISMSL data reside.
2. Select the data file to be converted and click convert.
- 
3. In the next dialog box specify the output TopSpin data set. Note that the data path variables are initialized as follows:
1. NAME is the file name of the DISNMR input data
2. EXPNO is the extension of the DISNMR input data set. If the extension is not numeric or if it is missing, EXPNO is initialized with 1.
3. PROCNO is set to 1 and cannot be changed.
4. DIR is the <DIR> value of the current TopSpin data path.
5. USER is the <USER> value of the current TopSpin data path.
 
The command conv executes the AU program disconv. This means the command expinstall must have been executed once, installing the Bruker AU programs, before you can use conv.
The dialog box shown above shows the button xau disinfo. Clicking this button executes the corresponding AU program showing the relevant data set parameters.


## INPUT FILES

<input directory>/* - A2000/3000 data


## OUTPUT FILES

<dir>/data/<user>/nmr/<name>/<expno>/
fid - Avance type 1D raw data
ser - Avance type 2D or 3D raw data
acqu - acquisition parameters
acqus - acquisition status parameters
 
<dir>/data/<user>/nmr/<name>/<expno>/pdata/<procno>
1r, 1i - converted processed 1D data
2rr, 2ir, 2ri, 2ii - converted processed 2D data
proc - processing parameters
procs - processing status parameters
For 2D data, the additional parameter files acqu2, acqu2s, proc2 and proc2s will be created. For 3D data, the additional parameter files acqu2, acqu2s, proc2 and proc2s and acqu3, acqu3s, proc3 and proc3s will be created.


## SEE ALSO

winconv, convdta, vconv, jconv, fconv
© 2025 Bruker BioSpin GmbH & Co. KG
