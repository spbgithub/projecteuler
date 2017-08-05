import pickle
import math

def gcd(a, b):
	if a < b:
		swap = a
		a = b
		b = swap
	while b > 0:
		a, b = b, a % b
	return a

def lcm(a,b):
	return (a*b)//gcd(a,b)

def ext_gcd_euclid(a, b):
	coeff = []
	while b > 0:
		coeff.append((a, b))
		if a < b:
			swap = a
			a = b
			b = a
		else:
			a, b = b, a % b
	d, u, v = a, 1, 0
	while len(coeff) > 0:
		a, b = coeff.pop()
		if a < b:
			u, v = v, u
		else:
			u, v = v, u - int(a/b)*v
	return d, u, v

def inv_mod_n(b, n):
	d, x, y = ext_gcd_euclid(n, b)
	if d > 1:
		return 0
	else:
		return (y % n)

def is_prime_div(n):
	if n % 2 == 0: return False
	if n % 3 == 0: return False
	j = 1
	nsq = int(math.sqrt(n)+1)
	while 6 * j - 1 < nsq:
		if n % (6 * j - 1) == 0: return False
		if n % (6 * j + 1) == 0: return False
		j += 1
	return True

def make_prime_list(upper_bound):
	lower_bound = 2
	ret_val = []
	ind = [True]*(upper_bound + 1)
	for num in range(2, (upper_bound//2)+1):
		for j in range(2*num, upper_bound, num):
			ind[j] = False
	for num in range(2, upper_bound):
		if ind[num] and num >= lower_bound:
			ret_val.append(num)
	print("Prime list made.")
	return ret_val

def serialize_prime_list(upper_bound):
	with open("/home/sean/workspace/projecteuler/primes_to_"+str(upper_bound)+".txt", "w") as f:
		pickle.dump(make_prime_list(upper_bound), f)

def unserialize_prime_list(upper_bound):
	with open("/home/sean/workspace/projecteuler/primes_to_"+str(upper_bound)+".txt", "r") as f:
		return pickle.load(f)

def is_in_prime_set(p, pset):
	return p in pset

def power_mod(a, exp, n):
	bitlist = []
	while exp > 0:
		bitlist.append(exp % 2)
		exp = exp >> 1
	d = 1
	while len(bitlist) > 0:
		d = (d * d) % n
		if bitlist.pop() == 1:
			d = (d * a) % n
	return d

def num_to_digs(n):
	l = []
	while n > 0:
		l.append(n % 10)
		n = n / 10
	l.reverse()
	return l

def digs_to_num(digs):
	return sum([10**(len(digs) - j - 1)*digs[j] for j in range(0, len(digs))])


def c(n, d):
	return factorial(n)/(factorial(d)*factorial(n-d))
	
#Read primes1.txt
def get_primes_n(ubound):
	plist=[]
	j = 1
	bound_reached = False
	while not bound_reached:
		with open("/home/sean/workspace/projecteuler/primes" + str(j) + ".txt", "r") as primes:
			for l in primes:
				ls = [int(u) for u in l.split()]
				if ls[-1] > ubound:
					ls = [u for u in ls if u <= ubound]
					plist += ls
					bound_reached = True
					break
				else:
					plist += ls
		j += 1
	return plist

def euler_totient(n, pset):
	ns = int(math.sqrt(n))+1
	ret_val =1 
	for p in pset:
		if p > ns: break
		if n == 1: break
		if n % p == 0:
			n = n / p
			ret_val *= p - 1
			while n % p == 0:
				ret_val *= p
				n /= p
	if n > 1:
		ret_val *= n - 1
	return ret_val

if __name__ == "__main__":
	serialize_prime_list(100000)
