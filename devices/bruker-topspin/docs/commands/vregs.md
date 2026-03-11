# vregs

**Category:** Commands > Process > Advanced

## NAME

**vregs** - View of regions of interest of a list of spectra (1D, 2D)


## DESCRIPTION

Displays several regions of interest of several spectra in a window, arranged in matrix form.
### SYNTAX

1. vregs
2. vregs reset
1. When first used, vregs will display a new empty window inside TopSpin with tool buttons allowing one to define the dataset list and the list of spectral regions required for the view.
2. When a region view was created earlier, vregs will re-display the last view. The view properties are read from the file <user home dir>/.topspin-<hostname>/prop/globals.prop
The respective properties are called:
SPEC_ROI_VIEWER_CELL_HEIGHT=200
SPEC_ROI_VIEWER_CELL_MINWIDTH=150
SPEC_ROI_VIEWER_REGPATH=<file path of the region list>
SPEC_ROI_VIEWER_DATAPATH=<file path of the dataset list>
SPEC_ROI_VIEWER_ORIENTATION=0
The properties above include example values.
1. vregs reset will always display a new empty window inside TopSpin, and not the last used view.
© 2025 Bruker BioSpin GmbH & Co. KG
