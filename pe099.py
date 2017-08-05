'''Largest exponential - Problem 99'''

from math import log10


with open("/home/sean/workspace/projecteuler/p099_base_exp.txt","r") as f:
	vals = [float(l.split(",")[1])*log10(float(l.split(",")[0])) for l in f]
print(1+vals.index(max(vals)))