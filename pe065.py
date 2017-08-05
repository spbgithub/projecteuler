'''Convergents of e
Problem 65'''

from num_theo import gcd, num_to_digs

def f(n):
	if n == 0:
		return 2
	if n % 3 == 2:
		return (2*n + 2)/3
	return 1

def evaluate_cont_frac_func(func, j):
	work = j
	if j == 0:
		return (func(0), 1)
	else:
		result = (func(j), 1)
		while j > 0:
			j -= 1
			a, b = (result[1] + result[0] * func(j), result[0])
			g = gcd(a, b)
			result = (a / g, b / g)
	return result


print(evaluate_cont_frac_func(f, 99))
print(sum(num_to_digs(evaluate_cont_frac_func(f, 99)[0])))
