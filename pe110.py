#!/usr/bin/python3.5

'''Problem 110 - Diophantine reciprocals'''
from math import log, sqrt, inf
from sympy import nextprime, factorint
import time

#Our analysis proceeds as follows: suppose that, in the equation
#    1/x + 1/y = 1/n, or equiv, n(x+y) = xy,
#that we write x = qn, where q=r/s is rational with (r,s) = 1. Then we have y = rn/(r-s),
#and since (r,s)=1, we have (r,r-s)=1. Thus each of r,s,r-s must divide n. So the question becomes: how many 
#relatively prime pairs of divisors does n have? Now, write (using TeX notation)
#
#      n = p_1^{e_1} \cdots p_j^{e_j}.
#
#Then we know that, if r,s divide n and are relatively prime, then each p_i can divide at most one of r,s. 
#Restated, there are at most 2e_i + 1 ways to place powers of p_i in r,s: we can have p_i, p_i^2, \ldots, 
#p_i^e_i as a divisor of either r or s (but not both), or p_i divides neither r nor s. Then the number of 
#(unordered) pairs of relatively prime divisors of n is equal to D = (2e_1 + 1)(2e_2 + 1) \cdots (2e_j + 1).
#(This argument found at stackexchange, albeit poorly explained, both here and there.)
#There is precisely one pair r,s for which r=s; namely, r=s=1. Then the number of pairs r>=s where r,s | n and 
#(r,s)= 1 is equal to d = (D+1)/2. This does yield d = 113 when n = 1260.
#
#So we can phrase (perhaps unhelpfully) the problem as a minimization: given e_j = 0 for all but finitely many 
#j>=1, we seek to minimize q_1^{e_1} q_2^{e_2} ..., subject to d >=1001 (d as given in the previous paragraph.), #where q_j is the jth prime number (so q_1 = 2, q_2 = 3, etc.). 

def numb_from_layers(layers, primes):
	retval = 1
	for l in layers:
		for j in range(0, l):
			retval *= primes[j]
	return retval

def pairs_from_layers(layers):
	retval = (2 * len(layers) + 1)**layers[-1]
	for l in range(len(layers)-1, 0, -1):
		retval *= (2*l + 1)**(layers[l-1] - layers[l])
	return retval

def next_layer_start(layers, targ_pairs):
	m = len(layers)
	v = layers[-1]
	k = int(log(targ_pairs/pairs_from_layers(layers))/log((2*m+3)/(2*m+1))) + 1
	if k > v: k = v
	return k

def min_with_layers(targ_pairs, layers, cur_min, primes):
	while layers[0] > 0:
		while layers[-1] > 0:
			if pairs_from_layers(layers) >= targ_pairs:
				z = numb_from_layers(layers, primes)
				if z < cur_min:
					cur_min = z
				layers[-1] -= 1
			elif layers[-1] == 1 and numb_from_layers(layers, primes) > cur_min:
				while len(layers) > 2 and layers[-1] == 1:
					layers = layers[0:-1]
				layers[-1] -= 1
			else:
				layers = layers + [next_layer_start(layers, targ_pairs)]
		layers = layers[0:-1]
		layers[-1] -= 1

	return cur_min

start = time.time()

min_val    = inf
num_sols   = 4000001 #for problem 110
bound      = 2*num_sols - 1
num_primes = int(log(2*num_sols - 1)/log(3)) + 1

p = 1
mth_primes = []
while len(mth_primes) < num_primes:
	mth_primes.append(nextprime(p))
	p = mth_primes[-1]

print(min_with_layers(bound, [num_primes], min_val, mth_primes))

print(time.time() - start)