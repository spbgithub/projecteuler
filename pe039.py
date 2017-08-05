'''Integer right triangles
Problem 39

If p is the perimeter of a right angle triangle with integral length sides, {a,b,c}, there are exactly three solutions for p = 120.

{20,48,52}, {24,45,51}, {30,40,50}

For which value of p <= 1000, is the number of solutions maximised?'''


import math
import time

def ord_triple((a,b,c)):
	if a > b:
		swap = a
		a = b
		b = swap
	return (a,b,c)

def gcd(a,b):
	if a < b:
		swap = a
		a = b
		b = swap
	while b > 0:
		a,b = b, a % b
	return a

start = time.time()
print(sorted([(len({ord_triple((o*(m*m - n*n), 2*o*m*n, o*(m*m + n*n))) for (o,m,n) in [(l,j,k) for j in range(2, int(math.sqrt(p/2)+1)) for k in range(1,j) if gcd(j,k) == 1 for l in range(1, 1001/(2*j*(j+k)) + 1) if 2*l*j*(j+k) == p]}), p) for p in range(12, 1001)])[-1])
print time.time() - start