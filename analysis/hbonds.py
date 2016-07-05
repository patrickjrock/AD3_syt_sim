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
  def metric(self, psf, dcd):
    u = MDAnalysis.Universe(psf, dcd)
    data = []
    h = MDAnalysis.analysis.hbonds.HydrogenBondAnalysis(u, selection1="(resid 144:152 or resid 156:166 or resid 178:186 or resid 207:213 or resid 223:231 or resid 237:246 or resid 256:261) and protein and backbone",selection2="(resid 144:152 or resid 156:166 or resid 178:186 or resid 207:213 or resid 223:231 or resid 237:246 or resid 256:261) and protein and backbone", selection1_type="donor", distance=3.0, angle=20.0)
    h.run()

    i = 0
    for frame in h.timeseries:
      n = len(frame)
      i = i+1
      row = [i, n, os.path.basename(dcd)[:-6]]
      data.append(row)
    return data
  
  def write(self, data, filename="out.data"):
    print('frame distance label')
    for row in data:
      print(str(row[0]) + ' ' + str(row[1]) + ' ' + row[2])
