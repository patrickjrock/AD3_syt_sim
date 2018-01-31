mol new "/home/prock/Desktop/AD3_syt_sim/structures/pdb/c2b_wtcalbound.pdb"

proc drawframe {} {
  draw delete all
  
  set s1 [atomselect top "resid 311 and name CA"]
  set s2 [atomselect top "resid 370 and name CA"]

  set p1 [lindex [$s1 get {x y z}] 0] 
  set p2 [lindex [$s2 get {x y z}] 0]

  puts $p1
  puts $p2

  draw line $p1 $p2 width 7
}

proc enabletrace {} {
    global vmd_frame
    trace variable vmd_frame([molinfo top]) w drawcounter
}

proc disabletrace {} {
    global vmd_frame
    trace vdelete vmd_frame([molinfo top]) w drawcounter
}

proc drawcounter { name element op } {
    drawframe 
}

drawframe
enabletrace
