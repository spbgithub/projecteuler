'''Problem 401'''

from sympy.ntheory import divisor_sigma

#f = open("/home/macboyd/workspace/projecteuler/596py.txt", "w")

s = 0
for n in range(1, 795):
	s = s + divisor_sigma(n,2)
	#f.write(str(n) + ", " + str(s % 10**9) + "\n")
print(s % 10**9)
#f.close()