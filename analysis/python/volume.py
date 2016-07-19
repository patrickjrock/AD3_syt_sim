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
    raise NotImplementedError("get_selection not implemented")

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
       selection is broken 
    """
    s = self.get_selection(psf)
    u = MDAnalysis.Universe(psf, dcd)
    data = []
    for i, ts in enumerate(u.trajectory): 
      points = []    
      points.extend([atom.position for atom in u.select_atoms(s)])
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
      points.extend([atom.position for atom in u.select_atoms(s)])
      hull = ConvexHull(points)
      name = os.path.basename(dcd)[:-4].split('_')
      row = [i, hull.volume, name[0], name[1], name[2]]
      data.append(row)
    return data

  def write(self, data, filename="out.data"):
    self.base_write(data, "volume")

#v.compute_hull("../../structures/psf/c2a_wt.psf", "../tcl/out.dcd")
