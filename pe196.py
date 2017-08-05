'''Problem 196'''

from sympy import nextprime, isprime, primerange
from math import sqrt

def rowcol(n):
	r = int(round(sqrt(2*n)))
	c = n - (r*(r-1))/2
	return r,c

def numb(r,c):
	return (r*(r-1))/2 + c


def is_in_triple(n):
	adjs     = [(-1,-1), (-1,0), (-1,1), (1, -1), (1,0), (1,1)]
	
	primes   = [n]
	primeset = {n}

	while len(primes) > 0:
		m        = primes.pop(0)
		r, c     = rowcol(m)
		tocheck  = [(r+u[0], c+u[1]) for u in adjs if r+u[0] >= c+u[1] and c+u[1] >= 1 and r+u[0] >=1]
		for a,b in tocheck:
			if len(primeset) >= 3: return True
			q = numb(a,b)
			if isprime(q):
				if q not in primeset:
					primeset.add(q)
					primes.append(q)
	return len(primeset) >= 3


def S(r):
	print("row {}".format(r))

	psum = 0
	p    = nextprime((r*(r-1))/2)
	pmax = (r*(r+1))/2
	while p <= pmax:
		print("checking prime {}".format(p))
		if is_in_triple(p):
			psum += p
		p = nextprime(p)
	return psum


r1 = 5678027
r2 = 7208785



print(S(r1) + S(r2))