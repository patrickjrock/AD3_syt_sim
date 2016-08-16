"""
Author: Patrick Rock
Date: July 4th, 2016
"""

import MDAnalysis
import MDAnalysis.analysis.hbonds
import sys
import os
from base import Analysis


class Hbonds(Analysis):
  """
  class can currently only handle C2A
  """
 
  def get_selection(self, psf): 
    fname = os.path.basename(psf)
    s = ""
    if fname[:3] == "c2a":
      s = "protein and backbone and (resid 144:152 or resid 157:166 or resid 179:186 or resid 193:194 or resid 205:212 or resid 223:231 or resid 237:246 or resid 256:261)"
    if fname[:3] == "c2b":
      s = "(resid 275:283 or resid 288:297 or resid 310:318 or resid 321:330 or resid 338:346 or resid 356:363 or resid 371:379 or resid 401:406) and protein and backbone"
    return s

  def metric(self, psf, dcd):
    u = MDAnalysis.Universe(psf, dcd)
    data = []
    s = self.get_selection(psf)
    h = MDAnalysis.analysis.hbonds.HydrogenBondAnalysis(u, selection1=s,selection2=s,selection1_type="donor", distance=3.0)
    h.run()

    i = 0
    for frame in h.timeseries:
      n = len(frame)
      i = i+1
      name = os.path.basename(dcd)[:-4].split('_')
      row = [i, n, name[0], name[1], name[2]] 
      data.append(row)
    return data
  
  def write(self, data, filename="out.data"):
    self.base_write(data, 'hbonds')

h = Hbonds()
h.prun()
