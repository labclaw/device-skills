# lock

**Category:** Commands > Acquire > Lock

## NAME

**lock** - Lock the magnetic field


## DESCRIPTION

The command lock performs the lock-in procedure. It takes one argument and can be used in the following ways:
1. lock 
- Opens a dialog box with a list of solvents (see the next figure).
 
When you select a solvent and click OK, it reads the lock parameters for that solvent from the lock table which has been set up with the command edlock and performs an autolock. The autolock procedure is also suitable for solvents with multiple lock signals. For each solvent with multiple signals only one lock signal is defined in the edlock table. 
Right-click in the table to copy or export the selected entry or to modify the table properties.
### NOTE

Note that lock only shows the Solvents for the current lock nucleus (parameter LOCNUC), in this case 2H. 
1. lock <solvent> 
- Reads the lock parameters for the specified solvent and performs an autolock accordingly.
2. lock –acqu
- Reads the lock parameters for the solvent defined by the acquisition parameter SOLVENT and performs an autolock. 
- 
### NOTE

Note that IconNMR executes lock -acqu.
3. lock –noauto
- Reads the lock parameters for the solvent defined by the acquisition parameter SOLVENT and performs a lock. It does not adjust the field (capture range 10 units).
The autolock procedure involves the following steps:
1. Irradiation of the lock nucleus with frequency Lock Freq + Reference Shift.
2. Acquisition of the lock nucleus FID.
3. Fourier transform and magnitude calculation of the acquired FID.
4. Determination of the position of the lock signal in the spectrum.
5. Adjusting the Field such that the lock signal is exactly on resonance.
6. Optimization the lock power and lock gain.
### NOTE

Note that the lock irradiation frequency (Lockfreq + Reference Shift) is solvent dependent. The value of Reference Shift is the chemical shift of the lock nucleus in the current solvent. As such, the irradiation frequency is approximately on resonance and lock needs to make only minimum field adjustments (capture range 1000 units). The advantage of this procedure is that the signal of the reference substance (e.g. TMS) appears at approximately the same position for each solvent.
 
The lock signal can be viewed in the lock display window which can be opened with the command lockdisp (see the description of this command).
The lock-in procedure can also be performed through the bsmsdisp command by pressing the Auto Lock or Lock On/Off key. 
 
In that case the lock parameter values that are currently stored on the BSMS unit are used. These can be modified in the BSMS display.


## INPUT PARAMETERS

1. Set by the user with eda or by typing solvent etc.:
1. SOLVENT - sample solvent (input for lock -acqu and lock -auto)
2. LOCNUC - lock nucleus
2. Set by the user with edlock:


## USAGE IN AU PROGRAMS

1. LOCK 
- Executes the command lock -acqu.


## SEE ALSO

edlock, lopo, lockdisp, lgain, ltime, lfilter
© 2025 Bruker BioSpin GmbH & Co. KG
