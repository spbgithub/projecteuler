'''Spiral primes
Problem 58

Starting with 1 and spiralling anticlockwise in the following way, a square spiral with side length 7 is formed.

37 36 35 34 33 32 31
38 17 16 15 14 13 30
39 18  5  4  3 12 29
40 19  6  1  2 11 28
41 20  7  8  9 10 27
42 21 22 23 24 25 26
43 44 45 46 47 48 49

It is interesting to note that the odd squares lie along the bottom right diagonal, but what is more interesting is that 8 out of the 13 numbers lying along both diagonals are prime; that is, a ratio of 8/13, or roughly 62%.

If one complete new layer is wrapped around the spiral above, a square spiral with side length 9 will be formed. If this process is continued, what is the side length of the square spiral for which the ratio of primes along both diagonals first falls below 10%?'''

import math

def make_prime_list(upper_bound):
	#upper_bound = 10**(int(math.log10(upper_bound)) + 1)
	lower_bound = 2
	ret_val = []
	ind = [True]*(upper_bound + 1)
	for num in range(2, (upper_bound/2)+1):
		for j in range(2*num, upper_bound, num):
			ind[j] = False
	for num in range(2, upper_bound):
		if ind[num] and num >= lower_bound:
			ret_val.append(num)
	print("Prime list made.")
	return ret_val

#doubles size of existing prime list by computing primes up to 2*max of old prime list
def extend_prime_list(plist):
	ret_val = []
	max_p = max(plist)
	ubound = 10**(int(math.log10(max_p))+2)
	ind = [True]*(ubound - max_p+1)
	for p in plist:
		start = p - max_p % p
		if start == 0:
			start += p
		for j in range(start, len(ind), p):
			ind[j] = False
	for j in range(1, len(ind)):
		if ind[j]:
			ret_val.append(max_p + j)
	print("Prime list extended.")
	return ret_val

'''def is_prime(n, pset):
	return n in pset'''

def is_prime(n):
	nsqr = int(math.sqrt(n)+1)
	if n % 2 == 0: return False
	if n % 3 == 0: return False
	i = 1
	while (6*i - 1) < nsqr:
		if n % (6*i - 1) == 0:
			return False
		if n % (6*i + 1) == 0:
			return False
		i += 1
	return True

#plist = make_prime_list(10000000)
#pset = set(plist)
diag_nums = {}
num_diag_primes = 0
#max_plist = max(plist)

ring = 1
while True:
#	if max_plist < (2*ring+1)**2:#
#		plist = plist + extend_prime_list(plist)
#		pset = set(plist)
#		max_plist = max(plist)
	for a in [-2,0,2]:
		if is_prime(4*ring*ring + a*ring + 1):
			num_diag_primes += 1
	if 10 * num_diag_primes < 4*ring + 1:
		print("Side length: " + str(2*ring+1) + "  Primes: " + str(num_diag_primes) + "   Diag elts: " + str(4*ring + 1) + "  Ratio: " + str(float(num_diag_primes)/float(4.0*ring + 1.0)))
		break
	ring += 1
print("Done!")