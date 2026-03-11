# lopo

**Category:** Commands > Manage > Spectrometer > BSMS Control

## NAME

**lopo** - Set the lock parameters


## DESCRIPTION

The command lopo shows a list of available solvents (see the next figure).lopo
When you select a solvent and click OK, it sets the lock parameters according to the edlock table. As such, the lock power, loop gain, loop time, loop filter, lock phase and frequency shift are set to the lock table values of Lockpower, LoopGain, LoopTime, LoopFilt, LockPhase and Distance, respectively. These values are set on the BSMS unit without performing lock-in.
Right-click in the table to copy or export the selected entry or to modify the table properties.
The command lopo is useful if you want to observe the lock signal first. The lock-in procedure can then be performed by pressing the Lock On/Off or Autolock key in the BSMS display.
### NOTE

Note that:
  lopo => Autolock is equivalent to lock -acqu 
  lopo => Lock On/Off is equivalent to lock -noauto


## INPUT PARAMETERS

1. Set by the user with eda or by typing solvent etc.:
1. SOLVENT - sample solvent
2. LOCNUC - lock nucleus
2. Set by the user with edlock :
1. See also edlock


## INPUT FILES

1. <dir>/data/<user>/nmr/<name>/<expno>/
1. acqu - acquisition parameters
2. <tshome>/conf/instr/
1. probe - current probe as defined by edprobe
3. <tshome>/conf/instr/<instrum>/
1. 2Hlock - lock table for nucleus 2H
2. 19Flock - lock table for nucleus 19F
<tshome>/conf/instr/<instrum>/prosol/<probeID>/<solvent>/
bsmspar - solvent and probe dependent lock parameters


## USAGE IN AU PROGRAMS

1. LOPO


## SEE ALSO

lock, edlock, lockdisp, lgain, ltime, lfilter
© 2025 Bruker BioSpin GmbH & Co. KG
