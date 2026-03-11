# sym, syma, symj, symt

**Category:** Commands > Process > Processing Spectrum

## NAME

**sym** - Symmetrize spectrum about the diagonal (2D)

**syma** - Symmetrize spectrum about the diagonal, keep sign (2D)

**symj** - Symmetrize spectrum about central horizontal line (2D)

**symt** - Open symmetrization and tilt commands dialog box (2D)


## DESCRIPTION

The symt command opens the symmetrize/tilt dialog box:
 
This dialog box offers several options, each of which selects a certain command for execution.
### Symmetrize COSY type spectrum

This option selects the command sym for execution. It symmetrizes a 2D spectrum about a diagonal from the lower left corner (data point 1,1) to the upper right corner (data point F2-SI, F1-SI). It compares each data point with the corresponding data point on the other side of the diagonal and determines which one has the lowest (most negative) intensity. Then both data points are set to that intensity. The following table shows the intensities of four pairs of data points before and after sym: 
before sym
after sym
-370000, 12000
-370000, -370000
1000, -700 
-700, -700
18000, 6000
6000, 6000
-13000, -8000
-13000, -13000
sym is typically used on magnitude cosy spectra.
### Symmetrize phase sensitive spectrum

This option selects the command syma for execution. It works like sym, except that it compares each data point with the corresponding data point on the other side of the diagonal and determines which one has the lowest absolute intensity. Then both data points are set to that intensity while each point keeps its original sign. The following table shows the intensities of four pairs of data points before and after syma: 
before syma
after syma
-370000, 12000
-12000, 12000
1000, -700 
700, -700
18000, 6000
6000, 6000
-13000, -8000
-8000, -8000
syma is typically used on phase sensitive cosy spectra.
### Symmetrize J-resolved spectrum

This option selects the command symj for execution. It symmetrizes a 2D spectrum about a horizontal line through the middle. It is similar to sym, i.e. it compares each data point with the corresponding data point on the other side of the horizontal line and determines which one has the lowest (most negative) intensity. Then both data points are set to that intensity. The following table shows the intensities of 5 pairs of data points before and after symj: 
before symj
after symj
-370000, 12000
-370000, -370000
1000, -700 
-700, -700
18000, 6000
6000, 6000
-13000, -8000
-13000, -13000
symj is typically used on J-resolved spectra which have been tilted with the command tilt.
sym* commands only work on the real data. After using it, the imaginary data no longer match the real data and cannot be used for phase correction.
When executed from the command line, the command sym, syma and symj select the corresponding option in the dialog box. This means, you can just click OK or hit Enter to start the command. In contrast, symt selects the last used symmetrization command. 
### OUTPUT PARAMETERS

Can be viewed with dpp or by typing s symm :
SYMM - type of symmetrization (no, sym, syma or symj) done


## INPUT FILES

<dir>/data/<user>/nmr/<name>/<expno>/pdata/<procno>/
2rr - real processed 2D data


## OUTPUT FILES

<dir>/data/<user>/nmr/<name>/<expno>/pdata/<procno>/
2rr - real processed 2D data
auditp.txt - processing audit trail


## USAGE IN AU PROGRAMS

SYM
SYMA
SYMJ
 
© 2025 Bruker BioSpin GmbH & Co. KG
