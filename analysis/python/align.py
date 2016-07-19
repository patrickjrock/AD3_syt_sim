"""
Author: Patrick Rock 
Date: July 5th 2016
"""

import MDAnalysis
from MDAnalysis import *
import MDAnalysis.analysis.distances
from MDAnalysis.analysis.align import *
from MDAnalysis import Universe
import numpy as np
import sys
import os 
from base import Analysis

class Align(Analysis):
  """
  shows pca space, for each frame write out pc projections 
  """  

  def metric(self, psf, dcd):
    """
    https://gist.github.com/kain88-de/0bfe0813e27ad601004b247fedb2ee7d
    """
    trj = Universe(psf, dcd)
    out_file = self.d + "/align/" + os.path.basename(dcd)
    rms_fit_trj(trj, trj, select="protein and name CA", filename=out_file)
    return []

  def write(self, data, filename="out.data"):
    return ""

a = Align()
a.prun()
