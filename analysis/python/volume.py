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
import base

class Volume(Analysis):

  def get_selection(self, psf): 
    """defines the boundaries of the hull for C2A 
       versus C2B
    """
    fname = os.path.basename(psf)
    s = []
    if fname[:3] == "c2a":
      s.extend(range(171,179))
      s.append(200)
      s.extend(range(230,239))
    if fname[:3] == "c2b":
      s.extend(range(303,309))
      s.append(333)
      s.extend(range(365,371))
    return s

  def write_hull(self, h, ps):
    """write out points in hull for use by vmd"""
    out = ""
    for sim in h.simplices:
      points = [ps[sim[x]] for x in range(0,3)]
      for p in points:
        out += str(p[0]) + ' ' + str(p[1]) + ' ' + str(p[2]) + ','
      out = out[:-1] + '\n'
    print out[:-1] + ';'

  def compute_hull(self, psf, dcd):
    """used to get hull coordinates for rendering,
       this should be refactored to remove redundant code 
       in metric
    """"
    s = self.get_selection(psf)
    u = MDAnalysis.Universe(psf, dcd)
    data = []
    for i, ts in enumerate(u.trajectory): 
      points = []    
      for res in s:
        points.extend([atom.position for atom in u.select_atoms("resid " + str(res) + " and name CA")])
      hull = ConvexHull(points)
      self.write_hull(hull, points)

  def metric(self, psf, dcd):
    """measure volmue of convex hull defined by selection"""
    s = self.get_selection(psf)
    u = MDAnalysis.Universe(psf, dcd)
    data = []
    for i, ts in enumerate(u.trajectory): 
      self.log(i)
      points = []    
      for res in s:
        points.extend([atom.position for atom in u.select_atoms("resid " + str(res) + " and name CA")])
      hull = ConvexHull(points)
      name = os.path.basename(dcd)[:-4].split('_')
      row = [i, hull.volume, name[0], name[1], name[2]]
      data.append(row)
    return data

  def write(self, data, filename="out.data"):
    self.base_write(data, "volume")

v = Volume()
v.prun()
#v.compute_hull("../../structures/psf/c2a_wt.psf", "../tcl/out.dcd")
