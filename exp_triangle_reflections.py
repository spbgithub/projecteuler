from fractions import Fraction
from math import sqrt

#stores in the form (a + b\sqrt{d}), where a,b are fractions
#we initialize as d=0

class Root3(object):
	def __init__(self, a, b):
		if type(a) is int:
			self.a = Fraction(a)
		elif type(a) is Fraction:
			self.a = a
		else:
			self.a = None

		if type(b) is int:
			self.b = Fraction(b)
		elif type(b) is Fraction:
			self.b = b
		else:
			self.b = None

	def __neg__(self):
		return Root3(-self.a, -self.b)

	def __add__(self, other):
		return Root3(self.a + other.a, self.b + other.b)

	def __sub__(self, other):
		return Root3(self.a - other.a, self.b - other.b)
		
	def __mul__(self, other):
		return Root3(self.a * other.a + self.b * other.b * 3, self.a * other.b + self.b * other.a)

	def conjugate(self):
		return Root3(self.a, -self.b)

	def norm(self):
		return self.a * self.a - 3 * self.b * self.b

	def tofloat(self):
		return float(self.a + sqrt(3) * self.b)

	def __div__(self, other):
		z = self * other.conjugate()
		n = other.norm()
		return Root3(z.a/n, z.b/n)

	def __eq__(self, other):
		if type(other) is int:
			return self.a == other
		if type(other) == type(self):
			return self.a == other.a and self.b == other.b
		return False

	def __repr__(self):
		return "{} + {} sqrt(3)".format(self.a, self.b)

class Complex(object):
	def __init__(self, a, b):
		if type(a) is int or type(a) is Fraction:
			self.a = Root3(a,0)
		elif type(a) is Root3:
			self.a = a
		else:
			self.a = None

		if type(b) is int or type(b) is Fraction:
			self.b = Root3(b,0)
		elif type(b) is Root3:
			self.b = b
		else:
			self.b = None

	def __neg__(self):
		return Complex(-self.a, -self.b)

	def __add__(self, other):
		return Complex(self.a + other.a, self.b + other.b)

	def __sub__(self, other):
		return Complex(self.a - other.a, self.b - other.b)
		
	def __mul__(self, other):
		return Complex(self.a * other.a - self.b * other.b, self.a * other.b + self.b * other.a)

	def conjugate(self):
		return Complex(self.a, -self.b)

	def norm(self):
		return self.a * self.a + self.b * self.b

	def __div__(self, other):
		z = self * other.conjugate()
		n = other.norm()
		return Complex(z.a/n, z.b/n)

	def __eq__(self, other):
		if type(other) is int:
			return self.a.a == other
		if type(other) is Root3:
			return self.a == other
		if type(other) == type(self):
			return self.a == other.a and self.b == other.b
		return False

	def __neq__(self, other):
		if type(other) is int:
			return self.a.a != other
		if type(other) is Root3:
			return self.a != other
		if type(other) == type(self):
			return self.a != other.a and self.b != other.b
		return False


	def Re(self):
		return self.a

	def Im(self):
		return self.b

	def __repr__(self):
		return "({}) + ({}) i".format(self.a, self.b)


#we orient our triangle with point C at the origin, and the line through points A and B
#with x=1
#here line 0 goes through A,B
#     line 1 goes through B,C
#     line 2 goes through A,C

def int_with_line_0(pt, dir):
	t = (-pt.Re() + Root3(1, 0))/dir.Re()
	return Complex(Root3(1,0), pt.Im() + t * dir.Im())

def int_with_line_1(pt, dir):
	d = Root3(1,0)/(dir.Im() * Root3(3,0) - dir.Re())
	x = dir.Im() * Root3(0,1) * pt.Re() - dir.Re() * Root3(0,1) * pt.Im()
	y = dir.Im() * pt.Re() - dir.Re() * pt.Im()
	return Complex(x/d, y/d)

def int_with_line_2(pt, dir):
	d = Root3(1,0)/(dir.Im() * Root3(-3,0) - dir.Re())
	x = -dir.Im() * Root3(0,1) * pt.Re() + dir.Re() * Root3(0,1) * pt.Im()
	y = dir.Im() * pt.Re() - dir.Re() * pt.Im()
	return Complex(x/d, y/d)

def on_seg_0(pt):
	return (pt.Re() ==1) and (abs(pt.Im().tofloat()) <= 1.0)

def on_seg_1(pt):
	return (pt.Re() == pt.Im() * Root3(0,1)) and pt.Re().tofloat() >=0 and pt.Re().tofloat() <= 1

def on_seg_2(pt):
	return (pt.Re() == pt.Im() * Root3(0,-1)) and pt.Re().tofloat() >=0 and pt.Re().tofloat() <= 1

def new_dir(pt, dir):
	if on_seg_0(pt):
		return pt.conjugate()
	if on_seg_1(pt):
		u = -zeta2 * pt
		return u.conjugate()
	u = -zeta * pt
	return u.conjugate()

if __name__ == "__main__":
	#if either of these vertexes are reached, we will abort checking
	badvert1 = Complex(1, Root3(0, Fraction(1,3)))
	badvert2 = badvert1.conjugate()

	#zeta and zeta2 are used to help compute reflections from the non-vertical edges of the triangle
	#zeta2 = zeta**2
	zeta     = Complex(Fraction(-1,2), Root3(0,Fraction(1,2)))
	zeta2    = zeta.conjugate()

	#current point and direction
	
	cur_dir  = Complex(Root3(0,7), 3)
	cur_pt   = int_with_line_0(Complex(0,0), cur_dir)
	numrefl = 1

	while cur_pt != 0:
		cur_dir = new_dir(cur_pt, cur_dir)

		new_pt0 = int_with_line_0(cur_pt, cur_dir)
		new_pt1 = int_with_line_1(cur_pt, cur_dir)
		new_pt2 = int_with_line_2(cur_pt, cur_dir)

		if (new_pt0 == new_pt1) or (new_pt0 == new_pt2):
			print("bad vertex reached - exiting")
			break

		if (new_pt1 == new_pt2):
			print("we found our way out! - exiting")
			break

		if on_seg_0(new_pt0):
			cur_pt = new_pt0
		elif on_seg_1(new_pt1):
			cur_pt = new_pt1
		elif on_seg_2(new_pt2):
			cur_pt = new_pt2
		else:
			print("somethings fucked up - exiting")
			break

		numrefl += 1
		print(numrefl)

	print(numrefl)				