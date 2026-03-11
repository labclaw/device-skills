# tilt, ptilt, ptilt1

**Category:** Commands > Process > Processing Spectrum

## NAME

**tilt** - Tilt a 2D spectrum

**ptilt** - Tilt a 2D spectrum by shifting the data in the F2 direction

**ptilt1** - Tilt a 2D spectrum by shifting the data in the F1 direction

**symt** - Open symmetrization and tilt commands dialog box (2D)


## DESCRIPTION

The symt command opens the symmetrize/tilt dialog box. 
 
This dialog box offers several options, each of which selects a certain command for execution.
### Auto-tilt along rows

This option selects the command tilt for execution. It tilts the 2D spectrum, shifting each row of the 2D spectrum by the value: 
  n = tiltfactor * (nsrow/2 - row)
The variables in this equation are defined as:
  tiltfactor = (SW_p1/SI1) / (SW_p2/SI2)
  nsrow = total number of rows 
  row = the row number
Where SW_p1, SI1, SW_p2 and SI2 represent the processing status parameters SW_p and SI in F1 and F2, respectively.
The upper half of the spectrum is shifted to the right, the lower half to the left. Furthermore, this is a circular shift, i.e. the data points which are cut off at the right edge of the spectrum are appended at the left edge and vice versa. 
### Tilt along rows

This option selects the command ptilt for execution. It tilts the 2D spectrum about a user defined angle, by shifting the data points in the F2 direction. It is typically used to correct possible magnet field drifts during long term 2D experiments. The tilt factor is determined by the F2 processing parameter ALPHA which can take a value between -2 and 2. Each row of the 2D matrix is shifted by n points where n is defined by: 
  n = tiltfactor * (nsrow/2 - row)
The variables in this equation are defined by:
  tiltfactor = ALPHA*SI2 / SI1
  nsrow = total number of rows 
  row = the row number
Where SI2 and SI1 are processing status parameter SI in F2 and F1, respectively.
### Tilt along columns

This option selects the command ptilt1 for execution. It tilts the 2D spectrum about a user defined angle, by shifting the data points in the F1 direction. The tilt factor is determined by the F1 processing parameter ALPHA which can take a value between -2 and 2. Each column of the 2D matrix is shifted by n points where n is defined by: 
  n = tiltfactor * (nscol/2 - col)
The variables in this equation are defined by:
  tiltfactor = ALPHA*SI1/ SI2
  nscol = total number of columns 
  col = the column number
Where SI2 and SI1 are processing status parameter SI in F2 and F1, respectively.
For F2-ALPHA = 1 and F1-ALPHA = 1:
1. the sequence ptilt - ptilt1 rotates the spectrum by 90° 
2. the sequence ptilt1 - ptilt rotates the spectrum by -90°.
When executed from the command line, the command tilt, ptilt and ptilt1 select the corresponding option in the dialog box. This means, you can just click OK or hit Enter to start the command. In contrast, symt selects the last used tilt command.


## INPUT PARAMETERS

Set from the symt dialog box, with edp or by typing alpha:
  ALPHA - tilt factor (used by ptilt and ptilt1)
Set by initial processing command, e.g. xfb, can be viewed with dpp:
  SW_p - spectral width of the processed data (used by tilt)
  SI - size of the processed data
### OUTPUT PARAMETERS

Can be viewed with dpp:
  TILT - shows whether tilt, ptilt or ptilt1 was done (true or false)


## INPUT FILES

<dir>/data/<user>/nmr/<name>/<expno>/pdata/<procno>/
  2rr - real processed 2D data


## OUTPUT FILES

<dir>/data/<user>/nmr/<name>/<expno>/pdata/<procno>/
  2rr - real processed 2D data
  auditp.txt - processing audit trail


## USAGE IN AU PROGRAMS

TILT
  PTILT
  PTILT1


## SEE ALSO

sym, syma, symj, symt
© 2025 Bruker BioSpin GmbH & Co. KG
