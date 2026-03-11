# expinstall

**Category:** Commands > Manage > Spectrometer > Experiments/Parameters

## NAME

**expinstall** - Install pulse programs, AU programs, parameter sets etc.


## DESCRIPTION

The command expinstall installs pulse programs, AU programs, parameter sets and various other resources for spectrometer usage. On a spectrometer, it must be performed once, after the installation of TopSpin and after cf has been done. On a datastation, cf is not needed and you can run expinstall immediately after the installation of TopSpin.
### Configure a Spectrometer

1. Click Manage | Spectrometer | Experiments/Parameters | expinstall or enter expinstall on the command line. A password request window is displayed.
 
1. Enter NMR administrator password to display the first Expinstall window.
 
1. Click Next. Bruker supplies Parameter files, AU-programs, Pulseprograms and other files in particular folders. Expinstall moves these folders to <TopSpin installation dir.>/exp/stan/nmr/_expinstall_automatic_backup and installs new copies.
2. Individual Parameter files, AU-programs, Pulseprograms and other files that reside in user-specific folders are not affected by expinstall.
3. In the next window select the type of acquisition. In the example a High Resolution System has been checked.
 
1. Click Next
 
1. Select the spectrometer or data station configuration for expinstall. Here the CAB AV4 400 MHZ BASIC has been selected. If this window is not displayed, then TopSpin has found only one valid configuration, namely the one for the current spectrometer, and immediately continues with the next window. Click Next.
2. In the next window enter the basic frequency of the spectrometer and the pre-scan delay. All settings should be correct. Nevertheless, in case of a configuration to control a spectrometer they should be checked. Click Next.
 
1. Click Next to display a summary of options executed by expinstall.
 
1. Check this list.
2. To change an option, click Back to the window(s) where corrections have to be done. Then click Finish.
The installation of the selected items will start now. Wait until this process has finished. In the TopSpin status line, the progress of the installation is monitored. At the end of expinstall a Cron check window is displayed.
 
### Configure a Datastation like a Spectrometer

If you want to configure your datastation like your spectrometer, you must first copy the configuration directory:
  <tshome>/conf/instr/<instrum>
From that spectrometer to the data station. Here:
1. <tshome> is TopSpin home, the directory where TopSpin is installed.
- 
### NOTE

Note that this can be different on the spectrometer than on the datastation.
2. <instrum> is the configuration name.
See also the description of the command nmr_save.
After copying the configuration directory, execute expinstall as described above for the spectrometer.


## INPUT PARAMETERS

If the task Convert standard parameter sets is selected, expinstall uses the following input parameters:
From the parameter sets as delivered with TopSpin:
1. BF1 – BF8 - basic frequencies for channel f1 to f8.
2. SFO1- SFO8 - irradiation (carrier) frequencies for channels f1 to f8.
3. IN0 - increment for delay D0 (2D and 3D parameter sets only).
4. IN10 - increment for delay D10 (3D parameter sets only).
5. SW - spectral width in ppm.
6. SPOFFS[0-63] - shaped pulse frequency offset.
### OUTPUT PARAMETERS

If the task Convert standard parameter sets is selected, expinstall stores the following parameters in the parameter sets: 
1. BF1 – BF8 - basic frequencies for channel f1 to f8.
2. SFO1- SFO8 - irradiation (carrier) frequencies for channels f1 to f8.
3. SF - spectral reference frequency.
4. IN0 - increment for delay D0 (2D and 3D parameter sets only).
5. IN10 - increment for delay D10 (3D parameter sets only).
6. SW - spectral width in ppm.
7. SPOFFS[0-63] - shaped pulse frequency offset.
8. DIGTYP - digitizer type.
9. DR - digital resolution.
10. DIGMOD - digitizer mode.
11. DECIM - decimation factor of the digital filter.
12. DE - prescan delay.
13. All routing parameters as defined with the commands edsp / edasp.


## SEE ALSO

cf, rpar, wpar, edpar
© 2025 Bruker BioSpin GmbH & Co. KG
