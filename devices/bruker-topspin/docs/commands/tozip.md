# tozip

**Category:** Commands > Miscellaneous > Dataset Handling

## NAME

**tozip** - Write current dataset to a ZIP file (nD)


## DESCRIPTION

The command tozip converts a TopSpin dataset to ZIP format.
It opens a dialog box where you can enter the required information:
This information includes:
Name of archive file: output file name and extension (<datasetname> .topspin.zip)
Directory of archive file: directory where output file is stored.
 
Type of archive:
1. ZIP-compress - Compressed nmr data in zip format.
2. ZIP-no compress - Uncompressed nmr data in zip format.
 
Data types included:
1. FID+RSPEC+ISPEC: Raw, real and imaginary processed data.
2. FID+RSPEC: Raw + real processed data.
3. FID: Raw data.
4. RSPEC+ISPEC: Real and imaginary processed data.
5. RSPEC: Real processed data.
 
Zip current EXPNO/PROCNO only, or all of ...: Archive current expno/procno or all expnos/procnos in current data set. 
 
Options for tozip dialog window:
Without argument, tozip will open it’s dialog showing the default destination file <dataname>.topspin.zip. You can change this default as follows:
1. Enter expl prop in TopSpin command line to open the file explorer in the user properties directory.
2. Edit the file globals.prop.
3. Add the line: 
- TOZIP_CONFIG=option1|option2
- Where the options must be separated by the character "|" and 
1. option1= N, NE or NEP, for name, name-expno or name-expno-procno, respectively.
2. option2 = any string, e.g. “-mycompany.zip“
 
Example:
Dataset: "exam1d_13C 102 1 c:\bruker\topspin guest"
option2=.bruker.zip
1. If option1=N:
1. the default name is: exam1d_13C.bruker.zip.
2. If option1= NE: 
1. the default name is exam1d_13C-102.bruker.zip
3. If option1 was NEP:
1. the default name is exam1d_13C-102-1.bruker.zip
 
Options for the command tozip
1. Arguments for the command tozip:
2. The command tozip takes four arguments, "tozip optionA, optionB, optionC, optionD":
1. optionA = nmr-data which should be transferred to zip file.
2. optionB = name and directory of archive data.
3. optionC = FID_RE_IM, FID_RE, FID, RE_IM, RE, PARAMS.
4. optionD = COMPRESS, NO_COMPRESS.
 
Zipfile from command line: 
The command tozip can be executed on the command line with the option ’- d’ and only the path name of the new zip file:
tozip -d <path>/<filename>.zip
This command transfers the raw and processed data in uncompressed zip-format. If the graphical user interface should be used, simply enter the command tozip as described above.
 
Zip file from within an AU Program: 
In AU Programs both commands tozip and tozip -d can be used with the command sendgui. 
The following two examples show the entering-procedure:
XCMD("sendgui tozip -d C:/mydata.zip")
QUIT
 
XCMD("sendgui tozip C:/Bruker/ts21pl1/data/guest/nmr/exam1d_1H/1/pdata/1, C:/testdata.zip, FID_RE_IM, NO_COMPRESS")
QUIT


## INPUT FILES

If Data type includes FID
<dir>/data/<user>/nmr/<name>/<expno>/
fid - 1D raw data
ser - 2D or 3D raw data
### If Data type includes RSPEC

<dir>/data/<user>/nmr/<name>/<expno>/pdata/<procno>
1r - real processed 1D data
2rr - real processed 2D data
3rrr - real processed 3D data
### If Data type includes ISPEC

<dir>/data/<user>/nmr/<name>/<expno>/pdata/<procno>
1i - imaginary processed 1D data
2ir, 2ri, 2ii - imaginary processed 2D data
3irr, 3rir, 3iii - imaginary processed 3D data
The parameter files acqu* and proc* are stored for all data types.


## OUTPUT FILES

<pathname>/<mydata.topspin.zip> - TopSpin data in ZIP format


## SEE ALSO

fromzip, tojdx, totxt
© 2025 Bruker BioSpin GmbH & Co. KG
