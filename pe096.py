'''Problem 96 - Su Doku'''

BAD_SUDOKU        = 0
INCOMPLETE_SUDOKU = 1
GOOD_SUDOKU       = 2

def read_sudoku_grids():
	with open("/home/sean/workspace/projecteuler/p096_sudoku.txt","r") as f:
		all_grids = []
		cur_grid = []
		for l in f:
			if "Grid" in l:
				if "01" not in l:
					all_grids.append(cur_grid)
					cur_grid = []
			else:
				cur_grid.append([int(u) for u in l[:-1]])
	return all_grids

def row_nums_present(r, grid):
	return set([grid[r][j] for j in range(0,9)]) - set([0])

def col_nums_present(c, grid):
	return set([grid[j][c] for j in range(0,9)]) - set([0])

def block_nums_present(r,c,grid):
	r = 3 * (r // 3)
	c = 3 * (c // 3)
	return set([grid[r+i][c+j] for i in range(0,3) for j in range(0,3)]) - set([0])

def nums_needed(r, c, grid):
	return set([1,2,3,4,5,6,7,8,9]) - row_nums_present(r, grid) - col_nums_present(c, grid) - block_nums_present(r, c, grid)

def naive_solver(grid):
	updated_grid = True
	while updated_grid:
		updated_grid = False
		#this loop pair checks all unfilled squares to see if any of them have only 
		#one possible number (by checking available numbers for the row, column and grid
		#sector they belongs to - if intersection of these sets leaves one element, 
		#it's the only possible value for that square)
		for r in range(0, 9):
			for c in range(0, 9):
				if grid[r][c] == 0:
					remaining = nums_needed(r,c,grid)
					if len(remaining) == 0: return (BAD_SUDOKU, grid)
					if len(remaining) == 1:
						grid[r][c] = remaining.pop()
						updated_grid = True
	return is_sudoku(grid)

def naive_recursor(grid):
	status, g = naive_solver(copy_grid(grid))
	if status == BAD_SUDOKU:
		return (status, grid)
	if status == GOOD_SUDOKU:
		return (status, g)
	for (r,c) in [(a,b) for a in range(0,9) for b in range(0,9)]:
		if grid[r][c] == 0:
			break
	needed = list(nums_needed(r, c, grid))
	for l in needed:
		grid[r][c] = l
		status, g = naive_recursor(copy_grid(grid))
		if status == GOOD_SUDOKU:
			return status, g
	grid[r][c] = 0
	return INCOMPLETE_SUDOKU, grid 

def is_sudoku(grid):
	for r in range(0,9):
		if 0 in grid[r]: return (INCOMPLETE_SUDOKU, grid)
		if len(set(grid[r])) < 9: return (BAD_SUDOKU, grid)
	for c in range(0,9):
		if len(set([grid[j][c] for j in range(0,9)])) < 9: return (BAD_SUDOKU, grid)
	for r in range(0,3):
		for c in range(0,3):
			if len(set([grid[3*r+i][3*c+j] for i in range(0,3) for j in range(0,3)])) < 9: return (BAD_SUDOKU, grid)
	return (GOOD_SUDOKU, grid)

def copy_grid(grid):
	return [list(u) for u in grid]

def top_left_num(grid):
	return 100*grid[0][0] + 10*grid[0][1] + grid[0][2]


if __name__=="__main__":
	ag = read_sudoku_grids()

	for j in range(0, len(ag)):
		s, g = naive_recursor(copy_grid(ag[j]))
		print(j, s)
		if s == GOOD_SUDOKU:
			ag[j] = copy_grid(g)

	print(sum([top_left_num(g) for g in ag]))
