# -*- coding: utf-8 -*-
"""
Created on Fri Dec 25 15:04:07 2015

@author: sean
"""
from sympy import divisors, isprime
from num_theo import make_prime_list

def sigma(n, primes, pset, sigs):
	if n == 0: return 0
	if sigs[n] > 0: return sigs[n]
	if n in pset:
		sigs[n] = 1
		return sigs[n]
	for p in primes:
		if n % p == 0:
			d = 1
			w = n
			while w % p == 0:
				w = w / p
				d = d * p
			sigs[n] = sigs[d]*sigs[w]
			break
	return sigs[n]

BOUND = 1000000

#primes = make_prime_list(BOUND)
#pset = set(primes)

#amicable[n] records -1 if n hasn't been tested yet, 0 if it isn't part of a qualifying amicable chain, and a pair (l,s) where l is the length of the chain and s is the smallest member of said chain if n is part of a chain
amicable = [-1]*(BOUND+1) 
sigs     = [0]*(BOUND + 1)

#every multiple of n, starting with 2n, has n as a divisor. we just use a sieve method
#to do this all ahead of time
for n in xrange(1, BOUND + 1):
	for m in xrange(2*n, BOUND+1, n):
		sigs[m] += n

for n in xrange(2, BOUND + 1):
	if n % 10000 == 0: print(n)
	if amicable[n] == -1:
		div_chain = [n]
		s = n
		while True:
			s = sigs[s]
			if s > BOUND or s < n:
				amicable[n] = 0
				break
			try:
				if div_chain.index(s) == 0:
					l = len(div_chain)
					m = min(div_chain)
					while len(div_chain) > 0:
						amicable[div_chain.pop()] = (l, m)
				else:
					amicable[n] = 0
				break
			except ValueError:
				div_chain.append(s)
am2 = sorted([u for u in amicable if type(u) is tuple])
print(am2[-1])