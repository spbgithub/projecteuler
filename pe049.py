'''Prime permutations
Problem 49

The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases by 3330, is unusual in two ways: (i) each of the three terms are prime, and, (ii) each of the 4-digit numbers are permutations of one another.

There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes, exhibiting this property, but there is one other 4-digit increasing sequence.

What 12-digit number do you form by concatenating the three terms in this sequence?'''

import time

def make_prime_set(lower_bound, upper_bound):
	ret_val = []
	ind = [True]*(upper_bound + 1)
	for num in range(2, (upper_bound/2)+1):
		for j in range(2*num, upper_bound, num):
			ind[j] = False
	for num in range(2, upper_bound):
		if ind[num] and num > lower_bound:
			ret_val.append(num)
	return {u for u in ret_val}

def fact(n):
	if n == 0: return 1
	return n * fact(n-1)

def dig_to_num(dig):
	return sum([dig[j]*10**(len(dig)-j-1) for j in range(0,len(dig))])

def lex_perm(sought_loc, num_to_perm):
	ordered_digits = [int(c) for c in str(num_to_perm)]
	div_size = 6
	perm_digits = []
	cur_ind = 0
	while len(ordered_digits) > 1:
		digit, sought_loc = divmod(sought_loc, div_size)
		digit = ordered_digits[int(digit)]
		perm_digits.append(digit)
		ordered_digits.remove(digit)
		div_size = div_size / len(ordered_digits)
		cur_ind += 1
	perm_digits.append(ordered_digits.pop())
	return dig_to_num(perm_digits)

def subset_n(l, n, prefix):
	if n == 0:
		return [sorted(prefix)]
	elif n > len(l):
		return subset_n(l, n-1, prefix)
	elif n == len(l):
		return subset_n(l[1:], n-1, prefix + [l[0]])
	else:
		return subset_n(l[1:], n - 1, prefix + [l[0]]) + subset_n(l[1:], n, prefix)

def perm_prime_set(prime_set):
	pset_list = []
	while len(prime_set) > 0:
		p = prime_set.pop()
		prime_set.add(p)
		pset = {lex_perm(j,p) for j in range(0,24)}
		if len(pset & prime_set) >=3:
			pset_list = pset_list + subset_n(list(pset & prime_set), 3, [])
		prime_set = prime_set - pset
	return pset_list


if __name__ == "__main__":
	start = time.time()

	primeset = make_prime_set(1000,10000)
	psetlist = perm_prime_set(primeset)
	for l in psetlist:
		if (l[2] - l[1] == l[1] - l[0]):
			print(l)

	print(time.time() - start)

	print(subset_n([1,2,3,4,5], 3, []))