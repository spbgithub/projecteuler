import math

count = 0
for b in range(4, 50000001):
	for a in range(1, b):
		c2 = a**2 + b**2
		c = int(math.sqrt(c2))
		if c2 == c*c:
			if a + b + c < 100000000:
				if c % (b - a) == 0:
					count += 1
print(count) 