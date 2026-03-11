# edmisc, rmisc, wmisc, delmisc

**Category:** Commands > Parameter Handling

## NAME

**edmisc** - Edit misc. lists (integrals, baseline, peaks, levels, etc.)

**rmisc** - Read misc. lists (integrals, baseline, peaks, levels, etc.)

**wmisc** - Write misc. lists (integrals, baseline, peaks, levels, etc.)

**delmisc** - Delete misc. lists (integrals, baseline, peaks, levels, etc.)


## DESCRIPTION

The commands *misc allow to read, edit, write or delete miscellaneous lists. When entered without arguments, they all open a related window for miscellaneous files. The difference is that wmisc only offers writing possibilities for miscellaneous files, rmisc only offers reading possibility, whereas with edmisc and delmisc you can read, write and edit the correesponding/selected miscellaneous file:
 
On the top right you can change the source and specify the miscellaneous type that should be shown in the table (see figure above). All items shown in the table can be edited, read, written or new written. This also corresponds to the commands edmisc, rmisc and wmisc.
 
 
### Types of Miscellaneous Files

The lists which can be edited are shown in the table below:
list type 
contains 
intrng 
integral regions, created by interactive integration or automatic baseline correction (abs). Used for spectrum display, print and integral listing.
base_info 
polynomial, sine or exponential baseline function, created from the baseline mode (.basl). Used by the baseline correction command bcm..
baslpnts 
baseline points created by def-pts from the baseline mode (.basl). Used by the spline baseline correction command sab.
peaklist 
peak information, created by the command ppp and mdcon auto. Used by the mixed deconvolution command mdcon.
reg 
plot regions, created in interactive integration mode (command .int). Used by pp, lipp when PSCAL=ireg or pireg.
Miscellaneous list types
 
When entered on the command line, rmisc takes two arguments and can be used as follows:
1. rmisc <type> - Shows all entries of the type <type>. If you select an entry, the corresponding list will be read.
2. rmisc <type> <name> - Reads the list <name> of the type <type>.
### INPUT/OUTPUT DIRECTORIES

The default directory for user-defined lists is:
<tshome>/exp/stan/nmr/lists/<listname>/user
intrng - integral range files
baslpnts - spline baseline points file
base_info - pol. exp. or sine baseline function files
peaklist - peak information files
reg - plot region files


## USAGE IN AU PROGRAMS

RMISC(type, file)
WMISC(type, file)


## SEE ALSO

edlist, dellist
© 2025 Bruker BioSpin GmbH & Co. KG
