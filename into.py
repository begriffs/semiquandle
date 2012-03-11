#!/usr/bin/python

import ladr_python
import funcs
import sys

if len(sys.argv) < 3:
  sys.exit('Usage: %s smalls bigs small_prefix big_prefix' % sys.argv[0])

(pref1, pref2) = (sys.argv[3], sys.argv[4])

smalls = ladr_python.opsInFile(open(sys.argv[1]))

i = 0
for (sd, su) in smalls:
  j = 0
  i += 1
  bigs = ladr_python.opsInFile(open(sys.argv[2]))
  for (bd, bu) in bigs:
    j += 1
    if funcs.embeds([ (sd, bd), (su, bu) ]):
      print "\t\"%s_%i\" -> \"%s_%i\";" % (pref1, i, pref2, j)

