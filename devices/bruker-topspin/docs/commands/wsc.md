# wsc

**Category:** Commands > Process > Advanced

## NAME

**wsc** - Replace column of 2D spectrum by 1D spectrum


## DESCRIPTION

The command wsc replaces one column of 2D processed data by 1D processed data. It is normally used in combination with rsc in the following way: 
1. Run rsc to extract column x from a 2D spectrum
2. Manipulate the resulting 1D data with 1D processing commands
3. Run wsc to replace column x of the 2D data with the manipulated 1D data
wsc can be entered on the source 1D dataset or on the destination 2D dataset.
Examples of the usage of wsc on the source 1D dataset:
1. wsc prompts for the column of the destination 2D data which must be replaced by the current 1D data. The 2D dataset is the one from which the 1D dataset was extracted.
2. wsc <column> the specified column of the destination 2D data is replaced by the current 1D data. The 2D dataset is the one from which the current 1D dataset was extracted.
3. wsc <column> <procno> the specified column of the destination 2D data is replaced by the current 1D data. The 2D dataset must reside under the current data name (however, if the current data name is ~TEMP, wsc <column> <procno> writes to the specified procno in the dataset from which the current 1D dataset was extracted), the current expno and the specified procno.
Examples of usage of wsc on the destination 2D dataset:
1. wsc <column> the specified column of the current 2D processed data is replaced. The source 1D data must reside under the data name ~TEMP
2. wsc <column> <procno> the specified column of the current 2D processed data is replaced. The source 1D data must reside under the current data name, the current expno and the specified procno.
Although wsc is normally used as described above, it allows to specify a full dataset path in the following way:
  wsc <column> <procno> <expno> <name> <user> <dir> 
When entered on a 1D dataset, the arguments specify the destination 2D dataset. When entered on a 2D dataset, the arguments specify the source 1D dataset. If only certain parts of the destination 2D data path are specified, e.g. the expno and name, the remaining parts are the same as in the current 1D data path. In AU programs, wsc must always have 6 arguments (see USAGE IN AU PROGAMS below).
wsc can also be started from the dialog box that is opened with the command slice.


## INPUT FILES

<dir>/data/<user>/nmr/~TEMP/1/pdata/1
  1r, 1i - 1D processed data
  used_from - data path of the 2D data (input of wsc on a 1D dataset)
or 
<dir>/data/<user>/nmr/<name>/<expno>/pdata/<procno>
  1r, 1i - 1D processed data
  used_from - data path of the 2D data (input of wsc on a 1D dataset)


## OUTPUT FILES

<dir>/data/<user>/nmr/<name>/<expno>/pdata/<procno>
  2rr, 2ri - processed 2D data
  auditp.txt - processing audit trail


## USAGE IN AU PROGRAMS

WSC(column, procno, expno, name, user, dir)


## SEE ALSO

r12, r13, r23, slice, rsc, rser2d, rsr, wser, wserp, wsr
© 2025 Bruker BioSpin GmbH & Co. KG
