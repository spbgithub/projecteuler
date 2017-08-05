'''Counting Capacitor Circuits
Problem 155
An electric circuit uses exclusively identical capacitors of the same value C. 
The capacitors can be connected in series or in parallel to form sub-units, which can then be connected in series or in parallel with other capacitors or other sub-units to form larger sub-units, and so on up to a final circuit.

Using this simple procedure and up to n identical capacitors, we can make circuits having a range of different total capacitances. For example, using up to n=3 capacitors of 60 F each, we can obtain the following 7 distinct total capacitance values:

If we denote by D(n) the number of distinct total capacitance values we can obtain when using up to n equal-valued capacitors and the simple procedure described above, we have: D(1)=1, D(2)=3, D(3)=7 ...

Find D(18).
'''

from myfrac import myfrac

def maximum(u,v):
	if u > v: return u
	return v


D = [set(), {myfrac(1,1)}]
T = {myfrac(1,1)}
nmax = 18
print(1, len(T))
for n in range(2, nmax + 1):
	print("n=", n)
	D.append(set())
	j = 1
	while j <= n - j:
		print("Pairing up ", j, " and ", n-j)
		D[n] = D[n].union(a + b, for a in D[j] for b in D[n-j]})
		j += 1
	D[n] = D[n].union({a.reciprocal() for a in D[n]})
	T = T.union(D[n])
	print("Running total:", len(T), "\n")