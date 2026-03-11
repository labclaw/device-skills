# bc

**Category:** Commands > Process > Baseline

## NAME

**bc** - Baseline correction of the FID (1D)


## DESCRIPTION

The command bc performs a baseline correction of raw 1D data. The type of correction is determined by the processing parameter BC_mod as shown in the following table:
BC_mod
Function subtracted from the FID 
Detection mode
no
no function
 
single
average intensity of the last quarter of the FID
single channel
quad
average intensity of the last quarter of the FID
quadrature
spol
polynomial of degree 5 (least square fit)
single channel
qpol
polynomial of degree 5 (least square fit)
quadrature
sfil
Gaussian function of width BCFW*
single channel
qfil
Gaussian function of width BCFW
Quadrature
*Marion, Ikura, Bax, J. Magn. Res. 84, 425-420 (1989)
 
spol/qpol and sfil/qfil are especially used to subtract strong signals, e.g. a water signal at the centre of the spectrum. Note that sfil/qfil perform a better reduction at the risk of losing valuable signal. For reducing off-centre signal, you can set the parameter COROFFS to the offset frequency.
In this table, s(ingle) stands for single detection mode and q(uad) for quadrature detection mode. bc evaluates BC_mod for the function to be subtracted but not for the detection mode. The latter is evaluated from the acquisition status parameter AQ_mod. This means, for example, it does not matter if you set BC_mod to single or quad. The same counts for the values spol/qpol and sfil/qfil. Furthermore, for AQ_mod = DQD, no baseline correction is performed for BC_mod = single or quad. Note that the commands trf and xtrf* do evaluate the detection mode from BC_mod and perform the baseline correction for BC_mod = single/quad when AQ_mod = DQD. 
The command bc is automatically executed as a part of the commands em, gm, ft, or any of the composite Fourier transform commands.
When executed on a 2D or 3D dataset, bc prompts you for the row and output procno. Alternatively, it can be entered with up to four arguments: 
bc <row> <procno> n y 
processes the specified row and stores it under the specified procno. 
The last two arguments are optional: n prevents changing the display to the output 1D data, y causes a possibly existing data to be overwritten without warning.
When executed on a dataset with 2D or 3D raw data but 1D processed data (usually a result of rsr, rsc or a 1D processing command on that 2D or 3D data set), bc takes one argument bc <row> to process the specified row and stores it under the current procno.
bc same processes the same row as the previous processing command and stores it under the current procno. The same option is automatically used by the AU program macro BC. When used on a regular 1D dataset (i.e. with 1D raw data) it has no effect.
bc can also be started from the baseline dialog box which is opened with the command bas.


## INPUT PARAMETERS

Set from the bas dialog box, with edp or by typing bc_mod, bcfw etc.:
BC_mod - FID baseline correction mode
BCFW - filter width for BC_mod = sfil or qfil
COROFFS - correction offset in Hz, for BC_mod = spol or qpol and sfil/qfil


## INPUT FILES

<dir>/data/<user>/nmr/<name>/<expno>/
fid - raw data (time domain)
<dir>/data/<user>/nmr/<name>/<expno>/pdata/<procno>/
proc - processing parameters


## OUTPUT FILES

<dir>/data/<user>/nmr/<name>/<expno>/pdata/<procno>/
1r, 1i - processed data (time domain)
procs - processing status parameters
auditp.txt - processing audit trail


## USAGE IN AU PROGRAMS

BC
© 2025 Bruker BioSpin GmbH & Co. KG
