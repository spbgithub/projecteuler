import time

def is_subpandig(num, length):
	l = [int(c) for c in str(num)]
	while len(l) < length:
		l = [0] + l
	return len(set(l)) == length, l

def dig_to_num(dig):
	return sum([dig[j]*10**(len(dig)-j-1) for j in range(0,len(dig))])

start = time.time()

prime_list = [2,3,5,7,11,13]
dig_list = [0,1,2,3,4,5,6,7,8,9]
p = 17
pan_list = []

ret_val = 0
cur_val = p
while (cur_val < 1000):
	is_pan, l = is_subpandig(cur_val, 3)
	if is_pan:
		pan_list.append(l)
	cur_val += p

while len(pan_list) > 0:
	l = pan_list.pop(0)
	if len(l) == 9:
		last_dig = list(set(dig_list) - set(l))
		ret_val += dig_to_num(last_dig + l)
	else:
		for dig in range(0,10):
			is_pan, l2 = is_subpandig(10**len(l)*dig + dig_to_num(l), len(l)+1)
			if is_pan and dig_to_num(l2[0:3]) % prime_list[9 - len(l2)] == 0:
				pan_list.append(l2)
print(ret_val)

print(time.time() - start)