"""
Author: Patrick Rock
Date: July 6th, 2016
"""

from vmd import *
from Molecule import *
import graphics
import VMDCallback

#from volume import volume
#import base



m = Molecule()
m.load("/home/prock/Desktop/AD3_syt_sim/structures/psf/c2a_wt.psf")
m.load("/home/prock/Desktop/AD3_syt_sim/data/dcds/c2a_wt_1.dcd")


#v = Volume()
#data = v.metric("/home/prock/Desktop/AD3_syt_sim/structures/psf/c2a_wt.psf", "/home/prock/Desktop/AD3_syt_sim/data/dcds/c2a_wt_1.dcd")

#f=open('test.txt','w')
#f.close()


p1 = 1,0,0
p2 = 0,1,0
p3 = 0,0,1
current = graphics.triangle(0,p1,p2,p3)

def draw(args):
  nframes = molecule.numframes(0)
  for frame in range(1, nframes):
    graphics.delete(0, "all")
    molecule.set_frame(0, frame)
    p1 = 1,0,0
    p2 = 0,frame,0
    p3 = 0,0,1
    current = graphics.triangle(0,p1,p2,p3)


VMDCallback.add_callback('timestep', draw)
