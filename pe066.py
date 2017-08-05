'''Diophantine equation
Problem 66

Consider quadratic Diophantine equations of the form:

x^2 - Dy^2 = 1

For example, when D=13, the minimal solution in x is 649^2 - 13x180^2 = 1.

It can be assumed that there are no solutions in positive integers when D is square.

By finding minimal solutions in x for D = {2, 3, 5, 6, 7}, we obtain the following:

3^2 - 2x2^2 = 1
2^2 - 3x1^2 = 1
9^2 - 5x4^2 = 1
5^2 - 6x2^2 = 1
8^2 - 7x3^2 = 1

Hence, by considering minimal solutions in x for D <= 7, the largest x is obtained when D=5.

Find the value of D <= 1000 in minimal solutions of x for which the largest value of x is obtained.'''

from math import sqrt, floor
from num_theo import gcd


def gcd3(a,b,n):
	return gcd(gcd(a,b),n)

def is_square(n):
	nn = int(sqrt(n))
	return nn*nn == n

#stores in the form (a + b\sqrt{d})/n.
class RootDFrac(object):
	def __init__(self, a, b, n, d):
		self.a = a
		self.b = b
		self.d = d
		self.n = n

	def mult_by(self, factor):
		self.a = self.a * factor.a - d * self.b * factor.b
		self.b = self.a * factor.b + self.b * factor.a
		self.n = self.n * factor.n
		g      = gcd3(self.a, self.b, self.n)
		self.a = self.a / g
		self.b = self.b / g
		self.n = self.n / g

	def divide_by(self, divisor):
		self.mult_by(RootDFrac(divisor.u, -divisor.v, divisor.u**2 - divisor.d*divisor.v**2, divisor.d))

	def floor(self):
		return int(floor(float(self.a + self.b * sqrt(self.d))/float(self.n)))

	def mod1(self):
		u = self.floor()
		self.a = self.a - u * self.n

	def reciprocal(self):
		u, v, p = self.a * self.n, -self.b * self.n, self.a**2 - self.d * self.b**2
		g = gcd3(u,v,p)
		self.a = u / g
		self.b = v / g
		self.n = p / g

	def equals(self, operand):
		return (self.a == operand.a and self.b == operand.b and self.n == operand.n and self.d == operand.d)

	def __repr__(self):
		return "(%s + %s sqrt(%s))/%s" % (self.a, self.b, self.d, self.n)

def find_in_list(num, num_list):
	for j in range(0, len(num_list)):
		if num.equals(num_list[j]):
			return j
	return -1

def compute_continued_fraction(num_d):
	fraction_stack = []
	cont_frac      = []
	static_part    = []
	static_part.append(num_d.floor())
	num_d.mod1()
	
	j = find_in_list(num_d, fraction_stack)
	while j < 0:
		fraction_stack.append(RootDFrac(num_d.a, num_d.b, num_d.n, num_d.d))
		num_d.reciprocal()
		cont_frac.append(num_d.floor())
		num_d.mod1()
		j = find_in_list(num_d, fraction_stack)

	if j > 0:
		static_part = static_part + cont_frac[0:j-1]
		cont_frac = cont_frac[j:]
	return (static_part, cont_frac)

#j=0 means just evaluating the static part
def evaluate_cont_frac(static, periodic, j):
	if j == 0:
		return (static[j], 1)
	if j >= len(static):
		result = (periodic[(j - len(static)) % len(periodic)], 1)
	else:
		result = (static[j], 1)
	while j > 0:
		j = j - 1
		if j > len(static) - 1:
			a, b = (result[1] + result[0]* periodic[(j - len(static)) % len(periodic)], result[0])
		else:
			a, b = result[1] + result[0] * static[j], result[0]
		g = gcd(a, b)
		result = (a / g, b / g)
	return result

if __name__ == "__main__":
	x_max = 0
	d_max = 0

	for d in range(2, 1001):
		if not is_square(d):
			(s,p) = compute_continued_fraction(RootDFrac(0,1,1,d))
			j = 0
			found = False
			while not found:
				(x, y) = evaluate_cont_frac(s, p, j)
				if x * x - d * y * y == 1:
					found = True
				j += 1
			if x > x_max:
				x_max = x
				d_max = d
	print("d="+str(d_max)+" and x="+str(x_max))