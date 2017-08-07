'''Problem 202'''

from sympy.ntheory import totient

r = 1000001
#r = 12017639147

d = (r + 3)/2
q = (- (d % 3)) % 3
#if (d % 3) == 0:
#	q = 0
#elif (d % 3) == 1:
	#q = 2
#else:
#	q = 1

z = int((d - 2*q)/3)

print(totient(z))