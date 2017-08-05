'''Totient maximum
Problem 69'''

'''Note: the answer is 2*3*5*7*11*13*17 = 510510, obtained via common sense
'''

from num_theo import unserialize_prime_list

pset = set(unserialize_prime_list(1000))

val_max = 0.0
n_max   = 0

for n in range(2, 1000001):
	print(n)
	val  = 1
	work = n
	for p in pset:
		if work % p == 0:
			val  *= float(p)/float(p-1)
			while work % p == 0:
					work /= p
		if work == 1: break
	if work > 1: val *= float(work)/float(work - 1)
	if val > val_max:
		n_max    =  n
		val_max  =  val
print(n_max, val_max)