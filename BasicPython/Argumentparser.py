import argparse

# Create the parser
parser = argparse.ArgumentParser(description="A simple argument parser")

# Add the arguments
parser.add_argument('Integers', metavar='N', type=int, nargs='+',
                    help='an integer for the accumulator')
parser.add_argument('--sum', dest='accumulate', action='store_const',
                    const=sum, default=max,
                    help='sum the integers (default: find the max)')

# Parse the arguments
args = parser.parse_args()

print(args.accumulate(args.Integers))


'''
In this script:  
An ArgumentParser object is created and a description is provided.
The add_argument method is used to specify which command-line options the program is expecting. In this case, it expects a list of integers and an optional --sum argument.
The parse_args method is used to parse the command-line arguments.
The result of the accumulate function (either sum or max, depending on whether --sum was provided) applied to the list of integers is printed.
You can run this script with a list of integers as arguments. If you include the --sum option, it will print the sum of the integers. If you don't include the --sum option, it will print the maximum of the integers (which is the default behavior).
'''

'''
Test the script with the following command:
python Argumentparser.py -h
python Argumentparser.py 1 2 3 4 5
python Argumentparser.py 1 2 3 4 5 --sum

'''