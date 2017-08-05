from num_theo import gcd, power_mod, lcm
from sympy import nextprime

BOUND = 1000000

def list_to_past_1m(l):
	l = sorted(l)
	r = [(u,v) for (u,v) in l if u < 1.1*BOUND]
	return r

def pad_prime_list(l, p):
	lm = l[-1][0]
	n  = l[-1][1]
	while n < BOUND:
		l.append((lm*p, n*p))
		lm = l[-1][0]
		n  = l[-1][1]
	l.append((lm*p, n*p))
	return l


		


if __name__=="__main__":
	list1 = [(1,3), (2, 9)]
	list1 = pad_prime_list(list1, 3)

	metalist = []
	metalist.append(list1)

	p = 7
	while p < BOUND:
		print(p)
		list1   = pad_prime_list([(period_of_10(p), p)], p)
		metalist.append(list1)
		p = nextprime(p)

	metasize = len(metalist)
	while metasize > 1:
		print("size="+str(metasize))
		metalist2 = []
		while len(metalist) > 1:
			list1 = metalist.pop()
			list2 = metalist.pop()
			result  = [(lcm(a,b), u*v) for (a,u) in list1 for (b,v) in list2 if lcm(a, b) < 1.1*BOUND]
			metalist2.append(result)
		if len(metalist) == 1:
			metalist2.append(metalist.pop())
		metalist = list(metalist2)
		metasize = len(metalist)

	list1.reverse()
	print(list1)
