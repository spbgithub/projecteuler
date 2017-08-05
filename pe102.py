'''Problem 102'''
from functools import reduce

def vec_diff(v1, v2):
	return [v1[0] - v2[0], v1[1] - v2[1]]

def dot_prod(v1, v2):
	return v1[0]*v2[0] + v1[1]*v2[1]

def left_perp(v1, v2):
	return [v1[1] - v2[1], v2[0] - v1[0]]

def pt_in_triangle(pt, triangle):
	v1   = triangle[0:2]
	v2   = triangle[2:4]
	v3   = triangle[4:6]
	
	d1   = dot_prod(left_perp(v1,v2), vec_diff(pt, v1))
	d2   = dot_prod(left_perp(v2,v3), vec_diff(pt, v2))
	d3   = dot_prod(left_perp(v3,v1), vec_diff(pt, v3))
	
	if d1 * d2 > 0 and d1 * d3 > 0 and d2 * d3 > 0:
		return 1
	else:
		return 0

with open("/home/sean/workspace/projecteuler/p102_triangles.txt", "r") as f:
	print(reduce(lambda z,w: z+w, [pt_in_triangle([0,0], [int(u) for u in l.split(",")]) for l in f]))
