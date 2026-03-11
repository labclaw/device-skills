# smail

**Category:** Commands > Miscellaneous > Dataset Handling

## NAME

**smail** - Send Data by E-Mail to E-Mail recipient


## DESCRIPTION

The command smail sends the current data set by E-mail. It opens a dialog box where you can specify the required information or accept the default values.
 
In the dialog box, you can select the:
1. Archive type: ZIP or JCAMP
2. Data type(s) included: FID, spectrum and/or parameters
For ZIP format data you can choose between compression and no compression.
For JCAMP format, you can choose between the following compression modes: 
1. FIX (=0) : Table format
2. PACKED (=1) : No spaces between the intensity values
3. SQUEEZED (=2) : The sign of the intensity values is encoded in the first digit
4. DIFF/DUP (=3) : The difference between successive values is encoded, suppressing repetition of successive equal values (default = DIFF/DUP)
For the included data types, you have the following choices: 
1. FID+RSPEC+ISPEC: Raw + real and imaginary processed data
2. FID+RSPEC: Raw + real processed data
3. FID: Raw data
4. RSPEC+ISPEC: Real and imaginary processed data
5. RSPEC: Real processed data
6. PARAMS: Parameter files
Before you can send the data you must fill in the fields: 
1. To: The E-mail address of the recipient 
2. From: Your own E-mail address
3. SMTP mail server: 
4. Subject: 
5. Text:


## INPUT FILES

<tshome>/prog/curdir/<user>/
curdat - current data definition
### If data type includes FID :

<dir>/data/<user>/nmr/<name>/<expno>/
fid - 1D raw data
ser - 2D raw data
### If data type includes RSPEC :

<dir>/data/<user>/nmr/<name>/<expno>/pdata/<procno>
1r - real processed 1D data
2rr - real processed 2D data
### If data type includes ISPEC :

<dir>/data/<user>/nmr/<name>/<expno>/pdata/<procno>
1i - imaginary processed 1D data
2ir - F2-imaginary processed 2D data
2ri - F1-imaginary processed 2D data
2ii - F2/F1-imaginary processed 2D data
All other files which are part of a data set like parameter files, audit trails files etc. are sent for all data types.


## OUTPUT FILES

<userhome>/<mydata.dx> - TopSpin data in JCAMP-DX format
<userhome>/<mydata.bnmr.zip> - TopSpin data in ZIP format


## SEE ALSO

tojdx, tozip
© 2025 Bruker BioSpin GmbH & Co. KG
