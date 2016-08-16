"""
Author: Patrick Rock 
Date: August 2nd 2016
"""

import MDAnalysis
import MDAnalysis.analysis.distances
import sys
import os 
from base import Analysis
import numpy as np
from prody import *

class Stiff(Analysis):

  def get_selection(self, psf): 
    raise NotImplementedError("run not implemented")

  def metric(self, psf, dcd):
    dcdf = DCDFile(dcd)
    structure = parsePSF(psf)  
    sele = structure.select('name CA')

    dcdf.setAtoms(sele)    

    eda_trajectory = EDA('trajectory')
    eda_trajectory.buildCovariance( dcdf )
    cov = eda_trajectory.getCovariance()
    for line in cov:
      # maybe write cov out to file separately for each 
      # maybe format into table with resid columns
      print line
      print ",".join(map(str, line))
    data = []

    return data  

  def write(self, data, filename="out.data"):
    self.base_write(data, 'distance')

s = Stiff()
s.run()
