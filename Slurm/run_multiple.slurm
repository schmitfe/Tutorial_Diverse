#!/bin/bash

# Define the arguments
args=("1" "2" "3")

# Loop over the arguments
for arg in "${args[@]}"; do
    # Create a temporary Slurm script
    echo "#!/bin/bash
#SBATCH --job-name=python_job
#SBATCH --output=python_job_%j.out
#SBATCH --cpus-per-task=1
#SBATCH --time=10:00
#SBATCH --mem-per-cpu=100
#SBATCH --partition=smp-rh7

module load miniconda/py38_4.12.0

export MY_ENV_VAR=\"Hello, World!\"

python Example.py --arg $arg" > temp.slurm

    # Submit the job
    sbatch temp.slurm

    # Remove the temporary Slurm script
    rm temp.slurm
done