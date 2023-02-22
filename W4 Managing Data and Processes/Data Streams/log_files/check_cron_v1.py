#!/usr/bin/env python3

import sys
import re

# logfile = sys.argv[1]
# with open(logfile) as f:
#     for line in f:
#         print(line.strip())

# # When working with log files and scripts, our first step is usually to open them so our code can access their contents.
# # Remember that for performance reasons, when files are large, it's generally a good practice to read them line by line instead of loading the entire contents into memory.

# logfile = sys.argv[1]
# with open(logfile) as f:
#     for line in f:
#         if "CRON" not in line:
#             continue
#         print(line.strip())

# # The server that generates this log file has been acting strangely and we suspect it's due to a Cron job started by one of the system administrators. You may remember that Cron jobs are used to schedule scripts on UNIX-based operating systems. To find out what's happening with the server, we want to audit the log files and see exactly who's been launching CRON jobs. By looking at the sample log, we can see that the lines that'll be most interesting to us are the ones that contain the Cron substring. These lines also show the user who started the Cron job wrapped in parentheses. With this info, we can ignore any line without the Cron substring in it.

logfile = sys.argv[1]
with open(logfile) as f:
    for line in f:
        if "CRON" not in line:
            continue
        pattern = r"USER \((\w+\)$"
        result = re.search(pattern, line)
        print(result[1])
# # To run function in CLI
# ./check_cron_v1 syslog

# Once we know we're processing to write log line, we can use our knowledge of regular expressions to extract the username.
# Let's take a closer look at this expression. Since the username is found at the end log line, we use the dollar sign anchor to only match texts that is at the end of the line. To find the username, we look for the word user followed by a string wrapped in parentheses as that's how these lines are structured. This means that we need to escape those parentheses with a backslash. Since we want to extract the actual username, we use another couple of parentheses to create a capturing group. For the username itself, we're matching any alphanumeric characters by using backslash w plus.
