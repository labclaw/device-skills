# getlim1d, getlcosy, getlxhco, getljres, getlinv

**Category:** Commands > Acquire > Set Limits

## NAME

**getlim1d** - Calculate 1D spectral width from integral ranges

**getlcosy** - Calculate 2D COSY spectral width from 1D integral ranges

**getlxhco** - Calculate 2D XHCO spectral width from 1D integral ranges

**getljres** - Calculate 2D jres spectral width from 1D integral ranges

**getlinv** - Calculate 2D inverse spectral width from 1D integral ranges


## DESCRIPTION

The getl* commands listed above calculate and set the optimum spectral width for the specified experiment types. The optimum spectral width is determined from one or two associated 1D datasets, which are defined as the so called second and third dataset. Before the actual experiment is performed, the second (and if necessary the third) dataset must be acquired, Fourier transformed, and baseline corrected. The latter processing step implicitly determines the integral ranges. The getl* commands determine the spectral width such that it includes all integral ranges, in other words, all signals.
getl* commands are typically used in automation. They are called from AU programs like au_getl1d, au_getlcosy, au_getlinv and au_getlxhco. These, in turn, are called by IconNMR where the preparation and the actual experiment are defined as a so-called composite 2D experiment (see IconNMR Online help for more information).
getlim1d determines the optimum spectral width on a 1D preparation experiment and then sets the parameter SW on the current 1D dataset accordingly.
getlcosy determines the optimum spectral width on one 1D preparation experiment. Then it sets the F2-SW and F1-SW on the current 2D COSY dataset accordingly.
getlxhco determines the optimum spectral width for F2 and F1 on two different 1D preparation experiments (typically 1H and X). Then it sets the F2-SW and F1-SW on the current 2D XH correlation dataset accordingly.
getljres determines the optimum spectral width on one 1D preparation experiment. Then it sets F2-SW on the current 2D J-resolved dataset in accordingly.
getlinv determines the spectral width on one 1D preparation experiment. Then it sets F2-SW on the current 2D INVERSE dataset accordingly.
### NOTE

Note that F2-SW refers to the acquisition parameter SW in the F2 direction and F1-SW refers to the same parameter in the F1 direction. 
The first 1D preparation experiment is defined as the so called second dataset. The second 1D preparation experiment is defined as the so called third dataset.
### OUTPUT PARAMETERS

1. SW - spectral width in ppm


## INPUT FILES

1. <dir>/data/<user>/nmr/<name>/<expno>/pdata/<procno>
1. intrng - integral regions
2. curdat2 - definition of second and third dataset


## OUTPUT FILES

1. <dir>/data/<user>/nmr/<name>/<expno>/
1. acqu - acquisition parameters
2. acqu2 - F1 acquisition parameters of a 2D dataset


## USAGE IN AU PROGRAMS

1. GETLIM 
executes the command  getlim1d 
2. GETLCOSY
3. GETLXHCO
4. GETLJRES
5. GETLINV
© 2025 Bruker BioSpin GmbH & Co. KG
