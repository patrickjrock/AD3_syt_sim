"""
Author: Patrick Rock
Date: July 6th, 2016
"""

import MDAnalysis
import MDAnalysis.analysis.distances
import sys
import os
from base import Analysis
import base
import math
import numpy as np

class Sphere(Analysis):
  """ Computes the minum bounding sphere of 4 CAs in the calcium binding pocket.
  """

  def get_selection(self, psf): 
    fname = os.path.basename(psf)
    s = []
    if fname[:3] == "c2a":
      s = [173, 234, 230, 200] 
    if fname[:3] == "c2b":
      s = [305, 333, 367, 363]
    return s

  def sphere_volume(self, points):
    """ find furthest points => diameter 
    """ 
    m1 = -1   
    m2 = -1
    d = -1
    for i in range(0,4):
      for j in range(0,4):
        dist = np.linalg.norm(points[i]- points[j])
        if dist > d:
          d = dist
          m1 = i
          m2 = j
    vol = (4/3)*math.pi*(d/2)**3 
    ctr = (points[m1] + points[m2])/2
    rad = d/2
    return (vol, ctr, rad)

  def write_sphere(self, psf, dcd):
    """ not the moset elegant way to do this, 
        try to do this by implementing a writer
        subclass in the future.
    """
    s = self.get_selection(psf)
    u = MDAnalysis.Universe(psf, dcd)
    i = 0
    data = []
    for ts in u.trajectory: 
      self.log(i) 
      i = i+1
      points = []    
      for res in s:
        points.extend([atom.position for atom in u.select_atoms("resid " + str(res) + " and name CA")])
      svol, ctr, rad = self.sphere_volume(points)
      print str(rad) + ' ' + str(ctr[0]) + ' ' + str(ctr[1]) + ' ' + str(ctr[2]) 

  def metric(self, psf, dcd):
    s = self.get_selection(psf)
    u = MDAnalysis.Universe(psf, dcd)
    i = 0
    data = []
    for ts in u.trajectory: 
      self.log(i) 
      i = i+1
      points = []    
      for res in s:
        points.extend([atom.position for atom in u.select_atoms("resid " + str(res) + " and name CA")])
      svol, ctr, rad = self.sphere_volume(points)
      name = os.path.basename(dcd)[:-4].split('_')
      row = [i, svol, name[0], name[1], name[2]]
      data.append(row)
    return data

  def write(self, data, filename="out.data"):
    self.base_write(data, "volume")

s = Sphere("/home/prock/Desktop/AD3_syt_sim/staging/cpy/dcds")
s.prun()
