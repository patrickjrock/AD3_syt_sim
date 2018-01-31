"""
Author: Patrick Rock
Date: July 5th, 2016
"""

import MDAnalysis
import MDAnalysis.analysis.distances
import sys
from scipy.spatial import ConvexHull
import os
from base import Analysis
import base

class LoopVolume(Volume):

  def get_selection(self, psf): 
    """defines the boundaries of the hull for C2A 
       versus C2B
    """
    fname = os.path.basename(psf)
    s = ""
    if fname[:3] == "c2a":
      s = 'resid 171:179 or resid 200 or resid 230:239'
    if fname[:3] == "c2b":
      s = 'resid 303:309 or resid 333 or resid 365:371' 
    return s

v = LoopVolume()
v.prun()
#v.compute_hull("../../structures/psf/c2a_wt.psf", "../tcl/out.dcd")
