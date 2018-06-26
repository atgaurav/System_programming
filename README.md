# getdiskusage.py

## Purpose
	A program in python which takes a mount point as an argument and return a list of all the files on the mountpoint and their disk usage in bytes in json format.
	It runs for both windows and linux servers.

Eg
getdiskusage.py /tmp
{
 	"files":
	[
 		{"/tmp/foo", 1000},
 		{"/tmp/bar", 1000000},
 		{"/tmp/buzzz", 42},
 	],
}

### Language	: Python 3

### How to run the script?
- If Python3 is set in the environment variables: python3 getdiskusage.py /mnt
- If python is set in the environment variables:	python getdiskusage.py /mnt

### Exceptions to look for:
1. Check if only 1 argument is sent with the script name.
   - Exception: Please enter the correct number of arguments i.e. script name and mount path only
2. Check if 'path exists'
   - Exception: _____ is not a directory
3. Check if the path is not accessible
   - Exception: _____ is not accessible			[_____ = value of variable passed while calling the script]
