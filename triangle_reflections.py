from fractions import Fraction

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




#points and vectors are both stored as pairs (u,v).


#evaluates to see if a point is on a line, given a point on line and direction 
#vector of the line
def is_on_line(pt, pt_on_line, dir_of_line):


#the following function will, given a start point and direction, will determine 
#
#return values:
#-2: degenerate condition (reaches one of the non-origin vertices)
#-1: returned to the origin
#0: x == 1
#1: y = -x/sqrt(3)
#2: y = x/sqrt(3)
#so, with starting direction of (a,b) from origin, first intercept is on line 0 at (1, b/a).




zeta = QuadRat(-1,1,2,3)
zeta2 = QuadRat(-1,-1,2,3)