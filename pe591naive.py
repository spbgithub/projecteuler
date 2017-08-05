import math
from bigfloat import BigFloat, precision, const_pi






with precision(160):
	d = 2
	range_max = 10**6
	print(naive_sol(d, range_max))
