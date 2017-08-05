'''Problem 76'''

PROBLEM_SIZE = 5

cache = []
for j in range(0, PROBLEM_SIZE + 1):
	cache.append([0]*(PROBLEM_SIZE + 1))

def phi(n,b):
	if n < b:
		return 0
	if n == b or b==1:
		return 1
	if cache[n][b] > 0:
		return cache[n][b]
	else:
		cache[n][b] = sum(phi(n-b,j) for j in range(1, b+1))
		return cache[n][b]

print(sum([phi(PROBLEM_SIZE,j) for j in range(1,PROBLEM_SIZE+1)])-1)
