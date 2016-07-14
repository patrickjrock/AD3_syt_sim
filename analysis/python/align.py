from MDAnalysis import *
from MDAnalysis.analysis.align import *
from MDAnalysis.analysis.rms import rmsd

psf = '../../structures/psf/c2a_wt.psf'
pdb = '../../structures/pdb/c2a_wt.pdb' 
dcd = '../../data/dcds/alpha10000/c2a_wt_1.dcd'

ref = Universe(psf, pdb)
mobile = Universe(psf, dcd)
alignto(mobile, ref, select="protein and name CA", mass_weighted=True)

protein = mobile.select_atoms("protein")
with MDAnalysis.Writer("protein.dcd", protein.n_atoms) as W:
  for ts in mobile.trajectory:
    W.write(protein)	
