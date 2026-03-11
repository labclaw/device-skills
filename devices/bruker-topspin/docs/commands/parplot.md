# parplot

**Category:** Commands > Miscellaneous > Print/Export

## NAME

**parplot** - Select parameters to appear on the plot (1D, 2D)


## DESCRIPTION

The command parplot opens a dialog where you can select the acquisition and processing parameters that must appear on the plot:
 
To select the acquisition parameters to be shown on the plot: 
1. Enable the radio button Acquisition Parameters. By default, all acquisition parameters are shown and the Hide column is empty. 
2. In the Show column: select the parameters to be hidden.
3. Click the < button in the center of the dialog. 
4. If desired, you can also select experiment specific (ased) parameters by selecting the respective Parameter filter and repeating step 2 and 3. 
To select the processing parameters to be shown on the plot: 
1. Enable the radio button Processing Parameters.
2. By default, some processing parameters are shown while most are hidden. 
3. In the Show column: select the parameters to be hidden.
4. Click the < button in the center of the dialog.
5. In the Hide column: select the parameters to be shown.
6. Click the > button in the center of the dialog. 
After selecting the acquisition and/or processing parameters click OK to save the selection.
The dialog offers the following buttons:
1. Save as... : save the current selection under a user defined name
2. Open... : open a user defined selection
3. Restore Defaults  : restore the TopSpin default selection
4. OK : save the current selection
5. Cancel : Close the dialog
The Save as... and Open button allow to store several selections. Note that these can only be activated from the parplot dialog by using the Open and OK buttons, respectively and then count for all data set.
Only parameters selected with parplot will appear on the plot (on datasets created with TopSpin 1.3 or older, first remove the files format.temp in the dataset EXPNO and parm.txt in the dataset PROCNO).
This counts for both interactive plotting (command plot) and automated plotting (command autoplot).
### INPUT AND OUTPUT FILES

<tshome>/exp/stan/nmr/form/acqu.l
normpl - acquisition parameters that appear on the plot
<tshome>/exp/stan/nmr/form/proc.l
normpl - processing parameters that appear on the plot
<tshome>/exp/stan/nmr/form/
<name> - user defined selection of acquisition/processing parameters
### INPUT AND OUTPUT FILES

parplot
© 2025 Bruker BioSpin GmbH & Co. KG
