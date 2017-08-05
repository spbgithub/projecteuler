'''Problem 124'''

#from sympy import nextprime

MAX_NUM = 100000

radvals = [1]*(MAX_NUM + 1)
nums    = list(range(0, MAX_NUM + 1))

j = 2
while j < MAX_NUM + 1:
	if radvals[j] == 1:
		k = 1
		while j*k < MAX_NUM + 1:
			radvals[j*k] *= j
			k += 1
	j += 1

vals = sorted(zip(radvals[1:], nums[1:]))

print(vals[9999])