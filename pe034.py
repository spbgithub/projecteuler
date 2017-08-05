'''Digit factorials
Problem 34

145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

Find the sum of all numbers which are equal to the sum of the factorial of their digits.

Note: as 1! = 1 and 2! = 2 are not sums they are not included.'''

#note: this requires six or fewer digits: if n is the number of digits, then 10**n - 1 > n*9!, the maximum possible factorial digit sum

def fact(n):
	if n == 0: return 1
	return n * fact(n-1)

factlist = [fact(n) for n in range(0,10)]

def fact_dig_sum(n):
	nwork = n
	cur_sum = 0
	while nwork > 0:
		cur_sum += factlist[nwork % 10]
		nwork = nwork / 10
	return cur_sum


print(sum([u for u in range(10,1000000) if u == fact_dig_sum(u)]))
