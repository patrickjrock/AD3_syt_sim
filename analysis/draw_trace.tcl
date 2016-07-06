mol new "/home/prock/Desktop/AD3_syt_sim/structures/psf/c2a_wt.psf"
mol addfile "/home/prock/Desktop/AD3_syt_sim/data/dcds/c2a_wt_1.dcd"

proc enabletrace {} {
    global vmd_frame
    trace variable vmd_frame([molinfo top]) w drawcounter
}

proc disabletrace {} {
    global vmd_frame
    trace vdelete vmd_frame([molinfo top]) w drawcounter
}

proc drawcounter { name element op } {
    global vmd_frame
    set f {}
 
    draw delete all 
    set f {}
    lappend f 0
    lappend f [molinfo top get frame]
    lappend f 0
  
    draw triangle {1 0 0} $f {0 0 1}

}

enabletrace
