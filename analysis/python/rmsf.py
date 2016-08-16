"""
Author: Patrick Rock
Date: July 5th, 2016
"""

import MDAnalysis.analysis.distances
from MDAnalysis import *
from MDAnalysis.analysis.align import *
from MDAnalysis.analysis.rms import rmsd
from MDAnalysis.tests.datafiles import PSF, DCD, PDB_small

from prody import *

import sys
from scipy.spatial import ConvexHull
import os
from base import Analysis
import time
start_time = time.time()

class Rmsf_ana(Analysis):

  def metric(self, psf, dcd):
    ensemble = parseDCD(dcd)
    structure = parsePSF(psf)  
    sele = structure.select('name CA')

    ensemble.setAtoms(sele)    
    ensemble.superpose()
    rmsf = ensemble.getRMSFs()

    data = []
    for i, val in enumerate(rmsf):
      
      name = os.path.basename(dcd)[:-4].split('_')
      resid = sele.getResnums()[i]
      
      row = [resid, val, name[0], name[1], name[2]]  # row format is [index, distance, run label]
      data.append(row)
    return data

  def write(self, data, filename="out,data"):
    print('resid rmsf c2 mutant bound run')
    for row in data:
      b = ""
      m = ""
      if "unbound" in row[3]:
        b = "unbound" 
      else:
        b = "bound"
      if "wt" in row[3]:
        m = "wt"
      else:
        m = "mutant"
      print(str(row[0]) + ' ' + str(row[1]) + ' ' + row[2] + ' ' + m + ' ' + b + ' ' + row[4])



r = Rmsf_ana()
r.run()
