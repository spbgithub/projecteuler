from functools import reduce
from math import sqrt
import time


def smallest_divisor(ubound):
	divlist = [0]*(ubound + 1)
	for j in range(2, ubound + 1):
		if not divlist[j]:
			divlist[j] = j
			for m in range(j, ubound + 1, j):
				divlist[m] = divlist[m] or j
	return divlist

def make_divisor_list(num, sdlist):
	dlist = set([sdlist[num]])
	num = num/sdlist[num]
	while sdlist[num] > 1:
		dlist.add(sdlist[num])
		num = num/sdlist[num]
	return list(dlist)

def sgn(x):
	if x < 0: return -1
	if x > 0: return 1
	return 0

def mult_list(l, bound):
	if len(l) == 0: return 1
	dlist = coprime_divisors([1], list(l))
	return sum(sgn(u)*(bound//abs(u)) for u in dlist)


def coprime_divisors(divlist, factors):
	if len(factors) == 0: return divlist
	return coprime_divisors(divlist + [-factors[0]*u for u in divlist], factors[1:])


def bound(n,m):
	return int((-m + sqrt(2.0*n - m*m))/2.0)

def coprime_in_range(n, rmax, divlist):
	if n == 1: return rmax
	if n % 100000 == 0: print(n)
	return mult_list(make_divisor_list(n, divlist), rmax)

def create_radical_list(ubound, plist):
	rad_list = []
	for j in range(0, ubound):
		rad_list.append([]) 
	for p in plist:
		print(p)
		for j in range(1, ubound//p + 1):
			rad_list[p*j].append(p)
	return rad_list
 
start = time.time()
MAXVAL = 3141592653589793
MAXSQRT = int(sqrt(MAXVAL))

divlist = smallest_divisor(MAXSQRT)
print("Divisors computed")
print(time.time() - start)
total = 0
for n in range(1, MAXSQRT + 1, 2):
	total += coprime_in_range(n, bound(MAXVAL, n), divlist)
print(total)
print(time.time() - start)