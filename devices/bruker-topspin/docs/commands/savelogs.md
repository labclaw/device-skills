# savelogs

**Category:** Commands > Manage > Commands

## NAME

**savelogs** - Save all TopSpin logfiles for debugging purposes


## DESCRIPTION

savelogs is mainly used for debugging purposes. This tool will collect support information about the current TopSpin installation (log and configuration files, by default no NMR data) and allows to transfer it to Bruker. It offers a Comments field to enter a description of your issue. 
Note: If already in contact with Bruker, give a reference to a mail or phone call or ticket number. 
If issues with spectra are observed, please add the respective NMR data with the Additional files or directories option.
The file transfer process has been changed from ftp to a https secured transfer method.
This tool is also available in the menu bar: 
1. Click Manage | Commands  | Collect & Save LogFiles
The Execute Savelogs window is displayed:
 
The recommended token will be provided by the Bruker support. If not available, enter your name and the name of your institution or company.
Once the savelogs command has created the savelogs file, the window changes and offers a direct upload of the file to Bruker.
 
1. Click Send to transfer the file and notify your Bruker Support team member once the upload has been completed. 
2. Click Open to see the resulting savelogs file for other transfer options. 
When the transfer has finished a message window is displayed. Click Close.
If TopSpin cannot be started: 
1. Under Windows:
1. Click the Bruker Utilities<topspin version> icon on your desktop. An Explorer will be opened.
2. Double-click Miscellaneous .
3. Execute the script savelogs .
2. Under Linux:
1. Open a shell.
2. Enter savelogs .
3. Under macOS:
1. Open Applications - <topspin version> Utilities .
2. Execute savelogs .


## INPUT FILES

User-specific installation files like history files etc. named:
<tshome>/prog/curdir/<user>/*


## OUTPUT FILES

<TS home>\savelogs\TopSpinSupport_<Token><user><YY><MM><DD><HH><MM>.zip


## SEE ALSO

hist 
© 2025 Bruker BioSpin GmbH & Co. KG
