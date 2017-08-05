from subset import next_subset
from functools import reduce

def class_prod(nums, classes):
	m = max(classes)
	s = [1]*(m+1)
	for j in range(1, len(nums)):
		s[classes[j]] *= nums[j]
	return reduce(lambda u,v: u * v, s)

def class_sum(nums, classes):
	m = max(classes)
	s = [1]*(m+1)
	for j in range(1, len(nums)):
		s[classes[j]] *= nums[j]
	return reduce(lambda u,v: u + v, s)

print(class_prod([0,1,2,3,4,5], [0, 1, 2, 1, 3, 1]))
print(class_sum([0,1,2,3,4,5], [0, 1, 2, 1, 3, 1]))