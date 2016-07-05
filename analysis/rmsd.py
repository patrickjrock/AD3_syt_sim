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
    rmsd_out.run(start=0, stop=2000)
    
    for n  in rmsd_out.rmsd:
      i = i+1 
      row = [i, n[2], os.path.basename(dcd)[:-4]]  # row format is [index, distance, run label]
      data.append(row)
    return data

  def write(self, data, filename="out,data"):
    print ('frame rmsd label')
    for row in data:
      print(str(row[0]) + ' ' + str(row[1]) + ' ' + row[2])

r = Rmsd_ana()
r.prun()
