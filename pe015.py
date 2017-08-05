'''
Lattice paths
Problem 15
Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.


How many such routes are there through a 20×20 grid?
'''

grid_size = 20
num_paths = []
for j in range(0,grid_size+1):
	num_paths.append([0]*(grid_size+1))

for j in range(0,grid_size + 1):
	num_paths[grid_size][j] = 1
	num_paths[j][grid_size] = 1

for j in range(grid_size-1, -1, -1):
	for i in range(grid_size-1, -1, -1):
		num_paths[i][j] = num_paths[i+1][j] + num_paths[i][j+1]

print(num_paths)
print(num_paths[0][0])