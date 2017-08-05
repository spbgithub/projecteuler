'''Pythagorean tiles
Problem 139

Let (a, b, c) represent the three sides of a right angle triangle with integral length sides. It is possible to place four such triangles together to form a square with length c.

For example, (3, 4, 5) triangles can be placed together to form a 5 by 5 square with a 1 by 1 hole in the middle and it can be seen that the 5 by 5 square can be tiled with twenty-five 1 by 1 squares.

However, if (5, 12, 13) triangles were used then the hole would measure 7 by 7 and these could not be used to tile the 13 by 13 square.

Given that the perimeter of the right triangle is less than one-hundred million, how many Pythagorean triangles would allow such a tiling to take place?'''

from math import sqrt
from fractions import gcd

MAX_PER = 100000000.0
MAX_SQRT = int(sqrt(MAX_PER/2.0)+1)

pythag = [(j,k) for j in range(2, MAX_SQRT) for k in range(1,j) if gcd(j,k) == 1  if (j - k) % 2 != 0 if (j*j + k*k) % (j*j - k*k - 2*j*k) == 0]
print(sum([int(MAX_PER)//(2*j*(j+k)) for (j,k) in pythag]))