#!/usr/bin/python

import ladr_python
import sys
import funcs
import itertools

ops = ladr_python.opsInFile(sys.stdin)
i = 1
for (down_table, up_table) in ops:
  every_a_good = True
  for a in range(len(down_table)):
    for c in range(len(down_table)):
      this_c_good = True
      for b in range(len(down_table)):
        if down_table[a,b] != up_table[c, up_table[a, b]]:
          this_c_good = False
          break
      if this_c_good == True:
        print "found a -> c = %i %i" % (a,c)
        break
    if this_c_good == False:
      every_a_good = False
      break
  if every_a_good == True:
    print "***** %i good\n" % (i)
  else:
    print "%i bad\n" % (i)
  i += 1
