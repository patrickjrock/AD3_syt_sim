import MDAnalysis
import MDAnalysis.analysis.distances
import sys
import os 
from analysis import Analysis


class Distance(Analysis):
  def metric(self, psf, dcd):
    u = MDAnalysis.Universe(psf, dcd)
    data = []
    i = 0
    for ts in u.trajectory:
      i = i + 1
      loop3 = u.select_atoms("resid 234 and name CA")
      loop1 = u.select_atoms("resid 173 and name CA")
      d = MDAnalysis.analysis.distances.dist(loop1, loop3)
      row = [i, d[2][0], os.path.basename(dcd)[:-4]]  # row format is [index, distance, run label]
      data.append(row)
    return data  

  def write(self, data, filename="out.data"):
    #f = open(filename, "w")
    print('frame distance label')
    for row in data:
      print(str(row[0]) + ' ' + str(row[1]) + ' ' + row[2])
    #f.close()


d = Distance('/home/prock/Research/namd/data', '/home/prock/Research/namd/structures')
d.prun(16)
