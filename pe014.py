'''
Longest Collatz sequence
Problem 14
The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
'''

steps = [0]*1000001
steps[2] = 1
max_steps_loc = 2

for i in range(3,1000001):
	j = i
	cur_num_steps = 0
	while (j > 1000000 or steps[j] == 0):
		cur_num_steps += 1
		if j % 2 == 0:
			j = j//2
		else:
			j = 3*j + 1
	cur_num_steps += steps[j]
	steps[i] = cur_num_steps
	if (cur_num_steps > steps[max_steps_loc]):
		max_steps_loc = i

print(max_steps_loc, steps[max_steps_loc])