#!/usr/bin/python

import ladr_python
import sys
import funcs
import itertools

def generate(perms):
  grp = set(perms)
  while True:
    n = len(grp)
    for (a,b) in itertools.product(grp, grp):
      grp.add( funcs.compose(a,b) )
    if len(grp) == n:
      break
  return grp


ops = ladr_python.opsInFile(sys.stdin)
i = 1
for (down_table, up_table) in ops:
  up_grp = generate(map(tuple, zip(*up_table)))
  dn_grp = generate(map(tuple, zip(*down_table)))
  whole_grp = generate(up_grp.union(dn_grp))
  print [sys.argv[1] + "_" + str(i), len(up_grp), len(dn_grp), len(whole_grp)]
  i += 1


