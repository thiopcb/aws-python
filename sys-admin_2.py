import subprocess as sp
# Set lab exercise to run in the following Python codes:
print("Exercise 2: Using subprocess.run")
print("Exercise 3: Using subprocess.run with two arguments")
print("Exercise 4: Using subprocess.run with three arguments")
print("Exercise 5: Retrieving system information")
print("Exercise 6: Retrieving information about disk space")

excercise = int(input("Choose the exercise to run, select number from 2 to 6: "))


# Exercise 2: Using subprocess.run
# Though os.system() is simple to use because it takes a string argument, 
# it is recommended that you use the more powerful subprocess.run() function. 
# You can use the subprocess module to spawn new processes, connect to input/
# output/error pipes, and obtain error codes. The subprocess.run() function 
# can take many new arguments, but those additional arguments are optional.
if excercise == 2:
    sp.run(['ls'])

# Exercise 3: Using subprocess.run with two arguments
# In Python, the square brackets are list data types, which means that run() 
# can take a # list of arguments. Continue to add to the Python script.
elif excercise == 3:
    sp.run(['ls', '-l'])

# Exercise 4: Using subprocess.run with three arguments
# You will now call subprocess.run() with three arguments. The third argument 
# will be a directory name.
elif excercise == 4:
    sp.run(['ls', '-l', 'README.md'])

# Exercise 5: Retrieving system information
# The subprocess.run() function is powerful because you can use it to run any 
# Bash command. In this exercise, you will call the uname command to get system 
# information.
elif excercise == 5:
    command = "uname"
    commandArgument = "-a"
    print(f'Gathering system information with command: {command} {commandArgument}')
    sp.run([command, commandArgument])

# Exercise 6: Retrieving information about disk space
# To emphasize that subprocess.run() allows you to run any command, you will run 
# the df command to get disk information.
elif excercise == 6:
    command = "ps"
    commandArgument = "-x"
    print(f'Gathering active process information with command: {command} {commandArgument}')
    sp.run([command,commandArgument])

else:
    print("No lad exercise selected. End of line.")