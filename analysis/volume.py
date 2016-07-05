"""
Author: Patrick Rock
Date: July 5th, 2016
"""

import MDAnalysis
import MDAnalysis.analysis.distances
import sys
from scipy.spatial import ConvexHull
import os
from base import Analysis

class Volume(Analysis):

  def get_selection(self, psf): 
    fname = os.path.basename(psf)
    s = []
    if fname[:3] == "c2a":
      s.append("234")
      s.append("173")
      s.append("170")
      s.append("176")
      s.append("236")
      s.append("231")
    if fname[:3] == "c2b":
      s.append("305")
      s.append("302")
      s.append("308")
      s.append("367")
      s.append("364")
      s.append("370")
    return s

  def metric(self, psf, dcd):
    s = self.get_selection(psf)
    u = MDAnalysis.Universe(psf, dcd)
    i = 0
    data = []
    for ts in u.trajectory: 
      i = i+1
      points = []    
      for res in s:
        points.append(u.select_atoms("resid " + str(res) + " and name CA")[0].position)
      hull = ConvexHull(points)
      row = [i, hull.volume, os.path.basename(dcd)[:-4]]
      data.append(row)
    return data

  def write(self, data, filename="out.data"):
    print ('frame volume label')
    for row in data:
      print(str(row[0]) + ' ' + str(row[1]) + ' ' + row[2])

v = Volume()
v.prun()
