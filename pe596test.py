import math
import time
from sympy.ntheory import divisor_sigma, nextprime

MODULUS = 1000000007

def ssd(N):
	div_sum, i = 0, 1
	q = int(math.sqrt(N))
	while i <= q:
		div_sum += (i * (N / i))
		i += 1
	i = 1
	while i <= N / (q + 1):
		m = N / i
		k = N / (i + 1)
		div_sum += (i * (m * (m + 1) - k * (k + 1)) / 2)
		i += 1
	return div_sum

R = 5
print(1 + 8*ssd(R*R) - 32*ssd(R*R/4))