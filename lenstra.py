import sys
import random


sys.path.append("/home/sean/workspace/projecteuler/")
import miller_rabin
import num_theo

ELLCURVE_IDENTITY         = 0
ELLCURVE_DIVISOR_FOUND    = 1
ELLCURVE_NEXT_POINT_FOUND = 2





#returns coefficients of Weierstrass form of elliptic curve
#y^2 = x^3 + ax + b (mod n), along with coordinates of point on 
#curve
def pick_random_ellcurve(n):
	x = random.randrange(1, n-1)
	y = random.randrange(1, n-1)
	a = random.randrange(1, n-1)
	b = (((y * y) % n) - ((((x * x) % n) * x) % n) - ((a*x) % n)) % n
	return (a, b, (x, y))

def ellcurve_next_point(a, b, n, p, q):
	if p == q:
		s_num   = 3*p[0]**2 + a
		s_denom = 2 * p[1]
	else:
		s_num   = q[1] - p[1]
		s_denom = q[0] - p[0]
	g       = num_theo.inv_mod_n(num_theo.gcd(s_num, n), n)
	s_num   = (s_num * g) % n
	s_denom = (s_denom * g) % n
	if s_denom == 0:
		return (ELLCURVE_IDENTITY, 0)
	g = num_theo.gcd(n, s_denom)
	if g > 1:
		return (ELLCURVE_DIVISOR_FOUND, g)
	else:
		s = s_num * num_theo.inv_mod_n(s_denom, n)
		x = (s*s - p[0] - q[0]) % n
		y = (p[1] + s*(x - p[0])) % n
		return (ELLCURVE_NEXT_POINT_FOUND, (x,y))


def find_ellcurve_factor(n, m):
	a, b, p = pick_random_ellcurve(n)
	q = p
	j = 1
	i = 1
	while j < m + 1:
		status, q = ellcurve_next_point(a, b, n, q, p)
		if status == ELLCURVE_IDENTITY:
			a, b, p = pick_random_ellcurve(n)
			q = p
			j = 1
			i = 1
		elif status == ELLCURVE_DIVISOR_FOUND:
			return q
		else:
			i = i + 1
			if i > j:
				j = j + 1
				i = 1
				p = q
	return False



if __name__ == "__main__":
	m = 5915587277 * 5463458053
	#m = 1915512350
	print(miller_rabin.is_strong_pseudoprime_milrab(m, 10))
	print(find_ellcurve_factor(m, 50))