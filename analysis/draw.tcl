mol new "/home/prock/Desktop/AD3_syt_sim/structures/psf/c2a_wt.psf"
mol addfile "/home/prock/Desktop/AD3_syt_sim/data/dcds/c2a_wt_1.dcd"

proc draw {args} {

  set f {}
  lappend f 0
  lappend f [molinfo top get frame]
  lappend f 0
  
  graphics top triangle {1 0 0} $f {0 0 1}

  graphics delete 0
}

trace add variable ::vmd_frame(0) write draw
