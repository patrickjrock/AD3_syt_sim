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
    """returns resid of the amino acid
       for which chi2 is measured
    """
    fname = os.path.basename(psf)
    if fname[:3] == "c2a":
      s = (97, "CD2")
    if fname[:3] == "c2b":
      s = (98, "OD1")
    return s 

  def metric(self, psf, dcd):
    """computes the chi2 angle in the residue which 
       forms hydrogen bonds with the mutant residue
    """
    u = MDAnalysis.Universe(psf, dcd)

    resid, atom_name = self.get_selection(psf) 
    data = []
    for i, ts in enumerate(u.trajectory):
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

c = Chi()
c.prun()
