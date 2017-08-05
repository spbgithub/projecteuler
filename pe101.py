'''Problem 101'''
import time

def v(n):
	return n*n*n

def u(n):
	return u_recurse(n, 10)

def u_recurse(n, deg):
	if deg == 0: return 1
	return 1 - n * u_recurse(n, deg - 1)

def lagint(x, xlist, ylist, indices):
	if len(indices) == 1: return ylist[indices[0]]
	i1 = indices[-1]
	i2 = indices[-2]
	iset = set(indices)
	return ((x - xlist[i1])*lagint(x, xlist, ylist, list(iset - set([i1]))) - (x - xlist[i2])*lagint(x, xlist, ylist, list(iset - set([i2]))))/(xlist[i2] - xlist[i1])

start = time.time()
degmax = 10
llen = 1
sumfit = 0
for llen in range(1, degmax + 1):
	x = llen + 1
	l = list(range(1, x))
	while True:
		s = lagint(x, list(l), [u(j) for j in l], [z-1 for z in l])
		if s != v(x):
			print(s)
			sumfit += s
			break
		x += 1
print("looping done")
print(sumfit)

print(time.time() - start)