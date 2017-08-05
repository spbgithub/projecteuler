'''Problem 532'''
from math import acos, sqrt, pi, tan, cos, atan
from scipy.integrate import romberg
import time

def sec(x):
	return 1.0/cos(x)

def f(x, n):
	return sqrt(sec(x)**2/tan(pi/n)**2 + 1)

start = time.time()
alpha_0 = acos(sqrt(1 - 0.999**2))
n = int(pi/atan(romberg(sec, 0, alpha_0)/1000.0))
l = 0.0
while l < 1000.0:
	l = romberg(lambda x: f(x, n), 0, alpha_0)
	if l >= 1000.0:
		break
	n += 1
print n, l, n*l
print(time.time() - start)