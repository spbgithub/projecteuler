def squared_sum(n):
	return n*n*(n+1)*(n+1)/4

def sum_squared(n):
	return n*(n+1)*(2*n + 1)/6

print(squared_sum(10) - sum_squared(10))
print(squared_sum(100) - sum_squared(100))