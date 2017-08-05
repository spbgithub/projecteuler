# -*- coding: utf-8 -*-
"""
Problem 94
"""

from time import time

start = time()
m = []

m.append([[-1,2,2], [-2, 1, 2], [-2, 2, 3]])
#m.append([[1, 2, 2], [2, 1, 2], [2, 2, 3]])
m.append([[1, -2, 2], [2, -1, 2], [2, -2, 3]])


def dot_prod(v, w):
	return v[0]*w[0] + v[1]*w[1] + v[2]*w[2]


def matrix_mult(m, v):
	return [dot_prod(m[0], v), dot_prod(m[1], v), dot_prod(m[2], v)]
	
LIMIT = 1000000000
total = 0

v = [3,4,5]
j = 0
k = 2
perim = 3*v[-1] + 1 - k

while perim <= LIMIT:
	print(perim, v)
	total += perim
	v = matrix_mult(m[j], v)
	j = 1 - j
	k = 2 - k
	perim = 3*v[-1] + 1 - k
print(total)
print(time() - start)