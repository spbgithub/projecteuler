'''Problem 72'''

from num_theo import euler_totient, unserialize_prime_list
import time

start = time.time()

MAX_VAL  = 1000000
results = [0]*(MAX_VAL + 1)

plist = unserialize_prime_list(MAX_VAL)
pset = set(plist)

for j in range(2, MAX_VAL + 1):
	if j in pset:
		results[j] = j - 1
	else:
		for p in plist:
			if j % p == 0:
				work = j / p
				if work % p == 0:
					results[j] = p * results[work]
				else:
					results[j] = (p-1) * results[work]
				break
print(sum(results))
print(time.time() - start)