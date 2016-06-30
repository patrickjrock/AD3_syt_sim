#!/bin/bash
# first argument is directory where to place new build
# second argumnet is path to pdb file

echo "----copying setup into new location"
cp -r ~/Desktop/AD3_syt_sim/setup $1
echo "----copying pdb file into script directory"
cp $2 $1/scripts
cd $1/scripts/
echo "----running setup.sh"
sh $1/scripts/setup.sh c2b_wt
echo "----done"
