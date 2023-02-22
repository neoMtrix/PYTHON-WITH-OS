#!/usr/bin/env python3

import subprocess

subprocess.run(["date"])
subprocess.run(["sleep", "2"])
# sleep command, which waits for a number of seconds that we tell it before returning

result = subprocess.run(["ls", "this_file_does_not_exist"])
print(result.returncode)
# If we call LS with a file name that doesn't exist, LS will print an error and return an exit status different than 0. This will be stored in the return code attribute of the completed process instance, and we can access that value in our code
