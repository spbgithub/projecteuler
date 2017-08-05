'''
Pandigital multiples
Problem 38

Take the number 192 and multiply it by each of 1, 2, and 3:

    192 x 1 = 192
    192 x 2 = 384
    192 x 3 = 576

By concatenating each product we get the 1 to 9 pandigital, 192384576. We will call 192384576 the concatenated product of 192 and (1,2,3)

The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4, and 5, giving the pandigital, 918273645, which is the concatenated product of 9 and (1,2,3,4,5).

What is the largest 1 to 9 pandigital 9-digit number that can be formed as the concatenated product of an integer with (1,2, ... , n) where n > 1?
'''

def fact(n):
	if n == 0: return 1
	return n * fact(n-1)

def lex_perm(sought_loc):
	ordered_digits = [1,2,3,4,5,6,7,8,9]
	div_size = 40320
	perm_digits = []
	while len(ordered_digits) > 1:
		digit, sought_loc = divmod(sought_loc, div_size)
		digit = ordered_digits[int(digit)]
		perm_digits.append(digit)
		ordered_digits.remove(digit)
		div_size = div_size / len(ordered_digits)
	perm_digits.append(ordered_digits.pop())
	return perm_digits

def dig_to_num(dig):
	return sum([dig[j]*10**(len(dig)-j-1) for j in range(0,len(dig))])


perm = fact(9)
while perm > 0:
	perm -= 1
	digits = lex_perm(perm)
	if dig_to_num(digits[0:4]) * 2 == dig_to_num(digits[4:]):
		perm = 0
print(dig_to_num(digits))