'''Totient permutation
Problem 70'''

from num_theo import unserialize_prime_list, get_primes_n, num_to_digs
from permutations import is_perm
from math import sqrt

pouter = get_primes_n()
pinner = [] + pouter

pouter = [p for p in pouter if p > int(sqrt(10**7))]
pinner = [p for p in pinner if p > 2 and p < int(sqrt(10**7))+1]

min_ratio = 10**7
min_n     = 10**7

for p in pouter:
	if p < int(sqrt(10**7)): break
	for q in pinner:
		n = p * q
		if n > 10**7: break
		phi = (p-1)*(q-1)
		#phi = compute_phi(n, plist)
		if is_perm(num_to_digs(phi), num_to_digs(n)):
			print(p,q,n,phi)
			ratio = float(n)/float(phi)
			if ratio < min_ratio:
				min_ratio = ratio
				min_n     = n
print(min_n, min_ratio)