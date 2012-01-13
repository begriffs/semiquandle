#################################################################
# Functions to generate all possible semiquandle operation tables
#################################################################


# Lists of length n^3 will be sliced into n-by-n matrices.
# This function creates unique lists to be sliced into
# an n-by-n matrix with entries between 0 and n-1.
# 
# Converts a number n into a list of its base-b digits.
def dec2base(n,b):
	return dec2base(n/b, b) + [n%b] if n else []

def leftzeropad(list, fullsize):
	return ([0] * (fullsize - len(list))) + list

def chunks(l, n):
    for i in xrange(0, len(l), n):
        yield l[i:i+n]

def ithNTable(n, i):
	return list(chunks(leftzeropad(dec2base(i, n), n*n), n))
