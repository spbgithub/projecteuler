import math

def is_prime(n):
	nsqrt = int(math.sqrt(n)+1)
	for j in range(2, nsqrt):
		if n % j == 0:
			return False
	return True

for n in range(2, 1000000):
	if is_prime(n):
		print(n)


l = list(range(0, 1000000))
