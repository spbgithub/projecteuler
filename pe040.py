'''Champernowne's constant
Problem 40

An irrational decimal fraction is created by concatenating the positive integers:

0.123456789101112131415161718192021...

It can be seen that the 12th digit of the fractional part is 1.

If dn represents the nth digit of the fractional part, find the value of the following expression.

d1 x d10 x d100 x d1000 x d10000 x d100000 x d1000000'''

import math

#the following function computes the location 
d_pow = [0]*7
d_pow[0] = 1
for n in range(1, 7):
	d_pow[n] = d_pow[n-1] + (10**n - 10**(n-1))*n

def find_list_interval(n):
	u = len([z for z in d_pow if z <= n]) - 1
	return u,d_pow[u]

def interpolate_to_n(d_loc):
	i, interval = find_list_interval(d_loc)

	num = 10**i + int((d_loc - interval)/(i+1))
	offset = (d_loc - interval) % (i+1)
	return num, offset

def digit_at_loc(num, dig):
	return int(str(num)[dig])

prod = 1
for n in range(0,7):
	a,b = interpolate_to_n(10**n)
	c = digit_at_loc(a,b)
	print(n,10**n,a,b,c)

	prod *= c
print(prod)
