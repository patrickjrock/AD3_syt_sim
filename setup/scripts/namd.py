import sys
from jinja2 import Environment, PackageLoader

env = Environment(loader=PackageLoader('namd',''))
template = env.get_template('template.namd')
render = template.render(psf=sys.argv[1], pdb=sys.argv[2], out_name=sys.argv[3])

f = open('namd.in','w')
f.write(render)
f.close()

restart_template = env.get_template('restart_template.namd')
render2 = restart_template.render(psf=sys.argv[1], pdb=sys.argv[2], out_name=sys.argv[3])

f2 = open('restart.namd','w')
f2.write(render2)
f2.close()
