# main.py
import argparse
# add path in docker container to import square, onla needed if run as remote interpreter
import sys
sys.path.append('/app')
from square import square

# Create the parser
parser = argparse.ArgumentParser(description="A simple script")

# Add the arguments
parser.add_argument('--arg', type=int, required=True, help='An integer argument')

# Parse the arguments
args = parser.parse_args()

# Print the square of the argument
print(square(args.arg))