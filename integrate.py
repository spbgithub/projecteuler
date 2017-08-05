from math import  tan, acos, sqrt, pi, cos

num_bots = 827

def sec(x):
	return 1.0/cos(x)

def f(x):
	return sqrt(sec(x)**2/tan(pi/num_bots)**2 + 1)

def trap(f, left, right):
	return (right - left)*(f(left) + f(right))/2.0

def integrate(f, lower, upper, tolerance):
	n = 5
	old_sum = 0.0
	new_sum = 100.0
	while abs(new_sum - old_sum) > tolerance:
		old_sum = new_sum
		new_sum = 0.0
		n = 2 * n
		xvals = [lower + float(j)*(upper - lower)/float(n) for j in range(0, n+1)]

		for j in range(1, len(xvals)):
			new_sum += trap(f, xvals[j-1], xvals[j])
	return new_sum

l = integrate(f, 0, acos(sqrt(1 - 0.999**2)), 0.000001)
print(num_bots*l)