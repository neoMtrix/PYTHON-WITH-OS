# Rename files using Python script
# In this section, you are going to write a Python script, changeJane.py, that takes oldFiles.txt as a command line argument and then renames files with the new username "jdoe". You will be completing the script, but we will guide throughout the section.

# Create a Python script changeJane.py under /scripts directory using nano editor.
nano changeJane.py

# Add the shebang line.

#!/usr/bin/env python3

# Now, import the necessary Python module to use in the Python script.

# import sys
# import subprocess

# The sys (System-specific parameters and functions) module provides access to some variables used or maintained by the interpreter and to functions that interact with the interpreter. The subprocess module allows you to spawn new processes, connect to their input/output/error pipes, and get their return codes.

# Continue writing the script to achieve the goal!

# Since oldFiles.txt is passed as a command line argument, it's stored in the variable sys.argv[1]. Open the file from the first argument to read its contents using open() method. You can either assign it to a variable or use a with block. Hint: traverse each line in the file using readlines() method. Use line.strip() to remove any whitespaces or newlines and fetch the old name.

# Once you have the old name, use replace() function to replace "jane" with "jdoe". This method replaces occurrences of any older substring with the new substring. The old and new substrings are passed as parameters to the function. Therefore, it returns a string where all occurrences of the old substring is replaced with the new substring.

# Syntax:
# string.replace(old_substring, new_substring)

# Now, invoke a subprocess by calling run() function. This function takes arguments used to launch the process. These arguments may be a list or a string.

# In this case, you should pass a list consisting of the command to be executed, followed by arguments to the command.

# Use the mv command to rename the files in the file system. This command moves a file or directory. It takes in source file/directory and destination file/directory as parameters. We'll move the file with old name to the same directory but with a new name.

# Syntax:
# mv source destination

# Now it must be clear. You should pass a list consisting of the mv command, followed by the variable storing the old name and new name respectively to the run() function within the subprocess module.

# Close the file that was opened at the beginning.
# f.close()

# Make the file executable using the following command:
chmod +x changeJane.py

# Run the script and pass the file oldFiles.txt as a command line argument.
./changeJane.py oldFiles.txt

# Navigate to the /data directory and use the ls command to view renamed files.
cd ~/data
ls

