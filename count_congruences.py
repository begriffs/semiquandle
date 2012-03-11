#!/usr/bin/python

import ladr_python
import sys
import congruences

ops = ladr_python.opsInFile(open(sys.argv[1]))

i = 1
for (d, u) in ops:
  print "%i\t%i" % (i, len(list(congruences.congruences(u, d))))
  i += 1
