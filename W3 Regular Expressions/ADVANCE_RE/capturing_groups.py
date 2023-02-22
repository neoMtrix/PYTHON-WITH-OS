# Capturing groups are portions of the pattern that are enclosed in parentheses. Let's say that we have a list of people's full names. These names are stored as last name, comma, first name. We want to turn this around and create a string that starts with the first name followed by the last name. We can do this using a regular expression with capturing groups. Let's see how this works. First we'll create a matching pattern that matches a group of letters followed by a comma, a space, and then another group of letters. To capture our groups, we'll put each group of letters between parentheses like this.
import re

result = re.search(r"^(\w*), (\w*)$", "Lovelace, Ada")
print(result)

# Because we defined two separate groups, the group method returns a tuple of two elements. 
print(result.group())

# The first element contains the text matched by the entire regular expression. Each successive element contains the data that was matched by every subsequent match group. So let's look at the element at index 0.
# That's the whole string. 
print(result[0])

# Now, the following index is correspond to each of the captured groups.
print(result[1])
print(result[2])

# So we can construct the name that we want by using these indexes.
print("{} {}".format(result[1], result[2]))

# Let's put this into a function that would do the rearranging for us. We'll start by defining a function called rearrange_name, that receives a name by parameter.
def reaarange_name(name):
    result = re.search(r"^(\w*), (\w*)$", "Lovelace, Ada")
    if result is None:
        return name
    return "{} {}".format(result[2], result[1])

reaarange_name("Lovelace, Ada")
reaarange_name("Ritchie, Dennis")


# Now, the regular expression didn't match because we used the \w character, which only matches letters. And so it didn't recognize the middle initial as part of the given name. 
reaarange_name("Ritchie, Dennis M.")

# Since we wanted to match the dot character specifically, we should have escaped the dot in the regular expression. The correct regular expression should be: "^([\w \.-]*), ([\w \.-]*)$"
# What we need to do here is add the extra characters that we want to allow in the names.
def reaarange_name(name):
    result = re.search(r"^([\w \.-]*), ([\w \.-]*)$", "Lovelace, Ada")
    if result is None:
        return name
    return "{} {}".format(result[2], result[1])

reaarange_name("Ritchie, Dennis M.")