from collections import deque

berggren = []
berggren.append([[-1, 2, 2], [-2, 1, 2], [-2, 2, 3]])
berggren.append([[1, 2, 2], [2, 1, 2], [2, 2, 3]])
berggren.append([[1, -2, 2], [2, -1, 2], [2, -2, 3]])

def dot_prod(v,w):
	return v[0]*w[0] + v[1]*w[1] + v[2]*w[2]
	
def apply_m(m, v):
	return [dot_prod(r, v) for r in m]

#3141592653589793
UBOUND = 314159265
triples = deque([[3,4,5]])
count = 1
while len(triples) > 0:
	v = triples.popleft()
	for m in berggren:
		vtemp = apply_m(m, v)
		if vtemp[-1] <= UBOUND:
			count += 1
			triples.append(vtemp)
print(count)
		
