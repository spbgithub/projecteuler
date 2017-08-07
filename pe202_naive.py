'''Problem 202'''

from fractions import gcd

#r = 1000001
r = 12017639147

d = (r + 3)/2

if (d % 3) == 0:
	x = 3
elif (d % 3) == 1:
	x = 2
else:
	x = 1

c = 0

while x < d - x:
	if gcd(x, d-x) == 1:
		c += 1
	x += 3

print(c*2)