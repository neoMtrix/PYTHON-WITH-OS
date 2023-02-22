# What if we wanted a pattern that repeats a specific number of times? This could happen if we're processing a line that we know has some specific data in a column, or we know that we want a string of a specific length. In cases like those, we would manually write the same pattern as many times as we need it. But it would be hard to read and hard to maintain. 
# And that's why Python also offers numeric repetition qualifiers. These are written between curly brackets and can be one or two numbers specifying a range. 
# For example, to match any string of exactly five letters, we can use an expression like this one
import re

# Remember, that the expression will match whichever part of the given string that fits the criteria. In this case, we're looking for letters that are repeated five times, and ghost has five letters, so it matched our pattern.
print(re.search(r"[a-zA-Z]{5}", "a ghost"))

# In this string, we actually have more matches for our search, but we only get the first one. Remember, what we can do to find more matches? That's right, use the findall function, like this.
print(re.findall(r"[a-zA-Z]{5}", "a scary ghost appeared"))

# What if we wanted to match all the words that are exactly five letters long? We can do that using \b, which matches word limits at the beginning and end of the pattern, to indicate that we want full words, like this
print(re.findall(r"\b[a-zA-Z]{5}\b", "a scary ghost appeared")) 


# We said that we can also have two numbers in the range. For example, if we wanted to match a range of five to ten letters or numbers, we could use an expression like this one.
print(re.findall(r"\w{5, 10}", "I really like strawberries")) 
# A number followed by a comma means at least that many repetitions with no upper boundary limited only by the maximum repetitions in the source text.

# These ranges can also be open ended.s
print(re.findall(r"\w{5,}", "I really like strawberries")) 

# a comma followed by a number means from zero up to that amount of repetitions.
print(re.findall(r"s\w{,20}", "I really like strawberries")) 
# Here we look for a pattern that was an S followed by up to 20 alphanumeric characters. So we got a match for strawberries which starts with S, and is followed by 11 characters.


