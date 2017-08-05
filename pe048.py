'''Self powers
Problem 48

The series, 1^1 + 2^2 + 3^3 + ... + 10^10 = 10405071317.

Find the last ten digits of the series, 1^1 + 2^2 + 3^3 + ... + 1000^1000.'''

def pow_mod(num, exp, base):
	if exp == 1:
		return num % base
	exp_half = exp/2
	a = pow_mod(num, exp_half, base)
	if 2*exp_half == exp:
		return (a * a) % base
	else:
		return (a * a * num) % base

modulus = 10000000000

sum_ten = 0
for i in range(1, 1001):
	sum_ten = (sum_ten + pow_mod(i, i, modulus)) % modulus
print(sum_ten)
