'''Problem 108 - Diophantine reciprocals'''
from math import log, sqrt
from sympy import nextprime
from functools import reduce
from sympy import factorint

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

def rel_pairs(n):
	npairs = factorint(n)
	return reduce(lambda u, v: u*v, map(lambda z: 2*npairs[z] + 1, npairs))

def x(t, p):
	return 1.0/(2*t*log(p)) - (1./2.)

num_sols   = 1001 #for problem 108
bound      = 2*num_sols - 1
num_primes = int(log(2*num_sols - 1)/log(3)) + 1
print(num_primes)
p = 1
primes_to_keep = []
while len(primes_to_keep) < num_primes:
	primes_to_keep.append(nextprime(p))
	p = primes_to_keep[-1]

nmax  = reduce(lambda u, v: u*v, primes_to_keep)
print(nmax)
tstar = float(bound) * reduce(lambda u,v: u * v, map(log, primes_to_keep))
tstar = 1.0/tstar**(1.0/num_primes)
nmin  = int(reduce(lambda u, v: u*v, map(lambda u: u**x(tstar, u), primes_to_keep)))

nums_to_check = set(range(nmin, nmax + 1))
while p < sqrt(nmax):
	p = nextprime(p)
	for j in range(nmin//p, nmax//p + 1):
		nums_to_check.discard(p*j)

nums_to_check = sorted(list(nums_to_check))
for n in nums_to_check:
	if rel_pairs(n) >= bound:
		print(n)
		break
