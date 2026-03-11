# exprof

**Category:** Commands > Manage > Spectrometer > Experiments/Parameters

## NAME

**exprof** - Display excitation profile of selective experiment


## DESCRIPTION

The command exprof displays the excitation profile of a selective experiment. The experiment must have been completely setup for acquisition, before exprof is executed. 
The command exprof opens the dialog shown in the next figure.
 
The dialog offers the following options:
1. Reference Pulse
- The 90° hard pulse in the same channel as the selective pulse.
2. Selective Pulse
- The selective pulse to be examined. If your pulse program contains only one selective pulse, and it follows the Bruker style guide (P1=90°, etc.) exprof automatically selects the correct reference pulse.
3. Selective Pulse Type
- The rotation type is a selective pulse which allows the excitation of a reduced defined frequency range of the spectrum. Automatically set to the value stored in the shape file. If the shape file does not contain a rotation type, it is set to „not yet known“ and must be selected in the dialog. Shapes created with external programs may not contain the rotation type.
4. Calculated Region (greyed if no spectrum exists)
- The profile can be calculated for the entire spectrum or for the currently displayed region. It always consists of 1000 points.
5. Keep Previous Results
- If enabled, the result of previous exprof command(s) is kept, allowing simultaneous display of multiple profiles.
If your pulse program contains only one selective pulse and the waveform contains rotation type, you don’t have to set anything in the exprof dialog. Just click OK, to confirm the dialog.
The command exprof requires that the NMRSim program, delivered on the TopSpin DVD, is installed.
For further Information please see the Shape Tool manual and the Pulse Programming Manual under Help | Manuals. 
### OUTPUT PARAMETERS

1. PULPROG - pulse program used for the acquisition
2. SHAPE - array of shaped pulse parameters


## INPUT FILES

1. <dir>/data/<user>/nmr/<name>/<expno>/
1. acqu - acquisition parameters
2. <tshome>/exp/stan/nmr/lists/wave/*
1. Shape files


## SEE ALSO

nmrsim
© 2025 Bruker BioSpin GmbH & Co. KG
