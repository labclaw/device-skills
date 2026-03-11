# uwm

**Category:** Commands > Process > Advanced > Miscellaneous Operations

## NAME

**uwm** - User-defined Window Multiplication


## DESCRIPTION

The command uwm multiplies the fid of the current data set with the fid of the second data set (to be defined with edc2) and stores the result as processed data (files 1r, 1i) of the current data set. The original fid is retained.
The fid of the second data set is considered as the user defined window function. Its size (TD) must be equal or greater than the size TD of the fid of the current data set. In the latter case the window is truncated before multiplication is applied.
In order to generate a user defined window, proceed as follows:
1. Type new and define a new data set, whose fid will serve as the window.
2. Execute the AU program calfun. This AU program calculates an arbitrary function and stores it as the file fid in the current data set. This will become the user defined window. Calfun is set up so that you can modify it by adding your desired window function. You must recompile it after changing it. Please read the header of calfun how to do that. Calfun also contains examples, e.g. how an exponential window is programmed.
© 2025 Bruker BioSpin GmbH & Co. KG
