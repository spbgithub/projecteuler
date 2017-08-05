'''Problem 93'''

from sympy.combinatorics.subsets import ksubsets
from sympy.combinatorics import Permutation
import operator

def applyop(oplist, n1, n2, diglist):
	op = oplist.pop()
	if type(n1) is int and type(n2) is int:
		try:
			return op(diglist[n1], diglist[n2])
		except ZeroDivisionError:
			return False
	else:
		if type(n1) is list:
			u = applyop(oplist, n1[0], n1[1], diglist)
		else:
			u = diglist[n1]
		if type(n2) is list:
			v = applyop(oplist, n2[0], n2[1], diglist)
		else:
			v = diglist[n2]
		try:
			return op(u, v)
		except ZeroDivisionError:
			return False

def digstring(s):
	n = 0
	while (n+1) in s:
		n += 1
	return n

op_list = [operator.add, operator.sub, operator.mul, operator.truediv]
op_triples = [[a,b,c] for a in op_list for b in op_list for c in op_list]

#corresponding to the five possible ways to parenthesize, since even unparenthesized expressions
#are basically parenthesized
groupings = [[[0,1],[2,3]], [0, [1, [2, 3]]], [0, [[1, 2], 3]], [[[0, 1], 2], 3], [[0, [1, 2]], 3]]

max_runs = []

for diglist in ksubsets([1,2,3,4,5,6,7,8,9], 4): #this iterates through all 4-subsets of the digits
	vals_found = set()
	p = Permutation(3)
	while p:	#this iterates through all permutations of the current selection of digits
		dperm = p(list(diglist))
		#these three nested loops consider all possible combinations (with replacement)
		#of the four arithmetic operators allowed
		for ops in op_triples:
			for g in groupings:
				cur_ops = list(ops)
				val = applyop(cur_ops, g[0], g[1], dperm)
				if val and val == int(val):
					vals_found.add(int(val))
		p = p.next_lex()
	dlength = digstring(vals_found)
	max_runs.append((dlength, diglist))

print(sorted(max_runs)[-1])