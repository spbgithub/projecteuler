'''Problem 85'''

prods = [(u,v) for u in range(1, 2002) for v in range(1, 2002) if u <= v]

def tri(n):
	return (n*(n+1))/2

c = min([abs(2000000 - tri(u)*tri(v)) for (u,v) in prods])
for (u,v) in prods:
	if abs(2000000 - tri(u)*tri(v)) == c:
		print(u,v, u*v)
