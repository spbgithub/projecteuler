# -*- coding: utf-8 -*-
"""
Created on Sun Dec 27 13:30:01 2015

@author: sean
"""

def f(x,y):
	return (x*y)//(y*y - x*y - x*x)

x = 0
y = 1
n = 0
count = 1
while n <=29:
	if n > 0 and n % 2 == 0:
		print(count, x, y, f(x,y))
		count += 1
	x, y = y, x + y
	n += 1

print(f(x,y))
	