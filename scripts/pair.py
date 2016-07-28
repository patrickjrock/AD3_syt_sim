# new row format
# resid rmsf bound mutant c2

def write_cols(wt_run, mut_run):
  for i in range(0, len(wt_run)):
    wt_line = wt_run[i]
    mut_line = mut_run[i]
    assert wt_line[0] == mut_line[0]
    assert wt_line[3] == mut_line[3]    

    resid = wt_line[0]
    rmsf_bound_wt = wt_line[1]
    rmsf_unbound_wt = wt_line[2]
    rmsf_bound_mutant = mut_line[1]
    rmsf_unbound_mutant = mut_line[2]
    c2 = wt_line[3]

    s1 = [resid, rmsf_bound_wt, 'bound', 'wt',  c2]
    s2 = [resid, rmsf_unbound_wt, 'unbound', 'wt',  c2]
    s3 = [resid, rmsf_bound_mutant, 'bound', 'mutant',  c2]
    s4 = [resid, rmsf_unbound_mutant, 'unbound', 'mutant',  c2]

    print ' '.join(s1)
    print ' '.join(s2)
    print ' '.join(s3)
    print ' '.join(s4)
 

f = open("../data/split_rmsf.data", 'r')
head = f.readline()


wt_v = [[],[],[]]
mut_v = [[],[],[]]

for l in f:
  line = l.split(" ")
  c2 = line[3] 
  mutant = line[4]
  run = int(line[5])

  if mutant == 'wt':
    wt_v[run-1].append(line)
  else:
    mut_v[run-1].append(line)
f.close()

print "resid rmsf bound mutant c2"
for i in range(0,3):
  wt_run = wt_v[i]
  for j in range(0,3):
    mut_run = mut_v[j]
    wt_a = [item for item in wt_run if item[3] == "c2a"]
    mut_a = [item for item in mut_run if item[3] == "c2a"]
    write_cols(wt_a, mut_a) 

    wt_b = [item for item in wt_run if item[3] == "c2b"]
    mut_b = [item for item in mut_run if item[3] == "c2b"]
    write_cols(wt_b, mut_b) 

