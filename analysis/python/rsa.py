"""
Author: Patrick Rock
Date: July 15th, 2016
TTUHSC
Credit for residue_max_acc data, Amir Shahmoradi
https://github.com/wilkelab/influenza_HA_evolution/blob/master/structure/calculate_rsa.py

Usage: python rsa.py structure.pdb
"""
from Bio import *
from Bio.PDB.DSSP import *
import sys
import os

residue_max_acc = {'A': 129.0, 'R': 274.0, 'N': 195.0, 'D': 193.0, \
                   'C': 167.0, 'Q': 225.0, 'E': 223.0, 'G': 104.0, \
                   'H': 224.0, 'I': 197.0, 'L': 201.0, 'K': 236.0, \
                   'M': 224.0, 'F': 240.0, 'P': 159.0, 'S': 155.0, \
                   'T': 172.0, 'W': 285.0, 'Y': 263.0, 'V': 174.0}

def compute_rsa(pdb_file):
  """ calculates relative solvent accesability"""   

  d, keys = dssp_dict_from_pdb_file(pdb_file)
  
  def aa_rsa(item):
    aa_code = item[0][1][1] 
    acc =  item[1][2]
    resid = item[1][0]
    rsa = acc / residue_max_acc[resid]
    return (resid, aa_code, rsa)

  rsa_out = map(aa_rsa, d.items())
  rsa_sorted = sorted(rsa_out, key=lambda tup:tup[1])



  name = os.path.basename(pdb_file).split('_')
  for t in rsa_sorted:
    line = " ".join(map(str, t))
    line = line + " " + name[0]
    line = line + " " + name[1].split('.')[0]
    print line

compute_rsa(sys.argv[1])
