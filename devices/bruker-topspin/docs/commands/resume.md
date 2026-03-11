# resume

**Category:** Commands > Acquire > Run

## NAME

**resume** - Resume a suspended acquisition


## DESCRIPTION

The command resume resumes an acquisition that has been suspended.
An acquisition can be suspended with the command suspend. When this is entered, the acquisition holds as soon as the pulse program statement suspend or calcsuspend is encountered. If the pulse program does not contain such a statement, suspend has no effect. Alternatively, an acquisition can be suspended with the pulse program statement autosuspend or calcautosuspend. They automatically hold the acquisition, without user interaction. The command resume continues acquisition that was suspended, either automatically or with the command suspend.
For more information on the suspend pulse program statements click:
Help | Manuals | Programming Manuals | Pulse Programming
A resumed acquisition does not start with dummy scans. This can be a problem if the recycle delay is shorter than 4 times the T1 value of the measured nucleus.
### NOTE

Note that the suspend information is temporarily stored on the spectrometer hardware, not on the workstation disk. As soon as you enter stop or halt, or switch off the spectrometer, the suspend information is lost and the acquisition cannot be resumed.


## SEE ALSO

suspend, zg, go
© 2025 Bruker BioSpin GmbH & Co. KG
