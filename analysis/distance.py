"""
Author: Patrick Rock 
Date: July 8th 2016
"""

import MDAnalysis
import MDAnalysis.analysis.distances
import sys
import os 
from base import Analysis

class Distance(Analysis):

  def get_selection(self, psf): 
    raise NotImplementedError("run not implemented")

  def metric(self, psf, dcd):
    s = self.get_selection(psf)

    u = MDAnalysis.Universe(psf, dcd)
    data = []
    i = 0
    for ts in u.trajectory:
      self.log(i)
      i = i + 1
      loop3 = u.select_atoms(s[0])
      loop1 = u.select_atoms(s[1])
      d = MDAnalysis.analysis.distances.dist(loop1, loop3)
      name = os.path.basename(dcd)[:-4].split('_')
      row = [i, d[2][0], name[0], name[1], name[2]]  # row format is [index, distance, run label]
      data.append(row)
    return data  

  def write(self, data, filename="out.data"):
    self.base_write(data, 'distance')

