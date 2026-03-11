# lockdataset

**Category:** Commands > Manage > Security

## NAME

**lockdataset** - Lock dataset (change permissions) to prevent future changes


## DESCRIPTION

The command lockdataset applies permission changes on the current data set. Content of the EXPNO and PROCNO directories will be protected against further overwrite/append/delete operations, and the directory objects itself will lose permissions to add file and subdirectories in it. Effectively, the directory will be frozen. It is still possible to add and process new PROCNOs for the same raw data while the initial PROCNO remains protected. This is especially useful in GLP environments and allows to implement a standard procedure like e.g. the following:
Automatically acquire and process data set in PROCNO 1→ digitally sign data by command esign 
→ apply lockdataset to protect against modification 
→ use command wrp 2 to create new PROCNO → change to it by rep 2 
→ perform interactive processing there (without touching original signed data)
 
The command lockdataset can be used as part of AU scripts like e.g. the one defined by AUNMP. It is also available by interactive menu selection Manage/Security/Lock Data Set Against Changes
 
© 2025 Bruker BioSpin GmbH & Co. KG
