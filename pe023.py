'''
Non-abundant sums
Problem 23

A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of two abundant numbers is 24. By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers. However, this upper limit cannot be reduced any further by analysis even though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.

Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.
'''
import math

def sigma_alt(n):
	sum = 1
	d = 1
	lim = int(math.sqrt(n))
	if (lim * lim == n):
		sum += lim
	else:
		lim += 1
	for d in range(2, lim):
		if n % d == 0:
			sum += d + n/d
	return sum



def is_abundant(n):
	return (sigma_alt(n) > n)

abundant_nums = [u for u in list(range(12,28124)) if is_abundant(u)]
abundant_sums = [u + v for u in abundant_nums for v in abundant_nums]
non_abundant = list(set(range(1, 28124)) - set(abundant_sums))
print(sum(non_abundant))
#print(abundant_nums)