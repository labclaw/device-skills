# wserp

**Category:** Commands > Process > Advanced

## NAME

**wserp** - Replace row of 2D raw data by 1D processed data


## DESCRIPTION

The command wserp replaces one row of 2D raw data by processed 1D data. It can be entered on the source 1D dataset or on the destination 2D dataset. When entered on a 1D dataset, wserp opens the following dialog box: 
 
Here, you can enter the FID number to be replaced and the destination data path.
Usage of wserp with arguments on the source 1D dataset:
1. wserp <row> the specified row of the 2D raw data is replaced by the current 1D processed data. The 2D dataset is the one from which the current 1D dataset was extracted. 
2. wserp <row> <expno> the specified row of the 2D raw data under the specified expno is replaced by the current 1D processed data. The 2D dataset name, user and dir are the same as in the dataset as the current 1D data were extracted from.
Usage of wserp with arguments on the destination 2D dataset:
1. wserp <row> <expno>  the specified row of the current 2D raw data is replaced. The source 1D dataset must reside under the current data name, specified expno and procno 1.
wserp can also be started from the dialog box that is opened with the command slice.


## INPUT FILES

<dir>/data/<user>/nmr/~TEMP/1/pdata/1/
  1r, 1i - 1D processed data (real, imaginary)
  used_from - data path of the 2D data (input of wserp on a 1D dataset)
or 
<dir>/data/<user>/nmr/<name>/<expno>/pdata/<procno>/
  1r, 1i - 1D processed data (real, imaginary)
  used_from - data path of the 2D data (input of wserp on a 1D dataset)


## OUTPUT FILES

<dir>/data/<user>/nmr/<name>/<expno>/
  ser - raw 2D data
  audita.txt - acquisition audit trail


## USAGE IN AU PROGRAMS

WSERP(row, name, expno, procno, dir, user)
Note that the order of the arguments in AU programs is different from the order on the command line.


## SEE ALSO

r12, r13, r23, slice, rsc, rser2d, rsr, wsc, wser, wsr
© 2025 Bruker BioSpin GmbH & Co. KG
