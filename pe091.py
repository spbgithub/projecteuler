'''Problem 91'''

from math import gcd
from time import time

start = time()
M = 50

total = 3 * M**2  	#this accounts for the M^2 triangles with right angle at the origin, M^2 triangles with one leg and right angle on the positive vertical axis, and the M^2 triangles with one leg and right angle on the positive horizontal axis

for a in range(1, M+1):
	for b in range(1, M+1):
		d = gcd(a,b)
		#Every other triangle has right angle off of the axes. If (a,b) are the coordinates of the vertex with the right angle and (c,d) are the coordinates of the other vertex, then orthogonality leads to the condition ac + bd = a^2 + b^2. Since (a,b) divides a^2 + b^2, this leads to solutions (c,d) which can be found as follows: it is clear that one solution is (c,d) = (a,b). Of course, this does not lead to a triangle, but it allows us to parameterize the entire solution space as (a + (b/d)t, b - (a/d) t), where d = (a,b) and t is an integer. Then t must satisfy the inequalities 0 <= a + (b/d)t <= M, 0 <= b - (a/d) t <= M; the set of common solutions is easily solved.
		total += min( (a*d)//b, (d*(M-b))//a) + min( (d*b)//a , (d*(M-a)) // b)
print(total)
print(time() - start)