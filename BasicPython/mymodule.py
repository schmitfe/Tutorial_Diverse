# mymodule.py

def function1():
    print("Function 1")

def function2():
    print("Function 2")

if __name__ == "__main__":
    # This block will be executed when the script is run directly,
    # but not when the script is imported as a module.
    function1()
    function2()

'''
The `if __name__ == "__main__"` check in Python is used to determine whether a script is being run directly or being imported as a module. 

When a Python script is run directly, the special variable `__name__` is set to `"__main__"`. Therefore, the code block under `if __name__ == "__main__"` will be executed. This is often used to write code that you only want to be executed when the script is run directly, such as a main function that coordinates the execution of the program, or for running tests for the script.

However, when a Python script is imported as a module, the `__name__` variable is set to the name of the script/module. Therefore, the code block under `if __name__ == "__main__"` will not be executed. This is useful when you want to use the functions or classes defined in the script in another script, without executing the main functionality of the script.

In the provided `mymodule.py` script, the `if __name__ == "__main__"` check is used to call `function1` and `function2` only when the script is run directly. If `mymodule.py` is imported as a module in another script (like in `another_script.py`), `function1` and `function2` will not be called until they are explicitly called in the other script.

This allows for more modular and reusable code. You can define functions or classes in a script, and then choose whether to use the script as a standalone program or as a module that provides functionalities to other scripts.
'''