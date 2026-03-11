# at

**Category:** Commands > Miscellaneous > Run a Program

## NAME

**at** - Schedule a TopSpin command for execution


## DESCRIPTION

The command at performs command scheduling. When entered without arguments, it opens the dialog shown:
 
Here you can specify the command to be scheduled, e.g. zg, and the starting time and date.
The Time and Date fields are initialized with the current time and date, respectively. By clicking OK, the specified is scheduled for execution.
The time and date, as well as the command to be scheduled can also be specified on the command line, using the following syntax:
1. at [HH[:mm]] [DD[.MM[.YY]]] command
Here are some examples:
1. at 23:30 25.12.07 zg - will start an acquisition on the 25th of December 2007 at 23.30.
2. at 13 zg - will start an acquisition today at 13:00.
The command at works user specific, i.e. the scheduled command is only executed if TopSpin runs at the specified time and the TopSpin internal user is the user who scheduled the command. For more flexible time definition and user independent scheduling, you can use the command.
Scheduled commands can be viewed in the command spooler, which can be started with the command spooler and is available in the spectrometer status bar.


## SEE ALSO

cron, qu, qumulti, atmulti, spooler
© 2025 Bruker BioSpin GmbH & Co. KG
