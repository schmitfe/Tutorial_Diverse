#!/bin/bash
#SBATCH --job-name=python_job
#SBATCH --output=python_job_%j.out
#SBATCH --ntasks=1
#SBATCH --time=10:00
#SBATCH --mem-per-cpu=100


module load miniconda/py38_4.12.0
#module load module load gnu/9.4.0
#conda activate /home/fschmi69/Software/NEST3_3

export MY_ENV_VAR="Hello, World!"

python Example.py --arg $i