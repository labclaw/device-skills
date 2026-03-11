# atmm

**Category:** Commands > Acquire > Tune

## NAME

**atmm** - Manual tuning and matching of ATM probes


## DESCRIPTION

The command atmm is a manual tuning and matching procedure for ATM probes. It is not needed very often because ATM probes are designed for automatic tuning and matching with atma. Sometimes, however, the probes resonance frequency is so far away from the optimum that atma would take very long to finish or would fail. In practice, this only occurs for certain nuclei at broadband probes. In that case, atmm allows you to manually tune and match the probe for that nucleus.
atmm performs the following steps:
1. It reads the nucleus with the lowest frequency as it was set up with edasp.
2. It determines the optimum sweep width and number of steps.
3. It shows the reflected power (tuning/matching curve) in the TopSpin acquisition data field.
4. It opens the atmm control window from where you can:
1. See information about the connected probe and the status of the atma server.
2. Select the nucleus for which you want to tune and match the probe. By default, the nucleus with the lowest frequency is selected.
3. Start ATMA with a click on the start button which will perform an automatic tuning/matching. The positions will be stored for further use of atma or atmm.
4. Open an optional window where the complex wobble curve (real and imaginary part) is displayed in a sophisticated representation visualizing more information compared to a conventional wobble curve; this can be helpful to optimize more quickly. Instead of the normal wobble curve, a circle with a red dot is shown which has to be moved into the center of the coordinate system to achieve optimal tuning/matching.
5. Perform coarse tuning/matching on broadband probes. This is the equivalent of setting the sliders on a non-ATM probe to predefined numbers.
6. Perform fine tuning/matching while observing the curve in the TopSpin acquisition data field. This is the equivalent of turning the knobs or moving the sliders on a non ATM probe. See wobb for a description on how to reach the optimum tuning and matching.
During tuning and matching with the arrow keys, the positions are saved for the current channel and nucleus combination. atmm will move to these positions automatically on startup if the channel and nucleus combination will be selected again after rerouting.
7. Click Close to finish the tuning/matching process.
 
If atmm is used with the argument manWbsw, it does not determine the sweep width and number of steps automatically but interprets the parameters WBSW and WBST, respectively. atmm options will show you a complete list of arguments.
The difference between atmm and wobb is that:
1. atmm can only be used on ATM probes.
2. atmm, when used without arguments, automatically determines the optimum sweep width and number of steps whereas wobb uses the values of WBSW and WBST, respectively.
3. atmm allows you to optimize tuning and matching from TopSpin whereas wobb requires you to turn the knobs (or move the sliders) on the probe.
For more information on the tuning and matching process, see wobb.
 
Note: When using an IProbe, the command might appear unresponsive due to processes that can take a few minutes: 
1. After installation of a new TopSpin version the atma server might install a new firmware to the IProbe electronics.
2. After finishing an automatic tuning procedure, the data on the probe might need compres-sion.
In both cases, the status is reported accordingly in the atmm window or the topspin status bar.


## INPUT PARAMETERS

1. NUC1 - NUC4 - nuclei as defined with edasp 
2. WBSW - sweep width (only used by atmm manwbsw)
3. WBST - number of steps (only used by atmm manwbsw)


## INPUT FILES

1. <dir>/data/<user>/nmr/<name>/<expno>/
1. acqu - acquisition parameters
2. <tshome>/prog/wobble/
1. acqu_go4 - wobble parameters 
2. Pulsprog_X - wobble pulse program


## SEE ALSO

atma, wobb
© 2025 Bruker BioSpin GmbH & Co. KG
