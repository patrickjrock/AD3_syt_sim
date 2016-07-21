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
from volume import Volume

class CalciumVolume(Volume):

  def get_selection(self, psf): 
    """defines the boundaries of the hull for C2A 
       versus C2B
       do not run on C2B
    """
    fname = os.path.basename(psf)
    s = "empty"
    if fname[:3] == "c2a":
      s = '(resid 171 and name O)'
      s = s + ' or (resid 172 and (name OD2 or name OD1))'
      s = s + ' or (resid 178 and name OD2)'
      s = s + ' or (resid 230 and (name OD1 or name OD2))'
      s = s + ' or (resid 232 and (name OD1 or name OD2))'
      s = s + ' or (resid 238 and (name OD1 or name OD2))'
      s = s + ' or (resid 236 and name O)'
      s = s + ' or (resid 235 and name OG)'
      s = s + ' or (resid 231 and name O)'
    if fname[:3] == "c2b":
      s = '(resid 302 and name O)'
      s = s + 'or (resid 303 and (name OD2 or name OD1))'
      s = s + 'or (resid 309 and name OD1)'
      s = s + 'or (resid 364 and name O)'
      s = s + 'or (resid 365 and (name OD2 or name OD1))'
      s = s + 'or (resid 363 and (name OD2 or name OD1))'
    return s

v = CalciumVolume()
v.prun()
#v.compute_hull("../../structures/psf/c2b_wt.psf", "../../data/dcds/control/c2b_wt_1.dcd")
