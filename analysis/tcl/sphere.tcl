mol new "/home/prock/Desktop/AD3_syt_sim/structures/psf/c2a_Y180F.psf"
mol addfile "/home/prock/Desktop/AD3_syt_sim/data/dcds/alpha200/c2a_Y180F_1.dcd"


proc readdata {} {
  set fp [open "/home/prock/Desktop/AD3_syt_sim/data/sphere_coordinates.data" r]
  set data [read $fp]
  close $fp
  set data [split $data "\n"]
  return $data
}

proc drawframe {f} {
  draw delete all
  set rd [lindex $f 0]
  set p1 [lindex $f 1]
  set p2 [lindex $f 2]
  set p3 [lindex $f 3] 
  set center [list $p1 $p2 $p3]
  
  # draw sphere {0 0 0} radius 10 
  draw sphere $center radius $rd
}

proc enabletrace {} {
    global vmd_frame
    trace variable vmd_frame([molinfo top]) w drawcounter
}

proc disabletrace {} {
    global vmd_frame
    trace vdelete vmd_frame([molinfo top]) w drawcounter
}



set data [readdata]

proc drawcounter { name element op } {
    global data
    set framenum [molinfo top get frame]   
    set framedata [lindex $data $framenum]
    set framedata [split $framedata " "]
    drawframe $framedata
}

graphics 0 materials on
graphics 0 material Transparent
enabletrace
