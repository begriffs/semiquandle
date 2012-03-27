#!/usr/bin/python

import itertools
import sys

def injections(M, N):
  return itertools.permutations(range(N), M)

def surjections(M, N):
  if M < N:
    raise "Range too big to create a surjection"
  return itertools.ifilter(
      lambda f: len(set(f)) == N,
      itertools.product(range(N), repeat=M))

def is_homom(f, opmatch):
  for (l, r) in opmatch:
    for (a, b) in itertools.product(range(len(l)), range(len(l))):
      if f[l[a][b]] != r[f[a]][f[b]]:
        return False
  return True

def embeddings(opmatch):
  return itertools.ifilter(
      lambda f: is_homom(f, opmatch),
      injections(len(opmatch[0][0]), len(opmatch[0][1])))

def epimorphisms(opmatch):
  return itertools.ifilter(
      lambda f: is_homom(f, opmatch),
      surjections(len(opmatch[0][0]), len(opmatch[0][1])))

def embeds(opmatch):
  try: embeddings(opmatch).next()
  except StopIteration: return False
  else: return True

def mapsonto(opmatch):
  try: epimorphisms(opmatch).next()
  except StopIteration: return False
  else: return True

def cycles(perm):
  remain = set(perm)
  result = []
  while len(remain) > 0:
    n = remain.pop()
    cycle = [n]
    while True:
      n = perm[n]
      if n not in remain:
        break
      remain.remove(n)
      cycle.append(n)
    result.append(cycle)
  return result
