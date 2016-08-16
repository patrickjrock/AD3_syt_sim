import MDAnalysis
import numpy as np
import sys

u = MDAnalysis.Universe(sys.argv[1], sys.argv[2])
p = u.selectAtoms("protein")

p_avg = np.zeros_like(p.positions)

# do a quick average of the protein (in reality you probably want to remove PBC and RMSD-superpose)
for ts in u.trajectory:
    p_avg += p.positions
p_avg /= len(u.trajectory)

# temporarily replace positions with the average
p.set_positions(p_avg)

# write average protein coordinates
p.write(sys.argv[3])
