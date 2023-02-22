# #!/usr/bin/env python3

import sys
import re

logfile = sys.argv[1]
usernames = {}
with open(logfile) as f:
    for line in f:
        if "CRON" not in line:
            continue
        pattern = r"USER \((\w+\)$"
        result = re.search(pattern, line)
        if result == None:
            continue
        name = result[1]
        usernames[name] = usernames.get(name, 0) + 1
print(usernames)
# # To run function in CLI
# ./check_cron_v2 syslog

# To improve our output, it would be a good idea to have a count of how many times each username appears in our log.
# As we've seen in earlier examples, dictionaries are great structure to use when we want to count appearances of strings.
# We'll store the user name as a keys of a dictionary and we'll use the value to count the number of times that each user name appears in the file.

# # NOTE
# # When searching log files using regex, which regex statement will search for the alphanumeric word "IP" followed by one or more digits wrapped in parentheses using a capturing group?
# pattern = r"IP \((\d+)\)$"
