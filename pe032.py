'''Pandigital products
Problem 32

We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once; for example, the 5-digit number, 15234, is 1 through 5 pandigital.

The product 7254 is unusual, as the identity, 39 x 186 = 7254, containing multiplicand, multiplier, and product is 1 through 9 pandigital.

Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.'''

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

def lex_perm2(sought_perm):
    digits = [1,2,3,4,5,6,7,8,9]
    cur_index = 0
    div_size = 40320

    while (cur_index < 8):
        digit = sought_perm / div_size;
        sought_perm = sought_perm % div_size;
        swap = digits[cur_index + digit]
        j = cur_index + digit
        while j > cur_index:
            digits[j] = digits[j-1]
        digits[cur_index] = swap
        div_size = div_size/(8 - cur_index)
        cur_index += 1
    return digits

def list_slice_to_int(int_list):
	ret_val = 0
	power = 1
	while len(int_list) > 0:
		ret_val += power * int_list.pop()
		power *= 10
	return ret_val

pattern_list = [[0,1,5,9], [0, 2, 5, 9], [0, 3, 6, 9]]

def is_pandigital(dig_list, pattern):
	a  = list_slice_to_int(dig_list[pattern[0]:pattern[1]])
	b  = list_slice_to_int(dig_list[pattern[1]:pattern[2]])
	if a > b: return False, 0
	ab = list_slice_to_int(dig_list[pattern[2]:pattern[3]])
	if a * b == ab: 
		print(a, b, ab)
		return True, ab
	return False, 0

if __name__ == "__main__":
	num_perms = fact(9)
	prods = []
	for n in range(0, num_perms):
		dig_list = lex_perm(n)
		for pattern in pattern_list:
			is_pan, prod = is_pandigital(dig_list, pattern)
			if is_pan:
				prods.append(prod)
	print(prods)
	print(sum(list(set(prods))))
