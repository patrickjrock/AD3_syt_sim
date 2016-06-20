import MDAnalysis
import MDAnalysis.analysis.hbonds
import sys

def p(e):
  if e[4].split(':')[0] == e[5].split(':')[0]:
    return False
  return True

u = MDAnalysis.Universe("c2a_wt.psf", "run1.dcd")
#beta_sheets = u.select_atoms("(resid 144:152 or resid 156:166 or resid 178:186 or resid 207:213 or resid 223:231 or resid 237:246 or resid 256:261) and protein and backbone")
h = MDAnalysis.analysis.hbonds.HydrogenBondAnalysis(u, selection1="(resid 144:152 or resid 156:166 or resid 178:186 or resid 207:213 or resid 223:231 or resid 237:246 or resid 256:261) and protein and backbone",selection2="(resid 144:152 or resid 156:166 or resid 178:186 or resid 207:213 or resid 223:231 or resid 237:246 or resid 256:261) and protein and backbone", selection1_type="donor", distance=3.0, angle=20.0)
h.run()

i = 0
for frame in h.timeseries:
    n = len(filter(p, frame))
    i = i+1
    print str(i) + ' ' + str(n)
