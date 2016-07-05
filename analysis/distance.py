"""
Author: Patrick Rock 
Date: July 4th 2016
"""

import MDAnalysis
import MDAnalysis.analysis.distances
import sys
import os 
from base import Analysis

class Distance(Analysis):

  def get_selection(self, psf): 
    fname = os.path.basename(psf)
    s1 = ""
    s2 = ""
    if fname[:3] == "c2a":
      s1 = "resid 234 and name CA"
      s2 = "resid 173 and name CA"

    if fname[:3] == "c2b":
      s1 = "resid 305 and name CA" 
      s2 = "resid 367 and name CA"
    return (s1, s2)

  def metric(self, psf, dcd):
    s = self.get_selection(psf)

    u = MDAnalysis.Universe(psf, dcd)
    data = []
    i = 0
    for ts in u.trajectory:
      i = i + 1
      loop3 = u.select_atoms(s[0])
      loop1 = u.select_atoms(s[1])
      d = MDAnalysis.analysis.distances.dist(loop1, loop3)
      name = os.path.basename(dcd)[:-4].split('_')
      row = [i, d[2][0], name[0], name[1], name[2]]  # row format is [index, distance, run label]
      data.append(row)
    return data  

  def write(self, data, filename="out.data"):
    print('frame distance c2 mutant run')
    for row in data:
      print(str(row[0]) + ' ' + str(row[1]) + ' ' + row[2])

d = Distance()
d.prun()
