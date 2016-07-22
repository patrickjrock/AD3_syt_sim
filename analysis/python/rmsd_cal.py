"""
Author: Patrick Rock
Date: July 5th, 2016
"""

import MDAnalysis.analysis.distances
from MDAnalysis import *
from MDAnalysis.analysis.align import *
from MDAnalysis.analysis.rms import rmsd
from MDAnalysis.tests.datafiles import PSF, DCD, PDB_small

import sys
from scipy.spatial import ConvexHull
import os
from base import Analysis
import time
start_time = time.time()

class Rmsd_cal(Analysis):

  def get_pdb(self, psf): 
    fname = os.path.basename(psf)
    if fname[:3] == "c2a":
      return "/home/prock/Desktop/AD3_syt_sim/structures/pdb/c2a_bound.pdb"
    if fname[:3] == "c2b":
      return "/home/prock/Desktop/AD3_syt_sim/structures/pdb/c2b_bound.pdb"
    raise Exception('unreachable')

  def get_selection(self, psf): 
    fname = os.path.basename(psf)
    if fname[:3] == "c2a":
      s = "(resid 170:176 and name CA)"
      s = s + " or (resid 231:237 and name CA)"
      return s
    if fname[:3] == "c2b":
      s = "(resid 364:371 and name CA)" 
      s = s +"or (resid 300:307 and name CA)"
      return s
    raise Exception('unreachable')

  def metric(self, psf, dcd):
    u = MDAnalysis.Universe(psf, dcd)
    ref = MDAnalysis.Universe(self.get_pdb(psf))    
    s = self.get_selection(psf)

    data = []
    for i, ts in enumerate(u.trajectory):
      self.log(i)
      rmsd_val = rmsd(u.select_atoms(s).positions, ref.select_atoms(s).positions, superposition=True)
      name = os.path.basename(dcd)[:-4].split('_')
      row = [i, rmsd_val, name[0], name[1], name[2]]  # row format is [index, distance, run label]
      data.append(row)
    return data

  def write(self, data, filename="out,data"):
    print ('frame rmsd c2 mutant run')
    for row in data:
      print(str(row[0]) + ' ' + str(row[1]) + ' ' + row[2] + ' ' + row[3] + ' ' + row[4])

r = Rmsd_cal()
r.prun()
