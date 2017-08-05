'''Problem 88'''

from sympy.utilities.enumerative import factoring_visitor
from sympy.utilities.enumerative import multiset_partitions_taocp
from sympy import factorint

debug = False
if not debug:

	upper_limit       = 12000 #upper limit on the value of k sought
	min_ps_num        = [0]*(1 + upper_limit)   #list to store the minimal k-product-sum numbers
	min_ps_num_count  = 0						#number of minimal k-product-sum numbers found
	min_ps_num_target = upper_limit - 1

	print("Begin computing minimal product-sum numbers")
	n = 4
	while n < 2 * upper_limit + 1 and min_ps_num_count <= min_ps_num_target:
		plist, multlist = zip(*factorint(n).items())
		states = multiset_partitions_taocp(multlist)
		partitions = list(factoring_visitor(state, plist) for state in states)

		for part in partitions:
			k = len(part) + n - sum(part)
					#print(n, csum, k)
			if k <= upper_limit:
				if min_ps_num[k] == 0:
					min_ps_num[k] = n
					min_ps_num_count += 1
		n += 1

	print(min_ps_num)
	print(sum(list(set(min_ps_num))))