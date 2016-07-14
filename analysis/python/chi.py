"""
Author: Patrick Rock
Date: July 14th, 2016
"""

import MDAnalysis
from MDAnalysis.core.topologyobjects import Dihedral
import base
from base import Analysis
import os

class Chi(Analysis):

  def __init__(self, psf, dcd, rid):
    super(Chi, self).__init__(psf,dcd)
    self.resid = rid

  def metric(self, psf, dcd):
    u = MDAnalysis.Universe(psf, dcd)
 
    data = []
    i = 0 
    for ts in u.trajectory:
      i = i +1
      self.log(i) 
      protein = u.select_atoms("protein")
      res = protein.residues[self.resid]
    
      atoms = [res['CA'], res['CB'], res['CG'], res['ND1']] 
      chi2 = MDAnalysis.core.AtomGroup.AtomGroup(atoms) 

      chidi = Dihedral(chi2).dihedral()
      name = os.path.basename(dcd)[:-4].split('_')
      row = [i, chidi, name[0], name[1], name[2]]
      data.append(row) 
    return data

  def write(self, data):
    self.base_write(data, "chi2") 

c = Chi(base.DCD_DIRECTORY, base.PSF_DIRECTORY, 97)
c.prun()
