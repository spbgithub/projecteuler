'''Problem 90'''

from sympy.combinatorics.subsets import ksubsets

count = 0
for set1 in ksubsets([0,1,2,3,4,5,6,7,8,9], 6):
	for set2 in ksubsets([0,1,2,3,4,5,6,7,8,9],6):
		s = [(a,b) for a in set1 for b in set2]
		#print(set1, set2, s)
		if set1 <= set2:
			if ((1,0) in s or (0,1) in s) and ((4,0) in s or (0, 4) in s) and ((6,0) in s or (0,6) in s or (9,0) in s or (0,9) in s) and ((1,6) in s or (6,1) in s or (1,9) in s or (9,1) in s) and ((2,5) in s or (5,2) in s) and ((6,3) in s or (3,6) in s or (9,3) in s or (3, 9) in s) and ((9,4) in s or (6,4) in s or (4,9) in s or (4,6) in s) and ((8,1) in s or (1,8) in s):
				#print(set1)
				#print(set2)
				#print(s)
				count += 1
		#if set1 == set2:
		#	count += 1
#print(count//2)
print(count)