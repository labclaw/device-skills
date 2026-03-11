# autocalib

**Category:** Commands > Process > Calibrate Axis

## NAME

**autocalib** - Automatic calibration to align 2D and 1D datasets relative to a 2D reference dataset


## DESCRIPTION

The command autocalib align 2D and 1D datasets relative to a reference (the first dataset given in the call). As a requirement, the reference must be a 2D dataset.
### OUTPUT PARAMETERS

Because of the shifting in the alignment the following parameter will be adapt (except for the reference):
SR – Spectrum reference frequency
### USAGE

autocalib F1 F2 “<path_reference>” “<path_data1>” “<path_data2>” ….
F1 / F2 – determine the direction for the alignment
<path_reference> - the first given dataset is the reference as a default (has to be 2D)
<path> - all paths have to be given in the following absolute format: 
<path-to-data>\<expno>\pdata\<procno>


## SEE ALSO

The interactive usage in the TopSpin User Manual – 2D Calibration in Multiple Display.
© 2025 Bruker BioSpin GmbH & Co. KG
