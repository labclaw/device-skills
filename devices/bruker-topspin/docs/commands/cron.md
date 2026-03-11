# cron

**Category:** Commands > Miscellaneous > Run a Program

## NAME

**cron** - Schedule a TopSpin command for execution


## DESCRIPTION

The command cron performs command scheduling. It allows you to executed commands periodically at predefined times. It is more versatile than the commands at and atmulti offering full flexibility in time definition, off-schedule execution and user control. When entered without arguments, it opens the dialog shown:
 
Here you can specify the command to be scheduled, some scheduling options and the starting time and date. The following fields are available:
Command
The command to be executed.
Description 
A description of the command.
Execution Scope
The scope of the command execution, User or TopSpin. For scope User, the scheduled command will only be executed if TopSpin is run by the same (internal) user that is active during cron definition. If the scope is TopSpin, the scheduled command will be executed for any (internal) user. Scheduled commands with TopSpin execution scope can only be defined, cancelled or modified after entering the NMR-Administration password.
Off-schedule execution
This flag allows you to execute commands that were scheduled to run at the time when TopSpin was not running. These commands are executed after TopSpin startup. Note that commands that were scheduled to run multiple times during TopSpin downtime are only executed once.
Direct execution
The option direct execution allows you to run commands directly, i.e. by passing the default queue mechanism. Usually, an expired cron job is moved into the priority queue, i.e. the job would wait for any other queued jobs to finish. Setting this flag by passes this mechanism i.e. the job is executed directly when its schedule is due. Please note that however processing commands can be run in parallel. This is a useful tool to execute for example nmr_save and another processing command at the same time.
The following time scheduling rules exist:
Minute of the hour: 00 through 59
Hour of the day: 00 through 23
Day of the month: 00 through 31
Month of the year: January through December
Day of the week: Sunday through Saturday
For each of these fields, you can define an interval by selecting a value in the From and a value in the To field. Setting the To field to Ignore, schedules the command for execution only at the time/date selected in the From field. An asterix (*) in the From field indicated all possible times.  Clicking the + button to the right of a field, adds an extra field of the same type, allowing multiple interval definition. Clicking the - button removes the extra field.
The cron dialog also offers a right-click menu which allows following options:
1. Add new rule - adding new scheduling rules
2. Remove rule - removing scheduling rules
3. Favorites - define favorites for scheduling rules


## SEE ALSO

at, atmulti, qu, qumulti, spooler
© 2025 Bruker BioSpin GmbH & Co. KG
