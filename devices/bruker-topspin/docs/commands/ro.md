# ro

**Category:** Commands > Acquire > Spin

## NAME

**ro** - Switch the sample rotation on or off


## DESCRIPTION

The command ro switches the sample rotation on or off. When entered without arguments, it opens a dialog box (see the next figure).
 
Here, you can set the rotation frequency and start/stop the rotation.
ro takes up to two parameters and can be used as follows:
1. ro on
- Switches the sample rotation on with the spin rate currently set thorugh the BSMS display (visible when you press the SPIN RATE key).
2. ro acqu 
- Sets the spin rate to the value of the acquisition parameter RO, then switches rotation on and waits for 60 seconds. If spin rate has not been reached within that time, an error message appears.
3. ro off 
- Switches the sample rotation off.
4. ro off wait 
- Switches the sample rotation off and waits until the rotation has reached zero. During the waiting time the BSMS unit cannot be accessed by other commands.
5. ro <value>
- Sets the acquisition parameter RO to <value>.
 
As an alternative to the command ro, you can press the SPIN ON/OFF, and SPIN RATE keys through the BSMS display (command bsmsdisp)


## INPUT PARAMETERS

1. RO - sample rotation frequency (input for ro acqu)


## INPUT FILES

1. <dir>/data/<user>/nmr/<name>/<expno>/
1. acqu - acquisition parameters


## USAGE IN AU PROGRAMS

1. ROT 
- Executes the command ro acqu. 
2. ROTOFF
- Executes the command ro off wait.


## SEE ALSO

ej, ij 
© 2025 Bruker BioSpin GmbH & Co. KG
