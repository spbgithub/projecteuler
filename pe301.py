'''Problem 301'''


'''
This work here let me see that the Fibonacci sequence was key
bmax = 10
b    = 1

sum_s = [0]

while b < bmax:
	n = 1
	s = 0
	while n <= 2**b:
		if n^(2*n)^(3*n) == 0: s += 1
		n += 1
	b += 1
	sum_s.append(s)

print(sum_s)'''

a, b, n = 2, 3, 2
while n < 30:
	a, b, n = b, a + b, n + 1
print(b)