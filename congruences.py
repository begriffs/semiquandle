#!/usr/bin/python

import ladr_python
import itertools
import sys

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
