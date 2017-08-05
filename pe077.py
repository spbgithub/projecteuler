'''Prime summations
Problem 77

It is possible to write ten as the sum of primes in exactly five different ways:

7 + 3
5 + 5
5 + 3 + 2
3 + 3 + 2 + 2
2 + 2 + 2 + 2 + 2

What is the first value which can be written as the sum of primes in over five thousand different ways?
'''

from num_theo import get_primes_n

primes = get_primes_n()
cache  = {(2,2):1}

def parts(n, p):
	if (n, p) == (2, 2): print("hi")
	if (n, p) in cache: return cache[(n, p)]
	if n  < p:  return 0
	if n == p: return 1
	retval = 0
	for q in primes:
		if q > p:
			break
		retval += parts(n - p,q)
	cache[(n,p)] = retval
	return retval

num = 3
qty = 0
while True:
	qty = sum([parts(num, p) for p in primes if p <= num])
	if qty > 5000:
		print(num)
		break
	num +=1

