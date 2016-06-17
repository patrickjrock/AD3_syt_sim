set mol1 [mol new dys_ionized.pdb type pdb waitfor all]

set allatoms [atomselect top all]
$allatoms set beta 0
set fixedatom [atomselect top "backbone"]
$fixedatom set beta 1
$allatoms writepdb fix_back.ref

