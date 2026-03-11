# tf3p, tf2p, tf1p

**Category:** Commands > Process > Advanced > Special Transforms

## NAME

**tf3p** - Phase correction in F3 (3D)

**tf2p** - Phase correction in F2 (3D)

**tf1p** - Phase correction in F1 (3D)


## DESCRIPTION

tf3p performs a phase correction in the F3 direction applying the values of PHC0 and PHC1. These values must first be determined, for example on a 2D plane. You can do that by typing xfb on the 3D data to process a 23 or 13 plane, do a phase correction on the resulting the 2D dataset and store the phase values to 3D.
tf2p works like tf3p, except that it works in the F2 direction applying the F2 parameters PHC0 and PHC1. These can be determined on a 2D plane extracted with r23 or r12. 
tf1p works like tf3p, except that it works in the F1 direction applying the F1 parameters PHC0 and PHC1. These can be determined on a 2D plane extracted with r13 or r12. 
tf3p can only be done:
1. directly after tf3 (not after tf2 or tf1)
2. if the F3 imaginary data exist
Note that the command tf3 n does not store the imaginary data. You can, however, create them data from the real data with a Hilbert transform (command tht3).
Phase correction is already done as a part of the commands tf3, tf2 and tf1, if PH_mod = pk and PHC0 and PHC1 are set.


## INPUT PARAMETERS

Set by the user with edp or by typing phc0, phc1 etc.
PHC0 - zero order phase correction value (frequency independent) 
PHC1 - first order phase correction value (frequency dependent) 
### OUTPUT PARAMETERS

Can be viewed with dpp or by typing s phc0, s phc1 etc.:
PHC0 - zero order phase correction value (frequency independent) 
PHC1 - first order phase correction value (frequency dependent)


## INPUT FILES

<dir>/data/<user>/nmr/<name>/<expno>/pdata/<procno>/
3rrr - real processed 3D data 
3irr - F3 imaginary processed data (input of tf3p)
3rir - F2 imaginary processed data (input of tf2p)
3rri - F1-imaginary processed data (input of tf1p)


## OUTPUT FILES

<dir>/data/<user>/nmr/<name>/<expno>/pdata/<procno>/
3rrr - real processed 3D data 
3irr - F3 imaginary processed data (output of tf3p)
3rir - F2 imaginary processed data (output of tf2p)
3rri - F1-imaginary processed data (output of tf1p)
auditp.txt - processing audit trail


## USAGE IN AU PROGRAMS

TF3P(store_imag), where store_image can be y or n
TF2P(store_imag), where store_image can be y or n
TF1P(store_imag), where store_image can be y or n


## SEE ALSO

tf3, tf2, tf1, pk, xfbp, xf2p, xf1p
© 2025 Bruker BioSpin GmbH & Co. KG
