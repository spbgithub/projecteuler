'''Path sum - four ways    Problem 83'''


'''Note: in order to not have to roll my own priority queue, we will use the
Python heapq functions as follows:
first, given the graph size, let n > 0 be such that 10**n > graph size. The edges of the graph have weight equal to the weight stored at the destination node. We can determine the maximum value of any such node; then the number we store is 10**n * w + l, where w is that weight and l is the node location. What this does is allow us to efficiently locate the node in the heap for the purpose of updating weights during the running of Dijkstra's algorithm, which is my choice for solving Problems 81, 82 and 83.


In fact, Problems 81, 82 and 83 will run with the same basic code, save for the graph
construction itself. In problems 81 and 83, we start at upper left and end at lower right, while in Problem 82 we start anywhere on the left and end anywhere on the right. The way we can make all of this work the same is to artificially add start and finish nodes. In Problems 81 and 83, our new start node will have precisely one outgoing edge which points to the upper left of the grid. In Problem 82, this node will point to each element of the left-most column. Analogous considerations abound for the finish node.'''

import math
from heapq import *

#create list of weights at nodes from text file - these serve as the edge weights
#in dijkstra's algorithm
weights = [0]
with open("/home/sean/workspace/projecteuler/p083_matrix.txt","r") as f:
	for l in f:
		weights += [int(u) for u in l.split(",")]
weights.append(0)
max_weight = sum(weights)
INFTY = 10**(int(math.log10(max_weight)) + 1)

#create edge list
n = int(math.sqrt(len(weights)-2))

SHIFT = 10**(int(math.log10(n*n+2))+1)

edges = []
for j in range(0, len(weights)-1):
	edges.append([])
	if j == 0:
		edges[j].append(1)
	else:
		if j % n != 0:
			edges[j].append(j+1)
		if j <=n*(n-1):
			edges[j].append(j+n)
		if j % n != 1:
			edges[j].append(j-1)
		if j > n:
			edges[j].append(j-n)
		if j == n*n:
			edges[j].append(n*n+1)
edges.append([])

#for k in range(0, len(edges)):
#	print(k, edges[k])

#update distance and prev lists
dist = []
prev = []
for j in range(0, len(weights)):
	if j == 0:
		dist.append(0)
	else:
		dist.append(INFTY)
	prev.append(False)

#create priority queue
pqueue = [10**n*dist[j] + j for j in range(0, len(weights))]
heapify(pqueue) #don't think I need to do this, given the way this is initialized

#implement dijkstra's algorithm
while len(pqueue) > 0:
	u = heappop(pqueue)
	dist_u, node_u = u // 10**n, u % 10**n
	for v in edges[node_u]:
		#print(node_u,v)
		alt = dist[node_u] + weights[v]
		if alt < dist[v]:
			old_dist_v = dist[v]
			dist[v] = alt
			prev[v] = node_u
			ind = pqueue.index(10**n*old_dist_v+v)
			pqueue[ind] = 10**n * dist[v] + v
			heapify(pqueue)


u = len(weights) - 1
output = []
while prev[u] > 0:
	output.append(weights[u])
	u = prev[u]
output.append(weights[u])

output.reverse()
print(sum(output), output)


