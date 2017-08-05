'''Sub-string divisibility
Problem 43

The number, 1406357289, is a 0 to 9 pandigital number because it is made up of each of the digits 0 to 9 in some order, but it also has a rather interesting sub-string divisibility property.

Let d1 be the 1st digit, d2 be the 2nd digit, and so on. In this way, we note the following:

    d2d3d4=406 is divisible by 2
    d3d4d5=063 is divisible by 3
    d4d5d6=635 is divisible by 5
    d5d6d7=357 is divisible by 7
    d6d7d8=572 is divisible by 11
    d7d8d9=728 is divisible by 13
    d8d9d10=289 is divisible by 17

Find the sum of all 0 to 9 pandigital numbers with this property.
'''

import math

prime_list = [2,3,5,7,11,13,17]

def fact(n):
	if n == 0: return 1
	return n * fact(n-1)

start_div_size = fact(9)
num_pan_ints = fact(10)

def dig_to_num(dig):
	return sum([dig[j]*10**(len(dig)-j-1) for j in range(0,len(dig))])

def lex_perm(sought_loc):
	ordered_digits = [0,1,2,3,4,5,6,7,8,9]
	div_size = start_div_size
	perm_digits = []
	cur_ind = 0
	while len(ordered_digits) > 1:
		digit, sought_loc = divmod(sought_loc, div_size)
		digit = ordered_digits[int(digit)]
		if (cur_ind == 3) and digit % 2 != 0:
			return False, []
		if (cur_ind == 5) and digit % 5 != 0:
			return False, []
		perm_digits.append(digit)
		ordered_digits.remove(digit)
		div_size = div_size / len(ordered_digits)
		cur_ind += 1
	perm_digits.append(ordered_digits.pop())
	return True, perm_digits

summ = 0
for perm in range(0, num_pan_ints):
	check, pan_num = lex_perm(perm)
	if check:
		cond = True
		test_num = dig_to_num(pan_num[0:3])
		for i in range(0,7):
			test_num = 10*(test_num % 100) + pan_num[i+3]
			if test_num % prime_list[i] != 0:
				cond = False
				break
		if cond:
			summ += dig_to_num(pan_num)
print(summ)