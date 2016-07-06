mol new "/home/prock/Desktop/AD3_syt_sim/structures/psf/c2a_wt.psf"
mol addfile "/home/prock/Desktop/AD3_syt_sim/data/dcds/c2a_wt_1.dcd"


proc readdata {} {
  set fp [open "/home/prock/Desktop/AD3_syt_sim/data/frame.data" r]
  set data [read $fp]
  close $fp
  set data [split $data "\n"]
  return $data
}

proc drawframe {f} {
  foreach shape $f {
    set points [split $shape ","]
    set p1 [lindex $points 0]
    set p2 [lindex $points 1]
    set p3 [lindex $points 2]

    puts "points"    
    puts $points

    draw triangle $p1 $p2 $p3
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

proc drawcounter { name element op } {
    set data [readdata]
    set framenum [molinfo top get frame]   
    set fdata [lindex $data framenum]
#    puts $fdata

    global vmd_frame

    set f {}
 
    draw delete all 
    set f {}
    lappend f 0
    lappend f [molinfo top get frame]
    lappend f 0
  
    draw triangle {1 0 0} {0 1 0} {0 0 1}

}



set  d [readdata]
#set f1 [lindex $d 0]
#puts "\n\n\n"
#set f1 [split $f1 ","]
#puts [lindex [lindex $f1 0] 0]

drawframe $d


#enabletrace
