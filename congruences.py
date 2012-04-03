#!/usr/bin/python

import ladr_python
import itertools
import sys

def root(i, V):
  j = V[i]
  if j < 0:
    return i
  else:
    r = root(j, V)
    V[i] = r # collapse tree for later
    return r

def join_blocks(r, s, V):
  (nr, ns) = (-V[r], -V[s])
  if nr >= ns:
    V[s] = r
    V[r] = -(nr + ns)
  else:
    V[r] = s
    V[s] = -(nr + ns)

def principal_congruence(a, b, op):
  n = len(op)
  V = [-1]*n
  pairs = [(a,b)]
  while len(pairs) > 0:
    (x, y) = pairs.pop(0)
    (r, s) = (root(x, V), root(y, V))
    if r != s:
      join_blocks(r, s, V)
      pairs += [ (op[r,z], op[s,z]) for z in range(n) ]
      pairs += [ (op[z,r], op[z,s]) for z in range(n) ]
  print "principal(%i,%i)" % (a, b)
  print V
  print
  return V

def is_trivial(cong):
  return len([x for x in cong if x < 0]) in [1, len(cong)]

def partitions(set_):
	if not set_:
		yield []
		return
	for i in xrange(2**len(set_)/2):
		parts = [set(), set()]
		for item in set_:
			parts[i&1].add(item)
			i >>= 1
		for b in partitions(parts[1]):
			yield [parts[0]]+b

def eqrel(partn):
  def sameclass(x,y):
    for eqclass in partn:
      if (x in eqclass) and (y in eqclass):
        return True
    return False
  return sameclass

def is_congruence(r, up_table, down_table):
  dom = range(len(up_table))
  for (x, x0, y, y0) in itertools.product(dom, dom, dom, dom):
    if r(x, x0) and r(y, y0):
      if (not r(up_table[x][y], up_table[x0][y0])) or (not r(down_table[x][y], down_table[x0][y0])):
        return False
  return True

def congruences(up_table, down_table):
  dom = range(len(up_table))
  return itertools.ifilter(
      lambda p: is_congruence(eqrel(p), up_table, down_table),
      partitions(dom))
