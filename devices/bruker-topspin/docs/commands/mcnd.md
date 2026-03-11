# mcnd

**Category:** Commands > Process > Adjust Phase

## NAME

**mcnd** - nD magnitude calculation (≥ 3D)


## DESCRIPTION

The command mcnd calculates the magnitude spectrum of a nD dataset. The intensity i is replaced by its absolute value according to the formula: 
where R and I are the real and imaginary part of the spectrum respectively. The imaginary part of nD QF datasets is kept in a separate file
in 3iii for 3D data
in 4iii for 4D data
in 5i for 5D data
in 6i for 6D data
when processing the last direction of a nD QF dataset. PH_mod in this direction is usually set to mc. This leads to a magnitude calculation after Fourier transform and the file holding imaginary data is removed.
With the mcnd command the magnitude calculation can be done in a separate processing step, especially if PH_mod in the last processing direction was not set to mc or ps.
If the command mcnd is applied to hypercomplex nD datasets imaginary data are calculated internally by a Hilbert transform.


## INPUT FILES

3rrrr, 3iii - for 3D data
4rrrr, 4iiii - for 4D data
5r, 5i - for 5D data
6r, 6i - for 6D data


## OUTPUT FILES

auditp.txt
3rrr - for 3D data
4rrrr - for 4D data
5r - for 5r data
6r - for 6D data


## SEE ALSO

mc, ps, apk, apks, apkm, apkf, ph, trf, trfp
© 2025 Bruker BioSpin GmbH & Co. KG
