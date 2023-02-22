# instead of taking a string as a separator, you can take any regular expression as a separator. For example we may want to split a piece of text into separate sentences. To do that we need to check not only for the dots but also for question marks or exclamation marks since they're also valid sentence endings.
import re

result = re.split(r"[.?!]", "One sentence. Another one? And the last one!")
print(result)

# If we want our split list to include the elements that we're using to split the values we can use capturing parentheses like this.
result = re.split(r"([.?!])", "One sentence. Another one? And the last one!")
print(result)

# Another interesting function provided by the RE module is called sub. It's used for creating new strings by substituting all or part of them for a different string, similar to the replace string method but using regular expressions for both the matching and the replacing. 
# Let's see this in an example. So we had some logs in our system that included e-mail addresses of users and we wanted to anonymize the data by removing all the addresses. We could do that by using an expression.
result = re.sub(r"[\w.%+-]+@[\w.-]+", "[REDACTED]", "Received an email for go_nuts95@my.example.com")
print(result)
# The expression that we're using for identifying email addresses has two parts: the part before that at sign and the part after it. Check out the part that comes before the at sign. We include the alphanumeric characters represented by backslash w which includes letters, numbers, and the underscore sign as well as a dot, percentage sign, plus, and dash. After the at sign, we only allow the alphanumeric characters dot and dash. This will match all email addresses as well as some strings that aren't really valid email addresses like an address with two dots.

# Let's now look at an example using sub where we use regular expressions for the replacing. For that, we'll go back to our code that switched the order of names of people and use sub to create the new string.
result = re.sub(r"^([\w .-]*), ([\w .-]*)$", r"\2 \1", "Lovelace, Ada")
print(result)
# So once again we'd use parentheses to create capturing groups. In the first parameter, we've got an expression that contains the two groups that we want to match: one before the comma and one after the comma. We want to use a second parameter to replace the matching string. We use backslash two to indicate the second captured group followed by a space and backslash one to indicate the first captured group. When referring to captured groups, a backslash followed by a number indicates the corresponding captured group. This is a general notation for regular expressions, and it's used by many tools that support regexes, not just Python. We can also use them to match patterns that repeat themselves which use capturing groups as back references.

# We want to split a piece of text by either the word "a" or "the", as implemented in the following code. What is the resulting split list?
result = re.split(r"the|a", "One sentence. Another one? And the last one!")
print(result)