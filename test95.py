from time import time;t=time();
L=10**6+1;
sd=[0]*L;
for i in xrange(1,L):
	for j in xrange(2*i,L,i):
		sd[j]+=i;
tested=set();max=0;
for n in xrange(L):
	if n in tested : 
		continue;
	m=sd[n];l=[n];
	while m<=L and m not in l and m>1:
		if m in tested : 
			break;
		l.append(m);
		m=sd[m];
	for x in l : 
		tested.add(x);
	if m in l : 
		k=1;i=len(l)-1;
		while l[i]!=m:
			i-=1;
			k+=1;
		if k>max : 
			max,sol=k,m
		

t=1000*(time()-t);
print "the number %d gives a cycle of length %d, this took %d secs %d ms." % (sol,max,t/1000,t%1000)