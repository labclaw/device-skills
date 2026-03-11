# xfbp, xf2p, xf1p

**Category:** Commands > Process > Adjust Phase

## NAME

**xfbp** - Phase correction in F2 and F1 direction (2D)

**xf2p** - Phase correction in F2 (2D)

**xf1p** - Phase correction in F1 (2D)

**ph** - Open phase correction command dialog box (1D, 2D)


## DESCRIPTION

2D phase correction can be started from the command line or from the phase correction dialog box. The latter is opened with the command ph:
 
This dialog box offers several options, each of which selects a certain command for execution.
Additive phasing using PHC0/1 (F2 and F1)
This option selects the command xfbp for execution. It performs a zero and first order 2D phase correction in the F2 and F1 direction. xfbp works like the 1D command pk. This means it does not calculate the phase values, it simply applies the current values of PHC0 and PHC1. 
Additive phasing using PHC0/1 (F2)
This option selects the command xf2p for execution. It works like xfbp, except that it only corrects the phase in the F2 direction. 
Additive phasing using PHC0/1 (F1)
This option selects the command xf1p for execution. It works like xfbp, except that it only corrects the phase in the F1 direction. 
xf*p are only useful when the PHC0 and PHC1 values are known. If they are not, you can perform 2D interactive phase correction. To do that, select the option Manual Phasing in the ph dialog box or click  in the toolbar. The interactive phase correction procedure is described in the TopSpin Users Guide.
The phase values can also be determined by the 1D interactive phase correction of a row or column. To do that, read a row (rsr) and/or column (rsc) and click  in the toolbar (see TopSpin Users Guide). Alternatively, you can phase correct a row or column with apk and view the calculated phase values with dpp. Then you can go back to the 2D dataset, set the determined phase values with edp and run xfbp to apply them.
xfbp uses but does not change the processing parameters PHC0 and PHC1 (edp). It does, however, change the corresponding processing status parameters (dpp), by adding the applied phase values.
The ph command can be used on 1D or 2D data. It recognizes the data dimensionality and opens a dialog box with the appropriate options and parameters.


## INPUT PARAMETERS

Set from the ph dialog box, with edp or by typing phc0, phc1: 
  PHC0 - zero order phase correction value (frequency independent) 
  PHC1 - first order phase correction value (frequency dependent)
### OUTPUT PARAMETERS

Can be viewed with dpp or by typing s phc0, s phc1: 
  PHC0 - zero order phase correction value (frequency independent) 
  PHC1 - first order phase correction value (frequency dependent)


## INPUT FILES

<dir>/data/<user>/nmr/<name>/<expno>/pdata/<procno>/
  2rr, ir, 2ri, 2ii - processed 2D data
  procs - F2 processing status parameters
  proc2s - F1 processing status parameters


## OUTPUT FILES

<dir>/data/<user>/nmr/<name>/<expno>/pdata/<procno>/
  2rr, ir, 2ri, 2ii - processed 2D data
  procs - F2 processing status parameters
  proc2s - F1 processing status parameters
  auditp.txt - processing audit trail


## USAGE IN AU PROGRAMS

XFBP
XF2P
XF1P


## SEE ALSO

xfb, ftf, xf2, xf1, xtrf, xtrf2, xtrfp, xtrfp2
© 2025 Bruker BioSpin GmbH & Co. KG
