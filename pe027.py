'''Quadratic primes
Problem 27

Euler discovered the remarkable quadratic formula:

n^2 + n + 41
It turns out that the formula will produce 40 primes for the consecutive values n = 0 to 39. However, when n = 40, 402 + 40 + 41 = 40(40 + 1) + 41 is divisible by 41, and certainly when n = 41, 41^2 + 41 + 41 is clearly divisible by 41.

The incredible formula  n^2 - 79n + 1601 was discovered, which produces 80 primes for the consecutive values n = 0 to 79. The product of the coefficients, -79 and 1601, is -126479.

Considering quadratics of the form:

    n^2 + an + b, where |a| < 1000 and |b| < 1000

    where |n| is the modulus/absolute value of n
    e.g. |11| = 11 and |-4| = 4

Find the product of the coefficients, a and b, for the quadratic expression that produces the maximum number of primes for consecutive values of n, starting with n = 0.'''

#Note: we assume that 1, -1 are not prime, and that if p is prime, then so is
#-p.

import math


def is_prime(n):
	nsqrt = int(math.sqrt(n))+1
	for d in range(2, nsqrt):
		if n % d == 0:
			return False
	return True

def prime_list(upper_bound):
	plist = []
	for j in range(2, upper_bound):
		if is_prime(j):
			plist.append(j)
	return plist

def quadratic_eqn(n, a, b):
	return b + n * (a + n)

def prime_list_length(a, b):
	n = 0
	while is_prime(math.fabs(quadratic_eqn(n, a, b))):
		n += 1
	return n

a_max = 0
b_max = 0
n_max = 0

plist = prime_list(1000)
print("List of primes generating. Proceeding.")
for b in plist:
	for a in range(-999, 1000):
		n_cur = prime_list_length(a,b)
		if n_cur > n_max:
			a_max = a
			b_max = b
			n_max = n_cur
		n_cur = prime_list_length(a,-b)
		if n_cur > n_max:
			a_max = a
			b_max = -b
			n_max = n_cur
print(a_max, b_max, a_max*b_max, n_max)
print()
for n in range(0, n_max):
	print quadratic_eqn(n, a_max, b_max)
