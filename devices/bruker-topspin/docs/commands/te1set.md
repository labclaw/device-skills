# teset, te1set, te2set, te3set, te4set

**Category:** Commands > Acquire > Sample

## NAME

**teset** - Set the temperature on the temperature unit

**te1set** - Equivalent to teset

**te2set** - Set the second temperature on the temperature unit

**te3set** - Set the third temperature on the temperature unit

**te4set** - Set the fourth temperature on the temperature unit


## DESCRIPTION

The command teset sets the temperature on the temperature unit. It takes one argument and can be used as follows:
teset
Sets the temperature to the value of the acquisition parameter TE. Before you enter teset without argument you must set TE to the desired temperature, in Kelvin, either from eda or by typing te on the command line.
teset <temperature>
Sets the temperature to the specified value.
The command teset is, for example, used in the AU programs au_zgte and multi_zgvt.
The command te2set works like teset except that it sets the so called second temperature to the value of the acquisition parameter TE2. This value is set on the second regulator of a temperature unit with two regulators. Such units are, for example, used in BEST NMR where the first regulator controls the sample temperature, and the second regulator controls the inlet capillary temperature.


## INPUT PARAMETERS

1. TE - demand temperature on the temperature unit (input of teset).
2. TE1 – demand temperature on the temperature unit (input of te1set).
3. TE2 - demand second temperature on the temperature unit (input of te2set).
4. TE3 - demand third temperature on the temperature unit (input of te3set).
5. TE4 - demand fourth temperature on the temperature unit (input of te4set).


## INPUT FILES

1. <dir>/data/<user>/nmr/<name>/<expno>/
1. acqu - acquisition parameters


## USAGE IN AU PROGRAMS

1. TESET
2. TE1SET
3. TE2SET
4. TE3SET
5. TE4SET
6. VT executes the command  teset <vt_list_index>


## SEE ALSO

edte, teget, te2get
© 2025 Bruker BioSpin GmbH & Co. KG
