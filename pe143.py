'''Problem 143'''

from math import sqrt
from fractions import gcd
import time

def sqsum(k):
	return (k*(k+1))//2

start = time.time()
MAX_VAL = 120000
M_SQRT  = int(sqrt(MAX_VAL))

list_of_pairs = {}
for m in range(2, M_SQRT + 2):
	for n in range(1, m):
		if gcd(m, n) == 1:
			p, q = sorted([m*m - n*n, 2*m*n + n*n])
			if (m - n) % 3 == 0:
				p, q = p//3, q//3
			for k in range(1, MAX_VAL//(p + q) + 1):
				if k*p not in list_of_pairs:
					list_of_pairs[k*p] = set()
				list_of_pairs[k*p].add(k*q)
print(time.time() - start)

triples = []
for p in list_of_pairs:
	for q in list_of_pairs[p]:
		if q in list_of_pairs:
			candidates = [r for r in list_of_pairs[p] & list_of_pairs[q] if p+q+r <= MAX_VAL]
			triples = triples + [p+q+r for r in candidates]

print(sum(set(triples)))
print(time.time() - start)