'''Number spiral diagonals
Problem 28

Starting with the number 1 and moving to the right in a clockwise direction a 5 by 5 spiral is formed as follows:

21 22 23 24 25
20  7  8  9 10
19  6  1  2 11
18  5  4  3 12
17 16 15 14 13

It can be verified that the sum of the numbers on the diagonals is 101.

What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?'''

r = 500
#this is closed form expression for:
#  \sum_{k=0}^r (2k+1)^2 + \sum_{k=1}^r [(2k+1)^2 - 2k] +
#     + \sum_{k=1}^r [(2k+1)^2 - 4k] + \sum_{k=1}^r [(2k+1)^2 - 6k]
#   = 1 + \sum_{k=1}^r (16k^2 + 4^k + 4).
sum = 1 + 16*r*(r+1)*(2*r+1)/6 + 2*r*(r+1) + 4*r
print(sum)