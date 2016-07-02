import MDAnalysis
import MDAnalysis.analysis.distances
import sys

# arg1 is psf file
# arg2 is dcd file
u = MDAnalysis.Universe(sys.argv[1], sys.argv[2])
i = 0
for ts in u.trajectory:
    loop3 = u.select_atoms("resid 234 and name CA")
    loop1 = u.select_atoms("resid 173 and name CA")
    d = MDAnalysis.analysis.distances.dist(loop1, loop3)
    i = i + 1
    print str(i) + ' ' + str(d[2][0])
