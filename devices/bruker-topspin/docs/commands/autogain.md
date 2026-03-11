# loopadj, autogain, autophase

**Category:** Commands > Acquire > Lock

## NAME

**loopadj** - AU program for optimization of LGAIN (loop gain), LTIME (loop time) and LFILTER (loop filter)

**autogain** - Automatic loop gain (LGAIN) optimization

**autophase** - Automatic lock phase (LOCPHAS) optimization


## DESCRIPTION

1. The AU program loopadj automatically optimizes the lock phase, lock gain, loop gain, loop filter and loop time. Note that loopadj optimizes these parameters for best long-term stability, but not for best lineshape, resolution or homogeneity (for more information type edau loopadj and look at the header of the AU program).
2. Prior to running the command loopadj, the lock power must be adjusted for saturation and then set to a value 2 to 3 dB lower.
3. Based on the lock power, the parameters lock gain and lock phase are then optimized with the commands autogain and autophase. 
4. Finally, LGAIN, LTIME and LFILTER are determined.


## SEE ALSO

edlock, edsolv, lock
© 2025 Bruker BioSpin GmbH & Co. KG
