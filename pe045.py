'''Triangular, pentagonal, and hexagonal
Problem 45

Triangle, pentagonal, and hexagonal numbers are generated by the following formulae:
T_n = n(n+1)/2
P_n = n(3n-1)/2
H_n = n(2n-1)
It can be verified that T285 = P165 = H143 = 40755.

Find the next triangle number that is also pentagonal and hexagonal.
'''
import math
import time


def tri(n):
	return (n*(n+1))/2

def is_pentagonal(num):
	u = 24*num + 1
	v = int(math.sqrt(u))
	return v * v == u and v % 6 == 5

def is_hexagonal(num):
	u = 8*num + 1
	v = int(math.sqrt(u))
	return v * v == u and v % 4 == 3

start = time.time()

found = False
n = 286

while not found:
	if is_pentagonal(tri(n)) and is_hexagonal(tri(n)):
		found = True
		break
	n += 1

print(tri(n))
print(time.time() - start)