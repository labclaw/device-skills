# qu

**Category:** Commands > Miscellaneous > Run a Program

## NAME

**qu** - Queue a TopSpin command for execution


## DESCRIPTION

The command qu queues a command for execution. It requires one argument, the command to be queued. 
 
For example, the command:
qu xfb
Queues the command xfb for execution. This means that xfb is executed as soon as the currently running command and previously queued commands have finished.
Command queuing can, for example be used, to process a 2D data set immediately after acquisition. This is done with the command sequence:
zg
qu xfb
Acquisition commands like zg, go, rga and atma are automatically queued, if auto-spooling is enabled in the User Preferences (command set).
Queued commands can be viewed in the command spooler, which can be started with the command spooler and is available in the spectrometer status bar.


## SEE ALSO

cron, at, atmulti, qumulti, spooler
© 2025 Bruker BioSpin GmbH & Co. KG
