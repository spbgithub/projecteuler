'''Problem 88'''

from subset import next_subset
from num_theo import make_prime_list
from functools import reduce

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

def class_sum(nums, classes):
	m = max(classes)
	s = [0]*(m+1)
	for j in range(0, len(nums)):
		if s[classes[j]] == 0:
			s[classes[j]] = nums[j]
		else:
			s[classes[j]] *= nums[j]
	return m, sum(s)

def class_prod(nums, classes):
	m = max(classes)
	s = [1]*(m+1)
	for j in range(1, len(nums)):
		s[classes[j]] *= nums[j]
	return reduce(lambda u,v: u * v, s)


upper_limit       = 12000  #upper limit on the value of k sought
min_ps_num        = [0]*(1 + upper_limit)   #list to store the minimal k-product-sum numbers
min_ps_num_count  = 0						#number of minimal k-product-sum numbers found
min_ps_num_target = upper_limit - 1
min_prime         = [0]*(1 + 2*upper_limit)
min_prime[2] = 2
min_prime[3] = 3

primes = make_prime_list(2*upper_limit)

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
		set_size      = len(pfactors)

		class_size    = [0]*(len(pfactors)+1)
		class_mem     = [1]*(len(pfactors)+1)
		class_size[1] = len(pfactors)
		pfactors      = [0] + pfactors
		class_mem[0]  = 0
		mtc           = True
		nc            = 1
		while mtc:
			nc, class_size, class_mem, mtc = next_subset(set_size , nc, class_size, class_mem, mtc)
			summands, csum = class_sum(pfactors[1:], class_mem[1:])
			
			k = summands + n - csum
			#print(n, csum, k)
			if k <= upper_limit:
				if min_ps_num[k] == 0:
					min_ps_num[k] = n
					min_ps_num_count += 1
	n += 1

print(min_ps_num)
print(sum(list(set(min_ps_num))))