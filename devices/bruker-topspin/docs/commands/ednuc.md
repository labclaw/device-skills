# ednuc

**Category:** Commands > Manage > Spectrometer > Experiments/Parameters

## NAME

**ednuc** - Edit nuclei table


## DESCRIPTION

The command ednuc opens the nuclei table showing a list of nuclei with their names, receptivity, spin and basic frequency (see the next figure).
 
The buttons of the nuclei table have the following functions:
1. Add/Edit
- Edit a table entry or add a new one. A dialog is opened (see the next figure) where you can enter or change values. If you enter a new Nucleus, an entry is added to the list, otherwise the current entry is edited.
2. Delete
- Delete the selected entry/entries.
3. Restore
- Restore the original nuclei table. All changes you made will be undone. This must be done once, if you have changed the basic frequency with cf.
4. Save
- Save any changes the nuclei table. You will be prompted for the NMR administration password.
5. Close
- Close the nuclei table.
 
### NOTE

Note that double-clicking a table entry also opens the dialog you see in the figure above but only allows you to change the frequency.


## INPUT FILES

1. <tshome>/conf/instr/<instrum>/
1. nuclei - nuclei table
2. <tshome>/exp/stan/nmr/lists/
1. nuclei.all - complete nuclei table (input and Restore)


## OUTPUT FILES

1. <tshome>/conf/instr/<instrum>/
1. nuclei - nuclei table


## SEE ALSO

edsolv, edprobe, edlock, edprosoll
© 2025 Bruker BioSpin GmbH & Co. KG
