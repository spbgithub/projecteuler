import fractions
import math
from sympy import nextprime
from sympy.ntheory.continued_fraction import continued_fraction_convergents, continued_fraction_iterator
from bigfloat import BigFloat, sqrt, const_pi, precision

def solve_bezout(A, B, C):
	if B < 0:
		return solve_bezout(-A, -B, -C)
	g = fractions.gcd(A, B)
	return solve_bezout_relprime(A/g, B/g, int(float(C)/float(g)))

#solves Ax + By = C, assuming (A,B)=1
def solve_bezout_relprime(A, B, C):
	if B == 0:
		return C,0
	u, v = solve_bezout(B, A % B, C) 
	return v, u - int(A/B) * v

def optimal_t(r0,r1, A, B, d):
	sd = sqrt(d)
	mypi = const_pi()
	return (A + B*sd - mypi)/(r1*sd - r0)

def best_int_t(A, B, r0, r1, t_opt, range_max):
	fA  = BigFloat(A)
	fB  = BigFloat(B)
	fmx = BigFloat(range_max)

	tmax = min((fmx - fA)/r0, (fB + fmx)/r1)
	tmin = max((-fmx - fA)/r0, (fB - fmx)/r1)
	
	tmax = int(tmax)
	if tmax < 0: tmax -= 1
	tmin = int(tmin)
	if tmin > 0: tmin += 1

	if int(tmax) <= int(tmin): return None

	toptint = int(round(t_opt))
	if toptint >= tmin and toptint <= tmax:
		return toptint
	if toptint > tmax: return tmax
	if toptint < tmin: return tmin
	return None

def actual_abrtd(a, b, d):
	return a + b*sqrt(d)

def aval(a, r0, t):
	return a + r0*t

def bval(b, r1, t):
	return b - r1*t


def list_convergents(num, num_fracs):
	fracs = []
	it = continued_fraction_convergents(continued_fraction_iterator(num))
	while len(fracs) < num_fracs:
		fracs.append(next(it).as_numer_denom())
	return fracs

def pair_to_float(intpair):
	return float(intpair[0])/float(intpair[1])


with precision(100):
	mypi      = const_pi()
	range_max = 1000000
	d         = 2
	sqrtd     = sqrt(d)
	tolerance = 10**(-6)
	#num_pi_conv = 10
	#num_d_conv  = 10*num_pi_conv
	d_conv = []
	pi_conv = []
	p = nextprime(1)
	while len(pi_conv) < 35:
		t = int(p * mypi)
		g = fractions.gcd(p, t)
		pi_conv.append((t/g, p/g))
		p = nextprime(p)

	p = nextprime(1)
	while len(d_conv) < 35:
		t = int(p*sqrtd)
		g = fractions.gcd(p, t)
		d_conv.append((t/g, p/g))
		p = nextprime(p)


	print(len(d_conv), len(pi_conv))
	#d_conv    = list_convergents(math.sqrt(d), num_d_conv)
	#pi_conv   = list_convergents(mypi, num_pi_conv)
	
	amin, bmin, errmin = 0, 0, mypi

	for r in d_conv:
		for p in pi_conv:
			a, b = solve_bezout(r[1], r[0], int(round(float(p[0] * r[1])/float(r[0]))))
			t = best_int_t(a, b, r[0], r[1], optimal_t(r[0], r[1], a, b, d), range_max)
			if t:
				anew, bnew = aval(a, r[0], t), bval(b, r[1], t)
				errnew = abs(actual_abrtd(anew, bnew, d) - mypi)
				if errnew < errmin:
					amin, bmin, errmin = anew, bnew, errnew
					print(amin, bmin, r, p)
	print(amin, bmin, errmin, actual_abrtd(amin, bmin, d))

