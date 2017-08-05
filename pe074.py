'''Problem 74'''

from permutations import factorial
from num_theo import num_to_digs
fact = [factorial(j) for j in range(0, 10)]

def fact_chain(num):
	retval = 0
	while num > 0:
		retval += fact[num % 10]
		num = num / 10
	return retval

MAX_RECORD = 1000000
CHAIN_LENGTH_NEEDED = 60
chains = [0]*MAX_RECORD

for d in range(0, MAX_RECORD):
	cur_chain = []
	cur_chain.append(d)
	n             = fact_chain(d)
	old_chain_len = 0
	while n not in cur_chain:
		cur_chain.append(n)
		n = fact_chain(n)
		if n < d:
			old_chain_len = chains[n]
			break

	chains[d] = len(cur_chain) + old_chain_len

print(len([u for u in chains if u == CHAIN_LENGTH_NEEDED]))