# rsr

**Category:** Commands > Process > Advanced

## NAME

**rsr** - Read row from 2D data and store as 1D data (2D, 1D)


## DESCRIPTION

The command rsr reads a row from a 2D spectrum and stores it as a 1D spectrum. When entered on a 2D dataset without arguments, rsr opens a dialog box where you can specify the row number and the procno of the output data. 
 
The row must be specified as a number between 1 and F1-SI. The latter is the F1 processing status parameter SI that can be viewed with s si. The procno can be any number other that the current procno. If the procno field is left empty, the output dataset is stored under data name ~TEMP.
When entered on a 2D dataset, rsr takes up to three arguments and can be used as follows:
1. rsr <row> stores the specified row under data name ~TEMP
2. rsr <row> <procno> stores the specified row under the current data name, the current expno and the specified procno. It changes the display to the output 1D data.
3. rsr <row> <procno> n stores the specified row under the current data name, the current expno and the specified procno. It does not change the display to the output 1D data.
After rsr has read a row and the display has changed to the destination 1D dataset, a subsequent rsr command can be entered on this 1D dataset. This takes two arguments and can be used as follows:
1. rsr opens the dialog box where you can specify the row and procno of the 2D data.
2. rsr <row> reads the specified row from the 2D dataset from which the current 1D dataset was extracted.
3. rsr <row> <procno> reads the specified row from the 2D dataset that resides under the current data name (however, if the current data name is ~TEMP, rsr <row> <procno> reads from the specified procno in the dataset from which the current 1D dataset was extracted), the current expno and the specified procno. Specifying the procno allows to read a row from a 2D dataset other than the one from which the current 1D dataset was extracted. Furthermore, the AU macro RSR requires two arguments, no matter if it is used on a 1D or on a 2D dataset. 
rsr can also be started from the dialog box that is opened with the command slice.


## INPUT FILES

<dir>/data/<user>/nmr/<name>/<expno>/pdata/<procno>/
2rr, 2ir, 2ri, 2ii - 2D processed data


## OUTPUT FILES

If no procno is specified:
<dir>/data/<user>/nmr/~TEMP/1/pdata/1/
1r, 1i - 1D spectrum
used_from - data path of the source 2D data and the row no.
auditp.txt - processing audit trail
If the output procno is specified:
<dir>/data/<user>/nmr/<name>/<expno>/pdata/<procno>/
1r, 1i - 1D spectrum
used_from - data path of the source 2D data and the row no.
auditp.txt - processing audit trail


## USAGE IN AU PROGRAMS

RSR(row, procno)
If procno = -1, the row is written to the dataset ~TEMP


## SEE ALSO

r12, r13, r23, slice, rsc, rser2d, rtr, wsc, wser, wserp, wsr
© 2025 Bruker BioSpin GmbH & Co. KG
