'''Number of lattice points in a hyperball
Problem 596
Let be T(r) the number of integer quadruplets x, y, z, t such that x^2 + y^2 + z^2 + t^2 <= r^2. In other words, T(r) is the number of lattice points in the four-dimensional hyperball of radius r.

You are given that T(2) = 89, T(5) = 3121, T(100) = 493490641 and T(10**4) = 49348022079085897.

Find T(10**8) mod 1000000007.'''


from math import sqrt


#factorial(n):
#a very reduced factorial function...don't need to compute more than
#factorial(4), so implementing for slight speed increase.
def factorial(n):
	if n == 4: return 24
	if n == 3: return 6
	if n == 2: return 2
	return 1


#gm(gridlist):
#provides the multiplicity of the grid; that is, the number of 
#times to count this grid due to symmetries of the first quadrant
#obtained from permuting coordinates. So for instance, (1,1,1,1) would 
#be counted once, (1,1,2,2) would be counted 6 times, (1,1,1,2) 4 
#times, (1,1,2,3) 12 times, and (1,2,3,4) 24 times.
def gm(gridlist):
	retval = factorial(len(gridlist))
	oldval = 0
	dcount = 1
	for c in gridlist:
		if c == oldval:
			dcount += 1
		else:
		    oldval = c
		    if dcount > 1:
		    	retval /= factorial(dcount)
		    	dcount = 1
	if dcount > 1:
		retval /= factorial(dcount)
	return retval



def gc2(radius, modulus):
	b = int(radius/sqrt(2)) 
	s = b
	for a in range(1, b+1):
		if (a % 1000000 == 0): print(a)
		s = (s + (2*(int(sqrt(radius*radius - a*a)) - a)) % modulus) % modulus
	return s

r       = 100000000
modulus = 1000000007
print(((4*gc2(r,modulus)) % modulus + (4*r) % modulus + 1) % modulus)