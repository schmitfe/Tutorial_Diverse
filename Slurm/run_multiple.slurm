#!/bin/bash

# Define the arguments
args=("1" "2" "3")

# Loop over the arguments
for arg in "${args[@]}"; do
    # Create a temporary Slurm script
    echo "#!/bin/bash
#SBATCH --cpus-per-task=1
#SBATCH --mem=100mb
#SBATCH --time=00:05:00
#SBATCH --account=fschmi69

module load miniconda/py38_4.12.0

export MY_ENV_VAR=\"Hello, World!\"

python Example.py --arg $arg" > temp.slurm

    # Submit the job
    sbatch temp.slurm

    # Remove the temporary Slurm script
    rm temp.slurm
done