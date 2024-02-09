'''Command line arguments and environment variables are two ways of passing information to a program when it is launched. They are used for different purposes and are accessed in different ways in Python.

**Command Line Arguments**

Command line arguments are parameters that are passed to a program when it is run from the command line. In Python, command line arguments can be accessed through the `sys.argv` list. The first item in the list, `sys.argv[0]`, is the name of the script itself. The following items are the arguments passed to the script.

Here's an example of how to parse command line arguments in Python:
'''
import sys

print(f"Script name: {sys.argv[0]}")
for i, arg in enumerate(sys.argv[1:], start=1):
    print(f"Argument {i}: {arg}")

'''
In this script, `sys.argv[0]` is the name of the script, and `sys.argv[1:]` are the command line arguments passed to the script.

**Environment Variables**

Environment variables are a set of dynamic named values that can affect the way running processes behave on a computer. They are part of the environment in which a process runs. In Python, environment variables can be accessed through the `os.environ` object, which is a dictionary-like object that allows you to retrieve the values of the environment variables.

Here's an example of how to access environment variables in Python:

'''
import os
import multiprocessing

print(f"HOME: {os.environ.get('HOME')}")
print(f"PATH: {os.environ.get('PATH')}")
print(f"Self: {os.environ.get('Self', 'not set')}")

# start a new process with the environment variable
os.environ['Self'] = 'HelloWorld'
print(f"Self: {os.environ.get('Self', 'not set')}")
multiprocessing.Process(target=lambda: print(f"Self in child process: {os.environ.get('Self', 'not set')}")).start()

'''

In this script, `os.environ.get('HOME')` retrieves the value of the `HOME` environment variable, and `os.environ.get('PATH')` retrieves the value of the `PATH` environment variable.

**Use Cases**

Command line arguments are typically used to specify configuration options and parameters for a program, while environment variables are used to convey information about the system environment to the program.

For example, a script that processes a data file might take the name of the file as a command line argument, while a script that connects to a database might use an environment variable to get the connection string for the database.
'''

'''
Run in terminal and use  export Self=HelloWorld to set the environment variable. Can be also set with os.environ['Self'] = 'HelloWorld' in the script.
Enviroment variables are passed to the child processes.
'''