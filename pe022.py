'''
Names scores
Problem 22

Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first names, begin by sorting it into alphabetical order. Then working out the alphabetical value for each name, multiply this value by its alphabetical position in the list to obtain a name score.

For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would obtain a score of 938 x 53 = 49714.

What is the total of all the name scores in the file?

'''

chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
char_pos = 0
char_vals = {}
for c in chars:
	char_pos += 1
	char_vals[c] = char_pos

def name_score(name):
	score = 0
	for c in name:
		score += char_vals[c]
	return score

with open("/home/sean/workspace/projecteuler/p022_names.txt", "r") as f:
	for l in f:
		names = [u[1:-1] for u in l.split(",")]
names.sort()

cur_name_index = 0
total = 0
for name in names:
	cur_name_index += 1
	total += cur_name_index * name_score(name)

print(total)

