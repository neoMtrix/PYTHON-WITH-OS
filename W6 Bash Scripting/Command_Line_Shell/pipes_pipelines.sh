# On top of the redirection to and from files that we saw in the last video, there's another powerful way to perform IO stream redirection called Piping. Using pipes, you can connect multiple scripts, commands, or other programs together into a data processing pipeline. Pipes connect the output of one program to the input of another. This means we can pass data between programs, taking the output of one and making it the input of the next. Pipes are represented by the pipe character. Using pipes is an extremely useful tool. It allows us to create new commands by combining the functionality of one command, with the functionality of another without having to store the contents in an intermediate file. So let's work on our plumbing, shall we? 
# Here's an example. Here, the output of the ls-l command is connected to the input of the less command, which is a terminal paging program.
ls -l | less
# This example can be pretty useful when you want to look at the contents of a directory containing lots of files. The list of files generated by ls is piped to less, which displays them one page at a time. We can scroll up or down using the page up, page down, or arrow keys. Once we're done looking at the files, we can quit with Q. But it doesn't have to stop there. It's possible to connect a lot more than just two programs using pipes. We'll check this out using a more elaborate example.
cat spider.txt | tr ' ' '\n' | sort | uniq -c | sort -nr | head
# That's a complex command line. Let's go through it step by step. We're first using cat to get the contents of our spider.txt file. Those contents are then sent to a command called tr, which gets its name from the word translate. It takes the characters in the first parameter, in this case, it's a space and then transform them into a character in the second parameter. In this case, it's a newline character. So basically, what we're doing is putting each word in its own separate line. Hurrah for organization. Next, we pass results to the sort command through a pipe. This command sorts results alphabetically. The sorted results are then passed to the unique command, which displays each match once, and by using a -c flag, it prefixes each unique line with a number of times it occurred. This output is passed via pipe to the sort command once more, this time, with the -nr flag, which sorts results numerically and in reverse order, from most to least hits. The output is finally passed to the head command, which prints the first 10 lines to stdl. That's a lot of process, but when you break it down, it makes lot of sense, right? The point isn't to memorize all these commands, but to know that we can pipe as many commands as we need to do exactly what we want. You can use your Python scripts and pipelines too. 
# Python can read from standard input using the stdin file object provided by the sys module. This is a file object like the one we obtained using the open function, and like your local library, this file object is already open for reading. Let's say we want to write a script that reads each line of the input and then prints a line with the first character in uppercase. To do this, we'll take advantage of the capitalize string method. It looks something like this.
cat capitalize.py
cat haiku.txt
# In this script, we're iterating over the contents of the sys.stdin file. Remember, that when we iterate a file object, we go through it line by line. For each of the lines of a file, we first use the strip method to remove the newline character at the end, then capitalize method to make the first character of the line uppercase, and then we print it out to standard output. Now, let's use a script to capitalize a file that we have in our computer called Haiku.txt. Let's see the contents of it using cat.

# Shakespeare couldn't have said it better. Now, let's use a pipeline to capitalize our haiku by combining the output of a cat command with our capitalized script.
cat haiku.txt | ./capitalize.py

# The cat command sends the contents of a Haiku.txt file to standard output, which we redirect to our script using a pipe. Our capitalized script uses the sys stdin file object to iterate through each line of standard input, printing the capitalized version to standard output. It's truly poetic, isn't it? We should also call out that we don't need to use a pipe to get the contents of the Haiku.txt file into standard input of our script. Instead, we use the redirection operator we saw in the last video like this.
./capitalize.py < haiku.txt
# As a rule, if you just need to get something from standard input into your script, using a redirection is enough. But if you want this to be part of a bigger pipeline of commands, you'll need to combine them with pipes. For example, if we only want to capitalize the lines that match a certain pattern, we could first call grip and then connect it with the pipe to our scripts. With a little practice, creating pipelines is a fast and powerful way to perform lots of system administration tasks. When a system command doesn't exist with the functionality that you need, you can write a Python script to fill in the gap and include it in your pipeline. Understanding how to redirect IO streams can come in handy in many situations and when writing code too. We'll see plenty of more examples of this down the pipe. Get it? Pipe? Okay, sorry. Up next, we'll dive into the different ways we can send signals to the running processes on our computer.