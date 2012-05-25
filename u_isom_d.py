#!/usr/bin/python

import ladr_python
import funcs
import sys
import itertools
import string

if len(sys.argv) < 1:
  sys.exit('Usage: %s semiquandles' % sys.argv[0])

sqs = ladr_python.opsInFile(open(sys.argv[1]))

i = 0
for (d, u) in sqs:
  opmatch = [ (u, d) ]
  maps = itertools.ifilter(
    lambda f: funcs.is_homom(f, opmatch),
    funcs.injections(len(opmatch[0][0]), len(opmatch[0][1])))
  i += 1
  if (u == d).all():
    print "%3i u=d" % i
  else:
    print "%3i %s" % (i, list(maps))
