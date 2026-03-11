# edlock, edsolv

**Category:** Commands > Manage > Spectrometer > Experiments/Parameters

## NAME

**edlock** - Edit the lock parameter table

**edsolv** - Edit the solvent parameter table


## DESCRIPTION

The command edlock opens the lock table; a dialog box in which the lock parameters can be set (see the next figure). For edlock, the Lock tab is automatically selected and highlighted. Please note that the same table is also opened with the edsolv command. Then, the Solvent tab is automatically selected and highlighted.
 
edlock must be executed once for each probe and each lock nucleus. The lock parameters can be determined from the BSMS display (command bsmsdisp). 
Before you run edlock, you must have defined the current probe with the command edprobe. Furthermore, you must have defined the lock nucleus by setting the parameter LOCNUC. This can be done with eda or by entering locnuc on the command line. In most experiments, the lock nucleus is deuterium. As such, LOCNUC is set to 2H in most Bruker standard parameter sets (see rpar).
The command edlock works on the solvent table which is managed by the command edsolv. If you add or modify a solvent entry, the edlock table may have to be updated or adjusted.
### The edsolv table

This table contains one line for each solvent and shows the solvent name and a short description. For edsolv, the Solvents tab is automatically selected and highlighted. Please note that the same table is also opened with the edlock command. Then, the Lock tab is automatically selected and highlighted.
The Solvents tab offers the following functionalities:
 
The Edit tab offers the following functions:
1. Add new solvent
- 
- 
- The easiest way to add a new solvent is to right click on an existing solvent with properties close to your new solvent. Select Copy and paste solvent to copy from this existing solvent to the new solvent. Enter the name of the new solvent and its description. 
- Example: For a new solvent CD2Cl2 right click on CDCl3, which has similar properties. Enter the name of the new solvent CD2Cl2 and in the description field, enter dichloromethane-d2. For the CD2Cl2 example, enter 176K for the melting point and 312K for the boiling point. These two values are just reference for now but might be used in future. You can define the solvent as hidden, specify if this solvent is used as lock solvent and activate the Auto Phase mode.
- Change to the Lock Parameters by clicking the Lock tab, select the new solvent and right click to select Edit Lock parameters. You'll find all parameters of the solvent used for copy and paste in the first step.
1. In the Signals part, change the shift in ppm according to the signal used for locking in your new solvent. For the CD2Cl2 example, change the shift of the dichloromethane resonance to 5.33 ppm.
2. You might want to optimize further lock parameters as described in Optimizing Lock Parameters (see edlock)
- Select the spectrum reference tab, right click the new solvent to select Edit spectrum reference parameters. Adjust the reference shift and search width according to your needs. For the most commonly used reference standard TMS just leave the reference shift at 0 ppm and the search width at 0.5 ppm. In this case the search range is +/- 0.25 ppm around 0 ppm, which is suitable for TMS.
- Please note, all solvents not marked as lock solvents will only appear in the list if the Show no locking solvents is active in the Solvents pull down menu (see above). These solvents cannot be used with the lock command.
2. Edit solvent
- The parameters entered here are shown when you click on the Properties tab. Double-clicking on a solvent line in the Properties table opens the Edit Solvent dialog.
3. Delete solvent
4. Copy and paste solvent
5. Update probe specific lock powers
6. Delete probe from all solvents
7. Search solvent
You can also right-click in the table to add, edit, delete, copy and paste or hide a solvent. 
Before you start an experiment, you must set the parameter SOLVENT to an entry from the solvent table. If you do this from eda, you can click the arrow button to the right of this parameter and select an entry from the solvent list.
### The edlock table

When edlock is executed for the first time on a certain probe, a default lock table, which is delivered with TopSpin, is opened.
The main part of the lock table shows a list of solvents and, for each solvent, the lock parameters. Most lock parameters are used for locking the magnetic field during the acquisition. Others, however, are used for referencing the spectrum after the acquisition has finished.
With a right-click on a solvent line several commands and options become available (see screenshot below).
 
### Lock Parameters Used To Lock The Magnetic Field:

1. Lock Power - power used to irradiate the lock nucleus (-60 to 0 dB).
- The actual range depends on the hardware code and on the frequency: The first series of RF boards (HW code 0) had a range from -50 to +10 dB, the next following series (HW code 1 and higher) had a range from -60 to +0 dB. For frequencies of 600 MHz and above, this range has been extended (-60 dB to +10 dB) on the hardware versions 6 and higher.
2. Lock Power Instep - displays the Initial Step for the Lock Power.
- This value is used for the Initial Lock Step, to be added to the Lock Power. Example: For CDCl3, the Lock Power is -28, the InStep is +10, so the Initial Lock Power Step will be done with -18 dB.
3. Loop Gain - lock regulator gain (-80 to 0 dB).
- It is set at the end of the acquisition to the loop gain currently set on the BSMS unit. This usually, but not necessarily corresponds to the value of the Loop Gain in the table. If lock-in was performed with the command lock, the loop gain is first read from the table and set on the BSMS unit. However, using autolock or Lock on/off in bsmsdisp performs lock-in without first reading the table.
4. Loop Time - lock regulator time constant (0.001 - 1.0 seconds).
5. Loop Filter - lock regulator cut-off frequency of the lowpass filter (1 - 200 Hz).
6. Lock Phase - the phase of the lock signal.
7. Shift [ppm] - Chemical shift of the lock nucleus (irradiation frequency offset).
8. Relative intensity - provides the relative intensity where a solvent has several signals.
9. Type - if a solvent has several signals, then Type defines which signal is used for locking. This is either the sharpest or the best separated one. Typically, the most intense signal is used (see relative intensity).
- Relative intensity and type are only shown when a solvent has been selected. 
The lock parameters are interpreted by the commands lock and lopo.
 
The loop gain, loop time and loop filter can also be set with the TopSpin commands lgain, ltime and lfilter, respectively. Furthermore, they can also be set from the BSMS keyboard menu.
### NOTE

Note the difference between loop gain which can be set in edlock or with lgain and lock gain which can be set in the BSMS display. The AU program loopadj automatically optimizes the lock phase, lock gain, loop gain, loop filter and loop time. 
Note that loopadj optimizes these parameters for best long-term stability, but not for best lineshape, resolution or homogeneity (for more information type edau loopadj and look at the header of the AU program).
 
### Optimizing Lock Parameters

Lock Power
After the sample has been locked and shimmed, start the auto-power routine from the bsmsdisp command. For lock solvents with long T1 relaxation times (e.g. CDCl3), auto-power might take an unacceptably long time. In this case a manual optimization of the lock power is recommended. Increase the lock power until the lock signals begins to oscillate (until saturation), and then reduce the power level slightly (approximately 3 - 6 dB). Do not reduce too much, as this will affect the field stability. Alternatively, you might use a gradient experiment (e.g. Parameter set COSYGPSW, or the pulse program preempgp2) to observe the gradients on the lock. In case of optimum lock power, the lock signal will return to normal level after the gradient. An overshoot before returning to the normal level is caused by saturation, so reduce the lock power until this overshoot is no longer visible.
Lock Phase
Use the auto-phase feature in bsmsdisp to optimize the Lock Phase.
Lock Gain
Use the auto-gain feature in bsmsdisp to optimize the Lock Gain.
Loop Gain, Loop Time and Loop Filter 
Generally, these parameters should be already suitable in the default Bruker Solvent list, so there should be no need to change them. However, the AU program loopadj can be used to automatically optimize loop gain, loop time and loop filter for optimal long-term stability.
Alternatively, the following procedure might be used:
Note the Lock Gain value after the auto-gain routine has optimized it. Using this value, select the appropriate values for the loop filter, loop gain and loop time as shown in the following table:
Lock RX Gain (after auto gain) [dB]
Loop Filter [Hz]
Loop Gain [dB]
Loop Time [sec]
120
20
-17.9
0.681
 
30
-14.3
0.589
110
50
-9.4
0.464
 
70
-6.6
0.384
 
100
-3.7
0.306
100
160
0.3
0.220
 
250
3.9
0.158
 
400
7.1
0.111
90
600
9.9
0.083
 
1000
13.2
0.059
 
1500
15.2
0.047
 
2000
16.8
0.041
### Example:

Auto-gain determines a lock gain of 100 dB. From the table, the user should set the loop filter to 160 Hz, the loop gain to 0.3 dB and the loop time to 0.220 sec.
This procedure is recommended to use with shielded magnets. For non-shielded magnets a general procedure cannot be given, so the relation between the three parameters should be determined individually. If in doubt, it is recommended to leave the Bruker default parameters unchanged.
### Optimizing Lock Phase

At the top of the edlock table, the auto phasing of the lock signal can be turned on or off. When auto phase is turned on, the algorithm can be selected from the dropdown list. Autophase and lock are treated differently. The behavior of the lock command with respect to Autophase handling can be controlled independently with a checkbox in the edlock window. When turned on, the FFA algorithm (Spectrum) is used. The default behavior is no Autophase during lock and lock level default for the algorithm. In this state the table will contain the lock phase column. With Autophase turned on, the lock phase column is not needed and therefore unavailable.
There are three selections for the Autophase algorithm:
1. Lock level default: This uses the old algorithm, optimization via lock level.
2. Enhanced lock level: This also uses the old algorithm, but with wider range. It will therefore need more time.
3. Spectrum: This is the new algorithm (FFA). It will also take longer, but not that much, because a spectrum is measured anyway during locking. This is the recommended selection if Autophase is activated for the L-TRX and execution time is not critical, e.g. in case of high throughput samples.
Calibration of the Autophase offset
This calibration is mandantory if Autophase is selected and spectrum selected for the algorithm. It can be selected via the pull down menu entry BSMS | Calibrate Autophase offset. This control can also be added to the BSMS Display (bsmsdisp) if needed. The following window will be displayed:
 
Please follow the instructions, insert the recommended sample and click OK when finished.
 
Please wait until the offset calibration is ready (approximately 1½-2 minutes). The result can be checked on the ELCB Webpage. Click LOCK | LOCK Configuration | Autolock Configuration and check Phase offset FFA to Lock.
 
The ELCB Webpage can also be used to activate the Phase offset calibration. Use the BSMS Service Page and choose Calibration | Auto Lock Phase Calibration. Again, use a suitable sample as outlined in the Auto Phase Calibration Info field.
 
### NOTE

Important: The phase offset calibration should be repeated if the 2H Preamplifier is exchanged.
 
### Lock Parameters Used To Reference The Spectrum:

Clicking the Spectrum reference tab opens the default list of spectrum reference parameters for the default solvents.
 
1. Noise – Signal to Noise value for reference signal detection (initially 10)
2. Reference Shift [ppm]- chemical shift of the reference signal (default 0).
3. Reference Shift Corr. [ppm] – additional chemical shift correction value. This value is added after the referencing signal has been detected and referenced. 
4. Search Width [ppm] - This specifies the search width window for the reference signals, e.g. a value of 0.5 ppm will search from -0.25 to 0.25 ppm from the specified reference shift.
5. Signal Regions – relative intensity scaling of spectrum peaks is performed on the listed regions. The gaps between the regions are excluded.
These parameters are interpreted by the command sref.
### Automation Tab with information for SpinPilot

The solvents table now includes information about the lock routine, shim routine and shim file used for automation for each solvent. It can be entered by clicking on the Automation tab in the edlock table.
 
This information is used by SpinPilot in a manner analogous to how IconNMR utilizes its internal table.
 
The BSMS Tab offers the following functionalities: 
 
In IconNMR automation, the lock parameters are read from the lock table and used as they are. For more information, refer to the spectrometer hardware documentation which is available on the BASH CDROM.
### INPUT AND OUTPUT PARAMETERS

See description above


## SEE ALSO

lock, lopo, edprobe, lockdisp, lgain, ltime, lfilter
© 2025 Bruker BioSpin GmbH & Co. KG
