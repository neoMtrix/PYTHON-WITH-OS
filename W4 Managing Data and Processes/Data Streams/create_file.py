#!/usr/bin/env python3

import os
import sys

filename = sys.argv[1]  # should be "filename=sys.argv[1]" in CLI
if not os.path.exists(filename):
    with open(filename, "w") as f:
        f.write("New file created\n")
else:
    print("Error, the file {} already exists!".format(filename))
    sys.exit(1)


# This script receives a file name as a command line argument. It first checks whether the file name exist or not. When the file doesn't exist, it creates it by writing a line to it. When the file exist, our script print an error message and exits with an exit value of one. To try this out let's first execute the script and pass a file that doesn't exist.
