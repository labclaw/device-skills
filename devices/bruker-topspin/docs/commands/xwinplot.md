# plot, xwp, xwpr, xwinplot

**Category:** Commands > Miscellaneous > Print/Export

## NAME

**plot** - Start Plot Editor

**xwp** - Same as plot

**xwpr** - Same as plot -r

**xwinplot** - Same as plot -n


## DESCRIPTION

The command plot starts the Plot Editor with the current dataset and the layout defined by the processing parameter LAYOUT. 
 
The plot limits of all data objects will be the same as in TopSpin. The command plot can take various arguments and can be used as follows:
The command plot can be used with the following arguments:
(no option) Force all data objects to use limits from TopSpin
-r Apply Reset Actions on all objects after loading the layout
-n Do not change anything after loading the layout
-p myfile.por Load the portfolio file myfile.por
-i Ignore a portfolio.por file found in the data set
The main window of the Plot Editor consists of a drawing area, a menu bar and a toolbar which offers various graphical objects. Here you can display objects like FIDs, one- or two-dimensional NMR spectra, Stacked Plots, parameter lists and titles. You can add integral curves and peak lists to a spectrum, combine several spectra to a stacked plot draw projections around a 2D spectrum.
Furthermore, the Plot Editor offers a set of so-called graphic primitives like lines, text, rectangles and bezier curves. You can place these objects anywhere on the screen and change their appearance. They can be superimposed on NMR-related graphics. All objects can be moved and resized interactively and for each object a range of editing modes is available. 
The TopSpin command autoplot allows you to plot a spectrum using a Plot Editor layout.
For a full description, please click:
Click Help | Manuals | Automation and Data Publishing | Data Publishing


## INPUT PARAMETERS

Set with edp or by typing layout etc.:
LAYOUT - Plot Editor layout
CURPLOT - Default plotter for Plot Editor
### INPUT AND OUTPUT FILES

<tshome>/plot/layouts/*.xwp - Bruker library Plot Editor layouts
portfolio.por - Plot Editor portfolio (input file is it exists)
<dir>/data/<user>/nmr/<name>/<expno>/pdata/<procno>/
layout.xwp - Plot Editor layout 
last_plot.xwp - Last stored Plot Editor layout
portfolio.por - Plot Editor portfolio


## INPUT FILES

<dir>/data/<user>/nmr/<name>/<expno>/pdata/<procno>/
1r - real processed 1D data 
procs - processing status parameters
intrng - integral regions
parm.txt - ascii file containing parameters which appear on the plot
title - default title file
outd - output device parameters
For a 2D dataset, the files 2rr, proc2s and clevels are also input.


## SEE ALSO

print, prnt, autoplot
© 2025 Bruker BioSpin GmbH & Co. KG
