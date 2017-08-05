import math

total_tiles = 0
max_perimeter = 100000000
outer_iters = int(0.5*math.sqrt(max_perimeter))
for j in range(2, outer_iters+1):
	for k in range(1, j):
		if (2 * j * (j+k) < max_perimeter):
			if (j**2 + k**2) % (j**2 - k**2 - 2*j*k) == 0:
				total_tiles += 1
print(total_tiles)