# submits all slurm jobs in all subdirectories

find -name "run.slurm" | xargs -L 1 -I {} sh -c 'cd "$(dirname {})"; sbatch "$(basename {})"'
