'''Powerful digit counts
Problem 63

The 5-digit number, 16807=7^5, is also a fifth power. Similarly, the 9-digit number, 134217728=8^9, is a ninth power.

How many n-digit positive integers exist which are also an nth power?
'''
import math

nums = set()

for a in range(1, 10):
	for n in range(1, 40000):
		if n == int(float(n)*math.log10(a)) + 1:
			nums.add(a**n)
			print(a,n,a**n)
print("Answer: " + str(len(nums)))