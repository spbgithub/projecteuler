'''Consecutive prime sum
Problem 50

The prime 41, can be written as the sum of six consecutive primes:
41 = 2 + 3 + 5 + 7 + 11 + 13

This is the longest sum of consecutive primes that adds to a prime below one-hundred.

The longest sum of consecutive primes below one-thousand that adds to a prime, contains 21 terms, and is equal to 953.

Which prime, below one-million, can be written as the sum of the most consecutive primes?'''

import math

def make_prime_list(lower_bound, upper_bound):
	ret_val = []
	ind = [True]*(upper_bound + 1)
	for num in range(2, (upper_bound/2)+1):
		for j in range(2*num, upper_bound, num):
			ind[j] = False
	for num in range(2, upper_bound):
		if ind[num] and num >= lower_bound:
			ret_val.append(num)
	return ret_val

def is_prime(num, ps):
	return num in ps

p_target = 0
count_primes = 0
pmax = 1000000
plist = make_prime_list(2,pmax)
pset = set(plist) #for lookups

for n in range(0, len(plist)):
	if n % 5000 == 0:
		print(n)
	psum = plist[n]
	for j in range(n+1, min(n + 1000,len(plist))):
		psum += plist[j]
		if is_prime(psum, pset):
			if j + 1 - n > count_primes:
				count_primes = j + 1 - n
				p_target = psum
print(count_primes, p_target)

