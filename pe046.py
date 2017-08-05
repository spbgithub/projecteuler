'''Goldbach's other conjecture
Problem 46

It was proposed by Christian Goldbach that every odd composite number can be written as the sum of a prime and twice a square.

9  =  7+2x1^2
15 =  7+2x2^2
21 =  3+2x3^2
25 =  7+2x3^2
27 =  19+2x2^2
33 =  31+2x1^2

It turns out that the conjecture was false.

What is the smallest odd composite that cannot be written as the sum of a prime and twice a square?'''

import math
import functools
import time

def is_odd_prime(n):
	nsqrt = int(math.sqrt(n)+1)
	for i in range(3, nsqrt):
		if n % i == 0:
			return False
	return True

def is_not_square(n):
	u = int(math.sqrt(n))
	return u * u != n

start = time.time()

odd_num = 3
prime_list = [] #we only need odd primes here
condition = False

while True:
	if is_odd_prime(odd_num):
		prime_list.append(odd_num)
	else:
		if functools.reduce(lambda u, v: u and v, [is_not_square((odd_num - p)/2) for p in prime_list]):
			print(odd_num)
			break
	odd_num += 2

print(time.time() - start)