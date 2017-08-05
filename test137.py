# -*- coding: utf-8 -*-
"""
Created on Sat Dec 26 09:07:51 2015

@author: sean
"""

from math import sqrt

def is_square(n):
	n2 = int(sqrt(n))
	return n2*n2 == n

s = []
for a in range(2, 10000001):
	if is_square(5*a*a + 2*a + 1):
		s.append(a)

t = [s[j+1]/s[j] for j in range(0, len(s)-1)]

print(s)
print(t)