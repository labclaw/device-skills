# rsh, wsh, vish

**Category:** Commands > Acquire > Shim

## NAME

**rsh** - Read a set of shim values

**wsh** - Write a set of shim values

**vish** - View a shim file


## DESCRIPTION

The *sh all open the shim dialog box when they are entered without arguments (see the next figure).
 
The following buttons are available:
1. Read 
- Executes the command rsh, reading the specified shim file. When you click on a shim set, its values are loaded to the shim unit. rsh can also be entered on the command line with a shim file as an argument. After reading a shim file, it is usually necessary to optimize the shims, especially the Z and Z2 shim. You can do that from the BSMS display (command bsmsdisp). rsh switches the autoshim function of the BSMS unit off. If you press the AUTOSHIM key in the BSMS display or enter autoshim on, the shims will be continuously optimized during the experiment.
- rsh -acqu reads the shim values from the current dataset.
2. Write 
- Executes the command wsh writing the shim values which are currently installed on the shim unit to the specified shim file. wsh can also be entered on the command line with a shim file as an argument.
 
1. View 
- Executes the command vish opening the specified shim file with an editor. vish can also be entered on the command line with a shim file as an argument.
2. Delete 
- Deletes the selected shim file. If he *sh commands are entered the command line with an argument, then they may contain wildcards, for example:
- rsh a* lists all shim files beginning with “a”
### NOTE

Note that rsh, wsh and vish open the dialog box with the Read, Write and View button activated, respectively.


## INPUT FILES

1. <tshome>/exp/stan/nmr/lists/bsms/
1. shim files


## USAGE IN AU PROGRAMS

1. RSH(name)
2. WSH(name)


## SEE ALSO

edtune, tune, bsmsdisp, setshim, setsh
© 2025 Bruker BioSpin GmbH & Co. KG
