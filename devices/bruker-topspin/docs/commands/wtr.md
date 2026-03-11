# wtr

**Category:** Commands > Process > Advanced

## NAME

**wtr** - Write 1D data to a trace of data ≥ 2D


## DESCRIPTION

The command wtr replaces a trace of processed data with dimension ≥ 2D with a 1D processed dataset. It is usually, but not necessarily, used to write back a trace that was extracted with rtr. This trace can be modified and/or written back to a different trace number. 
wtr takes up to three arguments. As an example we take a trace written to a 3D dataset:
<axis orientation> : 1, 2 or 3
The digit refer to the F3, F2 and F1 axes of the 3D data. 
<trace number> : 1 - MAX
Where MAX is the product of the SI value in the directions orthogonal to the trace orientation
<procno> 
Destination 3D procno (source 1D procno if wtr is entered on the destination 3D dataset)
wtr can be entered on the 1D source dataset or on the destination 3D dataset. The number of required arguments is different (see below).
### wtr entered on the source 1D dataset

In this case, wtr prompts the user for two arguments only, the trace number and the 1D destination procno. The axis orientation is taken from the 3D dataset (used_from file). The two arguments can also be specified on the command line. If, however, you specify three arguments, the axis orientation is taken from the first argument rather than from the 3D dataset. 
Examples:
wtr 
Prompt the user for the trace number and destination 3D procno, take the axis orientation from the current 1D dataset and write the trace accordingly.
wtr 11 1 
Write the current 1D data to trace 11 of the 3D dataset in procno 1. Take the axis orientation from the current 1D dataset.
wtr 3 11 2 
Write the current 1D data to F3 trace number 11 of the 3D data in procno 2.
Note that if the source 1D dataset does not contain a used_from file, for example because it is not an extracted trace, wtr will prompt the user for the axis orientation. 
### Entering wtr on the destination 3D dataset

In this case, wtr prompts the user for three arguments. Alternatively, these can be entered on the command line.
Examples: 
wtr 2 10 999 
Write the 1D data in procno 999 to F2 trace 10 of the current 3D data.
wtr 1 32 101 
Write the 1D data in procno 101, to the F1 trace 32 of the current 3D data.
wtr 1 
Prompt the user for the trace number and the procno of the source 1D dataset. Write the 1D dataset to the specified F1 trace accordingly.
### Entering wtr on a 4D dataset

On a data with dimension > 3, wtr works the same as on a 3D dataset, except that there are more axis orientations. For example on 4D dataset, possible orientations are 1, 2, 3 and 4.


## INPUT FILES

<dir>/data/<user>/nmr/<name>/<expno>/pdata/<procno>/
1r, 1i - processed 1D data
used_from - data path of the source nD data and the trace number


## OUTPUT FILES

<dir>/data/<user>/nmr/<name>/<expno>/pdata/<procno>/
2rr, 2ir, 2ri, 2ii - processed data (wtr on 2D data)
3rrr, 3irr, 3rir, 3rri, 3iii - processed data (wtr on 3D data)
4rrrr, 4iiii - processed data (wtr on 4D data)
auditp.txt - processing audit trail


## SEE ALSO

rtr, rpl, wpl, rcb, wser, wserp
© 2025 Bruker BioSpin GmbH & Co. KG
