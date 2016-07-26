"""
Author: Patrick Rock 
Date: July 28th 2016
WARNING: this file contains prody
"""

import sys
import os 
from base import Analysis
from prody import *
from MDAnalysis import *

class SplitRMSF(Analysis):
  """ split a trajectory by bound/unbound state and compute RMSF of each 
      MSD = (1/t)*sum( (x(t)-mean(x))**2 )
  """
  def get_bound_vector(self, psf, dcd):
    u = Universe(psf, dcd)
    return [self.bound(u) for ts in u.trajectory]

  def metric(self, psf, dcd):
    traj = Trajectory(dcd)
    structure = parsePSF(psf)  
    traj.link(structure)    

    boundv = self.get_bound_vector(psf, dcd)

    bound_coors = Ensemble()
    unbound_coors = Ensemble()
    for i, frame in enumerate(traj):
      self.log(i)
      frame.superpose()
      if boundv[i]:
        bound_coors.addCoordset(structure.select('name CA').getCoords())
      else:     
        unbound_coors.addCoordset(structure.select('name CA').getCoords())

    rmsf_bound = bound_coors.getMSFs()
    rmsf_unbound = unbound_coors.getMSFs()

    data = []
    for i in range(0,len(rmsf_bound)):
      
      name = os.path.basename(dcd)[:-4].split('_')
      resid = structure.select('name CA').getResnums()[i]
      
      row = [resid, rmsf_bound[i], rmsf_unbound[i], name[0], name[1], name[2]]  # row format is [index, distance, run label]
      data.append(row)
    return data

  def write(self, data, filename="out.data"):
    print('resid rmsf_bound rmsf_unbound c2 mutant run')
    for row in data:
      print(str(row[0]) + ' ' + str(row[1]) + ' ' + str(row[2]) + ' ' + row[3] + ' ' + row[4] + ' ' + row[5])

b = SplitRMSF()
b.prun()
