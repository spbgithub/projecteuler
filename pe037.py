'''Truncatable primes
Problem 37

The number 3797 has an interesting property. Being prime itself, it is possible to continuously remove digits from left to right, and remain prime at each stage: 3797, 797, 97, and 7. Similarly we can work from right to left: 3797, 379, 37, and 3.

Find the sum of the only eleven primes that are both truncatable from left to right and right to left.

NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.'''

import math
import time


def is_prime(n):
	if n == 1: return False
	if n == 2: return True
	if n % 2 == 0: return False
	nsqrt = int(math.sqrt(n)+1)
	for i in range(3, nsqrt, 2):
		if n % i == 0: return False
	return True

def is_left_truncatable(n):
	exp = int(math.log10(n))
	while exp > 0:
		if not is_prime(n % 10**exp): return False
		exp = exp - 1
	return True

def is_right_truncatable(n):
	exp = int(math.log10(n))
	j = 1
	while j <= exp:
		if not is_prime(n / 10**j): return False
		j += 1
	return True 


i = 11
num_trucs = 0
sum_trucs = 0
while num_trucs < 11:
	if is_prime(i):
		if is_left_truncatable(i) and is_right_truncatable(i):
			print(i)
			sum_trucs += i
			num_trucs += 1
	i += 2
print()
print(sum_trucs)
