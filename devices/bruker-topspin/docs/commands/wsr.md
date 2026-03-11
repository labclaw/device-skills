# wsr

**Category:** Commands > Process > Advanced

## NAME

**wsr** - Replace row of a 2D spectrum by 1D spectrum


## DESCRIPTION

The command wsr replaces one row of 2D processed data by 1D processed data. It is normally used in combination with rsr in the following way: 
1. run rsr to extract row x from a 2D spectrum
2. manipulate the resulting 1D data with 1D processing commands
3. run wsr to replace row x of the 2D data with the manipulated 1D data
wsr can be entered on the source 1D dataset or on the destination 2D dataset. 
Examples of the usage of wsr on the source 1D dataset:
1. wsr prompts for the row of the destination 2D data which must be replaced by the current 1D data. The 2D dataset is the one from which the current 1D dataset was extracted.
2. wsr <row> the specified row of the destination 2D data is replaced by the current 1D data. The 2D dataset is the one from which the current 1D dataset was extracted.
3. wsr <row> <procno> the specified row of the destination 2D data is replaced by the current 1D data. The 2D dataset must reside under the current data name (however, if the current data name is ~TEMP, wsr <row> <procno> writes to the specified procno in the dataset from which the current 1D dataset was extracted), the current expno and the specified procno.
Examples of usage of wsr on the destination 2D dataset:
1. wsr <row> the specified row of the current 2D processed data is replaced. The source 1D data must reside under the data name ~TEMP.
2. wsr <row> <procno> the specified row of the current 2D processed data is replaced. The source 1D data must reside under the current data name, the current expno and the specified procno.
wsr can also be started from the dialog box that is opened with the command slice.


## INPUT FILES

<dir>/data/<user>/nmr/~TEMP/1/pdata/1
  1r, 1i - 1D processed data
  used_from - data path of the 2D data (input of wsr on a 1D dataset)
or 
<dir>/data/<user>/nmr/<name>/<expno>/pdata/<procno>
  1r, 1i - 1D processed data
  used_from - data path of the 2D data (input of wsr on a 1D dataset)


## OUTPUT FILES

<dir>/data/<user>/nmr/<name>/<expno>/pdata/<procno>
  2rr, 2ir - processed 2D data
  auditp.txt - processing audit trail


## USAGE IN AU PROGRAMS

WSR(row, procno, expno, name, user, dir)


## SEE ALSO

wsc, rsr, rsc, wser, wserp, rser, rser2d, r12, r13 
© 2025 Bruker BioSpin GmbH & Co. KG
