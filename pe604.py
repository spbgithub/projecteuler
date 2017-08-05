'''Problem 604'''

from fractions import gcd
from sympy.ntheory import totient

def count_em(smax):
	n    = 2
	c    = 1
	s    = 0

	cur_c = totient(n)
	cur_s = (n * cur_c)/2
	
	while s + cur_s <= smax:
		s    += cur_s
		c    += cur_c
		n    += 1
		cur_c = totient(n)
		cur_s = (n * cur_c)/2
		
	u, v = 1, n - 1
	
	while s + n <= smax and u >= 1:
		if gcd(u, v) == 1:
			c += 2
			s += u + v
		u += 1
		v -= 1

	print(n, c, s, u, v)
	if s + n/2 < smax + 1:
		c += 1

	return c


def count_em_again(smax):
	n    = 2
	c    = 1
	s    = 0

	while s <= smax:
		for u in range(1, n):
			if gcd(u, n-u)  == 1:
				if s + n <= smax:
					s += n
					c += 2
				elif 
		n += 1

	if s + (n+1)/2 <= smax:
		s += (n+1)/2
		c += 1
	
	return c


smaxlist = [1, 3, 9, 11, 100, 50000, 10**18]

for smax in smaxlist:
	print(smax, count_em_again(smax))