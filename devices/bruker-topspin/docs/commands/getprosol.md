# getprosol

**Category:** Commands > Acquire > Prosol

## NAME

**getprosol** - Get probe- and solvent-dependent parameters


## DESCRIPTION

The command getprosol reads the probe and solvent dependent parameters (the prosol parameters) and copies them to the corresponding acquisition parameters. Entering getprosol on the command line is equivalent to clicking the AcquPars tab and then clicking the  button. The relations between the prosol and acquisition parameters are shown in table Default relations between prosol and acquisition parameters. These are the default relations which apply to most standard high-resolution experiments. Protein, DNA/RNA, LC-NMR and several other types of experiments require different relations which are defined in the files, triple, triple_na, lcnmr, etc., respectively (see INPUT FILES). To use relations other than default, the so called relations file must be specified in the pulse program. You can do that by editing the pulse program (with edpul or edcpul) and adding the line:
prosol relations=<filename> 
before the actual pulse sequence. To look at an example, you can enter edpul lc2 or edpul zgesgp.
### NOTE

Note that the file default, for default relations can, but does not need to be specified in the pulse program.Default relations between prosol and acquisition parameters
Description
edprosol
eda
F1 90° hard pulse length 
P90[F1]
P[0], P[1]
F1 180° hard pulse length 
P90[F1]*2
P[2]
F2 90 ° hard pulse length 
P90[F2]
P[3]
F2 180° hard pulse length 
P90[F2]*2
P[4]
F1 Tocsy spin lock 60° pulse length 
PTOC[F1]*0.66
P[5]
F1 Tocsy spin lock 90° pulse length
PTOC[F1]
P[6]
F1 Tocsy spin lock 180° pulse length
PTOC[F1]*2
P[7]
F1 Roesy spin lock pulse length
PROE[F1]
P[15]
Gradient 1 pulse length 
P_grad1
P[16]
F1 Tocsy trim pulse length
P_mlev
P[17]
Gradient 2 pulse length 
P_grad2
P[19]
F3 90° hard pulse length 
P90[F3]
P[21]
F3 90° hard pulse length 
P90[F3]*2
P[22]
F1 HSQC trim pulse length 
P_hsqc
P[28]
F2 Roesy spin lock pulse length
PROE[F2]
P[31]
F1 90° hard pulse power level
PL90[F1]
PL[1]
F2 90° hard pulse power level
PL90[F2]
PL[2]
F3 90° hard pulse power level
PL90[F3]
PL[3]
F1 Tocsy spin lock power level 
PLTOC[F1]
PL[10]
F1 Roesy spin lock power level 
PLROE[F1]
PL[11]
F2 CPD power level 
PLCPDP[F2]
PL[12]
F2 Second CPD (bilev) power level
PLCPD2[F2]
PL[13]
F3 CPD power level 
PLCPDP[F3]
PL[16]
F2 Homodecoupling power level
PLHD[F2]
PL[24]
Gradient recovery delay
D_grad
D[16]
F2 CPD pulse length
PCPDP[F2]
PCPD[2]
F2 CPD pulse length
PCPDP[F3]
PCPD[3]
### Usage Of Getprosol With Command Line Options

The command getprosol (get probe and solvent dependent parameters from the edprosol table) can be called with three options:
1. The nucleus.
2. P90, the value for 90° hard pulse length.
3. PL90, the value for 90°hard pulse power level.
The existing prosol parameterset, set up by edprosol, is not modified.
getprosol Nuc P90 PL90 recalculates standard hard power levels with:
PLx = 20*log (Px/P90) and the standard soft power levels PLSH1 - PLSH16 by:
PLSHx = 20*log (integFac*Px/totRot * (P90/90.0) where integFac (=SHAPE_INTEGFAC) and totRot (SHAPE_TOTROT) are read from the shapes <TOPSPINHOME>/exp/stan/nmr/lists/wave/PNSHx 
and 
<TOPSPINHOMME>/exp/stan/nmr/lists/wave/Gaus1.100 (e.g.)
### INPUT AND OUTPUT PARAMETERS

See table Default relations between prosol and acquisition parameters.


## INPUT FILES

1. <tshome>/conf/instr/<instrum>/prosol/relations
1. default - relations file for most experiments
2. triple - relations file for Protein experiments
3. triple_na - relations file for DNA experiments
4. lcnmr - relations file for LC-NMR
5. etc. 
2. <tshome>/conf/instr/<instrum>/prosol/<probeID>/<solvent>
1. nucleus.channel.amplifier - prosol parameters


## OUTPUT FILES

1. <dir>/data/<user>/nmr/<name>/<expno>/
1. acqu - acquisition parameters
2. relations - copy of the input relations file


## SEE ALSO

edprosol, eda
© 2025 Bruker BioSpin GmbH & Co. KG
