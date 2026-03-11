# bnmr, bpan, buttonnmr, butselnmr

**Category:** Commands > Acquire > More

## NAME

**bnmr** - Start Workflow for Setting up Some Basic 1D and 2D Experiments

**buttonnmr** - Same as bnmr

**butselnmr** - Same as bnmr

**bpan** - Opens a user-defined button panel (nD)


## DESCRIPTION

The command bnmr opens a new Workflow Button Bar for the setup of some basic 1D and 2D experiments.
 
It combines the commands buttonnmr and butselnmr from earlier TopSpin versions into one workflow. The experiments that can be started from this workflow are the same as the ones that can be started from a button panel started with the command bpan (see below).
The experiments from the 1D and 2D drop-down list in the workflow are the same experiments that can be started from the button panel called bnmr.
 
The experiments from the Selective drop-down list in the workflow are the same experiments that can be started from the button panel called bnmrsel. 
 
The command bpan opens a user defined button panel. It prompts for the name of the desired panel.
 
A button panel is a window with user-defined buttons for executing TopSpin commands, AU programs, Jython programs or macros. It appears as an integral part of the active data window and acts on that. Bruker delivers a few standard button panels called exam, bnmr and bnmrsel. To create your own button panels, you can modify one of these or write them from scratch.
In this description we will create a very simple button panel with some 1D processing commands and print/export buttons:
 
To write this button panel, take the following steps:
1. Open the File Explorer and navigate to the subdirectory TOPSPINHOME/classes/prop/English. Here you will find, for example, the panels cmdpanel_exam.prop, cmdpanel_bnmr.prop etc..
2. Create a text file with the name cmdpanel_<name>.prop, where <name> is the name of the button panel.
3. Enter the button definitions including Panel title, Colors, Toggle buttons, Top buttons, Panel layout, Panel buttons and Tooltips.
4. Save the file. Make sure the extension of the file is .prop and not .txt, .prop.txt or anything else.
5. Enter bpan <name> on the command line to open the button panel.
Here is the content of the properties file for the button panel above:
# Color definitions used in this file (RGB) 
BLUE1=51$ 204$ 255 
YELLOW1=255$ 255$ 0 
GREEN1=84$ 196$ 20 
# Title definition 
TITLE=1D Processing Panel 
TITLE_COLOR=0$ 0$ 255 
# Toggle button definition 
TOGGLE_BUTTON=To 2D 
TOGGLE_CMD=bpan bproc2d 
TOGGLE_TIP=Switch to 2D processing 
# Top row button definition 
TOP_BUTTONS=EM$ $FT$ $PK$ $ 
TOP_COLORS=YELLOW1$ YELLOW1$ YELLOW1 
TOP_CMDS=em$ ft$ pk 
TOP_TIPS=Exponential multiplication $\ 
Fourier transform$\ 
Phase correction 
# Panel button definitions 
# LAYOUT format: rows columns hgap vgap 
PAN_LAYOUT=1$ 3$ 8$ 8 
PAN_BUTTONS=Print$ $ EXPORT$ $SEND TO$ $ 
PAN_COLORS=BLUE1$ BLUE1$ BLUE1 
PAN_CMDS=prnt$ exportfile$ smail 
PAN_TIPS=Print the spectrum<br>\ 
as it appears on the screen$\ 
Export the dataset<br>\ 
to png, jpg, bmp etc.$\ 
Send the dataset by email 
 
Note that:
1. The Close button and the Tips checkbox are automatically created. You don’t need to specify them.
2. The TOGGLE button is typically, but not necessarily, used to call another button panel. In this example it calls the panel bproc2d.
3. Items must be separated with the "$" character, button items with "$ $".
4. A "\" followed by "end of line" continues an item on the next line.
5. Tool tips may use html tags for text formatting.
6. Commands may be specified as single commands like "em" or as composite commands like "em\nft\npk". Note that in the latter case, the commands must be separated by "\n".


## INPUT FILES

<userhome>/<.topspin-hostname>/prop/userdefined/cmdpanel_<name>.prop
© 2025 Bruker BioSpin GmbH & Co. KG
