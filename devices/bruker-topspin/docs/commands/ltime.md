# lgain, ltime, lfilter

**Category:** Commands > Manage > Spectrometer > BSMS Control

## NAME

**lgain** - Set the lock regulator loop gain

**ltime** - Set the lock regulator loop time

**lfilter** - Set the lock regulator loop filter


## DESCRIPTION

The command lgain allows you to set the loop gain, a lock regulator parameter. It takes one argument; a loop gain value between -80 and 0 dB. This value is only used when the lock-in process is done by pressing Lock On/Off or Autolock. When lock-in is done with the TopSpin command lock, the loop gain is set to the edlock parameter LGain. 
ltime and lfilter work like lgain, except that they set the regulator parameters loop time and loop filter, respectively.ltimelfilterlgain
The AU program loopadj automatically optimizes lock gain, lock phase, loop time, loop gain and loop filter.
The regulator (loop) parameters can also be set in the BSMS display. 
For information on how to determine the lock parameters click Help | Manuals 
| Acquisition User Guides | Basic 1D and 2D Experiments.
Furthermore, you can refer to the spectrometer hardware documentation which is available on the BASH CDROM.
### USAGE IN AU PROGAMS

LTIME(value)
LGAIN(value)
LFILTER(value)


## SEE ALSO

lock, lopo, edlock
© 2025 Bruker BioSpin GmbH & Co. KG
