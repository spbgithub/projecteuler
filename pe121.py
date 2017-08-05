'''Problem 121'''

from fractions import Fraction

def fact(n):
	if n == 0: return 1
	return n * fact(n-1)

P = [[]]
for n in range(1, 16):
	P.append(list([0]*16))

for n in range(1,16):
	P[n][0] = Fraction(1,n+1)
	P[n][n] = Fraction(1, fact(n+1))

for n in range(2, 16):
	for k in range(1, n):
		P[n][k] = Fraction(n,n+1)*P[n-1][k] + Fraction(1,n+1)*P[n-1][k-1]

s = sum([P[15][k] for k in range(8,16)])
print(int(1/s))
