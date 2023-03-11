# Set lab exercise to run in the following Python codes:
"""
    Example how to run this Python script:
    sys-admin.py README.md
"""
moduleOS = True

# Exercise 1: Using os.system
# Python has several modules to allow you to run Bash commands from Python. 
# In this exercise, you will use os.system() to run the Bash command ls, 
# which shows the directory contents.
if moduleOS == True:
    import os
    os.system('ls')

# Exercise 2: Using subprocess.run
# Though os.system() is simple to use because it takes a string argument, 
# it is recommended that you use the more powerful subprocess.run() function. 
# You can use the subprocess module to spawn new processes, connect to input/
# output/error pipes, and obtain error codes. The subprocess.run() function 
# can take many new arguments, but those additional arguments are optional.
else:
    import subprocess as sp
    sp.run(['ls'])
