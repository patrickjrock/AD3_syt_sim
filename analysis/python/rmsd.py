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

class Rmsd_ana(Analysis):
  def metric(self, psf, dcd):
    u = MDAnalysis.Universe(psf, dcd)
    bb = u.select_atoms('backbone')
    
    data = []
    i = 0 
    rmsd_out = MDAnalysis.analysis.rms.RMSD(u) 
    rmsd_out.run()
    
    for n  in rmsd_out.rmsd:
      i = i+1 
      name = os.path.basename(dcd)[:-4].split('_')
      row = [i, n[2], name[0], name[1], name[2]]  # row format is [index, distance, run label]
      data.append(row)
    return data

  def write(self, data, filename="out,data"):
    print ('frame rmsd c2 mutant run')
    for row in data:
      print(str(row[0]) + ' ' + str(row[1]) + ' ' + row[2] + ' ' + row[3] + ' ' + row[4])

r = Rmsd_ana()
r.run()
