# rser

**Category:** Commands > Process > Advanced

## NAME

**rser** - Read row from 2D raw data and store as 1D FID (2D,1D)


## DESCRIPTION

The command rser reads a row from 2D or 3D raw data (a series of FIDs) and stores it as a 1D dataset. It opens a dialog box where you can specify the FID number and the expno of the output data. 
 
For 2D data, the row must be specified as a number between 1 and F1-TD. The latter is the F1 acquisition status parameter TD that can be viewed with s td.
rser is normally entered on the 2D dataset. It then takes up to three arguments and can be used as follows:
rser prompts for the row number and stores it under data name ~TEMP
rser <row> stores the specified row under data name ~TEMP
rser <row> <expno> stores the specified row under the current data name and the specified expno and then changes the display to this expno 
rser <row> <expno> n stores the specified row under the current data name and the specified expno but does not change the display to this expno
rser <row> <expno> eao performes EA calculation in all dimensions with acquisition status parameter FnMODE = Echo-Antiecho and stores the specified row under the current data name and the specified expno.
After rser has read a row and the display has changed to the destination 1D dataset, a subsequent rser command can be entered on this 1D dataset. This takes two arguments and can be used as follows:
rser opens the above dialog box where you can specify the row number and the procno of the 2D dataset from which the current 1D dataset was extracted.
rser <row> reads the specified row from the 2D dataset from which the current 1D dataset was extracted.
rser <row> <expno> reads the specified row from the 2D dataset that resides under the current data name (however, if the current data name is ~TEMP, the input dataset is the one from which the current 1D dataset was extracted, except for the specified expno (procno), the specified expno and procno 1.
### NOTE

Note that on 3D data, rser does not distinguish between the F2 and F1 direction and treats the 3D dataset as a large 2D dataset. This implies that the row number must lie between 1 and (F2-TD) * (F1-TD).
rser can also be started from the dialog box that is opened with the command slice.


## INPUT FILES

<dir>/data/<user>/nmr/<name>/<expno>/
ser - 2D or 3D raw data


## OUTPUT FILES

If the output expno is specified:
<dir>/data/<user>/nmr/<name>/<expno>/
fid - 1D FID
audita.txt - acquisition audit trail
<dir>/data/<user>/nmr/<name>/<expno>/pdata/1/
used_from - data path of the source 2D data and the row no.
If no output expno is specified:
<dir>/data/<user>/nmr/~TEMP/1/
fid - 1D FID
<dir>/data/<user>/nmr/~TEMP/1/pdata/1
used_from - data path of the source 2D data and the row no.


## USAGE IN AU PROGRAMS

RSER(row, expno, procno)
If expno = -1, the row is written to the dataset ~TEMP


## SEE ALSO

r12, r13, r23, slice, rsc, rser2d, rsr, wsc, wser, wserp, wsr
© 2025 Bruker BioSpin GmbH & Co. KG
