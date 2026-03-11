# new

**Category:** Commands > Acquire

## NAME

**new** - Define a new dataset (nD)


## DESCRIPTION

The command new [Ctrl-n] opens a dialog box in which you can define a new data set.

 
### Dataset:

Here, you can specify the data set NAME, EXPNO and Directory (disk unit). Note that these are all parts of the data path name: 
<dir>\<name>\<expno>\pdata\<procno>
### Parameters:

1. Use current parameters – creates the new dataset with the parameters of the current dataset.
2. Read parameterset - copies the acquisition and processing parameters from the selected experiment. 
3. Set Solvent - sets the acquisition parameter SOLVENT. Default is the solvent of the current data set.
### Additional action:

1. Do nothing – no addional actions are performed.
2. Execute getprosol – reads the probe and solvent specific parameters. 
3. Keep parameters – keeps the listed parameters from the current dataset.
### Advanced:

1. Number of datasets (receivers) – defines the number of datasets for multi-receive experiments.
### Title:

1. Enter a description for the new dataset.
The command new remembers the last selected options. When you click OK, the data set is created and displayed as the current data window. If the specified data set already exists, you will be prompted to overwrite it or not. Note that this will only overwrite the parameters, not the data files.
new is equivalent to the command edc.


## INPUT FILES

<tshome>/prog/curdir/<user>/
curdat - current data set definition
If Experiment = Use current params:
<dir>/data/<user>/nmr/<name>/<expno>/
acqu - acquisition parameters
acqus - acquisition status parameters
<dir>/data/<user>/nmr/<name>/<expno>/pdata/<procno>/
proc - processing parameters
procs - processing status parameters
If Experiment ≠ Use current params.:
<tshome>/exp/stan/nmr/par/<experiment>/
acqu - acquisition parameters
proc - processing parameters


## OUTPUT FILES

<tshome>/prog/curdir/<user>/
curdat - current data set definition
If the data set specified with new does not exist yet, the current data set is copied:
<dir>/data/<user>/nmr/<name>/<expno>/
acqu - acquisition parameters
acqus - acquisition status parameters
<dir>/data/<user>/nmr/<name>/<expno>/pdata/<procno>/
proc - processing parameters
procs - processing status parameters
For 2D and 3D data the files acqu2, acqu2s etc. are also output.


## SEE ALSO

dir, dira, dirp, dirdat, browse, find, search, open, re, rep, rew, repw
© 2025 Bruker BioSpin GmbH & Co. KG
