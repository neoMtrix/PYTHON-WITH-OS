# We call the search function on the re module, and told it to use the pattern aza on the string plaza.

import re 

result = re.search(r"aza", "plaza")

# Our result is a match object. The output we get when calling print already shows some interesting information, like the position in the string that matched ,and what the actual matching string was.
print(result)

# r | rawstring
# r at the beginning of the pattern indicates that this is a rawstring. This means that Python interpreter shouldn't try to interpret any special characters, and instead, should just pass the string to the function as is. In this example, there are no special characters.

# The rawstring and the normal string are exactly the same, but it's a good idea to ALWAYS USE RAWSTRINGS FOR REGULAR EXPRESSIONS in Python.

result = re.search(r"aza", "plaZa")
print(result)

# if we want our match to be case insensitive, we can do this by passing the re.IGNORECASE option.