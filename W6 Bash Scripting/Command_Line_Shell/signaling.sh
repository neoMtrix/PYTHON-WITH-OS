# When dealing with the operating system, we usually have a bunch of different processes that we use to accomplish what we want. And like any well oiled machine, we generally need these processes to communicate with each other. For example, we might have a program that starts a background process and wants it to terminate after a timeout. One way of communicating this is through the pipelines we learned about in the last video. Another way of communicating is through the use of signals. Signals are tokens delivered to running processes to indicate a desired action. Using signals, we can tell a program that we want it to pause or terminate. We can also cause it to reload its configuration, or to close all open files. Knowing how to send these signals lets us interact with processes and have more control over how they behave. There are a bunch of different ways that we can send these signals. For example, let's execute the ping command in our terminal.
ping www.example.com
# The ping command is now running, sending ICMP packets to machine over the network once per second. And it will keep running forever unless we interrupt it. To do that, we can use the Ctrl-C combination.

# See how, when we interrupt it, the program doesn't just end abruptly. First it prints a summary of what it did and what the results were. It's very polite under these circumstances. What's happening behind the scenes is the process received a signal indicating that we wanted it to stop. When that signal's received, the process does whatever it needs to finish cleanly. The signal that control see sense is called SIGINT. It's just one of many signals that we can send. Another keyboard combination that we can use to send a signal is Ctrl-Z. Let's try this one out.

# So our ping is running once more, this time we'll interrupt it with Ctrl-Z.

# This time the process didn't finish properly. We get a message saying that it's stopped. What's going on? The signal that we sent is called SIGSTOP. This signal causes the program to stop running without actually terminating. But don't worry, we can make it run again by executing fg
fg
# The fg command makes our program run once more and will keep going until we interrupt it either with Ctrl-C, Ctrl-Z, or some other signal. Let's stop it now with Ctrl-C.

# By pressing Ctrl-C this time, we've made the program finish cleanly. To send other signals, we can use the command called Kill, yikes. By default, Kill will send a signal called SIGTERM that tells the program to terminate. Since Kill is a separate program, we need to run it on a separate terminal. And we also need to know the process identifier or PID of the process that we want to send the signal to. To find out the PID that we want to send the signal to, we'll use the ps command which list the currently running processes. Depending on what options that we pass, it'll show different subsets of processes with different amounts of detail. For this example, we'll call ps ax, which lists all the running processes in the current computer. And then we'll use the grep command to only keep lines that contain the name of the process that we're looking for. Sound good? Okay, let's try this out. We'll run ping on one terminal, and then find its PID and kill it from a second terminal.
ps ax | grep ping
# Cool. So our PS and grip commands found that the PID for the running ping command is 4619. We can now use this identifier to send the signal that we want using the Kill command.
kill 4619
# We've now sent the SIGTERM signal and the process was terminated. Hasta la vista process. Notice how in this case, we didn't get the nice summary at the end, the program just finished. As you might expect, there is more signals that we can send and they might cause programs to react differently. Many long running programs, for example, will reload their configuration from disk if we send them a signal. This way we can let the program know that there's an important change in the configuration and it can get applied without the program having to stop to reread it. Programs that provide web services may also receive a signal to tell them that they should finish dealing with any currently open connections and then terminate cleanly once it's done. Understanding what these signals are and how to send them will let you interact with the processes on your system that you're in charge of and make them behave as you want. Coming up, a couple of readings to put all this information in one place. We'll list all the system commands that we came across and some that we'll encounter later on. We'll also list other resources that you can use if you want to learn more. As we've said before, you don't need to memorize any of this. You'll get better by using them in our practice exercises and by experimenting on your own. To wrap this up, there'll be a quiz to let you practice your understanding of these concepts. The anticipation is killing me.