# qumulti

**Category:** Commands > Miscellaneous > Run a Program

## NAME

**qumulti** - Queue a TopSpin command for execution on multiple expnos


## DESCRIPTION

The command qumulti queues a command for execution on multiple expnos of the current dataset. When entered without arguments, qumulti opens the dialog shown:
 
Here you can enter the command to be executed and select the experiments numbers on which the specified command should work. The dialog shows all available expnos, with the active data set selected.
Clicking OK queues the command for execution.
The command qumulti takes two arguments, the command to be executed and the target experiment number(s). The dialog will open with the specified arguments pselected. Expnos can be specified in one of the following ways:
n : a single experiment number
* : all expnos under the current data name
n-m : expno n through m
n..m : equivalent to n-m
n,m : expno n and m
n m : equivalent to n,m
The command to be executed can be specified before or after the expno(s).
Examples of argument strings:
The argument efp 1,3,4-6 8 11 will preselect the command efp and the expnos: 1, 3, 4, 5, 6, 8 and 11.
The argument:
1..8,10 15-20 will preselect the expnos: 1, 2, 3, 4, 5, 6, 7, 8, 10, 15, 16, 17, 18, 19 and 20, and leave the command field empty.
Specified expnos which do not exist are ignored. The preselected command and expnos can be modified/extended in the dialog.
To select or deselect all expnos in the opened dialog:
Right-click in the dialog and choose Select all or Deselect all, respectively.
If qumulti is entered without argument, only the current expno is preselected.
On clicking OK, a priority job is created for each selected expno, starting with the lowest expno, and sent to the queue.
Queued commands can be viewed in the command spooler, which can be started with the command spooler and is available in the spectrometer status bar.
Note that if you try to exit TopSpin while a priority job is still active, you will be warned about this and requested to confirm exiting.


## SEE ALSO

cron, qu, at, atmulti, spooler
© 2025 Bruker BioSpin GmbH & Co. KG
