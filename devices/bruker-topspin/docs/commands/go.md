# go

**Category:** Commands > Acquire > Run

## NAME

**go** - Perform an acquisition, adding to existing data


## DESCRIPTION

The command go starts an acquisition on the current dataset adding to possibly existing raw data. It works like zg, except that it does not overwrite existing data. If raw data already exist, go will add the new data to them. This is, for example, useful if the signal to noise of your spectrum is too low and you want to acquire additional scans. If no data exist, go has the same result as zg.
### NOTE

If you have stopped an acquisition with halt or stop, you can, in principle, continue it with go. Note, however, that the acquisition might have been stopped in the middle of a phase cycle and go starts a new phase cycle. Therefore, if you want to be able to stop and continue an acquisition, we recommend using the commands suspend and resume (see the description of these commands).
### NOTE

Note that if you enter halt or stop during a 2D or 3D acquisition it might stop in the middle of a second or third direction increment (see above). However, this problem only occurs when you use the wr statement to write the data to disk. If you use the mc statement, the go command continues a 2D or 3D acquisition at the position where it was stopped. Caution: if you increment or decrement any pulses, delays, or phases within the acquisition loop, you must do that within one of the mc arguments F1PH, F1QF etc., for example:
d1 mc #1 to 1 F1PH(id0, ip1)
Most acquisitions are started with zg and run until they have finished. As such, the command go is not used very often. It is, however, used in some Bruker AU programs like noediff, noemult, deptcyc and multicyc.
Note the difference between the TopSpin command go and the pulse program statement go (see Pulse Programming Manual).
### INPUT AND OUTPUT PARAMETERS

See zg
### INPUT AND OUTPUT FILES

See zg


## USAGE IN AU PROGRAMS

1. GO
### COMMAND LINE OPTIONS

-D <define>
set precompiler directive <define>
-scaledByRg
divide the fid by the receiver gain
-scaledByNs
divide the fid by the number of scans
rgAdjust
adjust receiver gain during dummy scans
interactive
allow parameter change during runtime of experiment
o1calib
used for the O1 calibration experiment
o1calib <stepsize> <rangesize>
calibration of O1 with specified stepsize and rangesize (both in Hz)
-help
print help message


## SEE ALSO

zg
© 2025 Bruker BioSpin GmbH & Co. KG
