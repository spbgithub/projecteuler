from collections import deque

MAX_PERIM = 1500000

m  = []
m.append([[1, -2, 2], [2, -1, 2], [2, -2, 3]])
m.append([[1, 2, 2], [2, 1, 2], [2, 2, 3]])
m.append([[-1, 2, 2], [-2, 1, 2], [-2, 2, 3]])

def matrix_mult(m, x):
	return [sum([r[j]*x[j] for j in range(0,3)]) for r in m]

def perimeter(x):
	return sum(x)

tri_stack = deque([[3,4,5]])
peri_count = {}

while len(tri_stack) > 0:
	x = tri_stack.popleft()
	p = perimeter(x)
	for j in range(1, (MAX_PERIM/p) + 1):
		if j*p not in peri_count:
			peri_count[j*p] = 1
		else:
			peri_count[j*p] += 1
	for j in range(0,3):
		y = matrix_mult(m[j],x)
		if perimeter(y) <= MAX_PERIM:
			tri_stack.append(y)
out = sorted([u for u in peri_count if peri_count[u] == 1])
print(len(out))
print(out[0:10])
