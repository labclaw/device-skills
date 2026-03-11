# wbwr

**Category:** Commands > Acquire > Tune

## NAME

**wbwr** - Write wobble curve to disk


## DESCRIPTION

The command wbwr saves the wobble curve to disk.
### NOTE

Note that the command is only valid in the wobble mode (first enter command wobb).
 
wbwr prompts the user to enter a PROCNO which will be used to store the wobble curve.
 
As an alternative to wbwr entered on the command line, the button can be clicked in the TopSpin toolbar.
The wobble curve is stored as processed data (1r) and not as raw data (fid.). This provides the additional option of using standard processing tools like e. g. multiple display.
In addition, wbwr can directly be entered together with an additional parameter denoting the PROCNO that should be used, i.e. "wbwr 4".


## OUTPUT FILES

1. <dir>/data/<user>/nmr/<name>/<expno>/<procno>/
1. 1r - the wobble curve
2. procs - processing status bar


## SEE ALSO

wobb 
© 2025 Bruker BioSpin GmbH & Co. KG
