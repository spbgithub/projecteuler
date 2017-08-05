'''Problem 86
Note: testing for m<=100 yields the qty listed in problem statement

'''

from math import sqrt

def is_square(n):
	n2 = int(sqrt(n))
	return n2*n2 == n

def min_path_is_int(a,b,c):
	return is_square((a+b)*(a+b) + c*c)

m = 1
count = 0
for m in range(1, 1001):
	for y in range(1, m+1):
		for x in range(1, y+1):
			if min_path_is_int(x,y,m):
				count += 1
	if count > 1000000:
		print("Answer is " + str(m) + ", " + str(count))
		break
	print(str(m) + "," + str(count))