#!/bin/bash
#SBATCH --cpus-per-task=1
#SBATCH --mem=100mb
#SBATCH --time=00:05:00
#SBATCH --account=fschmi69

module load miniconda/py38_4.12.0
#module load module load gnu/9.4.0
#conda activate /home/fschmi69/Software/NEST3_3

export MY_ENV_VAR="Hello, World!"

python Example.py --arg 5