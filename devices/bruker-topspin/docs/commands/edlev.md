# edlev, levcalc

**Category:** Commands > Miscellaneous > Graphical User Interface

## NAME

**edlev** - Edit contour levels (2D, 3D)

**levcalc** - Calculate 2D contour levels


## DESCRIPTION

The command edlev opens a dialog box in which you can set the contour levels of a 2D dataset:
 
The command levcalc calculates the levels based on the parameters LEV0, TOPLEV and NLEV.
### Manual setup

This allows you to create an arbitrary sequence of levels
1. Enter the level values in the fields 1, 2, ... at the top of the dialog box.
2. Click Apply to update the display or OK to store the levels, update the display and close the dialog box. 
### Calculation

This allows you to easily create a geometric or equidistant sequence of levels.
1. Click one of the following items:
1. Multiply with increment 
2. to create a geometric sequence of levels. 
3. Add increment 
4. to create a equidistant sequence of levels. 
2. Enter the desired  Base level ,  Level increment  and Number of levels. 
3. Click Fill to display and activate the sequence. 
4. Click Apply to update the display or OK to store the levels, update the display and close the dialog box. 
The Contour level sign allows you to select positive or negative levels, or both.
Note that if you change the intensity interactively, for example with the buttons ,  or , the contour levels are automatically adjusted. Entering edlev will show the adjusted levels and clicking  will save them to disk.
### INPUT AND OUTPUT FILES

<dir>/data/<user>/nmr/<name>/<expno>/pdata/<procno>/
clevels - Contour levels


## SEE ALSO

.dist, .f1f2region, .gr, .hz, .keep, .ls, .lt, .lv, .setsw, .sync, .y, .zoommode (.ls, .lt)
© 2025 Bruker BioSpin GmbH & Co. KG
