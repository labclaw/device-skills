# totxt

**Category:** Commands > Miscellaneous > Dataset Handling

## NAME

**totxt** - Save the currently displayed region as a text file (1D, 2D)


## DESCRIPTION

The command totxt saves the currently displayed spectral region as text file. It will open the following dialog box in which you can enter the text file name and directory:
 
totxt works on 1D and 2D data sets and only stores the real processed data. The 1D file format is:
# File created = Wednesday, March 3, 2004 11:52:01 AM CET
# Data set = exam1d_13C 1 1 C:\bio guest
# Spectral Region:
# LEFT = 145.2549493926 ppm. RIGHT = 116.58206350384 ppm.
# SIZE = 3940 (= number of points)
# In the following ordering is from the 'left' to the 'right' limits!
# Lines beginning with '#' must be considered as comment..
# 1.4612096E7
3084512.0
4615664.0
1.6594048E7
4898192.0
-4555792.0 ...


## INPUT FILES

### For 1D data:

<dir>/data/<user>/nmr/<name>/<expno>/pdata/<procno>
1r - real processed 1D data
### For 2D data:

<dir>/data/<user>/nmr/<name>/<expno>/pdata/<procno>
2rr - real processed 2D data


## OUTPUT FILES

<pathname>/<mydata.txt> - text file containing displayed region


## SEE ALSO

tojdx, tozip
© 2025 Bruker BioSpin GmbH & Co. KG
