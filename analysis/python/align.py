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

  def metric(self, psf, dcd):
    trj = Universe(psf, dcd)
    out_file = self.d + "/align/" + os.path.basename(dcd)
    rms_fit_trj(trj, trj, select="protein and name CA", filename=out_file)
    return []

  def write(self, data, filename="out.data"):
    return ""

a = Align()
a.prun()
