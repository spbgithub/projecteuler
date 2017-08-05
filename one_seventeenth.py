n = 1
d = 17
iter = 0
max_iter = 30
while iter < max_iter:
	digit = n / d
	print(digit)
	n = 10*(n - digit * d)
	iter += 1
