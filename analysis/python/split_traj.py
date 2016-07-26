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
  def msd(self, matrix);
    """ compute msd of coordinate matrix """
    raise NotImplementedError("run not implemented")

  def get_bound_vector(self, psf, dcd):
    u = Universe(psf, dcd)
    return [bound(u) for ts in u.trajectory]

  def metric(self, psf, dcd):
    traj = Trajectory(dcd)
    structure = parsePSF(psf)  
    traj.link(structure)    

    boundv = self.get_bound_vector(psf, dcd)

    bound_coors = Ensemble()
    unbound_coors = Ensemble()
    for i, frame in enumerate(traj):
      frame.superpose()
      if boundv[i]:
        bound_coors.addCoordset(structure.select('name CA').getCoords())
      else:     
        unbound_coors.addCoordset(structure.select('name CA').getCoords())

    bound_coors.getMSFs()
    unbound_coors.getMSFs()

  def write(self, data, filename="out.data"):
    self.base_write(data, 'rmsf')

b = Bound()
b.prun()
