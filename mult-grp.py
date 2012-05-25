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

def table(M):
  n = len(M)
  M = list(M)
  T = [[-1 for x in range(n)] for x in xrange(n)]
  for i, a in enumerate(M):
    for j, b in enumerate(M):
      T[i][j] = M.index( funcs.compose(a,b) )
  return T

def isAbelian(M):
  for a, b in itertools.combinations(M, 2):
    if funcs.compose(a,b) != funcs.compose(b,a):
      return False
  return True

ops = ladr_python.opsInFile(sys.stdin)
i = 1
for (down_table, up_table) in ops:
  up_grp = generate(map(tuple, zip(*up_table)))
  dn_grp = generate(map(tuple, zip(*down_table)))
  print "Up:"
  print ladr_python.matrixToLadr(table(up_grp), i)
  print "Abelian=" + str(isAbelian(up_grp)) + ", cycle=" + str(max([len(generate([x])) for x in up_grp]))
  print "Dn:"
  print ladr_python.matrixToLadr(table(dn_grp), i)
  print "Abelian=" + str(isAbelian(dn_grp)) + ", cycle=" + str(max([len(generate([x])) for x in dn_grp]))
  print "Wh:"
  whole_grp = generate(up_grp.union(dn_grp))
  print ladr_python.matrixToLadr(table(whole_grp), i)
  print "Abelian=" + str(isAbelian(whole_grp)) + ", cycle=" + str(max([len(generate([x])) for x in whole_grp]))

  #print ladr_python.matrixToLadr(table(whole_grp), i)
  #print [sys.argv[1] + "_" + str(i), len(up_grp), len(dn_grp), len(whole_grp)]
  i += 1
