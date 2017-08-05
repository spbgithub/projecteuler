'''Problem 73'''

import math
from num_theo import gcd, unserialize_prime_list





results = [0]*12001
plist = unserialize_prime_list(10000)

for d in range(5, 12001):
	cur_val = int(float(d)/float(2)) - int(math.ceil(float(d)/float(3))) + 1
	if d % 3 == 0: cur_val -= 1
	if d % 2 == 0: cur_val -= 1
	if d not in plist:
		for div in range(5, int(d/2)+1):
			if d % div == 0:
				cur_val -= results[div]
	results[d] = cur_val
print(sum(results))


'''
accurate but very naive
counter = 0
for d in range(4, 12001):

	print(d, lower_bound, upper_bound)
	for j in range(lower_bound, upper_bound + 1):
		if gcd(d, j) == 1:
			counter += 1

print(counter)'''
