'''Problem 140'''

from fractions import gcd

def f(u,v):
	return (3*u*u + u*v)//(v*v - u*v - u*u)

lst = [(2,5), (1,2)]
while len(lst) < 30:
	p = lst[-2][0] + lst[-2][1]
	q = lst[-2][1] + p
	lst.append((p,q))
print(sum(f(u,v) for (u,v) in lst))