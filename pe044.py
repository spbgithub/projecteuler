# coding=<utf-8>
'''Pentagon numbers
Problem 44'''

import math
import time


def is_pentagonal(num):
	u = 24*num + 1
	v = int(math.sqrt(u))
	return v * v == u and v % 6 == 5

def pent(n):
	return n*(3*n - 1)/2

start = time.time()

pair_found = False
k = 2
j = 1
while not pair_found:
	if is_pentagonal(pent(k) + pent(j)) and is_pentagonal(pent(k) - pent(j)):
			a, b = k, j
			pair_found = True
			break
	j = j + 1
	if j == k:
		j = 1
		k = k + 1

d = pent(a) - pent(b)
max_iter = (d-1)/3
print(a,b,d)
print(time.time() - start)

pairs_checked = False
while not pairs_checked:
	if is_pentagonal(pent(k) + pent(j)) and is_pentagonal(pent(k) - pent(j)):
		if pent(k) - pent(j) < d:
			a, b = k, j
			d = pent(k) - pent(j)
			max_iter = (d-1)/3
			print(a,b,d)
			print(time.time() - start)
	j = j + 1
	if j == k:
		print(k)
		k = k + 1
		j = 1
	if k > max_iter:
		pairs_checked = True

print(a,b,d)
print(start - time.time())
print("Done!")