import MDAnalysis
import MDAnalysis.analysis.distances
import sys
from scipy.spatial import ConvexHull

# arg1 is psf file
# arg2 is dcd file


def hull_volume(psf, dcd):
  u = MDAnalysis.Universe(psf, dcd)
  i = 0
  vol = []
  for ts in u.trajectory: 
    points = []     
    points.append(u.select_atoms("resid 234 and name CA")[0].position)
    points.append(u.select_atoms("resid 173 and name CA")[0].position)
    points.append(u.select_atoms("resid 170 and name CA")[0].position)
    points.append(u.select_atoms("resid 176 and name CA")[0].position)
    points.append(u.select_atoms("resid 236 and name CA")[0].position)
    points.append(u.select_atoms("resid 231 and name CA")[0].position)
    hull = ConvexHull(points)
    vol.append(hull.volume)
  return vol

print "computing wt volume"
v1 = hull_volume("../structures/c2a_wt.psf", "../data/c2a_wt_1.dcd")
print "computing Y180F volume"
v2 = hull_volume("../structures/c2a_180F.psf", "../data/c2a_180F_1.dcd")
print "computing Y180N volume"
v3 = hull_volume("../structures/c2a_180N.psf", "../data/c2a_180N_1.dcd")

f = open("volume1.dat", "w")
f.write("frame volume run\n")

print "writing to file"
i = 0
for x in v1:
  i = i+1
  f.write(str(i) + ' ' + str(x) + ' ' + "wt\n")

i = 0
for x in v2:
  i = i+1
  f.write(str(i) + ' ' + str(x) + ' ' + "Y180F\n")

i = 0
for x in v3:
  i = i+1
  f.write(str(i) + ' ' + str(x) + ' ' + "Y180N\n")

f.close()
