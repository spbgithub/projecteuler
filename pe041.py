'''Pandigital prime
Problem 41

We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once. For example, 2143 is a 4-digit pandigital and is also prime.

What is the largest n-digit pandigital prime that exists?
'''

#note: largest n-digit pandigital prime must have n<=7 (n=8,9 yield integers all divisible by 3), while no integers for n=7 are. n=6,5 have the same issues as n=8,9, so our largest such prime must also satisfy n>=4. So, either n=4 or n=7. Something tells me we'll find one in n=7.
import math

def fact(n):
	if n == 0: return 1
	return n * fact(n-1)

def dig_to_num(dig):
	return sum([dig[j]*10**(len(dig)-j-1) for j in range(0,len(dig))])

def lex_perm(sought_loc):
	ordered_digits = [1,2,3,4,5,6,7]
	div_size = 720
	perm_digits = []
	while len(ordered_digits) > 1:
		digit, sought_loc = divmod(sought_loc, div_size)
		digit = ordered_digits[int(digit)]
		perm_digits.append(digit)
		ordered_digits.remove(digit)
		div_size = div_size / len(ordered_digits)
	perm_digits.append(ordered_digits.pop())
	return dig_to_num(perm_digits)

def is_prime(n):
	if n == 1: return False
	if n == 2: return True
	if n % 2 == 0: return False
	nsqrt = int(math.sqrt(n)+1)
	for i in range(3, nsqrt, 2):
		if n % i == 0: return False
	return True

for n in range(fact(7) - 1, fact(7) - fact(6), -1):
	if is_prime(lex_perm(n)): break
print(lex_perm(n))