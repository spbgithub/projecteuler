'''Extra testing for Problem 402'''

def div_by_3(a,b,c):
	return (b - 2) % 3 == 0 and (a + c) % 3 == 0

def div_by_8(a,b,c):
	return (a - 2) % 4 == 0 and (b - 3) % 4 == 0 and (c - 2) % 4 == 0

def div_by_4(a,b,c):
	return a % 2 == 0 and (b - 1) % 2 == 0 and c % 2 == 0

def div_by_2(a,b,c):
	return (a + b + c - 1) % 2 == 0


def comp_div(a,b,c):
	m = 1
	if div_by_3(a,b,c): m *= 3
	if div_by_8(a,b,c): m *= 8
	elif div_by_4(a,b,c): m *= 4
	elif div_by_2(a,b,c): m *= 2
	return m

'''a, b = 0, 1
p = 24
n = 0
m = 10**9

while n < 96:
	a, b = b, a + b
	print ((b/p) % m, b % p)
	n += 1'''

'''observations: clearly, the remainders are the Fibonacci
sequence modulo p. The quotients, though, are also Fibonacci-
like, at least once they are non-zero. In particular, 
q_{i+2} = q_{i+1} + q_i + e, where e=0 if r_{i+1} + r_i < p,
and e=1 otherwise. Since the sequence of r_i is periodic with
period p=24, we can compute precisely how many e are 1 in any
period.'''


a, b, n = 0, 1, 1
while n < 300:
	a, b, n = b, a + b, n + 1
	if b % 24 == 0:	print(n, b % 24, b)
