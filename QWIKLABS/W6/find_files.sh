# Find files using bash script
# In this section, you are going to write a script named findJane.sh within the scripts directory.

# This script should catch all "jane" lines and store them in another text file called oldFiles.txt. You will complete the script using the command we practiced in earlier sections. Don't worry, we'll guide you throughout the whole process.

# Navigate to /scripts directory and create a new file named findJane.sh.
cd ~/scripts

nano findJane.sh

# Now, add the shebang line.

# #!/bin/bash

# Create the text file oldFiles.txt and make sure it's empty. This oldFiles.txt file should save files with username "jane".

# > oldFiles.txt

# Now, search for all lines that contain the name "jane" and save the file names into a variable. Let's call this variable files, we will refer to it with that name later in the lab.
# Since none of the files present in the file list.txt are available in the file system, check if file names present in files variable are actually present in the file system. To do this, we'll use the test command that we practiced in the previous section.
# Now, iterate over the files variable and add a test expression within the loop. If the item within the files variable passes the test, add/append it to the file oldFiles.txt.
# Once you have completed writing the bash script, save the file by clicking Ctrl-o, Enter key, and Ctrl-x.

# Make the file executable using the following command:
chmod +x findJane.sh

# Run the bash script findJane.sh.
./findJane.sh

# This will generate a new file named oldFiles.txt, which consists of all the files containing the name "jane".

# Use the cat command followed by the file name to view the contents of the newly generated file.
cat oldFiles.txt
