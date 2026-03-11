# nmr_save, nmr_restore, user_save, user_restore

**Category:** Commands > Manage > Spectrometer > Save/Restore Installation

## NAME

**nmr_save** - Save installation-specific files

**nmrsave** - Same as nmr_save

**nmr_restore** - Restore installation-specific files

**user_save** - Save user-specific files

**user_restore** - Restore user-specific files


## DESCRIPTION

The commands nmr_save and user_save save installation/user specific files in a backup TAR-file.
The commands nmr_restore and user_restore extract a backup TAR-file to the same or to a different installation.
All these commands open the dialog window shown in the next figure, the individual commands being available as tabs.
 
Here you can specify:
1. Location of the backup file: the storage directory of the backup file.
2. Installation to be saved : The TopSpin home directory.
3. Spectrometer configuration: as enter during cf.
Furthermore, you can select 
1. Display default information: the path of the created backup file.
2. Display additional information: the path of the created backup file, information about directories being saved and converting/renaming information.
The button Define cron job opens the cron dialog where you can define a periodic save of Bruker or user files (see also command cron).
Here you can save or restore all TopSpin user defined files. This includes: 
1. Spectrometer configuration files (cf)
2. Parameter sets (rpar, wpar)
3. Pulse program (edpul, edcpul)
4. AU programs (edau)
5. Plot editor layouts (plot, autoplot)
6. Shim files (rsh, wsh)
7. IconNMR user information (iconnmr)
8. Program Licenses (TopSpin, NMRSim, NMR Guide)
9. Various lists like f1, ds (edlist, zg, gs)
10. TopSpin macros (edmac)
11. Probe and solvent dependant parameters (edprosol)
12. Lock parameters (edlock)
13. Probe information (edprobe)
14. Nucleus information (ednuc)
15. RF Shapes and gradients
etc.
Furthermore, the files prog/logfiles/heliumlog, 
prog/logfiles/heliumloig.err and Bruker/licenses/license.dat will be saved with the ending .backup. 
### NOTE

Please note that these files will be stored in the folder conf/instr/, no longer in the original folder.
Furthermore beginning with TopSpin 3.0 the whole directory <diskless>/crco_data/cryotool_log/ will be saved.
For more details about the commands nmr_save, nmr_restore, user-save and user-restore please refer to the respective Bruker TopSpin Installation Guides for Windows XP, Windows Vista or Linux.
### INPUT AND OUTPUT FILES

1. <tshome> /nmr_backup
1. nmr_backup_<date>-<time>.tar (nmr_save)
2. nmr_backup_<username>-<date>-<time>.tar (user_save)
2. <tshome>/exp/stan/nmr/au/src/
1. nmr_save - AU program executed by nmr_save
### INPUT AND OUTPUT DIRECTORIES

### nmr_save stores various subdirectories/files of:

1. <tshome>/exp/stan/nmr/py/
2. <tshome>/exp/stan/nmr/lists
3. <tshome>/exp/stan/nmr/par/
4. <tshome>/exp/stan/nmr/au/src/
5. <tshome>/plot/layouts/
6. <tshome>/conf/instr/
7. <tshome>/prog/tcl/xwish3_scripts/
8. <tshome>/exp/stan/nmr/parx/preemp/
9. <tshome>/QTP/
10. <tshome>/data/final/nmr/protocolfiles/
11. <tshome>/conf/global
12. <tshome>/prog/server/export.conf 
### user_save stores various subdirectories/files of:

1. <userhome>/.topspin-<hostname> 
2. <tshome>/exp/stan/nmr/py/
3. <tshome>/exp/stan/nmr/lists 
4. <tshome>/exp/stan/nmr/par/
5. <tshome>/exp/stan/nmr/au/src/
### INPUT AND OUTPUT DIRECTORIES


## SEE ALSO

cf, expinstall 
© 2025 Bruker BioSpin GmbH & Co. KG
