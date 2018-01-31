"""
Author: Patrick Rock 
Date: July 8th 2016
"""

import MDAnalysis
import MDAnalysis.analysis.distances
import sys
import os 
from distance import Distance

class Loop_distance(Distance):

  def get_selection(self, psf): 
    fname = os.path.basename(psf)
    s1 = ""
    s2 = ""
    if fname[:3] == "c2a":
      s1 = "resid 234 and name CA"
      s2 = "resid 173 and name CA"

    if fname[:3] == "c2b":
      s1 = "resid 305 and name CA" 
      s2 = "resid 367 and name CA"
    return (s1, s2)

d = Loop_distance()
d.prun()
