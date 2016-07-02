import MDAnalysis.analysis.distances

from MDAnalysis import *
from MDAnalysis.analysis.align import *
from MDAnalysis.analysis.rms import rmsd
from MDAnalysis.tests.datafiles import PSF, DCD, PDB_small


import sys
from scipy.spatial import ConvexHull
import os
from analysis import Analysis
import time
start_time = time.time()

class Rmsf_ana(Analysis):
  def metric(self, psf, dcd):
    u = MDAnalysis.Universe(psf, dcd)
    bb = u.select_atoms('backbone')
    
    data = []
    i = 0 
    rmsf_out = MDAnalysis.analysis.rms.RMSF(bb) 
    rmsf_out.run(start=0, stop=2000)
    for n  in rmsf_out.rmsf:
      i = i+1 
      row = [i, n, os.path.basename(dcd)[:-4]]  # row format is [index, distance, run label]
      data.append(row)
    return data

  def write(self, data, filename="out,data"):
    print ('frame rmsf label')
    for row in data:
      print(str(row[0]) + ' ' + str(row[1]) + ' ' + row[2])

r = Rmsf_ana('/home/prock/Research/namd/testdata', '/home/prock/Research/namd/structures')
r.prun()
