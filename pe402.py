'''Problem 402'''

from random import randint
from fractions import gcd


def poly(a,b,c,n):
	return n*(c + n*(b + n*(a + n)))


def compute_divisor(a,b,c,p):
	m = poly(a,b,c,1)

	for n in range(2, p+1):
		if m == 1: break
		m = gcd(m, poly(a,b,c,n))

	return m


def compute_divgrid(p):
	g=[]
	for a in range(1, p+1):
		h = []
		for b in range(1, p+1):
			k = []
			for c in range(1, p+1):
				k.append(compute_divisor(a,b,c,p))
			h.append(list(k))
		g.append(list(h))
	return g


def sum_grid(u,v,w, grid):
	s = 0
	for a in range(0,u):
		for b in range(0,v):
			for c in range(0,w):
				s += grid[a][b][c]
	return s


def cache_grid_sums(grid, p):
	c=[0]
	s=[0]
	t=[0]

	for j in range(1, p+1):
		c.append(sum_grid(j,j,j,grid))
		s.append(sum_grid(p,p,j,grid) + sum_grid(p,j,p,grid)+sum_grid(j,p,p,grid))
		t.append(sum_grid(p,j,j,grid) + sum_grid(j,j,p,grid)+sum_grid(j,p,j,grid))

	return c,s,t


def mod_mult(numlist, M):
	l = len(numlist)
	if l == 1: return (numlist[0] % M)
	return (mod_mult(numlist[0:l/2], M) * mod_mult(numlist[l/2:], M)) % M

def cube_count(q, r, p, c, s, t, M):
	#q = N / p
	#r = N % p	

	'''The genesis of this formula is as follows: experimental 
	evidence suggests that the function sum_grid is periodic of period
	24 in its first three arguments. I think I can prove this as well,
	but I haven't written it down as of yet. Then I am essentially
	decomposing a cube of side N into cubes of side q, plus 
	rectangular solids with sides (p,p,r), (p,r,r) and a cube
	of side r. The coefficients of powers of q indicate the
	multiplicity each should receive.'''
	rval = mod_mult([q,q,q,c[p]], M)
	rval = (rval + mod_mult([q,q,s[r]], M)) % M
	rval = (rval + mod_mult([q, t[r]], M)) % M
	return (rval + c[r]) % M


N = 1234567890123

p = 24
M = 5**9
Mper = 12*M
Nmod = N/Mper
Nrem = N % Mper

g = compute_divgrid(p)
c, s, t = cache_grid_sums(g, p)


smfib = 0
smmid = 0
x,y = 0,1
qx, qy = 0, 0
i = 0

smlist = []

while True:
	qx, qy = qy, qx + qy
	if x + y >= p:
		qy += 1
	qy = qy % M
	x,y = y, (x+y) % p

	#smfib = (smfib + cube_count(qy, y, p, c, s, t, M)) % M
	smlist.append(cube_count(qy, y, p, c, s, t, M))

	if (i > 3 and smlist[i-2] == smlist[0] and smlist[i-1] == smlist[1] and smlist[i] == smlist[2]):
		print("estimated period is {} ".format(i-2))
																																																																																																																			
	i += 1


#print(((smfib * Nmod) % M + smmid) % M)