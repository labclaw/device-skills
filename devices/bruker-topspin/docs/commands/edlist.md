# edlist, dellist

**Category:** Commands > Parameter Handling

## NAME

**edlist** - Edit various lists (vd, vp, va, f1, vt, vc etc.)

**dellist** - Delete various lists (vd, vp, va, f1, vt, vc etc.)


## DESCRIPTION

The command edlist allows to edit parameter lists like VD Delay lists, VP Pulse lists, VC Loop Counts lists, VA Amplitude lists, VT Temperature lists, F1 Frequency lists, SP Shape lists, DS Data Set lists and PHASE Phases lists.
The command edlist opens the Parameter Lists window:
 
On the top right the source and list type can be filtered. All items shown in the table can be edited in the upcoming text editor.
The dialog shown above offers the following buttons:
Edit - to edit a list in a text file, click Edit or double-click a parameter list. Saving the modifications will overwrite the existing list.
Close - closes the dialog.
The command dellist opens the same dialog box as edlist. To delete a list, right-click the selected item, and then click Delete… 
Hint: This is also possible with the command edlist, so dellist is historical and obsolete.
### INPUT/OUTPUT DIRECTORIES

The default directory for user-defined lists is:
<tshome>/exp/stan/nmr/lists/<listname>/user


## SEE ALSO

edmisc, rmisc commandr 
© 2025 Bruker BioSpin GmbH & Co. KG
