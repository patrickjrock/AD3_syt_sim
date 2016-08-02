#!/bin/bash
#----------------------------------------------------
# Example SLURM job script to run mpi applications
# on TACC's Lonestar 5 system.
#
# Example of MPI job submission to normal queue
#----------------------------------------------------
#SBATCH -J namd_job	   			# Job name
#SBATCH -o namd_job.o%j				# Name of stdout output file
#SBATCH -e namd_job.o%j 			# Name of stderr output file
#SBATCH -p normal	        		# Queue name
#SBATCH -N 8            			# Total number of nodes requested
#SBATCH -n 196 	 	        		# Total number of mpi tasks requested (24cores/node)
#SBATCH -t 30:00:00       			# Run time (hh:mm:ss) - 1.5 hours
#SBATCH --mail-user=patrick.rock@ttuhsc.edu     # Address email notifications
#SBATCH --mail-type=all                         # Email at begin and end of job
#SBATCH -A AD3-mutations-of-Syn   	  	# <-- Allocation name to charge job against

# This example will run 196 MPI tasks on 8 nodes

# Launch the hybrid application using ibrun
#ibrun ./my_mpi

module load namd/2.10
ibrun namd2 namd.in > namd.out

#Note:  ibrun does not bind tasks or threads by default
#       To bind task/threads to sockets or cores, you should use
#       ibrun with tacc_affinity.
#Note:  If you use this script with other queues please note the 
#       different number of cores per node in each.
