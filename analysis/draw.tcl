mol new "/home/prock/Desktop/AD3_syt_sim/structures/psf/c2a_wt.psf"
mol addfile "/home/prock/Desktop/AD3_syt_sim/data/dcds/c2a_wt_1.dcd"

global data

proc readdata{} {
  set fp [open "/home/prock/Desktop/AD3_syt_sim/data/hull_coordinates.data" r]
  set data [read $fp]
  close $fp
  set data [split $data "\n\n"]
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
    puts $data
    global vmd_frame

    set f {}
 
    draw delete all 
    set f {}
    lappend f 0
    lappend f [molinfo top get frame]
    lappend f 0
  
    draw triangle {1 0 0} {0 1 0} {0 0 1}

}
readdata()
enabletrace
