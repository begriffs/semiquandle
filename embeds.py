#!/usr/bin/python

import itertools
import numpy
import math
import sys
import re
import string

def injections(M, N):
  return itertools.permutations(range(N), M)

def op(ar):
  edge = round(math.sqrt(len(ar)))
  return numpy.reshape(ar, [edge, edge])

def is_homom(f, opmatch):
  for (l, r) in opmatch:
    for (a, b) in itertools.product(range(len(l)), range(len(l))):
      if f[l[a][b]] != r[f[a]][f[b]]:
        return False
  return True

def embeddings(opmatch):
  return itertools.ifilter(
      lambda f: is_homom(f, opmatch),
      injections(len(opmatch[0][0]), len(opmatch[0][1])))

def embeds(opmatch):
  try: embeddings(opmatch).next()
  except StopIteration: return False
  else: return True

def opsInFile(f):
  while f.readline():
    m = re.search('\[([^\]]+?)\]', f.readline())
    op1 = op(map(string.atoi, string.split(m.group(1), ',')))
    m = re.search('\[([^\]]+?)\]', f.readline())
    op2 = op(map(string.atoi, string.split(m.group(1), ',')))
    yield (op1, op2)


######################################################################


if len(sys.argv) < 3:
  sys.exit('Usage: %s smalls bigs' % sys.argv[0])

(pref1, pref2) = (sys.argv[3], sys.argv[4])

smalls = opsInFile(open(sys.argv[1]))

i = 0
for (sd, su) in smalls:
  j = 0
  i += 1
  bigs = opsInFile(open(sys.argv[2]))
  for (bd, bu) in bigs:
    j += 1
    if embeds([ (sd, bd), (su, bu) ]):
      print "\t\"%s_%i\" -> \"%s_%i\";" % (pref1, i, pref2, j)