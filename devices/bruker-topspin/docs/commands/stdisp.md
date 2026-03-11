# stdisp

**Category:** Commands > Manage > Spectrometer > Experiments/Parameters

## NAME

**stdisp** - ShapeTool for handling RF shapes and gradients


## DESCRIPTION

The command stdisp opens the ShapeTool window where you can create, manipulate and analyse RF shapes and gradients (see the next figure).
 
The functions of the buttons are available as tooltips. A detailed description of stdisp can be found under Help | Manuals | Acquisition | Application Manuals | Shapetool.
### Pulse Shapes

Pulse shapes (waveforms) are stored in the directory <XWINNMRHOME>/exp/stan/nmr/lists/wave/ in ASCII format conforming to JCAMP-DX. The example below shows a section of a shape file. The data points represent the amplitude and phase values.
Bruker shape file format:
##TITLE= sm. comp. Chirp: 60kHz, 2ms
##JCAMP-DX= 5.00 Bruker JCAMP library
##DATA TYPE= Shape Data
##ORIGIN= Bruker BioSpin GmbH
##OWNER= <demo>
##DATE= 2005/09/22
##TIME= 18:40:13
##$SHAPE_PARAMETERS= Type: CompositeSmoothedChirp Add Const. Phase -84.0
##MINX= 0.000000E00
##MAXX= 1.000000E02
##MINY= 1.110750E-01
##MAXY= 3.599617E02
##$SHAPE_EXMODE= CompositeAdiabatic
##$SHAPE_TOTROT= 1.800000E02
##$SHAPE_TYPE= Refocussing
##$SHAPE_USER_DEF= 
##$SHAPE_REPHFAC= 
##$SHAPE_BWFAC= 8.099400E01
##$SHAPE_BWFAC50= 
##$SHAPE_INTEGFAC= 2.558317E-02
##$SHAPE_MODE= 0
##NPOINTS= 4000
##XYPOINTS= (XY..XY)
0.000000E00, 1.833013E02
7.893367E-01, 1.779122E02
…………………………, …………………………
##END=
 
© 2025 Bruker BioSpin GmbH & Co. KG
