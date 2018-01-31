"""
Author: Patrick Rock
Date: July 17th, 2016
"""

import MDAnalysis
import MDAnalysis.analysis.hbonds
import sys
import os
from base import Analysis
import numpy

class CrossCorr(Analysis):
  """
  """
 
  def metric(self, psf, dcd):
    u = MDAnalysis.Universe(psf, dcd)
    data = []

    # each column contains the xyzs for each residue
    res_xyz = []
 
    protein = u.select_atoms("protein")
    for i, ts in enumerate(u.trajectory):
      res_xyz.append([])
      for res in protein.residues: 
        res_xyz[i].extend(res['CA'].position)     

    corr = numpy.corrcoef(res_xyz) 
    for res1 in range(0, len(corr)):
      for res2 in range(0, len(corr[0])): 
        name = os.path.basename(dcd)[:-4].split('_')
        row = [res1, res2, corr[res1][res2], name[0], name[1], name[2]] 
        data.append(row)
    os.remove(align_file)
    return data
  
  def write(self, data, filename="out.data"):
    print "res1 res2 corr c2 mutant run"   
    for row in data:
      print " ".join(map(str, row))


c = CrossCorr()
c.prun()
