# edscon

**Category:** Commands > Manage > Spectrometer > Experiments/Parameters

## NAME

**edscon** - Edit spectrometer constants


## DESCRIPTION

The command edscon opens a dialog window, where you can set certain spectrometer parameters (constants) (see the next figure).
 
The term constant refers to the fact that these parameters count for all datasets. edscon must be executed once as part of the spectrometer configuration.
Changes in the edscon parameters can be stored by clicking OK. You will be prompted for the NMR Administrator password. 
BLKTR is an array of amplifier blanking preset times. This means they only allow RF signals to pass during the time they are blanked. Because of the finite switching time, blanking is triggered before the start of the RF pulse. The amplifier is blanked BLKTR μsec before the pulse. It is unblanked (allows no further RF passing) at the end of the pulse. 
The use of the edscon preset parameter BLKTR can be switched off by inserting the statement 
preset off 
at the beginning of a pulse program. This has the same effect as setting all elements of BLKTR to zero. In this case, the blanking steps described above occur at the beginning of the RF pulse. Nevertheless, you can enable the preset blanking for each individual channel, e.g.: 
2μ gatepulse 1 ;enable blanking for channel f1
2μ gatepulse 1|2 ;enable blanking for channel f1 and f2
In this example, the blanking of the transmitter and preamplifier is triggered 2 μsec before the RF pulse.
The edscon dialog box also shows the so called pre-scan subdelays. These are all part of the pre-scan delay DE. This is a hidden delay (it is not specified in the pulse program) that is automatically introduced by the go statement.
DE consists of 5 pre-scan delays DE1, DERX, DEADC, DEPA and DE itself. The sub-delays DE1, DERX, DEPA and DEADC are global parameters which depend on the properties of the respective spectrometer hardware. DE is also set globally but can be changed temporarily by defining a value in the pulse program. DE mostly depends on the dead time of the probe, but also on the digitization mode of the current experiment for DIGMOD=baseopt it is additionally adjusted by the software in order to meet the preconditions for this procedure. DE starts with the "go = .." instruction of the pulse program. All delays end simultaneously at the beginning of the data sampling. They act as pre-delays to the data sampling. At the beginning of each subdelay a certain action is performed:
1. DE1: the intermediate frequency (if required) is added to the frequency of the observe channel. This corresponds to the execution of the syrec statement (default 4.5 μsec). 
2. DERX: the receiver gate is opened (default 1.5 μsec).
3. DEADC: the digitizer is enabled (default 0.5 μsec).
4. DEPA: the preamplifier is switched from transmit to observe mode (default 4.5 μsec).
For example, a DERX value of 3 μsec would mean that the receiver gate is opened 3μsec before the data sampling starts.
Please note that there is also a mandatory order required for those predelays in order to start the data sampling correctly, i.e. DE1 >= DEPA >= DERX >= DEADC.
Normally, the default values, which have been set during the installation of your spectrometer, can be used. Each subdelay has a maximum of DE - 1 μsec.
In most pulse programs, data sampling is performed by the go statement, which automatically triggers the actions mentioned above after the corresponding pre-scan subdelay. If, however, data sampling is performed by the adc statement, these actions must explicitly be specified in the pulse program. Each action can be performed by a statement with the same name, in lower case letters, as the corresponding pre-scan subdelay. For example, the receiver gate can be opened with the derx statement. You can type edpul zgadc to look at an example of a pulse program using the adc statement. For more information on this topic click:
Help | Manuals | Programming Manuals | Pulse Programming
### INPUT AND OUTPUT FILES

1. <tshome>/conf/instr/<instrum>/
1. scon - spectrometer constants


## SEE ALSO

cf 
© 2025 Bruker BioSpin GmbH & Co. KG
