class myfrac:
	numerator   = 0
	denominator = 1

	def __init__(self, n, d):
		self.numerator   = n
		self.denominator = d
		self.rationalize()

	def __hash__(self):
		return hash(str(self))

	def gcd(self, a, b):
		if a < b:
			return self.gcd(b,a)
		if b == 0:
			return a
		return self.gcd(b, a % b)

	def abs(self, u):
		if u < 0:
			return -u
		return u

	def rationalize(self):
		if self.denominator < 0:
			self.numerator   *= -1
			self.denominator *= -1
		g = self.gcd(self.abs(self.numerator), self.denominator)
		if g > 1:
			self.numerator /= g
			self.denominator /= g

	def __str__(self):
		return str(self.numerator) + "/" + str(self.denominator)

	def __repr__(self):
		return str(self.numerator) + "/" + str(self.denominator)

	def __eq__(self, other):
		return self.numerator * other.denominator == self.denominator * other.numerator

	def __add__(self, other):
		return myfrac(self.numerator*other.denominator + self.denominator*other.numerator, self.denominator*other.denominator)

	def __div__(self, other):
		return myfrac(self.numerator*other.denominator, self.denominator*other.numerator)

	def reciprocal(self):
		return myfrac(self.denominator, self.numerator)