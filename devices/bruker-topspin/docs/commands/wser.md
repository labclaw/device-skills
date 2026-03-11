# wser

**Category:** Commands > Process > Advanced

## NAME

**wser** - Replace row of 2D raw data by 1D raw data (2D)


## DESCRIPTION

The command wser replaces one row of 2D raw data by 1D raw data. It can be entered on the source 1D dataset or on the destination 2D dataset. When entered on a 1D dataset, wser opens the following dialog box: 
 
Enter the FID number to be replaced and the destination data path.
Usage of wser with arguments on the source 1D dataset:
1. wser <row> the specified row of the 2D raw data is replaced by the current 1D FID. The destination 2D dataset is the one from which the current 1D dataset was extracted.
2. wser <row> <expno> the specified row of the 2D raw data is replaced by the current 1D FID. The 2D dataset must reside under the current data name, the specified expno and procno 1.
Usage of wser with arguments on the destination 2D dataset:
1. wser <row> <expno>  the specified row of the current 2D raw data is replaced. The source 1D dataset must reside under the current data name, specified expno and procno 1.


## INPUT FILES

<dir>/data/<user>/nmr/~TEMP/1/
  fid - 1D raw data
<dir>/data/<user>/nmr/~TEMP/1/pdata/1
  used_from - data path of the 2D data (input of wser on a 1D dataset)
or
<dir>/data/<user>/nmr/<name>/<expno>/
  fid - 1D raw data
<dir>/data/<user>/nmr/<name>/<expno>/pdata/<procno>/
  used_from - data path of the 2D data (input of wser on a 1D dataset)
wser can also be started from the dialog box that is opened with the command slice.


## OUTPUT FILES

<dir>/data/<user>/nmr/<name>/<expno>/
  ser - raw 2D data
  audita.txt - acquisition audit trail


## USAGE IN AU PROGRAMS

WSER(row, name, expno, procno, dir, user)
Note that the order of the arguments in AU programs is different from the order on the command line.


## SEE ALSO

r12, r13, r23, slice, rsc, rser2d, rsr, wsc, wserp, wsr
© 2025 Bruker BioSpin GmbH & Co. KG
