# suspend

**Category:** Commands > Acquire > Run

## NAME

**suspend** - Suspend a running acquisition


## DESCRIPTION

The command suspend allows you to hold a running acquisition. When it is entered, the acquisition holds as soon as the pulse program statement suspend or calcsuspend is encountered. If the pulse program does not contain such a statement, suspend has no effect. Alternatively, an acquisition can be suspended with the pulse program statement autosuspend or calcautosuspend. They automatically hold the acquisition, without user interaction. The command resume continues acquisition that was suspended, either automatically or with the command suspend.
### NOTE

Note that the suspend information is temporarily stored on the spectrometer hardware, not on the workstation disk. As soon as you enter stop or halt, or switch off the spectrometer, this information is lost, and the acquisition cannot be resumed.
 
Standard Bruker pulse programs do not contain any suspend statements. Therefore, suspend can only be used with user defined pulse programs which contain a suspend statement at a certain position.


## SEE ALSO

resume, zg, go
© 2025 Bruker BioSpin GmbH & Co. KG
