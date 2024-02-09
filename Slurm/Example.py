import argparse
import os

# Create the parser
parser = argparse.ArgumentParser(description="A simple script")

# Add the arguments
parser.add_argument('--arg', type=int, required=True, help='An integer argument')

# Parse the arguments
args = parser.parse_args()

# Get the environment variable
env_var = os.getenv('MY_ENV_VAR')

# Print the square of the argument and the environment variable
print(f"Square of the argument: {args.arg ** 2}")
print(f"Environment variable: {env_var}")

# get SLURM environment variables
JobID = os.environ.get('SLURM_JOB_ID', '0')
ArrayID = os.environ.get('SLURM_ARRAY_TASK_ID', '0')

# print the SLURM environment variables
print(f"SLURM job ID: {JobID}")
print(f"SLURM array task ID: {ArrayID}")
