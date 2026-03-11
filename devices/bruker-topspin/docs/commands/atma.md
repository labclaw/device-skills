# atma

**Category:** Commands > Acquire > Tune

## NAME

**atma** - Automatic tuning and matching of ATM probes


## DESCRIPTION

The command atma performs tuning and matching of an ATM probe. It will automatically perform the following steps: 
1. Stop the sample rotation if it is on.
2. Read the nucleus with the lowest frequency as it was set up with edasp.
3. Determine the optimum sweep width and number of steps.
4. Tune and match the probe.
5. Repeat step 3 to 4 for all other nuclei which were set up with edasp in the order of increasing frequency.
6. Turn on the sample rotation if it was on before atma was started.
 
The command atma can be used with various options, for example:
1. atma exact will determine the optimum tuning and matching more precisely then atma without an argument and will therefore be slower.
2. atma coarse will determine the optimum tuning and matching less precisely then atma without an argument and will therefore be faster.
3. atma high will start with the nucleus with the highest frequency, and tune and match the probe for each nucleus in the order of decreasing frequency.
4. atma reset will reset all data collected by the atma software on the workstation and on the probe if it is an IProbe
5. atma storeWobb <x> will automatically save the wobble curve after optimisation. <x> stands for the respective procno of the used dataset.
- If more than one nucleus should be stored than the respectively next wobble curve n+1 will bei stored in the procno number <x+1> (see also command wbwr).
- Type atma options for a complete list of options.
 
On ATM probes, atma can be used instead of the wobb. These two commands differ in the following respects:
1. atma is fully automatic whereas wobb requires the user to perform the tuning and matching manually.
2. atma automatically determines the optimal sweep width and number of steps whereas wobb uses the values of WBSW and WBST, respectively.
3. wobb must be terminated with stop or halt whereas atma automatically finishes when optimum tuning and matching is reached. If you want to interrupt atma, you can do that with the command kill.
 
Automatic tuning and matching is not only convenient, it also allows you to tune and match the probe during automation. In IconNMR, you can choose to do that before each experiment, after each sample change or after each solvent change.
For more information on the tuning and matching process, see wobb.
 
Note: When using an IProbe, the command might appear unresponsive due to processes that can take a few minutes: 
1. After installation of a new TopSpin version the atma server might install a new firmware to the IProbe electronics.
2. After finishing an automatic tuning procedure, the data on the probe might need compres-sion.
In both cases, the status is reported accordingly in the atmm window or the topspin status bar.


## INPUT PARAMETERS

1. NUC1 - NUC4 - nuclei as defined with edasp


## INPUT FILES

1. <dir>/data/<user>/nmr/<name>/<expno>/
1. acqu - acquisition parameters
2. <tshome>/conf/instr/<instrum>/
1. nuclei - nuclei table
3. <tshome>/prog/wobble/
1. acqu_go4 - wobble parameters 
2. Pulsprog_X - wobble pulse program


## SEE ALSO

atmm, wobb, wbwr
© 2025 Bruker BioSpin GmbH & Co. KG
