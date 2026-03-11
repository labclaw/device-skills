# rtr

**Category:** Commands > Process > Advanced

## NAME

**rtr** - Read trace from data ≥ 2D and store as 1D data


## DESCRIPTION

The command rtr reads a trace from processed data with dimension ≥ 2D and stores it as a 1D dataset. 
rtr takes up to four arguments. As an example we take a trace read from a 3D dataset:
<axis orientation> : 1, 2 or 3
The digit refers to the F3, F2 and F1 axis of the 3D data. 
<trace number> : 1 - MAX
Where MAX is the product of the SI value in the directions orthogonal to the trace orientation.
<procno> : 
Destination 1D procno (source 3D procno if rtr is entered on the destination 1D dataset)
n : optional argument.
Prevents the destination dataset from being displayed/activated 
Obligatory arguments that are not specified on the command line will be prompted for. 
rtr can be entered on the source 3D dataset or, if this already exists, on the destination 1D dataset. The number of required arguments is different (see below).
### rtr entered on a source 3D dataset

In this case, rtr prompts the user for three arguments. Alternatively, these can be entered on the command line.
rtr 
Prompt the user for the axis orientation, trace number and destination procno and read the trace accordingly.
rtr 3 10 999 
Read F3 trace 10 and store it in procno 999. 
rtr 1 1 10 n 
Read F1 trace 1 and store it in procno 10. Do not display/activate the destination dataset. 
### rtr entered on a destination 1D dataset

This is typically done on a 1D dataset which is a trace extracted by a previous rtr command, which was entered on the source 3D dataset. In that case, rtr requires only one argument; the trace number. By default, the same axis orientation and source 3D dataset (procno) are used as with the previous rtr command (as defined in the used_from file of the 1D dataset). You can, however, use two or three arguments to specify a different axis orientation and/or 3D source procno. On a regular 1D dataset (not a trace from a 3D), rtr requires three arguments.
Here are some examples of rtr executed on a 1D dataset which is a trace from a 3D dataset:
rtr 
Prompt the user for the trace number, use the axis orientation and source 3D procno as defined in the current 1D dataset and read the trace accordingly.
rtr 11 
Read trace 11. Use the axis orientation and source 3D procno as defined in current 1D dataset.
rtr 3 11 2 
Read F3 trace 11 from the 3D dataset under procno 2
Note that on 2D data the command rtr works like rsr and rsc, except that the trace direction can be freely chosen. Furthermore, rtr always stores the 1D output data in a different procno of the same dataset whereas rsr and rsc can store data in the dataset ~TEMP. 
On 4D or higher dimensional datasets, rtr works the same as on a 3D dataset, except that there are more axis orientations.


## INPUT FILES

<dir>/data/<user>/nmr/<name>/<expno>/pdata/<procno>/
2rr, 2ir, 2ri, 2ii - processed data (rtr on 2D data)
3rrr, 3irr, 3rir, 3rri, 3iii - processed data (rtr on 3D data)
4rrrr, 4iiii - processed data (rtr on 4D data)


## OUTPUT FILES

<dir>/data/<user>/nmr/<name>/<expno>/pdata/<procno>/
1r, 1i - processed 1D data
auditp.txt - processing audit trail
used_from - data path of the source data and the trace number


## SEE ALSO

wtr, rpl, wpl, rcb, wser, wserp
© 2025 Bruker BioSpin GmbH & Co. KG
