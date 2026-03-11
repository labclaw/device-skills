# convdta

**Category:** Commands > Miscellaneous > Dataset Handling

## NAME

**convdta** - Convert Avance type raw data to AMX type (1D, 2D, 3D)


## DESCRIPTION

The command convdta converts Avance type raw data to AMX type raw data. It can handle 1D, 2D and 3D data. This is useful if you want to process data that have been acquired on an Avance spectrometer on an AMX or ARX spectrometer.
 
convdta takes up to six arguments and can be used as follows:
1. convdta
2. You will be prompted for an expno under which the raw data must be stored.
3. convdta <expno>
4. The raw data will be stored under the specified expno.
5. convdta <expno> <name> y
6. The output will be stored under the specified name and expno. The last argument (y) causes convdta to overwrite existing data without a warning.
7. convdta <expno> <name> <user> <dir> y n
8. The output will be stored under the specified expno, name, user and dir. The second last argument (y) causes convdta to overwrite existing data without a warning. The last argument (n) causes the display to remain on the current data set rather than change to the output data set.
You can use any other combination of arguments as long they are entered in the correct order. The processed data number (procno) of the new data set cannot be chosen, it is always set to 1.


## INPUT FILES

<dir>/data/<user>/nmr/<name>/<expno>/
fid - Avance type 1D raw data
ser - Avance type 2D or 3D raw data
acqu - acquisition parameters
acqus - acquisition status parameters
 
<dir>/data/<user>/nmr/<name>/<expno>/pdata/<procno>
proc - processing parameters
procs - processing status parameters


## OUTPUT FILES

<dir>/data/<user>/nmr/<name>/<expno>/
fid - AMX type 1D raw data
ser - AMX type 2D or 3D raw data
acqu - acquisition parameters
acqus - acquisition status parameters
audita.txt - acquisition audit trail
 
<dir>/data/<user>/nmr/<name>/<expno>/pdata/<procno>
proc - processing parameters
procs - processing status parameters
For 2D data, the additional parameter files acqu2, acqu2s, proc2 and proc2s will be used. For 3D data, the additional parameter files acqu2, acqu2s, proc2 and proc2s and acqu3, acqu3s, proc3 and proc3s will be used.


## USAGE IN AU PROGRAMS

CONVDTA(expno)


## SEE ALSO

conv, fconv, jconv, vconv
© 2025 Bruker BioSpin GmbH & Co. KG
