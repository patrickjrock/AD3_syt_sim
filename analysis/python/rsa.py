"""
Author: Patrick Rock
Date: July 15th, 2016
TTUHSC
Credit for residue_max_acc data, Amir Shahmoradi,
"""
from Bio import *
from Bio.PDB.DSSP import *

residue_max_acc = {'A': 129.0, 'R': 274.0, 'N': 195.0, 'D': 193.0, \
                   'C': 167.0, 'Q': 225.0, 'E': 223.0, 'G': 104.0, \
                   'H': 224.0, 'I': 197.0, 'L': 201.0, 'K': 236.0, \
                   'M': 224.0, 'F': 240.0, 'P': 159.0, 'S': 155.0, \
                   'T': 172.0, 'W': 285.0, 'Y': 263.0, 'V': 174.0}

def rsa(pdb_file):
  """ calculates relative solvent accesability"""   

  d, keys = dssp_dict_from_pdb_file(pdb_file)
  
  def compute_rsa(item):
    aa_code = item[0][1][1] 
    acc =  item[1][2]
    resid = item[1][0]
    rsa = acc / residue_max_acc[resid]
    return (resid, aa_code, rsa)

  rsa_out = map(compute_rsa, d.items())
  rsa_sorted = sorted(rsa_out, key=lambda tup:tup[1])

  print "code resid rsa" 
  for t in rsa_sorted:
    print " ".join(map(str, t))

rsa("../../structures/pdb/c2a_wt.pdb")
