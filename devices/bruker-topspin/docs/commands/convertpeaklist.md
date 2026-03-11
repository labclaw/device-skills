# convertpeaklist

**Category:** Commands > Analyze > Pick Peaks

## NAME

**convertpeaklist** - Convert XML-format peak list to TXT-format peak list


## DESCRIPTION

The command convertpeaklist converts an XML-format peak list to various other formats. The output format can be controlled with the argument:
txt - text format, file peak.txt
peaklist - Mixed Shape Deconvolution format, file peaklist
ml - AUREMOL format, file 1r.ml (1D), masterlist.ml (2D)
peaks - XEASY format, file xeasy.peaks)


## INPUT FILES

<dir>/data/<user>/nmr/<name>/<expno>/pdata/<procno>/
peaklist.xml - peak list for the Plot Editor in XML format


## OUTPUT FILES

<dir>/data/<user>/nmr/<name>/<expno>/pdata/<procno>/
peak.txt - peak list for the Plot Editor in TXT format


## SEE ALSO

pps, ppf, ppl, pph, ppj, dcon2d, dcon
© 2025 Bruker BioSpin GmbH & Co. KG
