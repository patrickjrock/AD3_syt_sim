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

  def get_selection(self, psf):
    fname = os.path.basename(psf)
    if fname[:3] == "c2a":
      s = (97, "CD2")
    if fname[:3] == "c2b":
      s = (98, "ND2")
    return s 

  def metric(self, psf, dcd):
    u = MDAnalysis.Universe(psf, dcd)

    resid, atom_name = self.get_selection(psf) 
    data = []
    i = 0 
    for ts in u.trajectory:
      i = i +1
      self.log(i) 
      protein = u.select_atoms("protein")
      res = protein.residues[resid]
    
      atoms = [res['CA'], res['CB'], res['CG'], res[atom_name]] 
      chi2 = MDAnalysis.core.AtomGroup.AtomGroup(atoms) 

      chidi = Dihedral(chi2).dihedral()
      name = os.path.basename(dcd)[:-4].split('_')
      row = [i, chidi, name[0], name[1], name[2]]
      data.append(row) 
    return data

  def write(self, data):
    self.base_write(data, "chi2") 

c = Chi(base.DCD_DIRECTORY, base.PSF_DIRECTORY)
c.prun()
