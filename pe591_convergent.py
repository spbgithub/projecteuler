import fractions
import math
#from sympy.ntheory.continued_fraction import continued_fraction_convergents, continued_fraction_iterator
#from sympy import N
from bigfloat import BigFloat, sqrt, const_pi, precision

#stores in the form (a + b\sqrt{d})/n.
class QuadRat(object):
	def __init__(self, a, b, n, d):
		self.a = a
		self.b = b
		self.d = d
		self.n = n
		self._sqrtd = math.sqrt(d)

	def mult_by(self, factor):
		self.a = self.a * factor.a - d * self.b * factor.b
		self.b = self.a * factor.b + self.b * factor.a
		self.n = self.n * factor.n
		g      = fractions.gcd(fractions.gcd(self.a,self.b),self.n)
		self.a = self.a / g
		self.b = self.b / g
		self.n = self.n / g

	def divide_by(self, divisor):
		self.mult_by(QuadRat(divisor.u, -divisor.v, divisor.u**2 - divisor.d*divisor.v**2, divisor.d))

	def floor(self):
		return int(float(self.a + self.b * self._sqrtd)/float(self.n))

	def mod1(self):
		u = self.floor()
		self.a = self.a - u * self.n

	def reciprocal(self):
		u, v, p = self.a * self.n, -self.b * self.n, self.a**2 - self.d * self.b**2
		g = fractions.gcd(fractions.gcd(self.a,self.b),self.n)
		self.a = u / g
		self.b = v / g
		self.n = p / g

	def equals(self, operand):
		return (self.a == operand.a and self.b == operand.b and self.n == operand.n and self.d == operand.d)

	def __repr__(self):
		return "(%s + %s sqrt(%s))/%s" % (self.a, self.b, self.d, self.n)

def actual_abrtd(a, b, d):
	return a + b*sqrt(d)

def naive_sol(d, range_max):
	mypi = const_pi()

	amin, bmin, errmin = BigFloat(0), BigFloat(0), mypi
	for b in range(-range_max, range_max + 1):
		a = BigFloat(int(round(math.pi - b*math.sqrt(d))))
		errnew = abs(actual_abrtd(a,b,d) - math.pi)
		if errnew < errmin and abs(a) <= range_max:
			amin, bmin, errmin = a, b, errnew

	return amin, bmin

def convergent_sqrt_d(d, range_max):
	qr = QuadRat(0,1,1,d)
	a  = qr.floor()
	qr.mod1()
	qr.reciprocal()
	convs = [(a,1)]
	a  = qr.floor()
	convs.append((convs[-1][0]*a + 1, a))
	while abs(convs[-1][1]) <= range_max * 10:
		qr.mod1()
		qr.reciprocal()
		a = qr.floor()
		convs.append((convs[-2][0] + a*convs[-1][0], convs[-2][1] + a*convs[-1][1]))
	return convs

def best_approx_bootstrap(d, range_max):
	sd = math.sqrt(d)
	amin, bmin, errmin = 0, 0, math.pi
	for b in range(-range_max, range_max + 1):
		a = int(round(math.pi - b*sd))
		errnew = abs(actual_abrtd(a,b,d) - math.pi)
		if errnew < errmin and abs(a) <= range_max:
			amin, bmin, errmin = a, b, errnew
	return amin, bmin


def best_approx(d, range_max):
	with precision(150):
		convs = convergent_sqrt_d(d, range_max * 100)
		amin, bmin = best_approx_bootstrap(d, 10)
		amin, bmin = BigFloat(amin), BigFloat(bmin)
		errmin = abs(actual_abrtd(amin, bmin ,d) - math.pi)
		#print("Bootstrap for {}: {},{}".format(d, int(amin), int(bmin)))
		reduction_found = True
		while reduction_found:
			reduction_found = False
			errcur = errmin
			for r, s in convs:
				#print("Does {},{} provide better estimate?".format(int(r),int(s)))
				errnew1 = abs(actual_abrtd(amin + r, bmin - s, d) - math.pi)
				errnew2 = abs(actual_abrtd(amin - r, bmin + s, d) - math.pi)

				if min(errnew1, errnew2) < errcur:
					if errnew1 < errnew2 and abs(amin + r) <= range_max and abs(bmin - s) <= range_max:
						rmin, smin, errcur = r, -s, errnew1
						reduction_found = True
						#print("yes!")
					elif errnew2 < errnew1 and abs(amin - r) <= range_max and abs(bmin + s) <= range_max:
						rmin, smin, errcur = -r, s, errnew2
						reduction_found = True
						#print("yes!!")

			if reduction_found:
				#print("Best update from {},{}".format(int(rmin),int(smin)))
				amin, bmin, errmin = amin + rmin, bmin + smin, errcur
				#print("New estimate: {}, {} \n".format(int(amin), int(bmin)))


		return amin, bmin


def best_approx_old(d, range_max):
	with precision(150):
		convs = convergent_sqrt_d(d, range_max * 100)
		amin, bmin = best_approx_bootstrap(d, 10)
		amin, bmin = BigFloat(amin), BigFloat(bmin)
		errmin = abs(actual_abrtd(amin, bmin ,d) - math.pi)

		jmax = len(convs)
		j = 0
		print("bootstrap estimate: {}, {}".format(int(amin), int(bmin)))
		while j < jmax:
			r, s = convs[j]
			print("next root d convergent: {},{}".format(int(r),int(s)))
			errnew1 = abs(actual_abrtd(amin + r, bmin - s, d) - math.pi)
			errnew2 = abs(actual_abrtd(amin - r, bmin + s, d) - math.pi)

			while min(errnew1, errnew2) < errmin:
				if errnew1 < errnew2 and abs(amin + r) <= range_max and abs(bmin - s) <= range_max:
					amin, bmin, errmin = amin + r, bmin - s, errnew1
					print("new estimate: {}, {}".format(int(amin), int(bmin)))
				elif errnew2 < errnew1 and abs(amin - r) <= range_max and abs(bmin + s) <= range_max:
					amin, bmin, errmin = amin - r, bmin + s, errnew2
					print("new estimate: {}, {}".format(int(amin), int(bmin)))
				else:
					break
				errnew1 = abs(actual_abrtd(amin + r, bmin - s, d) - math.pi)
				errnew2 = abs(actual_abrtd(amin - r, bmin + s, d) - math.pi)
			j += 1
		return amin, bmin


with precision(150):
	range_max = 10**13
	#dvals = [13, 55, 56, 89]
	dvals = sorted(set(range(1, 100)) - {n**2 for n in range(1,11)})
	
	sum_a = 0

	for d in dvals:
		print("Currently working on {}".format(d))
		r, s = best_approx(d, range_max)
		print("Smart estimate: {},{} \n".format(int(r),int(s)))
		sum_a += abs(int(r))
	print(sum_a)
