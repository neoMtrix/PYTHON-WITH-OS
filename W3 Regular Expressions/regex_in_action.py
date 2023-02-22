import re
# For example, say you had a list of all the countries in the world and you want to check which of those names start and end in a.
print(re.search(r"A.*a", "Argentina"))

# Surprising maybe, this happened because we didn't specify that we wanted our patterns match the whole string. So while Azerbaijan doesn't finish with A, it does have an A in its name. So it matches our pattern. We need to make our patterns stricter by adding the beginning of a line and end of a line characters.
print(re.search(r"A.*a", "Azerbaijan"))

# By adding a dollar sign to our pattern, we've made it clear that we only want to match lines that begin and end with the letter a. So Azerbaijan doesn't match anymore.
print(re.search(r"A.*a$", "Azerbaijan"))

# Using regular expressions, we can also construct a pattern that would validate if the string is a valid variable name in Python.
# We said it needs to start with a letter. So we'll start with circumflex to indicate that we wanted to start from the beginning, and now a character class with all lowercase and uppercase letters plus the underscore.
# The rest of the variable can have as many numbers letters or underscores that we want. So we needed another character class this time containing numbers with a star at the end.
#  One last thing, we want this to be the end of the string that we're matching. Otherwise, we could match something that could be a variable, but that also contains additional stuff after it. So we finish up with a dollar sign.
pattern = r"^[a-zA-Z_][a-zA-Z0-9_]*$"
print(re.search(pattern, "_this_is_a_valid_variable_name"))

# Once we use a space, it stops being a valid variable name. It doesn't matter pattern because spaces aren't included in the possible characters.
print(re.search(pattern, "this isn't a valid variable name"))

# we can use numbers inside the variable name. Our pattern includes all numbers as part of the variable
print(re.search(pattern, "my_variable1"))

# The variable the number at the beginning isn't a valid variable name. In our pattern doesn't match it because the first of two character classes doesn't include numbers.
print(re.search(pattern, "1my_variable"))

