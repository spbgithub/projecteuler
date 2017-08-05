'''Cubic permutations
Problem 62

The cube, 41063625 (345^3), can be permuted to produce two other cubes: 56623104 (384^3) and 66430125 (405^3). In fact, 41063625 is the smallest cube which has exactly three permutations of its digits which are also cube.

Find the smallest cube for which exactly five permutations of its digits are cube.
'''

from num_theo import num_to_digs, digs_to_num
from permutations import lex_perm_digs, factorial, is_perm

def is_cube(num):
	s = int(num**(1.0/3.0))
	return s**3 == num or (s-1)**3 == num or (s+1)**3 == num

def hash_num(num):
	return digs_to_num(sorted(num_to_digs(num)))

n = 22
counter = {}

found = False
u_bound = 100000
print("Working " + str(u_bound/10) + " to " + str(u_bound))
while not found:
	n3 = n**3
	if n3 > u_bound:
		for num in counter:
			if counter[num][1] == 5:
				print(counter[num][0])
				found = True
				break
		if found:
			break
		else:
			u_bound *= 10
			counter = {}
			print("Working " + str(u_bound/10) + " to " + str(u_bound))

	hn3 = hash_num(n3)
	if hn3 in counter:
		counter[hn3][1] += 1
	else:
		counter[hn3] = [n3, 1]

	n += 1

print("Done!")
