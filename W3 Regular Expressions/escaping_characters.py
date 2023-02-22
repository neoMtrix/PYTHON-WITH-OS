import re
# Here, we wanted to match on strings that had.com in them, but we match a string with something else in it. That's not what we wanted. To match an actual dot, we need to use an Escape character, which in the case of regular expressions is a backslash character. So let's add that to our pattern.
print(re.search(r".com", "welcome"))

# By escaping the dot, it no longer matched the word Welcome, and since there's no.com in the string, it returned none. Let's try something that should actually match.
print(re.search(r"\.com", "welcome"))
print(re.search(r"\.com", "mydomain.com"))

# \w matches any alphanumeric character including letters, numbers, and underscores
print(re.search(r"\w*", "This is an example"))
print(re.search(r"\w*", "And_this_is_another"))
# There's also \d for matching digits, \s for matching whitespace characters like space, tab or new line, \b for word boundaries and a few others. 