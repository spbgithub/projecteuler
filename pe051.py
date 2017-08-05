'''Prime digit replacements
Problem 51

By replacing the 1st digit of the 2-digit number *3, it turns out that six of the nine possible values: 13, 23, 43, 53, 73, and 83, are all prime.

By replacing the 3rd and 4th digits of 56**3 with the same digit, this 5-digit number is the first example having seven primes among the ten generated numbers, yielding the family: 56003, 56113, 56333, 56443, 56663, 56773, and 56993. Consequently 56003, being the first member of this family, is the smallest prime with this property.

Find the smallest prime which, by replacing part of the number (not necessarily adjacent digits) with the same digit, is part of an eight prime value family.'''

import functools
import math


def make_prime_list(upper_bound):
	upper_bound = 10**(int(math.log10(upper_bound)) + 1)
	lower_bound = 2
	ret_val = []
	ind = [True]*(upper_bound + 1)
	for num in range(2, (upper_bound/2)+1):
		for j in range(2*num, upper_bound, num):
			ind[j] = False
	for num in range(2, upper_bound):
		if ind[num] and num >= lower_bound:
			ret_val.append(num)
	print("Prime list made.")
	return ret_val

#doubles size of existing prime list by computing primes up to 2*max of old prime list
def extend_prime_list(plist):
	ret_val = []
	max_p = max(plist)
	ubound = 10**(int(math.log10(max_p))+2)
	ind = [True]*(ubound - max_p+1)
	for p in plist:
		start = p - max_p % p
		if start == 0:
			start += p
		for j in range(start, len(ind), p):
			ind[j] = False
	for j in range(1, len(ind)):
		if ind[j]:
			ret_val.append(max_p + j)
	print("Prime list extended.")
	return ret_val

#for better efficiency, make sure ps is a set, not a list
def is_prime(num, ps):
	return num in ps

def dig_to_num(dig):
	return sum([dig[j]*10**(len(dig)-j-1) for j in range(0,len(dig))])

def digit_replace(dig, old, new):
	if dig == old:
		return new
	else:
		return dig

def digit_replace_val(num_lst, dig_old, dig_new):
	return [digit_replace(u, dig_old, dig_new) for u in num_lst]

def max_prime_dig_repl(p):
	ret_val = 0
	p_dig = [int(c) for c in str(p)]
	dig_repl_list = list(set(p_dig))
	for dig in dig_repl_list:
		this_dig_val = 0
		for j in range(0, 10):
			ptest = dig_to_num(digit_replace_val(p_dig, dig, j))
			if is_prime(ptest, pset) and int(math.log10(ptest)) == int(math.log10(p)):
				this_dig_val += 1
		if this_dig_val > ret_val:
			ret_val = this_dig_val
	return ret_val

plistadd = make_prime_list(100000)
plist = [] + plistadd
pset = set(plist)
p_max, repl_max_num = 0, 0
found = False

while not found:
	for p in plistadd:
		cur_val = max_prime_dig_repl(p)
		if p == 111857:
			print cur_val, p
			print p in pset
		if cur_val > repl_max_num:
			repl_max_num = cur_val
			p_max = p
		if repl_max_num >= 8:
			print p_max, repl_max_num
			found = True
			break
	if not found:
		plistadd = extend_prime_list(plist)
		plist = plist + plistadd
		pset  = set(plist)


'''plist = make_prime_list(1000000)
padd = extend_prime_list(plist)
print(plist[-1])
print(padd)'''