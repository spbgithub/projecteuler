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

def generate_partitions(pfactors, partitions):
	new_parts     = []
	while len(pfactors) > 0:
		b = (pfactors.pop(), 1)
		for part in partitions:
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
		partitions = new_parts
		new_parts  = []
	return [sorted(q) for q in set(sorted([tuple(sorted(tuple(part))) for part in partitions]))]

gp = generate_partitions([2,2,2],[[(2,1)]])
for g in gp:
	print(g)


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
	'''print("Generating partition cache")
	part_cache = {}
	part_cache[2] = [[(2,1)]]
	part_cache[3] = [[(3,1)]]

	j = 2
	while 2**j < 2*upper_limit + 1:
		print("Caching " + str(2**j))
		part_cache[2**j] = generate_partitions([2], part_cache[2**(j-1)])
		j += 1

	j = 2
	while 3**j < 2*upper_limit + 1:
		print("Caching " + str(3**j))
		part_cache[3**j] = generate_partitions([3], part_cache[3**(j-1)])
		j += 1

	print(part_cache[4])
	print(part_cache[8])
	print("Done generating partition cache")'''





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
			pfactors      = list_of_prime_factors(n, p, min_prime)
			'''if pfactors[0] == 2:
				u = len([p for p in pfactors if p == 2])
				if u == len(pfactors):
					partitions = part_cache[2**u]
				else:
					partitions = generate_partitions(pfactors[u:], part_cache[2**u])
			elif pfactors[0] == 3:
				u = len([p for p in pfactors if p == 3])
				if u == len(pfactors):
					partitions = part_cache[3**u]
				else:
					partitions = generate_partitions(pfactors[u:], part_cache[3**u])

			else:'''
			b          = (pfactors.pop(), 1)
			partitions = generate_partitions(pfactors, [[b]])

			#print(n, partitions)
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