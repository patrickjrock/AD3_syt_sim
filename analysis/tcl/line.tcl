mol new "/home/prock/Desktop/AD3_syt_sim/structures/psf/c2a_wt.psf"
mol addfile "/home/prock/Desktop/AD3_syt_sim/staging/cpy/dcds/c2a_wt_1.dcd"

proc drawframe {} {
  draw delete all
  
  set s1 [atomselect top "resid 234 and name CA"]
  set s2 [atomselect top "resid 173 and name CA"]

  set p1 [lindex [$s1 get {x y z}] 0] 
  set p2 [lindex [$s2 get {x y z}] 0]

  puts $p1
  puts $p2

  draw line $p1 $p2  
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

enabletrace
