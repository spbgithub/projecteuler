'''Problem 78'''

parts = []
parts.append(1)
parts.append(1)

m = 2
s = -1
while s != 0:
	j, k, s = 1, 1, 0
	while j > 0:
		j = m - (3*k*k + k)/2
		if j >= 0: s = (s - (-1)**k*parts[j]) % 1000000
		j = m - (3*k*k - k)/2
		if j >= 0: s = (s - (-1)**k*parts[j]) % 1000000
		k = k+1
	parts.append(s)
	print(m,s)
	m += 1

print(m-1)