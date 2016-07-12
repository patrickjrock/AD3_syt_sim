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
    ca_xyz = ca_xyz.reshape(u.trajectory.n_frames, ca.n_atoms * 3, order='F')
    x = ca_xyz - ca_xyz.mean(0)
    cov = np.cov(x, rowvar=0)

    e_vals, e_vecs = np.linalg.eig(cov)
    sort_idx = np.argsort(e_vals)[::-1]
    variance = e_vals[sort_idx]
    PCs = e_vecs[:, sort_idx]
    PC_projection = np.dot(x, PCs)

    projections = [PC_projection[j] for j in range(0,5)]

    for i in range(0,len(PC_projection[:, 0])):
      weights = []
      name = os.path.basename(dcd)[:-4].split('_')
      row = [i]
      for j in range(0,2):
        row.append(PC_projection[i,j]) 
      row.extend([name[0], name[1], name[2]]) 
      sys.stderr.write("adding row: " + str(row) + "\n")
      data.append(row)
    return data 

  def write(self, data, filename="out.data"):
    print('frame pc1 pc2 c2 mutant run')
    for row in data:
      print(str(row[0]) + ' ' + str(row[1]) + ' ' + str(row[2]) + ' ' + row[3] + ' ' + row[4] + ' ' + row[5])

p = pca()
p.prun()
