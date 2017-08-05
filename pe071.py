'''Problem 71'''

import farey_sequence

d = 1000000

fs = farey_sequence.farey_sequence(d)

fs.set_value(3,7)
print(fs.prev())

