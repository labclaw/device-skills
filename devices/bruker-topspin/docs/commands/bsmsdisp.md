# bsmsdisp

**Category:** Commands > Acquire > Shim

## NAME

**bsmsdisp** - Open the BSMS (Bruker Smart Magnet control System) control panel


## DESCRIPTION

The BSMS provides an overview of the most important features and states of the shim system and magnet. It can be opened in four different ways:
1. From the TopSpin menu click Acquire | Shim | Shim manually using BSMS (bsmsdisp):
 
1. With right click in the Lock display in the Acquisition Status Bar | BSMS panel:
- 
2. Click the BSMS icon  in the TopSpin menu bar
3. or type bsmsdisp in the command line. 
 
The BSMS Control Suite main window is opened: 
 
The BSMS Main window tab offers the most prominent functions to control the magnet and the shim system:
1. AUTO – Automatic lock, phase, power, gain and shim procedure
2. LOCK – Switch lock on / off, lock phase, lock power, lock gain 
3. SAMPLE – LIFT or SPIN the sample on/off, Measure (show the actual spin rate in Hz), Rate (show/set the intended spin rate), Always locked shown green (is shown if the lock is on), Lock lost shown red (shows if the lock is lost)
4. SHIM – displays a subset of currently available shim gradients
5. The control window offers the possibility to change the respective values using the control knob, in steps using the stepsize or entering absolute values manually. 
6. The STD BY button  offers the possibility to deselect the settings. 
7. Shut down BSMS – is recommended before hardware turn-off
8. Config. – offers the possibility to show the BSMS window in TopSpin or in an external window.
9. The status bar at the bottom of the BSMS window shows the status of the current sample (down, missing or up) and the current shim coil temperature. 
 
The tab Lock/Level offers the possibility to change advanced lock parameters (e.g., AUTO, LOCK, LOOP, SWEEP, HELIUM LEVEL, SHIM COIL TEMPERATURE).
 
The tab Shim offers the possibility to change advanced LOCK & SPIN parameters and shows the complete set of shim parameters, dependent from the shim system.
 
The tab Autoshim offers the possibility to turn the shim on or off and to select the shim gradients and their interval to be used during autoshim.
 
### NOTE

Please note that all shim coordinates are inactive if their absolute value is set to 0. To activate shims for autoshim you need to activate the absolute value higher than 0.
The tab Service offers some more possibilities to control and check the BSMS, e.g. Helium Level and coil temperature settings. 
NOTICE! Please note that this service should only be used by experienced users. 
 
The tab Service offers the following functionalities: 
1. Helium Level – check the helium level and set Alarm level
2. Unlock BSMS
3. Check lock of BSMS – status check
4. BSMS logfile – show logfile
5. Coil temperature settings – change Maximum / Minimum coil temperature
The tab Log shows current error messages, error messages history and info messages which can be cleared or printed:
 
The Help tab refers to detailed information about the BSMS functionalities.


## SEE ALSO

edlock, lock
© 2025 Bruker BioSpin GmbH & Co. KG
