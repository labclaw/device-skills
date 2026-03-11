# gdcheck, auditc

**Category:** Commands > Manage > Security

## NAME

**gdcheck** - Ensure that the processing audit trail is consistent

**auditc** - Opens a dialog box to call gdcheck comment without having to write the comment into a file


## DESCRIPTION

The command gdcheck either adds a comment to the audit trail file or checks its data checksum.
1. Use argument raw to work on audita.txt instead of auditp.txt
2. Use argument comment or checksum to add a user comment to the audit file. Gdcheck expects the comment to be stored in a file named auditc.txt placed in the same folder as the audit file. Gdcheck will delete this file after reading it. If argument checksum is used, a new checksum will be recomputed from the data. If argument comment is used, gdcheck will use the last audited checksum, which may or may not be correct. In either case, the audit entry will not contain the annotation “Unknown data manipulation detected”.
When no comment should be added, gdcheck checks whether the data set has been manipulated since the last audit trail command, in which case it adds an audit trail entry containing the correct checksum with the annotation “Unknown data manipulation detected” for command auditcheck. Otherwise, gdcheck does not add any audit entry.
The command auditc opens a window allowing to run command gdcheck comment or gdcheck comment raw without having to manually create the file auditc.txt. If a file with the name auditc.txt already exists in the directory, it will be overwritten and then deleted.
 
### INPUT AND OUTPUT FILES

<dir>/data/<user>/nmr/<name>/<expno>/
audita.txt - Acquisition audit trail. Used when gdcheck is called with argument “raw” and when auditc is called with option “Add a comment to the RAW data audit trail”.
auditc.txt - Input file containing the comment. Used when gdcheck is called with arguments “raw” and either “comment” or “checksum”.
<dir>/data/<user>/nmr/<name>/<expno>/pdata/<procno>/
auditp.txt - Processing audit trail. Used when gdcheck is called without argument “raw” and when auditc is called with option “Add a comment to the processed data audit trail”.
auditc.txt – Input file containing the comment. Used when gdcheck is called without argument “raw” and without argument “comment”.


## USAGE IN AU PROGRAMS

GDCHECK: Executes the command gdcheck.
GDCHECK_RAW: Executes the command gdcheck raw.
AUDITCOMMENTA("user comment"): Put the user comment into a file auditc.txt and executes the command gdcheck comment raw. This is equivalent to using command auditc with option “Add a comment to the RAW data audit trail” and the user comment as comment.
AUDITCOMMENTP("user comment"): Put the user comment into a file auditc.txt and executes the command gdcheck comment. This is equivalent to using command auditc with option “Add a comment to the processed data audit trail” and the user comment as comment.


## SEE ALSO

audit, auditcheck 
© 2025 Bruker BioSpin GmbH & Co. KG
