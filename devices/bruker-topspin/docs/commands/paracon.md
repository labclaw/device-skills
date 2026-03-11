# paracon

**Category:** Commands > Manage > Spectrometer > Experiments/Parameters

## NAME

**paracon** - Change the basic frequency in parameter sets


## DESCRIPTION

The command paracon changes the basic frequency in parameter sets. This allows you to use parameter sets that were created on a spectrometer with a different frequency. It opens dialog box shown in the next figure.
 
Here you can setup a list of available parameter sets. You can select Bruker and/or User defined parameter sets and uses a match string. The matching parameter sets appear in the right part of the dialog box. To start the conversion, select one or more parameter sets and click OK.
### INPUT AND OUTPUT PARAMETERS

Acquisition parameters:
1. BF1 - BF8 - basic frequency for frequency channel f1 to f8.
2. SFO1 - SFO8 - irradiation (carrier) frequencies for channels f1 to f8.
3. O1 - O8 - irradiation frequency offset for frequency channel f1 - f8 in Hz.
4. SW - spectral width in ppm.
Processing parameters:
1. SF - spectral reference frequency.
### INPUT AND OUTPUT FILES

1. <tshome>/exp/stan/nmr/par/*/
1. acqu - acquisition parameters
2. proc - processing parameters


## SEE ALSO

expinstall 
© 2025 Bruker BioSpin GmbH & Co. KG
