from calcium_volume import *
from prody import *
from scipy.spatial import ConvexHull


def pdb_vol(pdb, psf):
  p = parsePDB(pdb)
  c = CalciumVolume()
  s = c.get_selection(psf)
  sele = p.select(s)
  atoms = [p[i] for i in sele.getIndices()]
  coords = [a.getCoords() for a in atoms]
  hull = ConvexHull(coords)
  print len(atoms)
  print pdb + ' volume: ' + str(hull.volume)
  #import readline
  #readline.write_history_file('calcium_history')

pdb_vol('../../structures/1byn.pdb', '../../structures/psf/c2a_wt.psf')
pdb_vol('../../structures/1tjx.pdb', '../../structures/psf/c2b_wt.psf')
