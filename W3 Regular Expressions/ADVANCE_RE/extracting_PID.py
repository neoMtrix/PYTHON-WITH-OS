# The first character of the pattern is the backslash, which is used as the escape character. This means that the next character, which is a square bracket here, is treated literally for matching purposes. After the square bracket, comes the first parentheses. Since it isn't escaped, we know it'll be used as a capturing group. The capturing group parentheses are wrapping the backslash d+ symbols. From our discussion of special characters and repetition qualifiers, we know that this expression will match one or more numerical characters. After the closing parentheses of the capturing group, we have the closing square bracket symbol, also proceeded by the escape character. After calling the search function, we know that because we're capturing groups in an expression, we can access the matching data by accessing the value at index 
import re

log = "July 31 07:05:51 mycomputer bad_process[12345]: ERROR Performing package upgrade"
regex = r"\[(\d+)\]"
result = re.search(regex, log)

print(result[1])

# Let's try our expression on a different string and check that it really works, no matter what the rest of the text is.
result = re.search(regex, "A completely different string that also has number [34567]")
print(result[1])

# But what if our string didn't actually have a block of numbers between the square brackets?
result = re.search(regex, "99 elephant in a [cage]")
print(result[1])
# Darn, an error, what happened? We tried to access the index 1 of a variable that was none. As Python tells us, this isn't something that we can do.

# So what should we do instead? We should have a function that extracts the process ID or PID when possible, and does something else if not. It's something like this; will start by defining a function called extract_pid.
def extract_pid(log_line):
    regex = r"\[(\d+)\]"
    result = re.search(regex, log_line)
    if result is None:
        return ""
    return result[1]
# We can now test our function with the original log line to check that it still does the right thing.
print(extract_pid(log))

# Nice, let's wrap this up by trying it out with a string that broke our code before.
print(extract_pid("99 elephant in a [cage]"))