# Exercise - 1
# We'll be working with a log file named syslog.log, which contains logs related to ticky.

# You can view this file using:
cat syslog.log

# The log lines follow a pattern similar to the ones we've seen before. Something like this:

# May 27 11:45:40 ubuntu.local ticky: INFO: Created ticket [#1234] (username)

# Jun 1 11:06:48 ubuntu.local ticky: ERROR: Connection to DB failed (username)

# When the service runs correctly, it logs an INFO message to syslog. It then states what it did and states the username and ticket number related to the event. If the service encounters a problem, it logs an ERROR message to syslog. This error message indicates what was wrong and states the username that triggered the action that caused the problem.

# In this section, we'll search and view different types of error messages. The error messages for ticky details the problems with the file with a timestamp for when each problem occurred.

# These are a few kinds of listed error:

# Timeout while retrieving information
# The ticket was modified while updating
# Connection to DB failed
# Tried to add information to a closed ticket
# Permission denied while closing ticket
# Ticket doesn't exist

# To grep all the logs from ticky, use the following command:
grep ticky syslog.log

# In order to search all the ERROR logs, use the following command:
grep "ERROR" syslog.log

# To enlist all the ERROR messages of specific kind use the below syntax.
# Syntax: grep ERROR [message] [file-name]
grep "ERROR Tried to add information to closed ticket" syslog.log

# Let's now write a few regular expressions using a python3 interpreter.

# We can also grep the ERROR/INFO messages in a pythonic way using a regular expression. Let's now write a few regular expressions using a python3 interpreter.

# Open Python shell using the command below:

python3

# This opens a Shell. Python provides a Python Shell (also known as Python Interactive Shell), which is used to execute a single Python command and get the result.

# Import the regular expression module (re).

import re
line = "May 27 11:45:40 ubuntu.local ticky: INFO: Created ticket [#1234] (username)"

# To match a string stored in line variable, we use the search() method by defining a pattern.

re.search(r"ticky: INFO: ([\w ]*) ", line)

# Output:
# <_sre.SRE_Match object; span=(29, 57), match='ticky: INFO: Created ticket '>

# You can also get the ERROR message as we did for the INFO log above from the ERROR log line.
line = "May 27 11:45:40 ubuntu.local ticky: ERROR: Error creating ticket [#1234] (username)"

# To match a string stored in a line variable, we use the search() method by defining a pattern.
re.search(r"ticky: ERROR: ([\w ]*) ", line)

# Output:
# <_sre.SRE_Match object; span=(29, 65), match='ticky: ERROR: Error creating ticket '>

# Now that you know how to use regular expressions with Python, start fetching logs of ticky for a specific username. We'll need them in later sections.