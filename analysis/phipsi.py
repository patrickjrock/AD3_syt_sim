import MDAnalysis
from MDAnalysis.core.topologyobjects import Dihedral
from base import Analysis
import os

class Phipsi(Analysis):

  def __init__(self, psf, dcd, rid):
    super(Phipsi, self).__init__(psf,dcd)
    self.resid = rid

  def metric(self, psf, dcd):
    u = MDAnalysis.Universe(psf, dcd)
 
    data = []
    i = 0 
    for ts in u.trajectory:
      i = i +1
      protein = u.select_atoms("protein")
      res = protein.residues[self.resid]

      phi = res.phi_selection()
      phidi = Dihedral(phi).dihedral()

      psi = res.psi_selection()
      psidi = Dihedral(psi).dihedral()

      row = [i, phidi, psidi, os.path.basename(dcd)[:-4]]
      data.append(row) 
    return data


  def write(self, data, filename="out.data"):
    print('frame phi psi resid label')
    for row in data:
      print(str(row[0]) + ' ' + str(row[1]) + ' ' + str(row[2]) + ' ' + str(self.resid) + ' ' + row[3])

