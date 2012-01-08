# all n-tuples from elements of lst
def ntuples(lst, n):
    return zip(*[lst[i:]+lst[:i] for i in range(n)])

def forallTuples(X, u, d, axiom, n):
	for t in ntuples(X, n):
		if not axiom(u, d, *t):
			return False
	return True

def forallABExistsUniqueC(X, u, d, axiom, ignoredN):
	for t in ntuples(X, 2):
		total = 0
		for c in X:
			if axiom(u, d, *(t + (c,))):
				total += 1
		if total != 1:
			return False
	return True

def check(X, u, d, conds):
	for c in conds:
		if not c[1](X, u, d, c[0], c[2]):
			return False
	return True



##################### SEMIQUANDLE AXIOM TEST FUNCTIONS ##########################

# In the following axiom check functions, "a", "b" are elements of a semiquandle,
# with operation "u", and "d"

def ax1(u, d, a, b, c):
	return a == u(c,b)

def ax2(u, d, a, b, c):
	return a == d(c,b)

def ax3(u, d, a, b):
	P = (d(a,b) == b)
	Q = (u(b,a) == a)
	# P iff Q
	return ((not P) or Q) and ((not Q) or P)

def ax4(u, d, a, b):
	return u(d(a,b), u(b, a)) == a

def ax5(u, d, a, b):
	return d(u(a,b), d(b,a)) == a

def ax6(u, d, a, b, c):
	return u(u(a,b), c) == u(u(a, d(c,b)), u(b,c))

def ax7(u, d, a, b, c):
	return u(d(a,b), d(c, u(b,a))) == d(u(a,c), u(b, d(c,a)))

def ax8(u, d, a, b, c):
	return d(d(a, u(b,c)), d(c, b)) == d(d(a,c), b)

######################## Extra conditions which may hold ########################
def latin1(u, d, a, b, c):
	return a == u(b,c)

def latin2(u, d, a, b, c):
	return a == d(b,c)


################### Bundle thse axioms and include helper function ##############
# converts an operation table into a binary function
def t2f(t):
	return lambda a, b: t[a][b]

semiquandle = [
	[ax1, forallABExistsUniqueC, 0],
	[ax2, forallABExistsUniqueC, 0],
	[ax3, forallTuples, 2],
	[ax4, forallTuples, 2],
	[ax5, forallTuples, 2],
	[ax6, forallTuples, 3],
	[ax7, forallTuples, 3],
	[ax8, forallTuples, 3],
]

latin = [
	[latin1, forallABExistsUniqueC],
	[latin2, forallABExistsUniqueC],
]
