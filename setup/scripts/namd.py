import sys
from jinja2 import Environment, PackageLoader

env = Environment(loader=PackageLoader('namd',''))
template = env.get_template('template.namd')
render = template.render(psf=sys.argv[1], pdb=sys.argv[2], out_name=sys.argv[3], alpha=sys.argv[4])

f = open('namd.in','w')
f.write(render)
f.close()
