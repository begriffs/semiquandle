#!/usr/bin/python

import ladr_python
import sys
import funcs

(down_table, up_table) = ladr_python.opsInFile(sys.stdin).next()
down_cols = [funcs.cycles(p) for p in zip(*down_table)]
up_cols   = [funcs.cycles(p) for p in zip(*up_table)]

print "------ up ------"
for c in up_cols:
  print "   ".join(map(lambda(s): str(list(s)),  c))
print "------ down ------"
for c in down_cols:
  print "   ".join(map(lambda(s): str(list(s)),  c))
