import MDAnalysis
import MDAnalysis.analysis.distances
import sys
from scipy.spatial import ConvexHull
import os
from analysis import Analysis
import time
start_time = time.time()

class Volume(Analysis):
  def metric(self, psf, dcd):
    u = MDAnalysis.Universe(psf, dcd)
    i = 0
    data = []
    for ts in u.trajectory: 
      i = i+1
      points = []     
      points.append(u.select_atoms("resid 234 and name CA")[0].position)
      points.append(u.select_atoms("resid 173 and name CA")[0].position)
      points.append(u.select_atoms("resid 170 and name CA")[0].position)
      points.append(u.select_atoms("resid 176 and name CA")[0].position)
      points.append(u.select_atoms("resid 236 and name CA")[0].position)
      points.append(u.select_atoms("resid 231 and name CA")[0].position)
      hull = ConvexHull(points)
      row = [i, hull.volume, os.path.basename(dcd)[:-4]]
      data.append(row)
    return data

  def write(self, data, filename="out.data"):
    print ('frame volume label')
    for row in data:
      print(str(row[0]) + ' ' + str(row[1]) + ' ' + row[2])

v = Volume('/home/prock/Research/namd/data', '/home/prock/Research/namd/structures')
v.prun(16)

print("--- %s seconds ---" % (time.time() - start_time))

