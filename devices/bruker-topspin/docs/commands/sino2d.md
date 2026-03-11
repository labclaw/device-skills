# sino2d

**Category:** Commands > Analyze > SiNo

## NAME

**sino2d** - Calculate signal-to-noise ratio (2D)


## DESCRIPTION

The command is implemented as a Jython script sino2d.py.
You may start it by typing xpy sino2d or sino2d in the command line.
sino2d requests the name of region file:
 
Enter the filename (e.g. by completing the proposed path) and click OK.
The result is displayed in a text window. It shows detailed information about noise calculation.


## INPUT PARAMETERS

2D sino requires a 2D signal region and a 2D noise region stored in an "int2drng" formatted file according to the following example:
0 0
a 1024 165 249 130.750166 117.206324
1024 279 314 7.416665 7.140323
a 1024 529 639 71.886546 54.175368
1024 375 421 6.667867 6.311296
Please see the format description below.
You may setup the file by hand, by a program, or most comfortably in the 2D integration mode:
1. Open a 2D spectrum in TopSpin.
2. Enter interactive integration mode using a menu entry or tool button or by entering the command .int.
3. Click on the tool button delete all regions to start from scratch.
4. Click on the tool button define new integration region.
5. Drag a region around a signal while keeping the left mouse button depressed. When the button is released, a popup menu is opened. Click on an integrate entry, e.g. the first one (which one doesn't matter).
6. Move the mouse to a signal-free region and drag again the mouse to mark the region. Again click on an integrate entry when releasing the left mouse button.
7. Click on the icon Export integration regions. The wmisc window is opened. Click on Write new.... Enter a filename. The file is stored in the .../list/intrng2d directory which can be inspected using the rmisc command.
Format description of int2drng file:
Mode SI_F1 row1 row2 row1(ppm) row2(ppm)
SI_F2 col1 col2 col1(ppm) col2(ppm)


## SEE ALSO

sino
© 2025 Bruker BioSpin GmbH & Co. KG
