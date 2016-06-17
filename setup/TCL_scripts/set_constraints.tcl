set mol1 [mol new dys_ionized.coor type pdb waitfor all]

set all [atomselect top "all"]
set sel [atomselect top "name CA and residue 226"]

$all set beta 0.0
$sel set beta 1.0

$all writepdb restraint_pro.pdb 
