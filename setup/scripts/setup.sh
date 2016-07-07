#!/bin/bash
#
# Author: Patrick Rock
# Date: July 6th, 2016
#
# $2 is restraint_index
# $3 is alpha

fname=$1"_center.pdb"
pdbname=$1".pdb"
psfname=$1".psf"

echo "----calculating center of mass"
~/Research/pdbtools/pdb_centermass.py -c ./$pdbname

mv $fname dys.coor

echo "----running model_setup.tcl"
vmd -e model_setup.tcl $2 # atom index to restrain

mv dys_ionized.pdb ../$pdbname
mv dys_ionized.psf ../$psfname
mv restraint.pdb ../restraint.pdb

echo "----generating namd file"
python namd.py $psfname $pdbname $1 $3
mv namd.in ../namd.in
