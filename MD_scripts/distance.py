import MDAnalysis
import MDAnalysis.analysis.distances
import sys

u = MDAnalysis.Universe(sys.argv[1], sys.argv[2])

for ts in u.trajectory:
  loop3 = u.select_atoms("resid 243 and name CA")
  loop1 = u.select_atoms("resid 173 and name CA")
  d = MDAnalysis.analysis.distances.dist(loop1, loop3)
  print d
