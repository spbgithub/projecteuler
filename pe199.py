'''Problem 199'''

from math import sqrt

def curvecomp(k):
	return k[0] + k[1] + k[2] + 2.0 * sqrt(k[0] * k[1] + k[0] * k[2] + k[1] * k[2])

def appolonius(curvatures, depth):
	global MAX_DEPTH
	if depth > MAX_DEPTH: return 0
	lencurve = 3
	if depth == 1: lencurve = 4
	retval = 0
	for j in range(0, lencurve):
		cur_ks = curvatures[:j] + curvatures[j+1:]
		new_k = curvecomp(cur_ks)
		
		retval += 1.0/new_k**2
		globalcount[depth].append(new_k) 
		retval = retval + appolonius(cur_ks + [new_k], depth + 1)

	return retval

k = (3.0 + 2.0 * sqrt(3))/3.0
MAX_DEPTH = 10

print(1 - (3.0/k**2 + appolonius([-1,k,k,k], 1)))