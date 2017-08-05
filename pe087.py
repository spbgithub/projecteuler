'''Prime power triples - Problem 87'''

from num_theo import unserialize_prime_list

primes = unserialize_prime_list(10000)

p2 = [p*p for p in primes if p <= 7071]
p3 = [p*p*p for p in primes if p <=369]
p4 = [p*p*p*p for p in primes if p <=85]

sumlist = [a + b + c for a in p2 for b in p3 for c in p4 if a + b + c < 50000000]
print(len(set(sumlist)))