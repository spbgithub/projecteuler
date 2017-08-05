import num_theo



def lex_perm_digs(sought_loc, ordered_digits):
	div_size = factorial(len(ordered_digits)-1)
	perm_digits = []
	cur_ind = 0
	while len(ordered_digits) > 1:
		digit, sought_loc = divmod(sought_loc, div_size)
		perm_digits.append(ordered_digits[int(digit)])
		ordered_digits.pop(digit)
		div_size = div_size / len(ordered_digits)
		cur_ind += 1

	perm_digits.append(ordered_digits.pop())
	return num_theo.digs_to_num(perm_digits)

def factorial(n):
	ret = 1
	while n > 1:
		ret *= n
		n -= 1
	return ret

def is_perm(perm1, perm2):
	return sorted(perm1) == sorted(perm2)

if __name__ == "__main__":
	for j in range(0, 6):
		print(lex_perm_digs(j, [1, 2, 3]))