#!/usr/bin/python

import ladr_python
import sys
import congruences

(down_table, up_table) = ladr_python.opsInFile(sys.stdin).next()

for c in congruences.congruences(up_table, down_table):
  print "   ".join(map(lambda(s): str(list(s)),  c))
