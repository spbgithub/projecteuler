'''
Maximum path sum II
Problem 67

By starting at the top of the triangle below and moving to adjacent numbers on the row below, the maximum total from top to bottom is 23.

3
7 4
2 4 6
8 5 9 3

That is, 3 + 7 + 4 + 9 = 23.

Find the maximum total from top to bottom in triangle.txt (right click and 'Save Link/Target As...'), a 15K text file containing a triangle with one-hundred rows.

NOTE: This is a much more difficult version of Problem 18. It is not possible to try every route to solve this problem, as there are 299 altogether! If you could check one trillion (1012) routes every second it would take over twenty billion years to check them all. There is an efficient algorithm to solve it. ;o)
'''
def string_to_list(s):
	return [int(u) for u in s.split()]

def read_nums():
	with open("/home/sean/workspace/projecteuler/p067_triangle.txt", 'r') as f:
		nums = [ string_to_list(s) for s in f]
	return nums

def create_weight_list(nums):
	w_list = []
	for n in nums:
		w_list.append([0]*len(n))
	return w_list


if __name__ == "__main__":
	nums = read_nums()
	weights = create_weight_list(nums)

	weights[0][0] = nums[0][0]
	for i in range(1, len(nums)):
		weights[i][0] = weights[i-1][0] + nums[i][0]
		weights[i][i] = weights[i-1][i-1] + nums[i][i]

	for i in range(2, len(nums)):
		for j in range(1,i):
			weights[i][j] = max(weights[i-1][j], weights[i-1][j-1]) + nums[i][j]

	print(weights)
	print(max(weights[len(weights)-1]))