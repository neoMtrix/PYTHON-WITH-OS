import re

# We want to match the word Python but allow for both lowercase or uppercase p.
print(re.search(r"[Pp]ython", "Python"))

# We can also define a range of characters using a dash. For example, we could use lowercase a to lowercase z to state any lowercase letter. So if we wanted to look for the string way preceded by any letter
print(re.search(r"[a-z]way", "The end of the highway"))

# We can define more ranges like upper case A to upper case Z for all upper case letters or 0 to 9 for all digits. 
print(re.search("cloud[a-zA-Z0-9]", "cloudy"))
print(re.search("cloud[a-zA-Z0-9]", "cloud9"))

# Sometimes we may want to match any characters that aren't in a group. To do that, we use a circumflex inside the square brackets. For example, let's create a search pattern that looks for any characters that's not a letter.
print(re.search(r"[^a-zA-Z]", "This is a sentence with spaces."))

# What if we also add a space to the list of characters that we don't want to match?
print(re.search(r"[^a-zA-Z ]", "This is a sentence with spaces."))

# If we want to match either one expression or another, we can use the pipe symbol to do that. This lets us list alternative options that can get matched. For example, we could have an expression that matches either the word cat or the word dog, like this.
print(re.search(r"cat|dog", "I like cats."))
print(re.search(r"cat|dog", "I like dogs."))
print(re.search(r"cat|dog", "I like cats and dogs."))

# If we want to get all possible matches, we can do that using the findall function
print(re.findall(r"cat|dog", "I like cats and dogs."))


