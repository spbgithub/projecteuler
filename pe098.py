'''Problem 98'''

from functools import reduce
from math import sqrt
import time

#takes, for instance, "banana" and returns "aaabnn"
def key_from_string(st):
	return reduce(lambda m,n: m+n, sorted(st))

#takes a key value (for instance, "aaabnn" for "banana", and returns "111233". this allows us
#to quickly determine if a given number can be fit into a given word via identifying
#letters and numbers. it does NOT say whether a given number will match a given word in this fashion
def signature(keyval):
	retval = ''
	symb   = 64
	char   = ''
	for c in keyval:
		if c != char:
			char  = c
			symb += 1
		retval += chr(symb)
	return retval

#returns a list from the input file, assumed to be comma-and-quote-delimited
def list_from_cdelim(pathname):
	with open(pathname, "r") as f:
		cdwords = ""
		for l in f:
			cdwords += l
	return [u[1:-1] for u in l.split(",")]

def read_ospd():
	with open("/home/sean/workspace/projecteuler/ospd.txt","r") as f:
		return [l for l in f]

#we store the words grouped by the signature, then by key value
#also, keep track of the maximum length word, as that determines where we 
#start searching for squares with the needed property
def words_to_struct(wordlist):
	groups = {}
	for w in wordlist:
		key  = key_from_string(w)
		if key not in groups:
			groups[key] = []
		groups[key].append(w)
	groups = {k:groups[k] for k in groups if len(groups[k]) > 1}
	retval = {}
	for g in groups:
		sig = signature(g)
		if sig not in retval:
			retval[sig] = {}
		retval[sig][g] = groups[g]
	return retval

#instead of considering all squares in the indicated range, we want to only
#consider those than HAVE a permutation which is a square. so given the max number
#of digits, 
def compute_valid_squares(maxlen, words):
	squarelist = []
	squarekeys = {}
	for u in range(int(sqrt(10**maxlen)), 0, -1):
		s = u*u
		skey = key_from_string(str(s))
		ssig = signature(skey)
		if ssig in words:
			if skey not in squarekeys:
				squarekeys[skey] = []
			squarekeys[skey].append(s)

	squarekeys = {k:squarekeys[k] for k in squarekeys if len(squarekeys[k]) > 1}
	squarelist = []
	for k in squarekeys:
		squarelist += squarekeys[k]
	return squarelist

#compares number and word, returning a (consistent) pairing of digits to characters
#if such a matching is possible, and returns False if such a matching is not possible
def pair_nums_to_chars(num, chars):
	num = str(num)
	val = {}
	for j in range(0, len(chars)):
		if chars[j] not in val:
			val[chars[j]] = int(num[j])
		if int(num[j]) != val[chars[j]]:
			return False
	return val

#takes the matching provided by pair_nums_to_chars() and computes the number
#derived from the current anagram word
def compute_number_from_charvals(vallist, word):
	val = 0
	for c in word:
		val = 10*val + vallist[c]
	return val

#given the current square, look through all groups of anagrams to determine if
#any such group yields at least two squares. returns the argument num if
#this succeeds, and False if it fails
def check_for_square_pairs(num, words, squares):
	key = key_from_string(str(num))
	sig = signature(key)
	wlists = words[sig]
	for k in wlists:
		curwords = wlists[k]
		for w in curwords:
			vallist = pair_nums_to_chars(str(num), w)
			if vallist:
				for w2 in curwords:
					if w2 != w:
						if compute_number_from_charvals(vallist, w2) in squares:
							return num
	return False


if __name__=="__main__":
	start = time.time()
	#first, we need to read in the list of words and group by signature, then by key value
	words = list_from_cdelim("/home/sean/workspace/projecteuler/p098_words.txt")
	#words = read_ospd()
	#print(len(words))
	words = words_to_struct(words)
	maxlen = max(len(w) for w in words)

	#generate list of squares - this ends up being a fairly short list. sort them in
	#decreasing order
	squares = compute_valid_squares(maxlen, words)
	squares = sorted(squares)
	squares.reverse()
	squareset = set(squares)

	#now, run the check - print any squares that pass the test (the first one is the
	#answer we seek)
	for s in squares:
		if check_for_square_pairs(s, words, squareset): 
			print(s)
			break
	print(time.time() - start)