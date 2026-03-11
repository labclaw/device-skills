# newtop

**Category:** Commands > Miscellaneous > TopSpin Interface

## NAME

**newtop** - Open a new TopSpin interface


## DESCRIPTION

The command newtop opens a new additional TopSpin interface. The additional interface is completely equivalent to the one it was started from. Entering newtop in the second or in the initial TopSpin interface opens another interface etc. The number of TopSpin interfaces is only limited by the available computer memory.
 
When single data set is displayed in multiple TopSpin interfaces, the display in each interface is completely independent from the others. As such, you can display different regions, scaling and data objects. When the data set is (re)processed from one interface, its display is automatically updated in all TopSpin interfaces.
The command exit closes the current TopSpin interface. Interfaces that were opened from that interface remain open. Entering exit in the last open TopSpin interface, finishes the entire TopSpin session.
The position and geometry of each TopSpin interface is saved and restored after restart.


## SEE ALSO

exit, hist, newwin, nextwin, close, closeall 
© 2025 Bruker BioSpin GmbH & Co. KG
