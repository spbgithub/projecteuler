"""
Problem 12
Published on Friday, 8th March 2002, 06:00 pm; Solved by 131507; Difficulty rating: 5%
The sequence of triangle numbers is generated by adding the natural numbers. So the 7th triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28. The first ten terms would be:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

Let us list the factors of the first seven triangle numbers:

 1: 1
 3: 1,3
 6: 1,2,3,6
10: 1,2,5,10
15: 1,3,5,15
21: 1,3,7,21
28: 1,2,4,7,14,28
We can see that 28 is the first triangle number to have over five divisors.

What is the value of the first triangle number to have over five hundred divisors?
"""

import functools
import time

#we will reduce number of divisors of 2 by 1, to account for the 2 in the denominator of i(i+1)/2
def compute_divisors(n):
	divisors = {}
	nloc = n
	cd = 2
	while nloc > 1:
		if nloc % cd == 0:
			counter = 0
			while nloc % cd == 0:
				nloc = nloc/cd
				counter += 1
			if cd == 2:
				divisors[cd] = counter - 1
			else:
				divisors[cd] = counter
		if cd == 2:
			cd += 1
		else:
			cd += 2
	return divisors

def num_divisors(div_list):
	return functools.reduce(lambda u, v: u * v, [1+w for w in div_list.values()])

def tri(i):
	return i*(i+1)/2

def smallest_triangle():
	i = 2
	even_div = compute_divisors(i)
	odd_div = compute_divisors(i+1)
	num_even_div = num_divisors(even_div)
	num_odd_div = num_divisors(odd_div)

	while (num_even_div * num_odd_div < 501):
		#print(i, tri(i), num_even_div, num_odd_div, num_even_div * num_odd_div)
		i += 1
		if (i + 1) % 2 == 0:
			even_div = compute_divisors(i + 1)
			num_even_div = num_divisors(even_div)
		else:
			odd_div = compute_divisors(i + 1)
			num_odd_div = num_divisors(odd_div)
		
	return tri(i), num_even_div * num_odd_div

t1 = time.clock()
print(smallest_triangle())
print(time.clock() - t1)