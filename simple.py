#!/usr/bin/python

import ladr_python
import sys
from congruences import *

(down_table, up_table) = ladr_python.opsInFile(sys.stdin).next()

print down_table
print up_table

for (x, y) in itertools.combinations_with_replacement(range(len(up_table)), 2):
  if x != y:
    cong = principal_congruence(x,y, [up_table, down_table])
    if not is_trivial(cong):
      sys.exit(1)

sys.exit(0)
