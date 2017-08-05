'''
Lexicographic permutations
Problem 24

A permutation is an ordered arrangement of objects. For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4. If all of the permutations are listed numerically or alphabetically, we call it lexicographic order. The lexicographic permutations of 0, 1 and 2 are:

012   021   102   120   201   210

What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?
'''

def fact(n):
	if n == 0: return 1
	return n * fact(n-1)

ordered_digits = [0,1,2,3,4,5,6,7,8,9]
div_size = fact(len(ordered_digits) - 1)
sought_loc = 1000000 - 1

perm_digits = []

while len(ordered_digits) > 1:
	digit, sought_loc = divmod(sought_loc, div_size)
	digit = ordered_digits[int(digit)]
	perm_digits.append(digit)
	ordered_digits.remove(digit)
	div_size = div_size / len(ordered_digits)
perm_digits.append(ordered_digits.pop())
print(perm_digits)
