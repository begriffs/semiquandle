#!/usr/bin/python

import ladr_python
import sys
from congruences import *

(down_table, up_table) = ladr_python.opsInFile(sys.stdin).next()

for (x, y) in itertools.combinations_with_replacement(range(len(up_table)), 2):
  up_bad = not is_trivial(principal_congruence(x,y, up_table))
  down_bad = not is_trivial(principal_congruence(x,y, down_table))
  if up_bad or down_bad:
    sys.exit(1)

sys.exit(0)
