'''Combinatoric Selections
Problem 53

How many, not necessarily distinct, values of  nCr, for 1 <= n <= 100, are greater than one-million?
 '''
import time

start = time.time()
cold = [1,2,1]
c = [0]*4
the_count = 0
target = 1000000
for n in range(3, 101):
	c = [0]*(n+1)
	for j in range(0, (n+1)):
		if j == 0 or j == n:
			c[j] = 1
		else:
			c[j] = cold[j] + cold[j-1]
			if c[j] > target:
				the_count += 1
	cold = [] + c
	
print(the_count)
print(time.time() - start)