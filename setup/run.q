#!/bin/bash
#$ -cwd
#$ -V
#$ -S /bin/bash
#$ -N aMD_wt_C2A
#$ -j y
#$ -o wt3.log
#$ -e wt3.err
#$ -q normal
#$ -pe fill 84
#$ -P hrothgar

# Command to run

unset SGE_ROOT

ldd /lustre/work/apps/NAMD_2.9b3_Source/Linux-x86_64-icc/namd2

/lustre/work/apps/openmpi/bin/mpirun -np 84 -machinefile machinefile.$JOB_ID /lustre/work/apps/NAMD_2.9b3_Source/Linux-x86_64-icc/namd2 wt_restartAM.namd 
