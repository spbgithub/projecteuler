'''Odd period square roots
Problem 64'''

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

'''count = 0
for n in range(2, 10001):
	if not is_square(n):
		(s,p) = compute_continued_fraction(RootDFrac(0,1,1,n))
		if len(p) % 2 == 1:
			count += 1
print(count)'''

if name == "__main__":
	c = 3
	for n in range(1, 30):
		if not is_square(c*n):
			print(c*n, len(compute_continued_fraction(RootDFrac(0,1,1,c*n))[1]))