'''Arranged probability - Problem 100'''
from math import sqrt
import time

start = time.time()
MIN_ALLOWABLE = 10**12
u, v, w = 3, 4, 5

while u + v +w < MIN_ALLOWABLE:
	u, v, w = u + 2*v + 2*w, 2*u + v + 2*w, 2*u + 2*v + 3*w

x = min(u, v)
print((1 + int(sqrt(x**2 + (x+1)**2)))/2)
print(time.time() - start)