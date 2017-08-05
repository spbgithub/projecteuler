from num_theo import gcd

class farey_sequence:
	def __init__(self, d):
		self.numer = 0
		self.denom = 1
		self.base  = d

	def set_value(self, n, d):
		if n < 0 or d <= 0 or n > d:
			return False
		if n == 0:
			d = 1
		g = gcd(d, n)
		self.numer = n / g
		self.denom = d / g

	def value(self):
		return (self.numer, self.denom)

	def front_of_list(self):
		return self.numer == 0 and self.denom == 1

	def end_of_list(self):
		return self.numer == 1 and self.denom == 1

	def next(self):
		if self.end_of_list(): return self.value()
		if self.numer == 0:
			self.denom = self.base
			self.numer = 1
			return self.value()
		else:
			for b in range(self.base -1, 0, -1):
				if (b * self.numer + 1) % self.denom == 0:
					self.numer = (b * self.numer + 1) / self.denom
					self.denom = b
					break
			return self.value()

	def prev(self):
		if self.front_of_list(): return self.value()
		for b in range(self.base - 1, 0, -1):
			if (b * self.numer - 1) % self.denom == 0:
				self.numer = (b * self.numer - 1) / self.denom
				self.denom = b
				break
		return self.value()

if __name__ == "__main__":
	fs = farey_sequence(45)
	fs.set_value(1,3)
	while fs.value() != (1,2):
		if fs.value()[1] in [2,4,8,5,10,20,40]:
			print(fs.value())
		fs.next()
