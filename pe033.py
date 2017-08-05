'''Digit cancelling fractions
Problem 33

The fraction 49/98 is a curious fraction, as an inexperienced mathematician in attempting to simplify it may incorrectly believe that 49/98 = 4/8, which is correct, is obtained by cancelling the 9s.

We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

There are exactly four non-trivial examples of this type of fraction, less than one in value, and containing two digits in the numerator and denominator.

If the product of these four fractions is given in its lowest common terms, find the value of the denominator.
'''

import functools

def pair_to_num(pair):
	x, y = pair
	return 10 * x + y

#implements the euclidean algorithm
def gcd(z,w):
	if w > z:
		work = z
		z = w
		w = work
	while w > 0:
		z,w = w, z % w
	return z

#first, makes list of all fractions with 2-digit nums and denoms
#then takes those < 1
#then checks the condition of the problem
#reduce produces the product of these numbers
#divide denom by gcd of num and denom to obtain reduced denom
print([v/gcd(u,v) for (u,v) in [functools.reduce(lambda (r,s), (t, u): (r*t, s*u), [(pair_to_num((a,b)), pair_to_num((x,y))) for a in range(1,10) for b in range(1,10) for x in range(1, 10) for y in range(1, 10) if pair_to_num((a,b)) < pair_to_num((x,y)) if (a==y and x * pair_to_num((a,b)) == b * pair_to_num((x,y))) or (b==x and y * pair_to_num((a,b)) == a * pair_to_num((x,y)))])]])


