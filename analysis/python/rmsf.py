"""
Author: Patrick Rock
Date: July 5th, 2016
"""

import MDAnalysis.analysis.distances
from MDAnalysis import *
from MDAnalysis.analysis.align import *
from MDAnalysis.analysis.rms import rmsd
from MDAnalysis.tests.datafiles import PSF, DCD, PDB_small


import sys
from scipy.spatial import ConvexHull
import os
from base import Analysis
import time
start_time = time.time()

class Rmsf_ana(Analysis):
  s = 806

  def metric(self, psf, dcd):
    u = MDAnalysis.Universe(psf, dcd)
    bb = u.select_atoms('backbone and name CA')
    protein = u.select_atoms('protein')    
    data = []
    i = 0 
    rmsf_out = MDAnalysis.analysis.rms.RMSF(bb) 
    rmsf_out.run(start=self.s, stop=2000)
   
    for i, val in enumerate(rmsf_out._rmsf):

      name = os.path.basename(dcd)[:-4].split('_')

      resid = protein.residues[i].resid

      row = [resid, val, name[0], name[1], name[2]]  # row format is [index, distance, run label]
      data.append(row)
    return data

  def write(self, data, filename="out,data"):
    print('resid rmsf c2 mutant run')
    for row in data:
      print " ".join(map(str, row))


r = Rmsf_ana()
r.prun()
