# tune

**Category:** Commands > Acquire > Shim

## NAME

**tune** - Perform automatic shimming of the magnet


## DESCRIPTION

The command tune shims the magnet in any automatic procedure according to a shim definition file. This file is called the tune file and can be set up with the command edtune. The command tune takes one argument and can be used in one of the following ways:
tune
Displays a list of available tune files (see the next figure). 
 
When you select an entry and click the Execute button, the corresponding tune file is interpreted, and auto shimming is performed accordingly.
tune <tunefile>
Perform auto shimming according to the specified tune file.
tune .sx
Perform auto shimming according to the tune file as it is specified for the current probe. This tune file can be setup from the edprosol dialog box by clicking Edit | Edit Tunefile.
An example tune file is delivered with TopSpin. You can use this as it is or modify it to your needs and store it under a different name. The statements you can use in a tune file are listed below. 
### NOTE

Note that some of these statements are settings whereas others are commands.
### Settings in a tune file:

1. USE_FIDAREA
1. Flag indicating to use the area under the FID envelope as a criterion for field homogeneity.
2. USE_LOCKLEVEL
1. Flag indicating to use the lock level as a criterion for field homogeneity.
3. LOCKDWELL n
1. The number of measurements used for determining the current lock level. The measured values are averaged to suppress the effects of the noise on the lock level. Only used when USE_LOCKLEVEL is defined.
4. MAXLOCK m
1. The maximum lock levels. Can be used to keep the lock signal from moving out of the display during the shimming procedure. The lock level is displayed at the TopSpin status line while tune is running.
5. DELAY n 
1. The time (in seconds) between adjusting a shim and reading the new lock level. In the example tune file, DELAY is set to one second which is usually enough for the lock level to settle.
6. SET <shim> w c 
1. Set the maximum step size (width) and the convergence limit for the SIMPLEX command. These parameters can be set for each shim separately. An example is:
2. SET Z1 20 3
- TIMES n
- ..
- END
Loop structure: all statements within the loop will be executed n times. Nested loops are possible to a depth of five.
### Commands in a Tune File

1. ROTATION ON WAIT 
1. Switches the sample rotation on, using the spin rate currently set on the BSMS unit.
2. ROTATION OFF WAIT 
1. Switches the sample rotation off.
### NOTE

Please note that these two commands are useful when switching from on-axis shims (Z1, Z2 etc ...) to off-axis shims (X, Y, XY...) since the first set (Z shims) are typically shimmed with a rotating sample and the off-axis shims (X, Y,XY ...) are adjusted with a non-rotating sample.
 
1. RSH, RSH <filename>
1. Reads a shim file. If an argument is specified, RSH will read the corresponding shim file. If not, it will read the shim file with the name of the solvent defined by the acquisition parameter SOLVENT.
2. Z s i, Z2 s i, ..., XY s i 
1. Optimizes single shims. These commands take two arguments: 
- s = step size; the shim increment used as long as the lock level increases 
- i = iterations; the maximum number of steps after passing the maximum 
 
A shim is first changed s units in one direction. If this increases the lock level, the shim is changed again s units in the same direction. This is repeated until a shim change decreases the lock level. Then the direction of change is reversed, and the step size is reduced. This process is continued until one of the following criteria has been met:
1. The lock level has not changed significantly during the last step.
2. The maximum number of iterations (i) has been performed.
3. The step size has been reduced to one.
Examples of shim commands are:
    Z 10 3
    Z2 10 3 
    Z3 10 3 
1. SIMPLEX <shim1 shim2 etc.> 
1. Optimizes the specified shims according to the simplex algorithm which can be used for lock level and FID area shimming. SIMPLEX uses the step size and convergence limit defined by the SET statement (see above). The simplex algorithm is described in the example file (see INPUT FILES below).
2. AUTOSHIM ON <shim1=m, shim2=n, ...>
1. Switches on the automatic shimming function on the shim unit after the tune command has finished. This command allows you to adjust the shims continuously during the entire experiment. Only the shims that are specified as arguments to the AUTOSHIM ON command will be optimized. For each shim, you can specify the step size used for auto shimming. If you do not specify the step size, the default value of 5 is used. An example of this command is:
3. AUTOSHIM ON Z1=2 Z2 
1. Since this command becomes effective after the tune command has finished, it can be specified anywhere in the tune file.
4. AUTOSHIM OFF 
1. Switches off automatic shimming on the shim unit. It makes sure that automatic shimming is switched off when it was switched on before, either from the last executed tune file or manually from the BSMS display. 
- 
### NOTE

Note that it would not make sense to use AUTOSHIM ON and AUTOSHIM OFF within one tune file.
5. LOCKPHASE s i 
1. Optimize the lock phase. This command takes two arguments: 
-   s = step size 
-   i = iterations; the maximum number of steps
2. As an alternative to the automatic shimming with tune, you can optimize the shims manually from the BSMS display. If the shims are far away from the optimum, you can read a standard shim set with the command rsh and then do manual shimming.
An alternative to the simplex procedure in tune is the AU program simplex.


## INPUT FILES

1. <tshome>/exp/stan/nmr/lists/group/
1. example - tune file 
2. <tshome>/conf/instr/<instrum>/prosol/<probeID>/
1. tunefile - tune file for the current probe (input for tune .sx)


## USAGE IN AU PROGRAMS

1. TUNE(tunefile)
2. TUNESX 
- Eexecutes the command tune .sx


## SEE ALSO

edtune, rsh, wsh, vish, delpar, delgp, delsh
© 2025 Bruker BioSpin GmbH & Co. KG
