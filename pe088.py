'''Problem 88'''

from subset import next_subset
from num_theo import make_prime_list
from functools import reduce
from collections import deque

def smallest_prime_divisor(n, primes):
	if n in primes: return n
	for p in primes:
		if n % p == 0: return p

#returns list of prime factors of n, given smallest prime divisor of n,
#by looking up smallest prime factor q of n/p, then of n/(pq), etc...
def list_of_prime_factors(n, p, min_prime_list):
	retval = [p]
	nwork = n // p
	while nwork > 1:
		p = min_prime_list[nwork]
		retval.append(p)
		nwork = nwork // p
	return retval

def class_sum(nums):
	return sum([a[1] for a in nums]), sum([u*v for (u,v) in nums])

def generate_partitions(pfactors, old_parts):
	parts = list(old_parts)
	new_parts     = []
	while len(pfactors) > 0:
		b = (pfactors.pop(), 1)
		for part in parts:
			#first, just adding b to the existing partition - need to do this based
			#on whether or not it is the only copy 
			part_to_add = [] + part
			tl = [a[0] for a in part_to_add]
			if b[0] in tl:
				indx = tl.index(b[0])
				part_to_add[indx] = (part_to_add[indx][0], part_to_add[indx][1] + 1)
			else:
				part_to_add = part + [b]
			new_parts.append(part_to_add)

			part_to_add = []
			for j in range(0, len(part)):
				if part[j][1] == 1:
					part_to_add = part[0:j]+part[j+1:] + [(part[j][0]*b[0], 1)]
				else:
					part_to_add = part[0:j]+part[j+1:]+[(part[j][0], part[j][1]-1)] + [(part[j][0]*b[0], 1)]
				new_parts.append(part_to_add)
		parts = new_parts
		new_parts  = []

	for j in range(0, len(parts)):
		proj_1 = list(set([u[0] for u in parts[j]]))
		parts[j] = [(p, sum([u[1] for u in parts[j] if u[0]==p])) for p in proj_1]

	return parts

debug = False
if not debug:

	upper_limit       = 12000 #upper limit on the value of k sought
	min_ps_num        = [0]*(1 + upper_limit)   #list to store the minimal k-product-sum numbers
	min_ps_num_count  = 0						#number of minimal k-product-sum numbers found
	min_ps_num_target = upper_limit - 1
	min_prime         = [0]*(1 + 2*upper_limit)
	min_prime[2] = 2
	min_prime[3] = 3

	primes = make_prime_list(2*upper_limit)


	#first, we want to cache the partitions corresponding to the powers of 2 that can
	#be encountered...this is where most of the work seems to be taken up. We may extend this
	#to including powers of 3 (and 5?) as needed to speed things up
	print("Initializing partition cache")
	partition_cache = {}
	for p in primes:
		partition_cache[p] = [[(p,1)]]
	print("Done initializing partition cache")


	print("Begin computing minimal product-sum numbers")
	n = 4
	while n < 2 * upper_limit + 1 and min_ps_num_count <= min_ps_num_target:
		if n % 100 == 0: print(n)
		p = smallest_prime_divisor(n, primes)
		min_prime[n] = p
		if p != n:
			#the first task is to generate the list of prime factors 
			# we use the algorithm for iterating over partitions of a finite set
			# {1,...,n}: we ignore the trivial partition consisting of {1,...,n} itself
			# (it bootstraps our iteration), then compute the appropriate product and sum
			# for each partition, determine what value of k is required, then see if a
			# minimum has already been found for that value of k. if not, record it and move on
			old_partitions = partition_cache[n//p]
			partitions = generate_partitions([p], list(old_partitions))
			partition_cache[n] = list(partitions)

			while len(partitions) > 0:
				part           = partitions.pop()
				if len(part) > 1 or part[0][1] > 1:
					summands, csum = class_sum(part)
					
					k = summands + n - csum
					#print(n, csum, k)
					if k <= upper_limit:
						if min_ps_num[k] == 0:
							min_ps_num[k] = n
							min_ps_num_count += 1
		n += 1

	print(min_ps_num)
	print(sum(list(set(min_ps_num))))