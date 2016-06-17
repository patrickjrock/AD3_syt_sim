mol load pdb c2a_wt.pdb

set sel [atomselect top all]

# cell basis vectors:
set m [measure minmax $sel]
foreach {j1 j2} $m {}
foreach {x2 y2 z2} $j2 {}
foreach {x1 y1 z1} $j1 {}
expr $x2 - $x1
expr $y2 - $y1
expr $z2 - $z1

# cellOrigin:
measure center $sel
