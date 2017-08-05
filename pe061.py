'''Cyclical figurate numbers
Problem 61

Triangle, square, pentagonal, hexagonal, heptagonal, and octagonal numbers are all figurate (polygonal) numbers and are generated by the following formulae:
Triangle 	  	P3,n=n(n+1)/2 	  	1, 3, 6, 10, 15, ...
Square 	  	    P4,n=n2 	  	    1, 4, 9, 16, 25, ...
Pentagonal 	  	P5,n=n(3n-1)/2 	  	1, 5, 12, 22, 35, ...
Hexagonal 	  	P6,n=n(2n-1) 	  	1, 6, 15, 28, 45, ...
Heptagonal 	  	P7,n=n(5n-3)/2 	  	1, 7, 18, 34, 55, ...
Octagonal 	  	P8,n=n(3n-2) 	  	1, 8, 21, 40, 65, ...

The ordered set of three 4-digit numbers: 8128, 2882, 8281, has three interesting properties.

    The set is cyclic, in that the last two digits of each number is the first two digits of the next number (including the last number with the first).
    Each polygonal type: triangle (P3,127=8128), square (P4,91=8281), and pentagonal (P5,44=2882), is represented by a different number in the set.
    This is the only set of 4-digit numbers with this property.

Find the sum of the only ordered set of six cyclic 4-digit numbers for which each polygonal type: triangle, square, pentagonal, hexagonal, heptagonal, and octagonal, is represented by a different number in the set.
'''
import time

def fc(remaining, num_stack, polys):
	if len(remaining) == 0:
		if num_stack[-1] % 100 == num_stack[0] / 100:
			print(num_stack, sum(num_stack))
		return
	else:
		for i in remaining:
			cur_list = [u for u in polys[i] if u / 100 == num_stack[-1] % 100]
			if len(cur_list) == 0:
				return
			else:
				for p in cur_list:
					num_stack.append(p)
					fc(remaining - set([i]), num_stack, polys)
					num_stack.pop()
	return
start = time.time()

polys = [[]]*6
polys[0] = [n*n for n in range(15, 200) if n*n > 1000 and n*n < 10000]
polys[1] = [(n*(n+1)/2) for n in range(15, 200) if (n*(n+1)/2) > 1000 and (n*(n+1)/2) < 10000]
polys[2] = [(n*(3*n-1)/2) for n in range(15, 200) if (n*(3*n-1)/2) > 1000 and (n*(3*n-1)/2) < 10000]
polys[3] = [(n*(2*n-1)) for n in range(15, 200) if (n*(2*n-1)) > 1000 and (n*(2*n-1)) < 10000]
polys[4] = [(n*(5*n-3))/2 for n in range(15, 200) if (n*(5*n-3))/2 > 1000 and (n*(5*n-3))/2 < 10000]
polys[5] = [n*(3*n-2) for n in range(15, 200) if (n*(3*n-2)) > 1000 and n*(3*n-2) < 10000]

cur_list = polys[0]
for p in cur_list:
	fc(set([1,2,3,4,5]), [p], polys)
print(time.time() - start)