'''Magic 5-gon ring
Problem 68'''

from subset import subset, subset_n
from permutations import factorial

PERIOD = 5
SIZE   = 2 * PERIOD

def lex_perm_digs(sought_loc, ordered_digits, div_size):
	perm_digits = []
	cur_ind = 0
	while len(ordered_digits) > 1:
		digit, sought_loc = divmod(sought_loc, div_size)
		perm_digits.append(ordered_digits[int(digit)])
		ordered_digits.pop(digit)
		div_size = div_size / len(ordered_digits)
		cur_ind += 1

	perm_digits.append(ordered_digits.pop())
	return perm_digits

def out_string((inner, outer)):
	ret_val = ""
	for j in range(0, PERIOD):
		ret_val += str(outer[j])  + str(inner[j]) + str(inner[(j+1) % PERIOD])
	return ret_val

def complete_outer_ring(in_list, outer_set, out_list, found_strings):
	#if there are no more elements in the set of available outer elements, 
	#the n-gon ring is "magic". thus, we rotate the lists of inner and outer 
	#elements to get the minimum outer element in the first position on the
	#outer ring, then append to list of found "magic" n-gon rings
	if len(outer_set) == 0:
		found_strings.append(out_string(rotate_lists(in_list, out_list)))
	#this bootstraps the check for "magicality". recurse with each available element
	elif len(outer_set) == PERIOD:
		for o in outer_set:
			complete_outer_ring(in_list, outer_set - set([o]), [o], found_strings)
	#this actually does the check for "magicality" - having determined the sum in the
	#previous case, this verifies that the next sum in question can possibly have the same value
	else:
		digs_left = len(outer_set)
		maybe = in_list[1] + in_list[0] + out_list[0] - in_list[PERIOD-digs_left] - in_list[(PERIOD +1 -digs_left) % PERIOD]
		if in_list == [1,3,2] and out_list == [5,4]: print(in_list, out_list, outer_set, digs_left, maybe)
		if maybe in outer_set:
			complete_outer_ring([]+in_list, outer_set - set([maybe]), out_list + [maybe], found_strings)

def rotate_list(l, j):
	return l[j:]+l[:j]

def rotate_lists(inlist, outlist):
	j = outlist.index(min(outlist))
	return rotate_list(inlist,j), rotate_list(outlist,j)

found_strings = []

available_nums = set(range(1, SIZE+1))

in_sets = subset_n(list(available_nums - set([10])), PERIOD, [])
for i in in_sets:
	out_nums = available_nums - set(i)
	for sought in range(0, factorial(PERIOD - 1)):
		inner_ring = lex_perm_digs(sought, []+i[1:], factorial(PERIOD - 2))
		complete_outer_ring(i[0:1]+inner_ring, out_nums, [], found_strings)

for fs in found_strings:
	print(fs)

print("Soln:")
print(max(found_strings))