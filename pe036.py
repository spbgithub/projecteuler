'''Double-base palindromes
Problem 36

The decimal number, 585 = 1001001001_2 (binary), is palindromic in both bases.

Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.

(Please note that the palindromic number, in either base, may not include leading zeros.)'''

import time

def base_reverse(num, base):
	worknum = 0
	while num > 0:
		worknum = base * worknum + (num % base)
		num = num / base
	return worknum

def is_bin_palindrome(num):
	return num == base_reverse(num, 2)


#note: even numbers can be ignored...all of these have trailing zeros in their
#binary expansion, and therefore cannot be palindromic

#how to generate the decimal palindromes?

start = time.time()

print(sum([num for num in [u for u in range(1,10)] + [11*u for u in range(1,10)] + [101*u + 10*v for u in range(1,10) for v in range(1,10)] + [100*u + base_reverse(u, 10) for u in range(10,100)] + [1000*u + 100*v + base_reverse(u, 10) for u in range(10,100) for v in range(1,10)] + [1000*u + base_reverse(u, 10) for u in range(100,1000)] if is_bin_palindrome(num)]))

print time.time() - start