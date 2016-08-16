"""
Author: Patrick Rock 
Date: July 8th 2016
"""

import MDAnalysis
import MDAnalysis.analysis.distances
import sys
import os 
from distance import Distance

class Muta_distance(Distance):

  def get_selection(self, psf): 
    fname = os.path.basename(psf)
    s1 = ""
    s2 = ""
    if fname[:3] == "c2a":
      s1 = "resid 237 and name CA"
      s2 = "resid 180 and name CA"

    if fname[:3] == "c2b":
      s1 = "resid 370 and name CA" 
      s2 = "resid 311 and name CA"
    return (s1, s2)

m = Muta_distance()
m.prun()
