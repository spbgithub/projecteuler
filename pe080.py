'''Square root digital expansion
Problem 80

It is well known that if the square root of a natural number is not an integer, then it is irrational. The decimal expansion of such square roots is infinite without any repeating pattern at all.

The square root of two is 1.41421356237309504880..., and the digital sum of the first one hundred decimal digits is 475.

For the first one hundred natural numbers, find the total of the digital sums of the first one hundred decimal digits for all the irrational square roots.
'''
from math import sqrt

def sum_digs(n):
	s = 0
	while n > 0:
		s += n % 10
		n /= 10
	return s

#radicand - a number
#digits - the currently computed digits - NOT A LIST
def next_digit(digits, remainder):
	remainder = 100 * remainder
	digits = 10 * digits
	n = remainder // (2*digits)
	if n*(2*digits + n) > remainder:
		n = n - 1
	remainder = remainder - n*(2*digits + n)
	digits = digits + n
	return digits, remainder

numbers = list(range(2,100))
for m in range(2, 10):
	numbers.remove(m*m)
total = 0
for n in numbers:
	dig       = int(sqrt(n))
	remainder = n - dig*dig
	for j in range(1, 100):
		dig, remainder = next_digit(dig, remainder)
	total += sum_digs(dig)
print(total)
