# tr

**Category:** Commands > Acquire > Run

## NAME

**tr** - Transfer data to disk during the acquisition.


## DESCRIPTION

The command tr transfers (writes) data to disk during a 1D acquisition. This is, for example, useful if you want to do a Fourier transform and view the spectrum before the acquisition has finished. Another reason to use tr is to save the currently acquired scans of a long-term acquisition. This avoids losing all data in case of a power loss.
As an alternative to entering tr on the command line, you can click the  button of the TopSpin toolbar.
The command tr can even be entered with an optional parameter as command tr <1...-NS> (please note that <1...-NS> must be integer and > 0). If <1...-NS> is defined the execution of tr is delyed until the total number of scans reaches a multiple of <1...-NS>. This option is useful if a fid with a complete phase cycle should be stored to disk.
As an alternative to typing tr <1...-NS> in the command line the button can be used from the TopSpin toolbar with this button: 
This button opens the following dialog:


## OUTPUT FILES

1. <dir>/data/<user>/nmr/<name>/<expno>/
1. fid - 1D raw data
2. acqus - acquisition status parameters


## SEE ALSO

zg, go
© 2025 Bruker BioSpin GmbH & Co. KG
