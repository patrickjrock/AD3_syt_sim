from volume import Volume
from hbonds import Hbonds
from loop_distance import Loop_distance
import sys

v = Volume()
h = Hbonds()
l = Loop_distance()

sys.stdout = open('volume.data', 'w')
v,prun()
sys.stdout = open('hbonds.data', 'w')
h.prun()
sys.stdout = open('distance.data', 'w')
l.prun()
