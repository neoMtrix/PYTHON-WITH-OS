# The Scenario
# Your coworker Jane Doe currently has the username "jane" but she needs to it to "jdoe" to comply with your company's naming policy. This username change has already been done. However, some files that were named with Jane's previous username "jane" haven't been updated. For example, "jane_profile_07272018.doc" needs to be updated to "jdoe_profile_07272018.doc".

# Navigate to data directory by using the following command:
cd data

# You can list the contents of the directory using the ls command. This directory contains a file named list.txt. You will also find some other files within this directory.

# To view the contents of the file, use the following command:
cat list.txt

# This file contains three columns: line number, username, and full path to the file.

# You could also view the complete /data directory using the ls command.
ls

# Let's try out the commands we learned in the previous section to catch all the "jane" lines.
grep 'jane' ../data/list.txt

# This returns all the files with the pattern "jane". It also matches the file that has string "janez" within it.

# Now, we'll list only the files containing the string "jane" and not include "janez".
grep ' jane ' ../data/list.txt

# This now returns only files containing the string "jane".

# Next, we'll use the cut command with grep command. For cut command, we'll use the whitespace character (‘ ‘) as a delimiter (denoted by -d) since the text strings are separated by spaces within the list.txt file. We'll also fetch results by specifying the fields using -f option.

# Let's fetch the different fields (columns) using -f flag :
grep " jane " ../data/list.txt | cut -d ' ' -f 1

grep " jane " ../data/list.txt | cut -d ' ' -f 2

grep " jane " ../data/list.txt | cut -d ' ' -f 3

# You can also return a range of fields together by using:
grep " jane " ../data/list.txt | cut -d ' ' -f 1-3

# To return a set of fields together:
grep " jane " ../data/list.txt | cut -d ' ' -f 1,3

# Test command
# We'll now use the test command to test for the presence of a file. The command test is a command-line utility on Unix-like operating systems that evaluates conditional expressions.

# The syntax for this command is:
# test EXPRESSION

# We'll use this command to check if a particular file is present in the file system. We do this by using the -e flag. This flag takes a filename as a parameter and returns True if the file exists.
# We'll check the existence of a file named jane_profile_07272018.doc using the following command:

if test -e ~/data/jane_profile_07272018.doc; then echo "File exists"; else echo "File doesn't exist"; fi

# Create a file using a Redirection operator
# We'll now use the redirection operator (>) to create an empty file simply by specifying the file name. The syntax for this is:
# > [file-name]

# Let's create a file named test.txt using the redirection operator.
> test.txt

# To append any string to the test.txt file, you can use another redirection operator (>>).
echo "I am appending text to this test file" >> test.txt

# You can view the contents of the file at any time by using the cat command.
cat test.txt

# Iteration
# Another important aspect of a scripting language is iteration. Iteration, in simple terms, is the repetition of a specific set of instructions. It's when a set of instructions is repeated a number of times or until a condition is met. And for this process, bash script allows three different iterative statements:

# For: A for loop repeats the execution of a group of statements over a set of items.
# While: A while loop executes a set of instructions as long as the control condition remains true.
# Until: An until loop executes a set of instructions as long as the control condition remains false.
# Let's now iterate over a set of items and print those items.

for i in 1 2 3; do echo $i; done