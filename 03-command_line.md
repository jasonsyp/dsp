# Learn command line

Please follow and complete the free online [Command Line Crash Course
tutorial](http://cli.learncodethehardway.org/book/). This is a great,
quick tutorial. Each "chapter" focuses on a command. Type the commands
you see in the _Do This_ section, and read the _You Learned This_
section. Move on to the next chapter. You should be able to go through
these in a couple of hours.


---

Make a cheat sheet for yourself: a list of at least **ten** commands and what they do, focused on things that are new, interesting, or otherwise worth remembering.

+ **man** - Everyone's trusted friend, the help file for a given command (although replaced in popularity by everyone's new BFF Google).  
+ **pushd** and **popd** - allow you to manipulate the the directory stack.  **pushd** stores the name of the current directory for use by the **popd** command before changing the current directory to the specified directory.
+ **rmdir** - when going through the Crash Course tutorial I got an error deleting some diretories that were presumably empty.  Found out that OS X creates a hidden file (.DS_Store) to remember display options about that folder.  Need to check for hidden files (i.e. **ls -a**) before deleting a directory.  Alternatively use the options **-rf** with **rm** command to delete all fiels and folders contained in the specificed directory.
+ **mkdir** - pretty straightforward, it creates a specified directory.  The **-p** option will create an entire path even if the directories don't exist.
+ **chmod** and **chown** - change permission modifiers and ownership, respectively.  When manipulating files it is important to understand what permissions and ownership are set to ensure you have the correct access (i.e. read/write, user vs super-user) to perform operations on the specified files.
+ **env** - look at the environment variables, or when run with options set each NAME to VALUE in the environment and run the specified COMMAND.
+ **grep** - search for strings or words inside files.  Useful when used with pipes and redirection.  Can be used recursively with the **-r** option to search all files within a directory and its subdirectories.
+ To view the contents of a file, usee **less** or **cat**.  **less** is used to see the contents of a file page by page, while **cat**, which is short for concatenate, prints the content of a file or files all at once to the command line.  For small files, **cat** is a simple file reader, but for larger files, **less** is more useful.  **cat** is useful more for string-manipulation, i.e. concatenation.  You can also use **head** and **tail** commands to view **-n** specified lines of the beginning or end of a file, respectively.
+ **find** - search for files.  Using the different options and expressions you can find files by permission, users, groups, file type, date, size, etc.

---


---

What does `ls` do? What do `ls -a`, `ls -l`, and `ls -lh` do? What combinations of those flags are meaningful?

+ **'ls'** lists the contents of a directory.
+ **'ls -a'** lists all the files in a directory, including hidden files.
+ **'ls -l'** lists the contents in long format, including the file type, permissions, number of hard links, owner, group, size, last-modified date and filename.
+ **'ls -lh'** adding the **h** option prints sizes of files and directories in human readable format (i.e. 1K, 200M, 3G, etc.).  
As a matter of preference, I've typically used the **-ltr** options.  The **t** and **r** sort by modification time and reverse the order, for readability the most recently modified file appears last right above the returned command prompt.  In general, I think that having the long format is important when deciding what operations to perform.

---


---

What does `xargs` do? Give an example of how to use it.

**xargs** allows you to build and execute command lines from standard input, whereby most other commands only execute with specific arguments. 
+ Example:  find . -name '*.py' | xargs grep 'import requests'  
The above example returns the name of python files in the current directory that use the requests module.

---

