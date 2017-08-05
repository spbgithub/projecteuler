'''Unfair race
Problem 573

n runners in very different training states want to compete in a race. Each one of them is given a different starting number k (1 <= k <= n) according to his (constant) individual racing speed being v_k=k/n.

In order to give the slower runners a chance to win the race, n different starting positions are chosen randomly (with uniform distribution) and independently from each other within the racing track of length 1. After this, the starting position nearest to the goal is assigned to runner 1, the next nearest starting position to runner 2 and so on, until finally the starting position furthest away from the goal is assigned to runner n. The winner of the race is the runner who reaches the goal first.

Interestingly, the expected running time for the winner is 1/2, independently of the number of runners. Moreover, while it can be shown that all runners will have the same expected running time of n/n+1, the race is still unfair, since the winning chances may differ significantly for different starting numbers:

Let P_n,k be the probability for runner k to win a race with n runners and E_n=\sum_k=k P_n,k be the expected starting number of the winner in that race. It can be shown that, for example, P_3,1=4/9, P_3,2=2/9, P_3,3=1/3 and E_3=179 for a race with 3 runners. 

You are given that E_4=2.21875, E_5=2.5104 and E_10=3.66021568.

Find E_1000000 rounded to 4 digits after the decimal point.'''

import math

def stirlingest(n,k):
	floatn = float(n)
	floatk = float(k)
	return math.sqrt(floatn/(2.0*math.pi*floatk*(floatn - floatk)))


def prodfrac(n,k):
	nkn     = n - 2*k + 1
	prodval = 1.0
	nminkovern = float(n-k)/float(n)
	for j in range(1,k):
		prodval *= float((n-j)*k*(n-k))/float((k-j)*n*n)
		while prodval > 1.0:
			prodval *= nminkovern
			nkn     -= 1
	while nkn > 0:
		prodval *= nminkovern
		nkn -= 1
	return prodval


def nextterm(lastterm, n, k):
	if k == 1: return math.exp((n-1)*(math.log(n-1) - math.log(n)))
	v1 = float(k-1)/float(k)
	v2 = float(n-k+1)/float(n-k)
	return lastterm / math.exp(float(k-1)*math.log(v1) + float(n-k)*math.log(v2))


nn = 1000000
kk = 1
kkmax = nn/2

#nextval  = prodfrac(nn,kk)
nextval = math.exp((nn-1)*(math.log(nn-1) - math.log(nn)))
print(nextval)
totalval = 1 + 2.0*nextval

kk += 1
while kk < kkmax:
	#if kk % 10000 == 0: print(kk)
	nextval = nextterm(nextval, nn, kk)
	totalval += 2.0*nextval
	kk      += 1
nextval = nextterm(nextval, nn, kk)
totalval += nextval
if nn % 2 != 0:
	totalval += nextval

print(totalval)