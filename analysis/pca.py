"""
Author: Patrick Rock 
Date: July 5th 2016
"""

import MDAnalysis
import MDAnalysis.analysis.distances
import numpy as np
import sys
import os 
from base import Analysis

class pca(Analysis):
  """
  shows pca space, for each frame write out pc projections 
  """  

  def metric(self, psf, dcd):
    """
    https://gist.github.com/kain88-de/0bfe0813e27ad601004b247fedb2ee7d
    """
    u = MDAnalysis.Universe(psf, dcd)
    data = []

    ca = u.select_atoms('name CA')
    ca_xyz = np.array([ca.positions.copy() for ts in u.trajectory])
    x = ca_xyz - ca_xyz.mean(0)
    cov = np.cov(x, rowvar=0)

    e_vals, e_vecs = np.linalg.eig(cov)
    sort_idx = np.argsort(e_vals)[::-1]
    variance = e_vals[sort_idx]
    PCs = e_vecs[:, sort_idx]

    i = 0
    for pc in variance:
      i = i+1
      name = os.path.basename(dcd)[:-4].split('_')
      row = [i, pc, name[0], name[1], name[2]]
      data.append(row)
    return data 


  def write(self, data, filename="out.data"):
    print('frame  c2 mutant run')
    for row in data:
      print(str(row[0]) + ' ' + str(row[1]) + ' ' + row[2] + ' ' + row[3] + ' ' + row[4])

d = Distance()
d.prun()
