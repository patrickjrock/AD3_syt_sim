import os
from os import listdir
from multiprocessing.pool import Pool
import copy_reg
import types
import time

## do not touch, black magic

def _pickle_method(m):
    if m.im_self is None:
        return getattr, (m.im_class, m.im_func.func_name)
    else:
        return getattr, (m.im_self, m.im_func.func_name)

copy_reg.pickle(types.MethodType, _pickle_method)

## wtf is that even? ^^

class Analysis:
  # abstract the data-managment and parallelism from analysis
  # run on all pairs of dcd and psf files in directory  

  def __init__(self, dcdpath, psfpath):
    self.d = dcdpath
    self.p = psfpath

  def metric(self, psf, dcd):
    raise NotImplementedError("run not implemented")

  def write(self, data, filename="out.data"):
    raise NotImplementedError("write not implemented")

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
