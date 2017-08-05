# -*- coding: utf-8 -*-
"""
Created on Thu Dec 24 19:10:52 2015

@author: sean
"""

m = []

m.append([[-1,2,2], [-2, 1, 2], [-2, 2, 3]])
m.append([[1, 2, 2], [2, 1, 2], [2, 2, 3]])
m.append([[1, -2, 2], [2, -1, 2], [2, -2, 3]])

triples = []



def dot_prod(v, w):
	return v[0]*w[0] + v[1]*w[1] + v[2]*w[2]


def matrix_apply(m, v):
	return [dot_prod(m[0], v), dot_prod(m[1], v), dot_prod(m[2], v)]

def next_triple(ms, v, stack_to_date, triples):
	if len(stack_to_date) == 14: return

	triples.append((stack_to_date, v))
	for j in range(0, 3):
		next_triple(ms, matrix_mult(ms[j], v), stack_to_date + str(j), triples)
	
def matrix_mult(m1, m2):
	r = [[0,0,0], [0,0,0], [0,0,0]]
	for j in range(0,3):
		for i in range(0,3):
			r[i][j] = sum(m1[i][k]*m2[k][j] for k in range(0,3))
	return r
			
	
	
m1 = matrix_mult(m[0], matrix_mult(m[1], matrix_mult(m[0], m[1])))
m2 = matrix_mult(m[2], matrix_mult(m[1], matrix_mult(m[2], m[1])))

for u in m1: print(u)
	
for u in m2: print(u)


#next_triple(m,[3,4,5],"", triples)	

a_list = [2, 15, 104, 714, 4895, 33552, 229970, 1576239, 10803704, 74049690]
'''for u in sorted(triples):
	v = sorted(u[1])
	if v[1] % 2 == 0 and v[1]//2 in a_list:
		print(u)
	elif v[1] % 2 == 1 and v[1] in a_list:
		print(u)'''

		