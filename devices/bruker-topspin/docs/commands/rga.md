# rga

**Category:** Commands > Acquire > Gain

## NAME

**rga** - Automatic receiver gain optimization


## DESCRIPTION

The command rga automatically optimizes the receiver gain. It performs an acquisition with varying receiver gain and finally sets it just below the value where no overflow occurs. In fact, rga repeatedly executes the current pulse program but only up to the first go=n or rcyc=n statement.
If you already know the proper value for the receiver gain, you can simply set RG in eda or by typing rg on the command line.
### OUTPUT PARAMETERS

1. can be viewed with eda or by typing rg:
1. RG - receiver gain
### USAGE IN AUTOMATION

1. RGA


## SEE ALSO

gs, zg, go
© 2025 Bruker BioSpin GmbH & Co. KG
