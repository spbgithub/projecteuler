'''Problem 138'''

def dot_prod(v,w):
	return v[0]*w[0] + v[1]*w[1] + v[2]*w[2]

def apply_matrix(m, v):
	return [dot_prod(m[0], v), dot_prod(m[1], v), dot_prod(m[2], v)]

m1 = [[1, 2, 2], [2, 1, 2], [2, 2, 3]]
m2 = [[-1, 2, 2], [-2, 1, 2], [-2, 2, 3]]

v = apply_matrix(m2, [3,4,5])
total = 0
for j in range(0, 12):
	print(v)
	total += v[-1]
	v = apply_matrix(m2, apply_matrix(m1, v))

print(total)
