# edgp

**Category:** Commands > Parameter Handling

## NAME

**edgp** - Edit gradient programs


## DESCRIPTION

The command edgp allows you to list, create or edit gradient programs. If you enter edgp without arguments, a list of all gradient programs is displayed (see the next figure). 
 
This shows a list of all Bruker and/or User gradient programs and allows you to edit or delete them.
To list Bruker gradient programs:
1. Click Options => Bruker defined
 
To list User gradient programs: 
1. Click Options => User defined
 
To list all gradient programs: 
1. Click Options => All defined
 
To edit the selected gradient program: 
1. Double-click the gradient program or select the gradient program and click Edit. The gradient program will be shown in an editor and can be saved by clicking Save. To save it under a different name, click Save as ...
 
To create a new gradient program: 
1. Click File --> New and write the gradient program in the appearing 
editor 
or 
1. Double-click an existing gradient program, modify the contents to your needs and store it under a different name by clicking Save as ... 
 
To delete a gradient program 
1. Click Delete and click OK in the warning dialog.
If you enter the command with an argument, i.e. edgp <name>, the gradient program <name> is opened or, if it does not exist, it is created. The argument may contain wildcards, e.g. edgp a* displays a list of all gradient programs which start with a.
Bruker gradient programs must be installed with the command:
expinstall before they can be opened with edgp.
edgp uses the editor which is defined in the TopSpin User Preferences. To change it, enter set, click Miscellaneous and select or change the editor. 
### INPUT AND OUTPUT FiLES

1. <tshome>/exp/stan/nmr/lists/gp/*
1. gradient programs


## SEE ALSO

edcpul, (edpu)l, expinstall 
© 2025 Bruker BioSpin GmbH & Co. KG
