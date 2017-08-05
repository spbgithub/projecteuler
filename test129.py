from sympy import nextprime, divisors, factorint
from fractions import gcd


def power_mod_list(a, exp, n, computed):
	if exp not in computed:
		u = power_mod_list(a, exp//2, n, computed)
		if exp % 2 == 0:
			computed[exp] = (u * u) % n
		else:
			computed[exp] = (((u * u) % n) * a) % n
	return computed[exp]

#assumes p is prime power - returns period of 10^j mod p
def period_of_10_prime(p):
	divs = divisors(p-1)
	computed = {}
	computed[1] = 10 % p
	for d in divs:
		if power_mod_list(10, d, p, computed) == 1:
			return d
	return 0 #error condition



from sympy import isprime, divisors, nextprime
from fractions import gcd
from num_theo import power_mod

def lcm(a, b):
	return (a*b)//gcd(a,b)

#assumes p is prime power - returns period of 10^j mod p
def period_of_10_prime(p, exp):
	divs = divisors((p-1)*p**(exp - 1))
	pexp = p**exp
	computed = {}
	computed[1] = 10 % pexp
	for d in divs:
		if power_mod_list(10, d, pexp, computed) == 1:
			return d
	return 0 #error condition


def power_mod_list(a, exp, n, computed):
	if exp not in computed:
		u = power_mod_list(a, exp//2, n, computed)
		if exp % 2 == 0:
			computed[exp] = (u * u) % n
		else:
			computed[exp] = (((u * u) % n) * a) % n
	return computed[exp]



def divides_rep_unit(k, p):
	dig = 0
	rem = 0
	q   = []
	cur = 0
	while dig < p:
		cur = 10*cur + 1
		q.append()

for n in range(2, 17):
	print(sorted(factorint((10**n - 1)//9)))