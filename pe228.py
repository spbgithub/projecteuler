'''Problem 228'''

from fractions import gcd
LBOUND = 1864
UBOUND = 1909

def lcm(a,b):
	if a == 0 or b == 0: return False
	return a*b//gcd(a,b)

multiple = LBOUND
for j in range(LBOUND + 1, UBOUND + 1):
	multiple = lcm(multiple, j)

s = set()
for j in range(LBOUND, UBOUND + 1):
	s = s | set([1 + multiple*k//j for k in range(1, j + 1)])
print(len(s))