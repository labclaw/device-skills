# gs

**Category:** Commands > Acquire > Run

## NAME

**gs** - Interactive parameter optimization during acquisition


## DESCRIPTION

The command gs opens a dialog box that consists of two panels. In the left panel, you can adjust parameters interactively during an acquisition (see the next figure). The right panel shows the FID display window where the fid is continuously updated showing the effect of each parameter change (see the figure gs display).
gs repeatedly executes the current pulse program but only up to the first go=n or rcyc=n statement. Therefore, gs:
1. Does not accumulate data.
2. Does not interpret the phase list.
3. Does not write data to disk.
 
The dialog box only shows the parameters which are typically set during gs like irradiation frequencies and offsets, pulse lengths and power levels. By default, the irradiation frequency Offset is selected for adjustment. You can adjust the indicated parameter by putting the cursor on the slider, pressing the left mouse button and moving the mouse. Alternatively, you can click above or below the slider bar. The slider sensitivity can be changed from the Sensitivity field. The following parameters can be changed from the gs dialog box:
1. SFO1 - SFO8 - irradiation frequency for channel f1- f8.
2. O1 - O8 - irradiation frequency offset for channel f1- f8.
3. PL[0-63] - square power levels.
4. AMP[0-31] – amplitude.
5. PHCOR[0-31] - reference phases.
6. PH_ref - receiver phase correction.
7. RG - receiver gain.
8. P[0-63] - pulse lengths.
9. D[0-63] – delays.
Frequency, Offset and Square Power appear for each channel that has been setup with edasp.
 
### NOTE

Note that moving the RG slider causes an exponential change in the receiver gain. The effect of changing RG will be shown immediately in the FID display. For all other parameters in the above list, the effect of a change will be shown after one or two scans.
 
The buttons of the FID window have the following functions:
Show FID in shuffled mode.
Show FID in unshuffled mode, vertically arranged.
Show FID in unshuffled mode, horizontally arranged.
Show FID in unshuffled mode, interleaved.
Switch between FID and spectrum.
Stop the acquisition [stop].
 Use current FID as reference for scaling [_noscale]
 
The  button toggles between FID and real time spectrum display and provides two extra buttons:
 Real time FT settings.
 Toggle calculation of peak width at 50%, 5.5% and 1.1% height (Shown as status parameters).
 
The GS dialog box also contains the following buttons: 
 
1. Save - save the parameter that was changed last.
2. Save all - save all changes.
3. Restore - restore the parameter that was changed last.
4. Restore all - restore all changes.
5. Stop - stop the acquisition and leave the gs dialog box.
If you click Stop without having saved your changes, gs shows you the changed parameters and allows you to select the ones to be saved.
 
### INPUT AND OUTPUT PARAMETERS

See the parameter list above.
### INPUT AND OUTPUT FILES

1. <dir>/data/<user>/nmr/<name>/<expno>/
1. acqu - acquisition parameters


## SEE ALSO

zg, go, rga
© 2025 Bruker BioSpin GmbH & Co. KG
