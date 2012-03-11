#!/usr/bin/python

import ladr_python
import funcs
import sys

if len(sys.argv) < 3:
  sys.exit('Usage: %s bigs smalls big_prefix small_prefix' % sys.argv[0])

(pref1, pref2) = (sys.argv[3], sys.argv[4])

bigs = ladr_python.opsInFile(open(sys.argv[1]))

i = 0
for (bd, bu) in bigs:
  j = 0
  i += 1
  smalls = ladr_python.opsInFile(open(sys.argv[2]))
  for (sd, su) in smalls:
    j += 1
    if funcs.mapsonto([ (bd, sd), (bu, su) ]):
      print "\t\"%s_%i\" -> \"%s_%i\";" % (pref1, i, pref2, j)

