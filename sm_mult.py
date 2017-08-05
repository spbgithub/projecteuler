import fractions
def smallest_multiple(n):
	i = 1
	prod = 1
	while (i <= n):
		prod = (prod*i)/fractions.gcd(prod,i)
		i = i+1
	return prod

print(smallest_multiple(20))