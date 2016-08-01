proc rep {molid} {
mol color Name
mol representation Lines 1.000000
mol selection all
mol material Opaque
mol addrep $molid
mol color Name
mol representation Lines 1.000000
mol selection all
mol material Opaque
mol addrep $molid
mol modstyle 0 $molid Cartoon 2.100000 24.000000 5.000000
mol modselect 1 $molid protein and not hydrogen
mol modstyle 2 $molid VDW 1.000000 12.000000
mol modselect 2 $molid name CAL
mol smoothrep $molid 2 5
mol smoothrep $molid 1 5
mol smoothrep $molid 0 5
}
