'''Circular primes
Problem 35

The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.

There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

How many circular primes are there below one million?'''

import math
import functools
import time

def is_prime(n):
	nsqrt = int(math.sqrt(n)+1)
	if n % 2 == 0: return False
	for j in range(3, nsqrt + 1, 2):
		if n % j == 0:
			return False
	return True

def is_rot_even_or_five(n):
	l = int_to_list(n)
	return 0 in l or 2 in l or 4 in l or 6 in l or 8 in l or 5 in l

def int_to_list(num):
	if num < 10:
		return [num]
	else:
		return int_to_list(num/10) + [num % 10] 

def list_to_int(l):
	return sum(l[len(l) - 1 - j] * 10**j for j in range(0,len(l)))


def rot(n):
	l = int_to_list(n)
	return {list_to_int(l[j:]+l[:j]) for j in range(0, len(l))}

start = time.time()

plist = set([p for p in range(2,1000000) if not is_rot_even_or_five(p) and is_prime(p)] + [2,5])
print(len(set(functools.reduce(lambda u, v: u | v, [rot(p) for p in plist if len(rot(p) - plist) == 0]))))

print(time.time() - start)
#print(len(set(rotlist)))