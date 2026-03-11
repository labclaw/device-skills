# paste

**Category:** Commands > Miscellaneous > Dataset Handling

## NAME

**paste** - Open the dataset that was last copied (nD)


## DESCRIPTION

The command paste opens the dataset which was previously copied from a TopSpin data window or from the File Explorer. This involves two steps:
1. Copy
- In the File Explorer:
1. Go to a dataset
2. Right-click a dataset folder or file, e.g. the data name, expno or procno folder or any file in it and click Copy
2. Paste
- In TopSpin: 
1. Click File | Paste or type paste
Note that if you select and copy a the data set in the File Explorer, its data path is copied to the Clipboard. The command Paste reads this path from the Clipboard. If you run Paste without first copying a data set from the Explorer, TopSpin tries to read whatever is currently stored in the Clipboard. If that is a data path, TopSpin will read it, otherwise you will get an error message.


## OUTPUT FILES

<tshome>/prog/curdir/<user>/
curdat - current data definition


## SEE ALSO

copy
© 2025 Bruker BioSpin GmbH & Co. KG
