import num_theo


def g_mod_n(x, n):
	return (x*x + 1) % n

def pollard_rho(n):
	x = 2
	y = 2
	d = 1
	while d == 1:
		x = g_mod_n(x, n)
		y = g_mod_n(g_mod_n(y, n), n)
		d = num_theo.gcd(abs(x - y), n)
	if d == n:
		return False
	return d

if __name__ == "__main__":
	print(pollard_rho(5915587277 * 5463458053))
