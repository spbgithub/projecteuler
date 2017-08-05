'''We are implementing the Miller-Rabin test as discussed in Cormen, Leiserson, et al'''

import random
import time
import math


def is_milrab_witness(a,n):
	work = n - 1
	bitlist = []
	while work > 0:
		bitlist.append(work % 2)
		work = work >> 1
	d = 1
	while len(bitlist) > 0:
		x = d
		d = (d * d) % n
		if (d == 1 and x != 1 and x != n - 1):
			return True
		if bitlist.pop() == 1:
			d = (d * a) % n
	if d != 1:
		return True
	return False



''' From wikipedia:
    if n < 2,047, it is enough to test a = 2;
    if n < 1,373,653, it is enough to test a = 2 and 3;
    if n < 9,080,191, it is enough to test a = 31 and 73;
    if n < 25,326,001, it is enough to test a = 2, 3, and 5;
    if n < 4,759,123,141, it is enough to test a = 2, 7, and 61;
    if n < 1,122,004,669,633, it is enough to test a = 2, 13, 23, and 1662803;
    if n < 2,152,302,898,747, it is enough to test a = 2, 3, 5, 7, and 11;
    if n < 3,474,749,660,383, it is enough to test a = 2, 3, 5, 7, 11, and 13;
    if n < 341,550,071,728,321, it is enough to test a = 2, 3, 5, 7, 11, 13, and 17.'''
'''Note: 2^340 = 1 mod 341 but 341 is prime. So wikipedia is, as often, full of shit'''


def milrab_witness_pool(n, iters):
	a = []
	while iters > 0:
		iters -= 1
		a.append(random.randrange(2, n-1, 1))
	return a

def is_strong_pseudoprime_milrab(n, iters):
	if n==2 or n==3: return True
	a = milrab_witness_pool(n, iters)
	while len(a) > 0:
		if is_milrab_witness(a.pop(), n):
			return False
	return True



#m = 20988936657440586486151264256610222593863921

#print(is_strong_pseudoprime_milrab(m, 100))