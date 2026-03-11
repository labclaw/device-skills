# rsc

**Category:** Commands > Process > Advanced

## NAME

**rsc** - Read column from 2D data and store as 1D data (2D, 1D)


## DESCRIPTION

The command rsc reads a column from a 2D spectrum and stores it as a 1D spectrum. When entered on a 2D dataset without arguments, rsc opens a dialog box where you can specify the column number and the procno of the output data. 
 
The column must be specified as a number between 1 and F2-SI. The latter is the F2 processing status parameter SI that can be viewed with s si. The procno can be any number other that the current procno. If the procno field is left empty, the output dataset is stored under data name ~TEMP.
When entered on a 2D dataset, rsc takes up to three arguments and can be used as follows:
rsc opens the above dialog box
rsc <column> stores the specified column under data name ~TEMP
rsc <column> <procno> stores the specified column under the current data name, the current expno and the specified procno. It changes the display to the output 1D data.
rsc <column> <procno> n stores the specified column under the current data name, the current expno and the specified procno. It does not change the display to the output 1D data.
After rsc has read a column and the display has changed to the destination 1D dataset, a subsequent rsc command can be entered on this 1D dataset. This takes two arguments and can be used as follows:
rsc opens the above dialog box
rsc <column> reads the specified column from the 2D dataset from which the current 1D dataset was extracted
rsc <column> <procno> reads the specified column from the 2D dataset that resides under the current data name (however, if the current data name is ~TEMP, rsc <column> <procno> reads from the specified procno in the dataset from which the current 1D dataset was extracted), the current expno and the specified procno. Specifying the procno allows to read a column from a 2D dataset other than the one from which the current 1D dataset was extracted. Furthermore, the AU macro RSC requires two arguments, no matter if it is used on a 1D or on a 2D dataset. 
rsr can also be started from the dialog box that is opened with the command slice.
A special case is a 2D dataset that has been Fourier transformed in F2 but not in F1. rsc then stores 1D processed data that are in the time domain rather than the frequency domain. Below are five different examples of this case. 
### Example 1

A 2D dataset is Fourier transformed in F2, column 17 (time domain) is extracted and stored under the same name and expno, in procno 2. The resulting 1D dataset is Fourier transformed. 
On the 2D dataset, enter the following commands:
xf2 - to Fourier transform in F2 only
rsc 17 2 - to read column 17 to procno 2 and switch to that dataset
ft - to Fourier transform the resulting 1D data according to FnMODE
### NOTE

The 1D data shares the expno, and the acquisition parameters in it, with the source 2D dataset. 1D processing commands automatically recognize that this 1D dataset is a column from a 2D dataset. The command ft interprets the F1 acquisition parameter FnMODE to determine the Fourier transform mode.
### Example 2

A 2D dataset with F1 acquisition mode States is Fourier transformed in F2. Column 17 (time domain) is extracted and stored under data name ~TEMP. The resulting 1D dataset is Fourier transformed.
On the 2D dataset, enter the following commands:
s fnmode – to check the FnMODE value (States), click Cancel.
xf2 - to Fourier transform in F2 only.
s mc2 – to check the MC2 value (States), click Cancel.
rsc 17 - read column 17 to ~TEMP and switch to that dataset.
s aq_mod – to check the AQ_mod value (qsim), click Cancel.
ft - Fourier transform the resulting 1D data according to AQ_mod.
### NOTE

The source 2D and the destination 1D have a separate a set of acquisition parameters. rsc reads the F1 status parameter MC2 of the 2D data and translates that to the corresponding AQ_mod of the 1D data. 1D processing commands recognizes this 1D dataset as regular 1D data. This means, for example, that ft interprets the AQ_mod to determine the Fourier transform mode.
### Example 3

A 2D dataset with an F1 acquisition mode States-TPPI is Fourier transformed in F2. Column 17 (time domain) is extracted and stored under data name ~TEMP. The resulting 1D dataset is Fourier transformed.
On the 2D dataset, enter the following commands:
s fnmode – to check the FnMODE value (States-TPPI), click Cancel.
xf2 - to Fourier transform in F2 only
s mc2 - to check the MC2 value (States-TPPI), click Cancel.
rsc 17 - to read column 17 to ~TEMP and switch to that dataset
ft_mod - to check the FT_mod value (fsc), click Cancel.
trfp - to Fourier transform the resulting 1D data according to FT_mod
### NOTE

The source 2D and the destination 1D have a separate a set of acquisition parameters. Since there is no value for AQ_mod that corresponds to States-TPPI, rsc sets the processing parameter FT_mod instead of the acquisition status parameter AQ_mod. As such, the resulting 1D dataset can only be Fourier transformed correctly with trfp.
### Example 4

A 2D dataset with an F1 acquisition mode QF is Fourier transformed in F2. Column 17 (time domain) is extracted and stored under data name ~TEMP. From the 2D dataset, enter the following commands:
s fnmode – to check the FnMODE value (QF), click Cancel.
xf2 - to Fourier transform in F2 only
s mc2 – to check the MC2 value (QF), click Cancel.
rsc 17 - to read column 17 to ~TEMP and switch to that dataset.
s si – to check the size of the 1D dataset, click Cancel.
### NOTE

For FnMODE = QF the 2D storage mode is different than for other values (see the description of xfb). As such, the size of the resulting 1D data is twice as large as for other values of FnMODE. If 2D imaginary data (file 2ii) exist, 1D imaginary (file 1i) are created. Only in that case, the 1D data can be Fourier transformed.
### Example 5

From a 3D dataset, a plane is extracted and, from this plane a column is extracted.
On the 3D dataset, enter the following commands:
xf2 s13 48 2 - to read the F3-F1 plane 48 to procno 2
rsc 19 3 - to read, from plane 48, column 19 to procno 3
ft : to Fourier transform the resulting 1D data according to FnMODE
### NOTE

The 3D, 2D and 1D dataset are stored in three different procno’s all under the same expno, i.e. they share the same acquisition parameters. 1D processing commands automatically recognize that the 1D dataset is a column from an F3-F1 plane that was extracted from a 3D dataset. As such, ft interprets the F1 parameter FnMODE to determine the Fourier transform mode. Note that F1 is the third direction of the 3D dataset. The parameter handling, however, is transparent to the user.


## INPUT FILES

<dir>/data/<user>/nmr/<name>/<expno>/pdata/<procno>/
2rr, 2ir, 2ri, 2ii - 2D processed data


## OUTPUT FILES

If no output procno is specified:
<dir>/data/<user>/nmr/~TEMP/1/pdata/1/
1r, 1i - 1D spectrum
used_from - data path of the source 2D data and the column no.
auditp.txt - processing audit trail
If the output procno is specified:
<dir>/data/<user>/nmr/<name>/<expno>/pdata/<procno>/
1r, 1i - 1D spectrum
used_from - data path of the source 2D data and the column no.
auditp.txt - processing audit trail


## USAGE IN AU PROGRAMS

RSC(column, procno)
If procno = -1, the column is written to the dataset ~TEMP


## SEE ALSO

rsr, rtr,  wsr, wsc, rser2d, wser, wserp, r12, r13
© 2025 Bruker BioSpin GmbH & Co. KG
