# We can change this default using the process called redirection. Redirection is a process of sending a stream to a different destination.

# This process is provided to us by the operating system and can be really useful when you want to store the output of a command in a file, instead of just looking at it on a screen. To redirect the standard output of a program to a file we use the greater than symbol. For example, take the following Python program, which just prints a single line of text using the print function.
cat stdout_example.py
./ stdout_example.py
# If we run this program without redirection the text will be sent to the display using the STD out normally.

# But now if we use a greater than character to redirect the output instead something else happens entirely.
./ stdout_example.py > new_file.txt
cat new_file.txt
# When you run it this way the STD out from stdout_example.py script is redirected to a file called new_file.txt. If that file doesn't exist, it's created. Let's look at the contents new_file.txt using the cat command.
# You see that? The output of our program ended up in the file that we wrote after the greater than symbol. Beware, just like we saw earlier with the w file mode used by the open function each time we perform of redirection of STD out, the destination is overwritten.

# So we need to be super careful when using this redirection that we're not overwriting a file with valuable contents. If we want to append the redirected standard out to a file we can use the double greater than sign instead of single greater than. Isn't that great?
./ stdout_example.py >> new_file.txt
cat new_file.txt

# In a similar way we can also redirect standard input. Instead of using the keyboard to send data into a program, we can use the less than symbol to read the contents of a file.

# Let's try this out with a new version of the streams.py file that we saw in an earlier video.
cat streams_err.py
# Okay. Now let's redirect the contents of our new file to this script.
./streams_err.py < new_file.txt
# Awesome, in this case, we don't see the input on the screen in the STDIN portion. This is expected because the input was read from a file. So it only appears in the STDOUT portion where we see that it read one of the two lines. This is also expected because the input function only reads until it encounters a new line character. It can also be useful to redirect STD_err or to capture errors and diagnostic messages from a program.

# This can be done by using the character combination 2> than similar to how we redirected STD out before. Let's execute our stream example again, this time redirecting the err output to a separate file.

# So this time we don't see the error message on the screen. That's because we redirected it to the error file. Let's see if we can find any goodies in the contents of that file.
./streams_err.py < new_file.txt 2> error_file.txt
cat error_file.py
# Aha, there's our error. If you're wondering about the number 2, it represents the file descriptor of the SCD Err stream. In this context you can think of a file descriptor as a kind of variable pointing to an IO resource. In this case the STD Err stream. 0 and 1 are the file descriptors for SCDIN and SCDOUT. Like we call it out already. None of this is exclusive the python we can operate in the same way with all other commands. For example We can create a file using the echo command and redirecting its output to the file that we want to create.
echo "These are contents of the file" > myamazingfile.txt
cat myamazingfile.txt
# Boom and as usual, we can see the contents of our new file using our friend cat.

