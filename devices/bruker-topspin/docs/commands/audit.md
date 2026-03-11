# audit, auditcheck

**Category:** Commands > Manage > Security

## NAME

**audit** - Open audit trail commands dialog box (nD)

**auditcheck** - Check data consistency (nD)


## DESCRIPTION

The command audit opens the audit trail dialog box:
 
This dialog box has several options, each of which selects a certain command for execution.
### Show current dataset audit trail

This option creates a report in pdf format, containing both the audit trails of the acquisition data (audita.txt) and of the processing data (auditp.txt).
 
### Verify audit trails

This option selects the command audit check / auditcheck for execution. It performs an audit trail check, i.e. a data consistency check. If both raw and processed data are consistent, you will get the following message:
 
If the data have been manipulated, e.g. with third party software or by changing certain status parameters (e.g. SI), the checksum will be inconsistent. The following figure shows the message for inconsistent processed data.
 
If a processing command has been used on a dataset with inconsistent checksum, the checksum will notify an unknown data manipulation, as shown in the following figure:
 
### View audit trails of a dataset list

This uses the list of datasets you have entered in the field labeled “Dataset List” and displays the audit trails of the given datasets in a window.
### Verify audit trails of a dataset list

This uses the list of datasets you have entered in the field labeled “Dataset List”, verifies each audit trail of the given datasets and displays the results in a window.
### Define dataset list

This opens this dialog box to allow for defining a list of datasets:
 
The options are as following:
1. Edit: opens a text window where the dataset names can be entered as text
2. Build list using find: opens a window where the datasets can be selected graphically
3. Browse: opens the file explorer where the datasets can be selected
### Further audit commands + auditcheck

The command audit can also be used along with one of the following arguments, in which case it executes without opening the popup window:
1. audit proc: Display the audit trail of the processed data (auditp.txt):
 
1. audit aqcu: Displays the audit trail of the acquisition data (audita.txt):
 
1. audit check = auditcheck: verify the checksums of the current data set. Does the same as the option “Verify datasets” with the audit command.


## INPUT FILES

<dir>/data/<user>/nmr/<name>/<expno>/
audita.txt - acquisition audit trail
<dir>/data/<user>/nmr/<name>/<expno>/pdata/<procno>/
auditp.txt - processing audit trail
Note that these are also the output files for audit com.


## SEE ALSO

gdcheck 
© 2025 Bruker BioSpin GmbH & Co. KG
