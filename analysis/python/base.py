"""
This module contains the base Analysis class that all analysis modules inherit from
Author: Patrick Rock
Date: July 4th, 2016
"""
import MDAnalysis
import MDAnalysis.analysis.distances
from MDAnalysis import *
import os
from os import listdir
from multiprocessing.pool import Pool
import copy_reg
import types
import time
import sys
import numpy

#from mpi4py import MPI

C2A_DIRECTORY = '/home/prock/Desktop/AD3_syt_sim/data/dcds/c2a'
C2B_DIRECTORY = '/home/prock/Desktop/AD3_syt_sim/data/dcds/c2b'
DCD_DIRECTORY = '../../dcds'
PSF_DIRECTORY = '../../structures/psf'
PDB_DIRECTORY = '/home/prock/Desktop/AD3_syt_sim/structures/pdb'

def _pickle_method(m):
  """ Not sure what this does exactly but its needed for the thread pool
      to work. Found it in a stack overflow post.
      http://stackoverflow.com/questions/31971180/picklingerror-cant-pickle-type-function-with-python-process-pool-executor 
  """
  if m.im_self is None:
    return getattr, (m.im_class, m.im_func.func_name)
  else:
    return getattr, (m.im_self, m.im_func.func_name)

copy_reg.pickle(types.MethodType, _pickle_method)


class Analysis(object):
  """ abstract the data-managment and parallelism from analysis
      run on all pairs of dcd and psf files in directory
  """

  def __init__(self, dcdpath=DCD_DIRECTORY, psfpath=PSF_DIRECTORY):
    self.d = dcdpath
    self.p = psfpath

  def metric(self, psf, dcd):
    raise NotImplementedError("run not implemented")

  def write(self, data, filename="out.data"):
    raise NotImplementedError("write not implemented")

  def sbound(self, u, s):
    """ returns true if any atoms in selection are bound to a calcium """
    sele = u.select_atoms(s)
    calc = u.select_atoms('name CAL')
   
    dist = MDAnalysis.analysis.distances.distance_array(calc.coordinates(), sele.coordinates())
    for i, row in enumerate(dist):
      
      if any([d<2.5 for d in row]):
	return (True, i)
    return (False, -1)

  def bound(self, u, psf):
   
    fname = os.path.basename(psf)
  
    atoms1 = []
    atoms2 = []
    if fname[:3] == "c2a":
      atoms1.append('resid 172 and (name OD1 or name OD2)')      
      atoms1.append('resid 238 and (name OD1 or name OD2)')      
  #    atoms1.append('resid 232 and (name OD1 or name OD2)')      
      atoms2.append('resid 178 and (name OD1 or name OD2)')      

    if fname[:3] == "c2b":
      atoms1.append('resid 303 and (name OD1 or name OD2)')
      atoms1.append('resid 371 and (name OD1 or name OD2)')
      atoms1.append('resid 365 and (name OD1 or name OD2)')
      atoms2.append('resid 309 and (name OD1 or name OD2)')

    boundv = zip(*[self.sbound(u,sele) for sele in atoms1])
    bound1 = all(boundv[0]) and len(set(boundv[1])) == 1
    bound2 = self.sbound(u,atoms2[0])[0]
    return bound1 

  def get_bound_vector(self, psf, dcd):
    u = Universe(psf, dcd)
    v = [self.bound(u, psf) for ts in u.trajectory]
    smooth = [0,0,0,0,0] 
    for i in range(5,len(v)-5):
      smooth.append(numpy.round( numpy.mean(v[(i-5):(i+5)]) ))
    smooth.extend([0,0,0,0,0]) 
    return smooth 

  def base_write(self, data, metric_name):
    print('frame ' + metric_name + ' c2 mutant run')
    for row in data:
      print " ".join(map(str, row))

  def log(self, i):
    """ write out progress for tracking pool performance """
    if i % 100 == 0:
      sys.stderr.write("process " + str(os.getpid()) + ": at timestep " + str(i) + "\n") 
 
  def getdcds(self):
    files = listdir(self.d)
    dcdfiles = []
    for f in files:
      fname, ext = os.path.splitext(f)
      if ext == '.dcd':
        dcdfiles.append(f)
    return dcdfiles
  
  def dcdtopsf(self, dcdname):
    cut = dcdname.split('_')
    name = cut[0] + '_' + cut[1]    
    return self.p + "/" + name + ".psf"

  def dcdtopdb(self, dcdname):
    cut = dcdname.split('_')
    name = cut[0] + '_' + cut[1]    
    return PDB_DIRECTORY + "/" + name + ".pdb"

  def run(self):
    dcds = self.getdcds()
    data = []
    for dcd in dcds:
        dcdpath = self.d + "/" + dcd
        data.extend(self.metric(self.dcdtopsf(dcd), dcdpath))
    self.write(data)

  def prun(self, cores=16):
    # parallel run
    pool = Pool(cores)
    dcds = self.getdcds()
    data = []
    procs = []

    for dcd in dcds:
      dcdpath = self.d + "/" + dcd
      procs.append(pool.apply_async(self.metric, (self.dcdtopsf(dcd), dcdpath)))
    pool.close()
    pool.join()        
    
    for proc in procs:
      data.extend(proc.get())
    self.write(data)

  def mpirun(self):
    """ implrments mpi for analysis module,
        each mpi process is assigned to trajectories
        modulo its index
    """
    comm = MPI.COMM_WORLD
    rank = comm.Get_rank()
    size = comm.Get_size()
    print rank 
    print size
    data = []
    dcds = self.getdcds()
    for i in range(0, len(dcds)):
      pid = i % size 
      if pid == rank:
        dcd = dcds[i]
        dcdpath = self.d + "/" + dcd
        data.extend(self.metric(self.dcdtopsf(dcd), dcdpath))
    self.write(data)
   
#a = Analysis('/home/prock/Research/namd/data', '~/Research/namd/structures')
#a.run()
