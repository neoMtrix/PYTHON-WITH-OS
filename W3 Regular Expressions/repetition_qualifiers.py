# In plain English, you could read this RegEx as match pi followed by any number of other characters followed by n. But with our dot star combination we expanded the range of the match to the whole word. See how the dot takes a different value for each letter? Let's try a different string, Python programming. What do you think the pattern will match?
# You might not have been expecting that. Remember, the Star takes as many characters as possible. In programming terms, we say that this behavior is greedy. It's possible to modify the repetition qualifiers to make them less greedy. But we won't get into that now. To learn more about that, check out the next reading. But back to our example. While our pattern could have matched the word Python, it expanded all the way until the last n in the string.

import re

print(re.search(r"Py.*n", "Pygmalion"))
print(re.search(r"Py.*n", "Python Programming"))


# Some implementations like the one used by grep only include the store qualifier that we just discussed. You can do a lot with just a star qualifier. So that's usually good enough. Other implementations like the one used by Python or by the Egrep command include two additional repetition qualifiers plus and question mark, that can help us construct more complex expressions. Let's check that out. The plus character(+) matches one or more occurrences of the character that comes before it. So we had the pattern O plus L plus. Let's check it against a few words.

# In this case, there was one occurrence of each. In the match pattern shows us the shortest possible matching string.
print(re.search(r"o+l+", "goldfish")) # True

# Here, there were two of each. Again, we can see the match is a whole string that matches the condition. Let's try something that doesn't match.
print(re.search(r"o+l+", "woolly")) # True

# So while our string here had an O and an L, it had another character in between them. Because of this, it doesn't match the search pattern. Does that make sense? The question mark symbol is yet another multiplier. It means either zero or one occurrence of the character before it. Let's see how this works.
print(re.search(r"o+l+", "boil")) # False

# The question mark symbol is yet another multiplier. It means either zero or one occurrence of the character before it. Let's see how this works.

# The P wasn't present but with the question mark we marked it as optional. So we still got a match. Let's see what happens when the P is present.

print(re.search(r"p?each", "To each their own"))
