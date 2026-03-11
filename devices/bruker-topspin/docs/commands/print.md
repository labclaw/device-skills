# print

**Category:** Commands > Miscellaneous > Print/Export

## NAME

**print** - Open Data Publishing Dialog Box


## DESCRIPTION

The command print opens the following dialog box:
 
Here, you can choose from three print options:
1. Print active window [prnt]
2. The data window is printed as it is displayed on the screen. Before printing starts, the operating system print dialog box will appear where you can, for example, select the printer and printer properties.
3. Print with layout - start Plot Editor  [  plot ] 
4. If you select this option and click OK , the Plot Editor will be started. This option is equivalent to entering plot on the TopSpin command line.
5. Print with layout - plot directly  [  autoplot ] 
6. Selecting this option activates the Plot Editor layout list box. Select the desired layout and click OK to print. Standard layouts are delivered with TopSpin. They use the Windows default printer. User defined layouts use the printer defined in the Plot Editor. On a 1D dataset, only 1D layouts are listed, on a 2D dataset only 2D layouts are listed etc.
For the last two options, the following required parameters are available:
Use plot limits 
1. from screen/ CY - the plot limits and maximum intensity are used as they are on the screen (processing parameter F1P, F2P and CY, respectively)
2. from Plot Editor Reset Actions - the plot limits and maximum intensity are set according to the Plot Editor Reset Actions (right-click inside the Plot Editor data field and choose Automation to set the Reset Actions).
3. as saved in Plot Editor - the plot limits and maximum intensity are set in the specified layout
Fill dataset list 
1. from your default portfolio - the portfolio contains the current TopSpin dataset plus the data from the default Plot Editor portfolio
2. from portfolio saved in dataset - the portfolio contains the current TopSpin dataset plus the data from the portfolio stored in this dataset
Override Plotter saved in Plot Editor
If enabled, the plotter defined in the Plot Editor layout will be overridden by the plotter defined by the processing parameter CURPLOT.
For each Option/Required Parameter combination, the corresponding command line command is shown in the title bar of the dialog box. In the example above this is the command plot -f.


## INPUT FILES

See the description of prnt, plot and autoplot


## SEE ALSO

prnt, plot, autoplot
© 2025 Bruker BioSpin GmbH & Co. KG
