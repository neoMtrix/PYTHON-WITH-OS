# This regular expression will work no matter where our process ID shows up or how long or short the line is. As long as there's a single sequence of numbers in the string marked by square brackets, this regex will extract those numbers for us.

import re

log = "July 31 07:05:51 mycomputer bad_process[12345]: ERROR Performing package upgrade"

regex = r"\[(\d+)\]"

result =re.search(regex, log)

print(result[1])
