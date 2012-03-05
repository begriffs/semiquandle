import re
import string
import numpy
import math

def op(ar):
  edge = round(math.sqrt(len(ar)))
  return numpy.reshape(ar, [edge, edge])

def opsInFile(f):
  while f.readline():
    m   = re.search('\[([^\]]+?)\]', f.readline())
    op1 = op(map(string.atoi, string.split(m.group(1), ',')))
    m   = re.search('\[([^\]]+?)\]', f.readline())
    op2 = op(map(string.atoi, string.split(m.group(1), ',')))
    yield (op1, op2)
