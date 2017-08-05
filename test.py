#! /usr/bin/python3
from sympy.utilities.iterables import partitions

def par_prod_cnt(p):
	prod = 1
	cnt  = 0
	for n in p:
		prod *= n**p[n]
		cnt  += p[n]
	return prod, cnt


boolloop = True
n = 1
while n < 50:
	lst_pars = {}
	pars     = [p.copy() for s, p in partitions(n, m=n, size=True)]
	for p in pars:
		prod, cnt = par_prod_cnt(p)
		if (prod, cnt) not in lst_pars:
			lst_pars[(prod, cnt)] = []
		lst_pars[(prod, cnt)].append(p.copy())
	for l in lst_pars:
		if len(lst_pars[l]) > 1:
			#boolloop = False
			print(n, l, lst_pars[l])
			#break
	n += 1