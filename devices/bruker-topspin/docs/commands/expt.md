# expt

**Category:** Commands > Acquire > Run

## NAME

**expt** - Calculate and show the experiment time


## DESCRIPTION

The command expt calculates and displays the experiment time for the current data set (see the next figure).
 
If this exceeds the time you have available, you can reduce the number of scans (parameter NS) until the experiment time is acceptable. 
Alternatively, the acquisition time (parameter AQ) can be reduced, modifying accordingly parameters SW and TD. Avoid truncation of the signal. Also D0 (relaxation delay) can be reduced). In this case take care not to saturate (overflow) the receiver, in case of too fast pulsing (complete relaxation should still occur).
For 2D experiments, the resolution in the indirect dimension F1 can be reduced (TD1 parameter), as long as the resolution remains sufficient (sometimes a compromise has to be made between all these possibilities).
For 2D and 3D experiments, expt also compares the file size of the raw data with the available disk space.
expt can also be executed by clicking the button in the toolbar.
expt optionally takes a command line argument - the name of the destination file. In this case, the result is written to a specified file in the procno folder of the current dataset. No dialog is displayed. Example:
1. expt result
2. Writes the experiment time to the file result.


## INPUT PARAMETERS

1. NS - number of scans
2. AQ - acquisition time in seconds


## SEE ALSO

zg, gs
© 2025 Bruker BioSpin GmbH & Co. KG
