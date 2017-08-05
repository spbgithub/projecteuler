'''Problem 92'''

def digit_sum_square(n):
	ret = 0
	while n > 0:
		ret += (n % 10)**2
		n = n // 10
	return ret


goes_to_1  = set([1, 10, 13, 32, 44])
goes_to_89 = set([85,89,145,42,20,4,16,37,58])
MAX = 10000000
k = 1
total = 0
while k <= MAX:
	if k % 100000 == 0: print(k)
	stack = [k]
	while True:
		if stack[-1] in goes_to_1:
			while len(stack) > 0:
				goes_to_1.add(stack.pop())
			break
		if stack[-1] in goes_to_89:
			while len(stack) > 0:
				goes_to_89.add(stack.pop())
			total += 1
			break
		stack.append(digit_sum_square(stack[-1]))
	k += 1
print(total)
