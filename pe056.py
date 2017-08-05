'''Square root convergents - Problem 57'''
import math

def num_digs(n):
	c = 0
	while n > 0:
		n /= 10
		c += 1
	return c


def gcd(a,b):
	if a < b:
		swap = a
		a = b
		b = swap
	while b > 0:
		a, b = b, a % b
	return a

cur_num, cur_denom = 3,2
count = 0

for n in range(1, 1000):
	cur_num, cur_denom = cur_num + 2*cur_denom, cur_num + cur_denom
	div = gcd(cur_num, cur_denom)
	cur_num /= div
	cur_denom /= div
	if n < 15:
		print cur_num, cur_denom
	if int(math.log10(cur_num)) > int(math.log10(cur_denom)):
		count += 1
print(count)
