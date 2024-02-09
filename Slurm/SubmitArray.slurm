#!/bin/bash
#SBATCH --job-name=python_job
#SBATCH --output=python_job_%A_%a.out
#SBATCH --cpus-per-task=1
#SBATCH --time=10:00
#SBATCH --mem-per-cpu=100
#SBATCH --array=1-10

module load miniconda/py38_4.12.0
#module load module load gnu/9.4.0
#conda activate /home/fschmi69/Software/NEST3_3

export MY_ENV_VAR="Hello, World!"

python Example.py --arg $SLURM_ARRAY_TASK_ID

#In this script, #SBATCH --array=1-10 is used to create a job array with 10 tasks. The SLURM_ARRAY_TASK_ID environment variable is set to the ID of the current task in the job array, which ranges from 1 to 10.  The Python script is run with --arg $SLURM_ARRAY_TASK_ID, so the argument to the script will be the ID of the current task in the job array.  The output file name is set to python_job_%A_%a.out, where %A is replaced with the job ID and %a is replaced with the array index. This ensures that the output of each task in the job array is written to a separate file.  This will submit 10 jobs to Slurm, each with a different argument passed to the Python script.