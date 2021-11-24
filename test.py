#! /usr/bin/env python3

#echo Hello World

import sys

f = open(sys.argv[1],"r")
commit_msg = f.read()
#print(f.read)

if 'STOP' in commit_msg:
    print ("stopped")
    exit(1)

exit(0)


