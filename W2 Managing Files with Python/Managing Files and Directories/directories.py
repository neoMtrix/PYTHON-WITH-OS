# WEEK 2 | Managing Files and Directories | Directories

import os

os.listdir("website")
# OUTPUT: ['images', 'index.html', 'favicon.ico']
dir = "website"
for name in os.listdir(dir):
    fullname = os.path.join(dir, name)
    if os.path.isdir(fullname):
        print("{} is a directory".format(fullname))
    else:
        print("{} is a file".format(fullname))



# This code is doing a bunch of interesting stuff but let's go through it step-by-step. First, we're defining a dir variable with the name of the directory that we want to check. This makes our code more readable and more usable. Then we're iterating through the file names returned by the os.listdir. We know from our previous execution of this function that these are just the names of the files without directory. So using os.path.join, we join the directory to each of those file names and create a String with a valid full name. Finally, we use that full name to call os.path.isdir to check if it's a directory or a file. Maybe you're wondering what's up with that join function? It seems to just add a slash between two strings. Well, the join function let's us be independent from the operating system again. In Linux and MacOS, the portions of a file are split using a forward slash. On Windows, they're split using a backslash. By using the os.path.join function instead of explicitly adding a slash, we can make sure that our scripts work with all operating systems. It's another one of those handy little tools that help us avoid errors when working on different platforms.