"""
This module contains the base Analysis class that all analysis modules inherit from
Author: Patrick Rock
Date: July 4th, 2016
"""
import MDAnalysis
import os
from os import listdir
from multiprocessing.pool import Pool
import copy_reg
import types
import time
import sys

C2A_DIRECTORY = '/home/prock/Desktop/AD3_syt_sim/data/dcds/c2a'
C2B_DIRECTORY = '/home/prock/Desktop/AD3_syt_sim/data/dcds/c2b'
DCD_DIRECTORY = '/home/prock/Desktop/AD3_syt_sim/data/dcds'
PSF_DIRECTORY = '/home/prock/Desktop/AD3_syt_sim/structures/psf'

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

  def base_write(self, data, metric_name):
    print('frame ' + metric_name + ' c2 mutant run')
    for row in data:
      print(str(row[0]) + ' ' + str(row[1]) + ' ' + row[2] + ' ' + row[3] + ' ' + row[4]) 

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
    cut = dcdname[:-6]    
    return self.p + "/" + cut + ".psf"

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
   
#a = Analysis('/home/prock/Research/namd/data', '~/Research/namd/structures')
#a.run()
