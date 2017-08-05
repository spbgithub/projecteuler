'''Permuted multiples
Problem 52

It can be seen that the number, 125874, and its double, 251748, contain exactly the same digits, but in a different order.

Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, contain the same digits.'''


n = 1
found = False

while not found:
	for j in range(0, 2*10**n/3 + 1):
		cur_num = 10**n + j
		dig_list = set([int(c) for c in str(cur_num)])
		found = True
		for k in range(2, 7):
			dig_list2 = set([int(c) for c in str(k * cur_num)])
			if dig_list != dig_list2:
				found = False
				break
		if found:
			print(cur_num)
			break
	n += 1
