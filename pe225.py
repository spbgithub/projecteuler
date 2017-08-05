'''Problem 225'''

def has_zero(modulus):
	a,b,c = 1,1,3
	while (a,b,c) != (1,1,1):
		if c % modulus == 0:
			return True
		a,b,c = b,c,(a+b+c) % modulus
	return False

modulus  = 3
no_zeros = 0
target   = 124

while no_zeros < target:
	if not has_zero(modulus):
		no_zeros += 1
		print(no_zeros, modulus)
	modulus += 2