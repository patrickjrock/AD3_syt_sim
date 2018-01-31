puts "draw.tcl"

mol new "/media/prock/data/AD3_syt_sim/structures/psf/c2b_wtcalbound.psf"
#mol addfile "/home/prock/Desktop/AD3_syt_sim/staging/cpy/dcds/c2a_wt_1.dcd"
mol addfile "out.dcd"

proc readdata {} {
  set fp [open "/media/prock/data/AD3_syt_sim/data/calcium_hull.data" r]
  set data [read $fp]
  close $fp
  set data [split $data ";"]
  return $data
}

proc drawframe {f} {
  draw delete all
  foreach shape $f {
    if {$shape != {}} {
      set points [split $shape ","]
      set p1 [lindex $points 0]
      set p2 [lindex $points 1]
      set p3 [lindex $points 2]
   
      draw triangle $p1 $p2 $p3
    } 
  }
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
    set framedata [split $framedata "\n"]

    drawframe $framedata
}

graphics 0 materials on
graphics 0 material Opaque

enabletrace

puts "done"
