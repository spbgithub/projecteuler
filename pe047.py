'''Distinct primes factors
Problem 47

The first two consecutive numbers to have two distinct prime factors are:

14 = 2 x 7
15 = 3 x 5

The first three consecutive numbers to have three distinct prime factors are:

644 = 2^2 x 7 x 23
645 = 3 x 5 x 43
646 = 2 x 17 x 19.

Find the first four consecutive integers to have four distinct prime factors. What is the first of these numbers?'''

import time


def prime_count(num):
	ret_val = 0
	div = 2
	while num > 1:
		if num % div == 0:
			ret_val += 1
			while num % div == 0:
				num = num / div
		if div > 2:
			div += 2
		else:
			div += 1
	return ret_val

start = time.time()

cur_int = 4
consecutive = []

while True:
	if prime_count(cur_int) == 4:
		consecutive = []
		consecutive.append(cur_int)
		j = 1
		while (prime_count(cur_int - j) == 4 and j < 4):
			consecutive.insert(0, cur_int - j)
			j += 1
		if len(consecutive) == 4: break
		j = 1
		while (prime_count(cur_int + j) == 4 and j < 4):
			consecutive.append(cur_int + j)
			j += 1
		if len(consecutive) >= 4: break
	cur_int += 4

print(consecutive)
print(time.time() - start)