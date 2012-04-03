#!/usr/bin/python

import ladr_python
import sys
from congruences import *

(down_table, up_table) = ladr_python.opsInFile(sys.stdin).next()

for (x, y) in itertools.combinations_with_replacement(range(len(up_table)), 2):
  princ_up = principal_congruence(x,y, up_table)
  princ_down = principal_congruence(x,y, down_table)
  if (princ_up == princ_down) and not is_trivial(princ_up):
    sys.exit(1)

sys.exit(0)
