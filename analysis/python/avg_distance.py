"""
Author: Patrick Rock 
Date: July 18th 2016
"""

import MDAnalysis
import MDAnalysis.analysis.distances
import sys
import os 
from distance import Distance

class Avg_distance(Distance):

  def get_selection(self, psf): 
    fname = os.path.basename(psf)
    s1 = ""
    s2 = ""
    if fname[:3] == "c2a":
      s1 = "resid 170:176 and name CA"
      s2 = "resid 231:237 and name CA"

    if fname[:3] == "c2b":
      s1 = "resid 364:371 and name CA" 
      s2 = "resid 300:307 and name CA"
    return (s1, s2)

d = Avg_distance()
d.prun()
