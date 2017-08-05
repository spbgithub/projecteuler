

n = 18

s = (n + 1) * [set()]
s[1] = {60}
t = set(s[1])

for i in range(2, n + 1):
    ss = set()
    for j in range(1, i // 2 + 1):
        ss |= {x + y for x in s[j] for y in s[i-j]} | {x * y / (x + y) for x in s[j] for y in s[i-j]}
        s[i] = ss
    t |= ss

print(len({round(x,10) for x in t}))