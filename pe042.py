'''Coded triangle numbers
Problem 42

The nth term of the sequence of triangle numbers is given by, tn = n(n+1)/2; so the first ten triangle numbers are:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

By converting each letter in a word to a number corresponding to its alphabetical position and adding these values we form a word value. For example, the word value for SKY is 19 + 11 + 25 = 55 = t10. If the word value is a triangle number then we shall call the word a triangle word.

Using words.txt (right click and 'Save Link/Target As...'), a 16K text file containing nearly two-thousand common English words, how many are triangle words?'''

import math

def char_to_int(char):
	return ord(char) - 64

def word_to_score(s):
	return sum([char_to_int(c) for c in s])

def is_triangular(num):
	a = int(math.sqrt(1 + 8 * num))
	return a*a == 1+8*num and a % 2 != 0

words = []
with open("/home/sean/workspace/projecteuler/p042_words.txt", 'r') as f:
	for l in f:
		words = l.split(",")
count = 0
print(words)
for w in words:
	score = word_to_score(w[1:-1])
	if is_triangular(score):
		count += 1
print(count)
print(is_triangular(1))