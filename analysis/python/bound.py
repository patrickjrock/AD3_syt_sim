"""
Author: Patrick Rock 
Date: July 27th 2016
"""

import MDAnalysis
import MDAnalysis.analysis.distances
import sys
import os 
from base import Analysis
import numpy as np

class Bound(Analysis):

  def metric(self, psf, dcd):

    u = MDAnalysis.Universe(psf, dcd)
    boundv = self.get_bound_vector(psf, dcd)

    data = [] 
    for i, frame in enumerate(boundv): 
      self.log(i)
      name = os.path.basename(dcd)[:-4].split('_')
      row = [i, frame, name[0], name[1], name[2]]  # row format is [index, distance, run label]
      data.append(row)
    return data  

  def write(self, data, filename="out.data"):
    self.base_write(data, 'bound')

b = Bound()
b.prun()
