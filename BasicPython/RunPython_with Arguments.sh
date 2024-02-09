#!/bin/bash

# we want to use the python3 interpreter to run ArgumentParser.py 3 times with different arguments
# here we could also load conda and activate a specific environment

python3 BasicPython/Argumentparser.py 1 2 3 4 5
python3 BasicPython/Argumentparser.py 6 7 8 9 10 --sum