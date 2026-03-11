# edcstm

**Category:** Commands > Manage > Spectrometer > Experiments/Parameters

## NAME

**edcstm** - Edit customer / system information


## DESCRIPTION

The command edcstm opens a window where customer / system information can be edited. This window can also be opened from Manage | Spectrometer | Experiment / Parameters | Edit customer / system information (edcstm).
The information entered here is used in preparation of the spectrometer and / or accessory acceptance protocols. All general information provided in these reports is taken from edcstm window. 
 
It contains three sections of information: 
1. Customer Info 
- Customer Name*, Operator Name, Company*, Address, Postal Code, City*, Country, Phone Contact Customer*, Mobile, Fax and E-Mail*
2. Bruker Info
- Engineer*, Office*, Central Hotline Phone*, Central Hotline E-Mail*
3. System Info
- Order No. *, Contact Service No., System Type, Console Part and Serial No., Coil, Dewar, Shim System Offset*, Shim System Angle, CryoProbe Order No., Location, Register No. 
It is advisable to enter the information as precisely as possible. The content will be used in spectrometer acceptance protocols, accessory installation protocols, repair, and maintenance protocols etc. The file is also copied into the savelogs archive to provide help desk functions with system and contact information. 
### NOTE

Please note that the fields marked with * are required fields. Some information will automatically be taken from the installation procedure (command cf). 
To edit this information the NMR administration password is required.
OUTPUT FILES
1. <tshome>/conf/global/edcstm.info
© 2025 Bruker BioSpin GmbH & Co. KG
