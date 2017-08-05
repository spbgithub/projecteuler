import time
import sys

sys.setrecursionlimit(10000)

MAX_PER = 100000000

def t1a(a,b,c):
	return a - 2*b + 2*c

def t1b(a,b,c):
	return 2*a - b + 2*c

def t1c(a,b,c):
	return 2*a - 2*b + 3*c

def t2a(a,b,c):
	return a + 2*b + 2*c

def t2b(a,b,c):
	return 2*a + b + 2*c

def t2c(a,b,c):
	return 2*a + 2*b + 3*c

def t3a(a,b,c):
	return -a + 2*b + 2*c

def t3b(a,b,c):
	return -2*a + b + 2*c

def t3c(a,b,c):
	return -2*a + 2*b + 3*c

def new_triple(a,b,c):
	if a + b + c >= MAX_PER: return 0
	ret_val = 0
	if c % (b - a) == 0:
		ret_val = MAX_PER//(a+b+c)
	#return ret_val + new_triple(t1a(a,b,c), t1b(a,b,c), t1c(a,b,c)) + new_triple(t2a(a,b,c), t2b(a,b,c), t2c(a,b,c)) + new_triple(t3a(a,b,c), t3b(a,b,c), t3c(a,b,c))
	return ret_val + new_triple(t2a(a,b,c),t2b(a,b,c),t2c(a,b,c))
      
start = time.time()
print(new_triple(3,4,5))
print(time.time() - start)