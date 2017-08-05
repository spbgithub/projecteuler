# -*- coding: utf-8 -*-
"""
Problem 122 - Efficient exponentiation
Algorithm is a modification of Dijkstra's Algorithm
Modification is due to the following considerations: it is possible that there
is more than one way to compute the most efficient exponentiation. For instance, we could
compute p^15 as is done in the problem statement:
	p    * p    = p^2
	p^2  * p    = p^3
	p^3  * p^3  = p^6
	p^6  * p^6  = p^12
	p^12 * p^3  = p^15

We could also do it like this:
	p    * p    = p^2
	p^2  * p    = p^3
	p^3  * p^2  = p^5
	p^5  * p^5  = p^10
	p^10 * p^5  = p^15

So in computing which exponents can be achieved in six steps, given that the process has
reached p^15 in 5 steps, we have two separate paths to consider. 
"""
import math
from heapq import heapify, heappush, heappop

UBOUND = 200

dist        = [math.inf for j in range(0, UBOUND + 1)]
dist[0]     = 0
dist[1]     = 0
prev        = []
for j in range(0, UBOUND+1):
	prev.append(set())
inlinks     = [[]]*(UBOUND + 1)

inlinks[1].append(set([1]))
nodes_to_do = [(dist[j],j) for j in range(1, UBOUND + 1)]
heapify(nodes_to_do)


total = 0
while len(nodes_to_do) > 0:	
	d, j = heappop(nodes_to_do)
	for curpath in [c for c in inlinks[j] if len(c) > 0]:
		for k in curpath:
			if k + j <= UBOUND:
				#first case: node hasn't been encountered before
				if dist[k+j] == math.inf:
					dist[k+j] = dist[j] + 1
					inlinks[k+j] = []
					inlinks[k+j].append(curpath | set([k+j]))
					prev[k+j].add(j)
				else:
					if dist[k+j] == dist[j] + 1:
						inlinks[k+j].append(curpath | set([k+j]))
						prev[k+j].add(j)
					elif dist[j] + 1 < dist[k+j]:
						for u in range(0, len(nodes_to_do)+1):
							if nodes_to_do[u][1] == k + j:
								nodes_to_do.pop(u)
								heapify(nodes_to_do)
								break
						dist[k+j] = dist[j] + 1
						inlinks[k+j] = []
						inlinks[k+j].append(curpath | set([k+j]))
						prev[k+j] = set([j])
						heappush(nodes_to_do, (dist[k+j], k+j))

print(dist)
print(sum(dist))


def print_predecessor(cur_val, prev_list, cur_list):
	if cur_val == 1:
		print(cur_list + [1])
	else:
		for p in prev_list[cur_val]:
			print_predecessor(p, prev_list, cur_list + [p])


print_predecessor(200, prev, [])