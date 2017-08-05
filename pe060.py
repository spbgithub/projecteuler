'''Prime pair sets
Problem 60

The primes 3, 7, 109, and 673, are quite remarkable. By taking any two primes and concatenating them in any order the result will always be prime. For example, taking 7 and 109, both 7109 and 1097 are prime. The sum of these four primes, 792, represents the lowest sum for a set of four primes with this property.

Find the lowest sum for a set of five primes for which any two primes concatenate to produce another prime.'''

import num_theo
import miller_rabin
import math
from subset import subset_n

#def concat_nums(m,n):#
#	return num_theo.digs_to_num(num_theo.num_to_digs(m) + num_theo.num_to_digs(n))

def concat_nums(m,n):
	u = int(math.log10(n))+1
	return (10**u*m) + n

def our_prime_test(p, pset, psetmax):
	if p < psetmax:
		return p in pset
	else:
		return miller_rabin.is_strong_pseudoprime_milrab(p, 10)


def bron_kerbosch1(r, p, x, graph):
	global clique_list
	if len(p) == 0 and len(x) == 0:
		clique_list.append(r)
	else:
		for v in p:
			neighbors = set(graph[v])
			bron_kerbosch1(r | set([v]), p & neighbors, x & neighbors, graph)
			p = p - set([v])
			x = x | set([v])

tuple_size = 5
prime_bound = 10000
prime_check_bound = 15485863
prime_graph = num_theo.make_prime_list(prime_bound)

#Read primes1.txt
prime_check = []
with open("/home/sean/workspace/projecteuler/primes1.txt", "r") as primes:
	for l in primes:
		prime_check += [int(u) for u in l.split()]
prime_check = set(prime_check)

print("Prime lists created.")

#prime_check = set(num_theo.unserialize_prime_list(prime_check_bound))
clique_list = []

#prime_graph has our list of nodes
graph = {}
for j in range(0, len(prime_graph)):
#for p in prime_graph:
	graph[prime_graph[j]] = []
	for i in range(0, j):
	#for q in [z for z in prime_graph if z < p]:
		if our_prime_test(concat_nums(prime_graph[j],prime_graph[i]), prime_check, prime_check_bound) and our_prime_test(concat_nums(prime_graph[i],prime_graph[j]), prime_check, prime_check_bound):
			graph[prime_graph[i]].append(prime_graph[j])
			graph[prime_graph[j]].append(prime_graph[i])

print("Graph made.")

bron_kerbosch1(set(), set(graph.keys()), set(), graph)

for c in [u for u in clique_list if len(u) >= tuple_size]:
	print(c, sum(c))