#!/usr/bin/env python

import sys, os, json
files = {}

def checkd(abc):
    os.chdir(abc)
    for file in os.listdir(os.getcwd()):
        file = os.path.join(os.getcwd(), file)
        if os.path.isfile(file):
            files[file] = os.lstat(file).st_size
    print(json.dumps({"files" : files}, indent=4))
    return

if len(sys.argv) != 2:
    print("Please enter the correct number of arguments i.e. script name and mount path only")
    sys.exit(1)

if os.path.lexists(sys.argv[1]):
    if os.path.isdir(sys.argv[1]):
        checkd(str(sys.argv[1]))
    else:
        print(sys.argv[1], "is not a directory")
else:
    print(sys.argv[1], "is not accessible")