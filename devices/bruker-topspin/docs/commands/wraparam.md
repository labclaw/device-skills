# wrpa, wra, wrp, wraparam, wrpparam

**Category:** Commands > Miscellaneous > Dataset Handling

## NAME

**wrpa** - Copy a complete data set, raw and processed data (nD)

**wr** - Same as wrpa

**wra** - Copy raw data (nD) including processing parameters

**wrp** - Copy processed data (nD)

**wraparam** - Copy acquisition dataset (parameters only) including processing parameters

**wrpparam** - Copy processing dataset (parameters only)


## DESCRIPTION

The command wrpa writes (copies) a data set. It opens a dialog box where you can specify the destination data set:
 
When you click OK, the entire expno directory is copied including raw data, acquisition parameters, processed data and processing parameters. 
wrpa takes six arguments: 
<name> - the data set name
<expno> - the experiment number
<procno> - the processed data number
<dir> - the disk unit (data directory)
<user> - the user
y - overwrite the destination dataset if it already exists
All arguments are parts of the destination data path (the data path of the foreground data set is displayed above the TopSpin data field), except for the last one which is a flag. You can, but do not have to, specify all of these arguments. If the first argument is a character string, it is interpreted as the destination data name. If the first argument is an integer value, it is interpreted as the destination experiment number. Examples of using wrpa are:
wrpa <name> 
wrpa <expno> 
wrpa <name> <expno> 
wrpa <name> <expno> <procno>  
wrpa <name> <expno> <procno> <dir> <user> y 
wra makes a copy of the current expno directory, including raw data, acquisition parameters, and processing parameters. The command takes two arguments and can be used as follows:
wra - prompts you for the destination experiment number
wra <expno> - copies the raw data to <expno>
wra <expno> y - overwrites existing raw data in <expno>
wrp makes a copy of the current procno directory, including the processed data and processing parameters. The command takes two arguments and can be used as follows: 
wrp - prompts you for the destination processed data number
wrp <procno> - copies processed data to <procno>
wrp <procno> y - overwrites existing processed data in <procno>
wrpparam works like wrp, except that it does not copy the processed data files and auditp.txt file.
wraparam works like wra, except that it does not copy the raw data files and audita.txt file.
Note that the wr* commands only work if user who started TopSpin has the permission to create the destination data set. 
### INPUT AND OUTPUT FILES

For wrpa, wra and wraparam: 
<dir>/data/<user>/nmr/<name>/<expno>/
fid - 1D raw data
ser - 2D or 3D raw data 
acqu - acquisition parameters
acqus - acquisition status parameters
For wrpa and wra :
<dir>/data/<user>/nmr/<name>/<expno>/
fid - raw data (1D)
ser - raw data (nD)
audita.txt - acquisition audit trail
For wrpa, wra, wrp and wrpparam: 
<dir>/data/<user>/nmr/<name>/<expno>/pdata/<procno>/
proc - processing parameters
procs - processing status parameters
For wrpa, wra and wrp: 
<dir>/data/<user>/nmr/<name>/<expno>/pdata/<procno>/
1r, 1i - processed data (1D)
2rr, 2ir, 2ri, 2ii - processed data (2D)
3rrr, 3irr, 3rir, 3rri, 3iii - processed data (3D)
4rrrr, 4iiii - processed 4D data
auditp.txt - processing audit trail
For 2D data, the additional parameter files acqu2, acqu2s, proc2 and proc2s will be created. For 3D, 4D etc. data, the respective additional parameter files will be created.
Note that apart from data and parameters several other files are copied.


## USAGE IN AU PROGRAMS

WRPA(name, expno, procno, diskunit, user)
WRA(expno)
WRP(procno)
Note that these macros overwrite possibly existing data.


## SEE ALSO

dir, dira, dirp, dirdat, browse, new, open, re, rep, rew, repw, reb
© 2025 Bruker BioSpin GmbH & Co. KG
