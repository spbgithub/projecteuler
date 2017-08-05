'''Problem 86
First: we assume that l >= w >= h. Then the min distance is given by
\sqrt{(w+h)^2 + l^2}. 



'''

from math import sqrt
import time

def gcd(a,b):
	if a < b:
		return gcd(b,a)
	else:
		while b > 0:
			a, b = b, a % b
		return a

def dot_prod(v,w):
	return v[0]*w[0] + v[1]*w[1] + v[2]*w[2]

def apply_matrix(m, v):
	return [dot_prod(m[0], v), dot_prod(m[1], v), dot_prod(m[2], v)]

#user Berggrem matrices to produce all primitive triples representing all right
#triangles with at least one leg less than the max size specified
def triples_to_size(max_size):
	#Berggren matrices
	m = []
	m.append([[1, -2,  2], [2, -1, 2], [2, -2, 3]])
	m.append([[1, 2, 2], [2, 1, 2], [2, 2, 3]])
	m.append([[-1, 2, 2], [-2, 1, 2], [-2, 2, 3]])

	triples = []
	triples.append([3,4,5])
	j = 0
	while j < len(triples):
		if min(triples[j][0], triples[j][1]) <= max_size:
			for k in range(0,3):
				triples.append(sorted(apply_matrix(m[k], triples[j])))
		j += 1
	return triples

#given a pythagorean triple (a,b,c) with a<b<c, c for our purposes
#represents the minimum distance as specified in the problem. if we assume
#that a box has dimensions l,w,h with l>=w>=h, then this minimum distance can be shown
#to be sqrt((w+h)^2 + l^2). thus, we have either w+h=a and l=b, or l=a and w+h=b. we have
#in either case that l is specified, and a natural range of values for w and h are then determined.

def triples_to_counts(triple, max_size, tracker):
	for q in range(1, (max_size // triple[1]) + 1):
		l = q * triple[1]
		w = q*triple[0] - 1
		h = 1
		if (w-h) % 2 == 0:
			tracker[l] += (w-h)/2 + 1
		else:
			tracker[l] += (w - h - 1)/2 + 1

	if 2*triple[0] > triple[1]:
		for q in range(1, (max_size // triple[0]) + 1):
			l = q * triple[0]
			w = l
			h = q * triple[1] - w
			if (w-h) % 2 == 0:
				tracker[l] += (w-h)/2 + 1
			else:
				tracker[l] += (w - h - 1)/2 + 1


MAX_BOX_SIZE = 20000

#make pythagorean triples
print("Making triples")
store_triples = triples_to_size(MAX_BOX_SIZE)
print("Triples made")


#turn this into boxes
print("Compute box sizes")
box_max = [0]*(MAX_BOX_SIZE + 1)

for t in store_triples:
	triples_to_counts(t, MAX_BOX_SIZE, box_max)
print("Boxes made")

print("Computing sums")
box_sum = [0]*(MAX_BOX_SIZE + 1)
box_sum[0] = box_max[0]
for j in range(1, MAX_BOX_SIZE + 1):
	box_sum[j] = box_sum[j-1] + box_max[j]

for j in range(0, len(box_sum)):
	if box_sum[j] > 1000000:
		print(j, box_sum[j])
		break


