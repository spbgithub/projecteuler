def int_to_list(n):
	ret_list = []
	ret_list2 = []
	nlocal = n
	r = 0
	while (nlocal > 0):
		r = nlocal % 10
		ret_list.append(r)
		ret_list2.append(r)
		nlocal = (nlocal - r)//10
	return ret_list, ret_list2

def largest_palindrome():
	max_palindrome = 0
	list_a = []
	list_b = []
	min_num = 100
	max_num = 999
	i = min_num
	while (i <= max_num):
		j = min_num
		while (j <= i):
			list_a, list_b = int_to_list(i*j)
			list_b.reverse()
			if (list_a == list_b):
				if i*j > max_palindrome:
					max_palindrome = i*j
			j = j + 1
		i = i + 1
	return max_palindrome

print(largest_palindrome())