# autoplot

**Category:** Commands > Miscellaneous > Print/Export

## NAME

**autoplot** - Print with layout, print directly


## DESCRIPTION

The command autoplot plots the current dataset according to a Plot Editor layout. The layout must be specified with the processing parameter LAYOUT. This layout can be a standard Plot Editor layout which is delivered with TopSpin or a user defined layout which has been set up from the Plot Editor.
autoplot can take the following arguments:
-s setup.prt 
Use printer setup file setup.prt instead of the printer setup that was saved with the layout (not available in Windows version).
-l N 
Remove N data sets from the portfolio and print again.
-n 
Don‘t reset before printing.
-f 
Force all 1D and/or 2D objects in the layout to use axis limits as used in TopSpin (uses the F1P/F2P parameter for each direction).
-e output.ps 
Create e.g. a Postscript file instead of printer output. Use the -? option to see a complete list of supported file formats.
-v 
Show autoplot version number.
-h 
Show help text.
-? 
Same as -h.
For an extended description of autoplot please refer to the Plot Editor online help.


## INPUT PARAMETERS

Set with edp or by typing layout etc.:
LAYOUT - Plot Editor layout
CURPLOT - Default plotter for Plot Editor


## INPUT FILES

<tshome>/plot/layouts/*.xwp - Bruker library Plot Editor layouts
<dir>/data/<user>/nmr/<name>/<expno>/pdata/<procno>/
1r - real processed 1D data 
procs - processing status parameters
intrng - integral regions
parm.txt - ascii file containing parameters which appear on the plot
title - default title file
outd - output device parameters
portfolio.por - Plot Editor portfolio (input file is it exists)
For a 2D dataset, the files 2rr, proc2s and clevels are also input.


## USAGE IN AU PROGRAMS

AUTOPLOT
AUTOPLOT_WITH_PORTFOLIO
AUTOPLOT_TO_FILE(outputfile)
AUTOPLOT_WITH_PORTFOLIO_TO_FILE(outputfile)


## SEE ALSO

plot, print, prnt
© 2025 Bruker BioSpin GmbH & Co. KG
