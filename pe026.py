'''Reciprocal cycles
Problem 26

A unit fraction contains 1 in the numerator. The decimal representation of the unit fractions with denominators 2 to 10 are given:

    1/2	= 	0.5
    1/3	= 	0.(3)
    1/4	= 	0.25
    1/5	= 	0.2
    1/6	= 	0.1(6)
    1/7	= 	0.(142857)
    1/8	= 	0.125
    1/9	= 	0.(1)
    1/10	= 	0.1 

Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be seen that 1/7 has a 6-digit recurring cycle.

Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.'''

n_max = 1
d_max = 1

cycle_len = {1:1, 2:1, 3:1, 4: 1, 5:1, 6:1, 7:6}

#this rho assumes that num is !=0 mod 2 or mod 5;
#i.e., that we have removed powers of 10 from the denominator
#(the numerator is unimportant)
def rho(num):
    if num in cycle_len:
        return cycle_len[num]
    else:
        n = 1
        while (10**n - 1) % num != 0:
            n += 1
        cycle_len[num] = n
        return n


for d in range(8,1000):
    if d % 2 != 0 and d % 5 != 0:
        est = rho(d)
        print(est, d)
        if est > n_max:
            n_max, d_max = est, d

print("The result: (period, num)")
print(n_max, d_max)