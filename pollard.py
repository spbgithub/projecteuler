import num_theo
import math
import random


def __g_mod_n(x, n):
	return (x*x + 1) % n

def pollard_rho(n):
	x = 2
	y = 2
	d = 1
	while d == 1:
		x = __g_mod_n(x, n)
		y = __g_mod_n(__g_mod_n(y, n), n)
		d = num_theo.gcd(abs(x - y), n)
	if d == n:
		return False
	return d

#for now, don't pick B>100000
def pollard_pminus1(n, B, primelist):
	a = 0
	while num_theo.gcd(a, n) != 1:
		a = random.randrange(2, n)
	for p in [q for q in primelist if q < B]:
		exp = int(math.log10(B)/math.log10(q))
		a = num_theo.power_mod(a, q**exp, n)
	g = num_theo.gcd(a - 1, n)
	return g


if __name__ == "__main__":
	found = False
	num = 9371057105
	while num > 1:
		out = pollard_rho(num)
		print(out)
		num = num / out

